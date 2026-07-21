---
source_url: https://cognition.com/blog/devin-can-now-schedule-devins
source_type: blog-post
title: "Devin can now Schedule Devins"
author: The Cognition Team
date_published: 2026-03-20
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2103"
---

# Devin can now Schedule Devins

> Cognition's announcement of Devin's self-scheduling feature — a
> natural-language-configured recurring session mechanism, distinguished
> from a plain scheduled script by carrying state (notes) across runs, and
> composable with the separately-launched Managed Devins parallel-agent
> feature — with three example prompts (feature-flag cleanup, release
> notes, staging QA) as concrete use cases.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, byline "By The
  Cognition Team," published 03.20.26 per the page's own byline — no
  individual author named, the same anonymous-team byline pattern as
  `blog-cognition-devin-in-windsurf.md` and `blog-cognition-auto-triage.md`).
- **Author credibility**: First-party vendor product announcement. No named
  customer, practitioner quote, adoption number, or independent validation
  appears anywhere in the post — it is a feature-mechanics description with
  three illustrative example prompts, not a case study. This is a thinner
  evidentiary source than `blog-cognition-auto-triage.md` (which has one
  named customer quote) or `blog-cognition-verifying-agentic-development.md`
  (which discloses failure modes and an adoption figure).
- **Scope**: Covers what Scheduled Devins do (natural-language cadence
  configuration, no cron/workflow-builder required), the state-persistence
  mechanism across runs (notes read/written between sessions), composition
  with the separately-announced Managed Devins feature (parallel sub-agents
  in isolated VMs), and three example recurring-task prompts. Does NOT
  cover: any metric (adoption, session count, cost, accuracy), any named
  customer or practitioner account, the underlying storage mechanism for
  the "notes" Devin reads/writes between runs, what happens if a scheduled
  run fails, how cadence inference actually works when a user's request is
  ambiguous, or any comparison to a competing vendor's scheduling feature.
  This is the thinnest kind of source in this corpus's Cognition cluster by
  evidentiary density, on par with `blog-cognition-devin-in-windsurf.md`.

## Extracted Claims

### Claim 1: Devin can now schedule its own recurring sessions from a natural-language description, eliminating the need to configure a cron job or learn a workflow builder
- **Evidence**: Direct product-mechanics statement in the article's opening
  paragraph.
- **Confidence**: emerging (first-party description of a shipped,
  publicly-usable feature; no adoption or reliability data)
- **Quote**: "Starting today, Devin can schedule its own sessions to take care of work like this. You simply describe what should happen on a recurring basis, and Devin figures out the cadence, sets up the schedule, and runs it automatically going forward. There's no cron job to configure and no workflow builder to learn; instead, you're just telling Devin what you need done, the same way you would for any other task, and Devin takes ownership of making sure it keeps happening."
- **Our assessment**: The core claim is that scheduling itself becomes a
  natural-language task rather than a separate configuration surface — the
  user describes the *what* and *when* in the same request they'd use for a
  one-off task, and Devin is responsible for translating that into a
  recurring mechanism. This is architecturally similar to Anthropic's
  Claude Code Routines (see Cross-References → Corroborates) in removing
  local cron/infrastructure management, but differs in framing: Routines
  are described as something a user "configures" (schedule, API call, or
  webhook event), while this source frames configuration itself as
  delegated to Devin ("Devin figures out the cadence").

### Claim 2: The intended onboarding path into the feature is to let Devin do a task once, then simply ask it to keep doing it on a stated cadence
- **Evidence**: A worked example (feature-flag audit) under the heading
  "It starts with one good session," followed by a stated natural-language
  trigger phrase.
- **Confidence**: emerging (first-party workflow prescription with a
  worked example; not validated by any named practitioner's actual usage)
- **Quote**: "The most natural way into this feature is to let Devin do something once and then tell it to keep doing it." ... "Now, you can simply tell Devin: "Schedule this for every Monday at 9am." Devin will set up a schedule to wake up each Monday at 9am and run the same workflow, so you can stop thinking about it."
- **Our assessment**: This is a specific, actionable onboarding pattern —
  "run it once, evaluate the result, then convert it to a schedule" — as
  opposed to configuring a recurring task from scratch before ever seeing
  its output. It lowers the risk of scheduling a task that turns out to
  behave differently than expected, since the first run is interactive and
  reviewed before recurrence is turned on.

### Claim 3: Scheduled Devins carry state between runs by reading and writing their own notes across sessions, so each run builds on the context of the prior one rather than starting from scratch — the article names this as the property distinguishing the feature from a plain scheduled script
- **Evidence**: Direct mechanism claim under "Devin remembers what it did
  last time," explicitly framed as a comparison against a "scheduled
  script."
- **Confidence**: emerging (first-party mechanism description; the
  underlying storage/retrieval implementation for the "notes" is not
  disclosed — no detail on format, retention window, or how notes are
  scoped per schedule)
- **Quote**: "One feature that makes this meaningfully different from a scheduled script is that Devin carries state between runs. It reads and writes its own notes across sessions, which means each run builds on the context of the one before it rather than starting from scratch."
- **Our assessment**: This is the article's central differentiating claim
  and its most citable one: state persistence, not scheduling mechanics
  themselves, is what the post argues makes this more than "cron for
  agents." No detail is given on the notes' underlying storage
  mechanism, so the claim should be treated as a described behavior, not a
  documented architecture — see Cross-References for how this compares
  mechanically to the memory mechanism already documented in
  `blog-cognition-auto-triage.md`.

### Claim 4: In the worked release-notes example, a weekly-scheduled Devin does not re-summarize PRs it already covered in the prior run, because it tracks where it left off and reports only what's new
- **Evidence**: Concrete worked example under "Devin remembers what it did
  last time," illustrating the state-persistence claim (Claim 3) with a
  specific recurring-task scenario.
- **Confidence**: anecdotal (illustrative example in a product announcement,
  not an observed customer account or metric — no PR count, error rate, or
  before/after comparison given)
- **Quote**: "If you set up a Devin to compile release notes every Friday, it won't re-summarize the PRs it already covered last week, because Devin knows where it left off, picks up from there, and gives you a clean summary of just what's new."
- **Our assessment**: This is a specific, checkable behavior claim (in
  principle a team could verify whether a scheduled release-notes Devin
  actually avoids duplicate coverage across runs), but it is presented only
  as an illustrative example, not a tested or measured outcome — no
  incident of this behavior succeeding or failing in practice is described.

### Claim 5: In the worked Slack-monitoring example, a scheduled Devin watching a channel tracks which messages it has already processed, notices recurring themes, and surfaces only what changed since the previous run
- **Evidence**: Second worked example under "Devin remembers what it did
  last time," illustrating the same state-persistence claim with a
  different recurring-task scenario.
- **Confidence**: anecdotal (illustrative example, not a tested or
  customer-reported outcome)
- **Quote**: "If you have a Devin watching your #feature-requests channel every morning, it tracks which messages it's already processed, notices when themes recur, and surfaces only what's changed since yesterday."
- **Our assessment**: This closely parallels the deduplication mechanism
  already documented with more mechanism detail (though still without a
  measured accuracy figure) in `blog-cognition-auto-triage.md` Claim 7 —
  see Cross-References → Corroborates. Neither source discloses how
  "already processed" is tracked (message IDs, timestamps, embeddings, or
  free-text notes), so the two claims should be read as the same general
  capability described twice from Cognition, at the same level of
  non-disclosure.

### Claim 6: Scheduled Devins compose with the separately-launched Managed Devins feature (parallel sub-agents, each in its own isolated VM, spawned by Devin to break a large task into pieces), illustrated by a weekly QA pass that fans out one managed Devin per application page, tests them in parallel, and posts a compiled report to Slack automatically
- **Evidence**: Direct composition claim under "Works with Managed Devins,"
  naming the prerequisite feature's own launch timing and describing a
  worked example combining both features.
- **Confidence**: emerging (first-party description of two composed shipped
  features; no example transcript, run count, or reliability data for the
  combined workflow)
- **Quote**: "Earlier this week we launched Managed Devins, which let Devin break large tasks into pieces and delegate them to parallel agents, each running in their own isolated VM. Scheduled Devins and Managed Devins compose naturally together." ... "That means you can set up a weekly QA pass where Devin spins up a managed Devin for each page of your application, tests them all in parallel, compiles the results into a single report, and posts it to your team's Slack channel — automatically, every Friday afternoon, without anyone needing to kick it off."
- **Our assessment**: This is the article's clearest statement that
  scheduling (when/why a session starts) and parallel decomposition (how a
  single session's work is split across sub-agents) are treated by
  Cognition as orthogonal, composable capabilities rather than a single
  feature. No corpus source note currently documents Managed Devins
  directly — the companion announcement issue (#2073) was closed with an
  `extraction-rejected` label and no source note exists for it in this
  corpus at time of writing — so this claim is the only place in the
  corpus this feature is described, and only at the level of this one
  sentence plus the QA worked example. This should not be conflated with
  Devin CLI's separately-documented "subagents" mechanism
  (`blog-cognition-devin-cli-terminal.md` Claims 11-14): that source
  describes a different, CLI-specific subagent system with its own cost
  model and `AGENT.md` profile format; this article gives no indication
  Managed Devins uses the same mechanism, and the two are never connected
  in either source.

### Claim 7: The article frames the problem this feature solves as a "quiet backlog" of recurring tasks (release notes, feature-flag cleanup, onboarding QA sweeps) that are individually easy but chronically deprioritized because no single instance feels urgent
- **Evidence**: Opening problem-framing paragraph, naming three specific
  example task categories before describing the feature.
- **Confidence**: anecdotal (a structural observation about team behavior,
  not a measured claim — no survey or data on how common this pattern is)
- **Quote**: "Every engineering team has a quiet backlog of things that should happen on schedule, but often slip – like weekly release notes, feature flag cleanups, and onboarding QA sweeps. None of these tasks are difficult, but they slip through the cracks precisely because no single instance feels urgent enough to prioritize."
- **Our assessment**: This is the marketing frame that motivates the rest
  of the post — a plausible, relatable problem statement, but presented
  as a general assertion about "every engineering team," not backed by any
  data or named example of a team actually experiencing this before
  adopting the feature.

### Claim 8: Cognition ships three named, directly-launchable example prompts for the feature: a Monday feature-flag cleanup, a Friday release-notes compilation, and a daily staging QA sweep using managed Devins for parallel page testing
- **Evidence**: The "Try it now" closing section, presenting each example
  as a full prompt with a stated intended cadence, described as clickable
  to open directly in Devin.
- **Confidence**: settled (verbatim, currently-published example prompts
  for a shipped feature — these are the exact prompt texts the product
  page offers, not a paraphrase of the feature's capability)
- **Quote**: "Check our feature flags. If any flag has been at 100% rollout for more than 14 days, open a PR to remove it and ping the owner. Then schedule this to run every Monday at 9am." / "Every Friday at 5pm, pull all PRs merged this week, categorize the changes into bug fixes, new features, and infrastructure, write release notes, and post them to #engineering in Slack." / "Every morning at 8am, run QA against our staging environment. Navigate through the core user flows, take screenshots, flag any regressions or visual issues, and post a report to #engineering. Use managed Devins to test flows in parallel."
- **Our assessment**: These three prompts are the most concrete artifact in
  the source — exact, reusable prompt text rather than a description of
  what a prompt might look like. The third prompt explicitly names managed
  Devins as a sub-component within a scheduled task, making it the
  clearest textual instance of Claim 6's composition claim.

## Concrete Artifacts

### Full "Try it now" example prompts, verbatim
```
Source: cognition.com/blog/devin-can-now-schedule-devins, "Try it now" section

### Clean up stale feature flags every Monday
Check our feature flags. If any flag has been at 100% rollout for more
than 14 days, open a PR to remove it and ping the owner. Then schedule
this to run every Monday at 9am.

### Compile release notes every Friday
Every Friday at 5pm, pull all PRs merged this week, categorize the
changes into bug fixes, new features, and infrastructure, write release
notes, and post them to #engineering in Slack.

### Run QA against staging every morning
Every morning at 8am, run QA against our staging environment. Navigate
through the core user flows, take screenshots, flag any regressions or
visual issues, and post a report to #engineering. Use managed Devins to
test flows in parallel.
```

### Article section structure (headings, in order)
```
Source: cognition.com/blog/devin-can-now-schedule-devins, 03.20.26

1. (intro, unheaded — "quiet backlog" problem framing)
2. It starts with one good session
3. Devin remembers what it did last time
4. Works with Managed Devins
5. Try it now (three clickable example prompts)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-routines.md` Claim 1 ("Routines eliminate
    the local-machine infrastructure requirement for scheduled AI
    automation," quoting "until now, teams managed cron jobs,
    infrastructure, and additional tooling like MCP servers themselves")
    and Claim 3 (scheduled routines operate on practitioner-configured
    cadences without local infrastructure) — this note's Claim 1 ("no cron
    job to configure and no workflow builder to learn") is the same
    infrastructure-elimination pitch from a second, independent vendor
    (Cognition vs. Anthropic), both replacing self-managed cron with a
    natural-language-configured cloud scheduling primitive. Neither source
    discloses failure/retry behavior for a missed or failed scheduled run.
  - `blog-cognition-auto-triage.md` Claim 6 (Devin "builds and maintains
    long-running context of prior investigations, recurring issues, and
    how your team prefers issues to be routed") and Claim 7 (memory lets
    Devin de-duplicate incidents by connecting new alerts to earlier
    threads) — this note's Claim 3 (state persistence across scheduled
    runs) and Claim 5 (Slack-monitoring example tracking already-processed
    messages) describe the same underlying cross-session memory capability
    applied to a different feature (self-scheduling rather than
    alert-triage). Neither source discloses the underlying storage
    mechanism for this memory in either feature.

- **Contradicts**: None identified. No claim in this source conflicts with
  an existing source note's claim under matching conditions. One candidate
  was considered and rejected: this source's natural-language,
  Devin-infers-the-cadence framing ("Devin figures out the cadence") versus
  `blog-anthropic-claude-code-routines.md`'s framing of a routine as
  something the user "configures once" — this is not a contradiction, since
  both sources still require the user to state a cadence in natural
  language (e.g. "every Monday at 9am" here; "every night at 2am" in the
  Anthropic post); the difference is emphasis in the marketing copy, not a
  documented mechanical disagreement about who sets the schedule.

- **Extends**:
  - `blog-cognition-devin-in-windsurf.md` Claim 4, which names "scheduling
    its own work" as one of four capability milestones in Devin's
    progression toward operating without a human in the loop, but supplies
    no mechanism detail — that note's own assessment explicitly flags
    "scheduling its own work" as "not independently documented elsewhere in
    this corpus at time of writing." This source is exactly that
    documentation: it supplies the mechanism (natural-language cadence
    configuration, state persistence via notes, composition with Managed
    Devins) that the Windsurf post's retrospective list item only named.
  - `blog-cognition-auto-triage.md` — see Corroborates above; this source
    extends that note's memory/deduplication mechanism from an
    alert-triage-specific context to a general recurring-task-scheduling
    context, suggesting the underlying state-persistence mechanism may be a
    shared Devin platform capability rather than something built separately
    for each feature (though neither source states this explicitly — it is
    an inference from the similarity of the two descriptions, not a
    documented fact).

- **Novel**: The natural-language, self-configuring recurring-session
  mechanism itself (Claim 1: "you simply describe what should happen on a
  recurring basis, and Devin figures out the cadence") is new to this
  corpus's Cognition cluster — prior sources document Devin acting
  proactively in response to external events (`blog-cognition-auto-triage.md`)
  but not a wall-clock recurring-schedule feature the agent configures for
  itself from a single natural-language request. The explicit
  "do-it-once-then-schedule-it" onboarding pattern (Claim 2) is also new.
  The composition of a scheduling primitive with a separate parallel-agent
  primitive (Claim 6, Scheduled Devins + Managed Devins) is a new pattern
  for this corpus: prior parallel-agent examples
  (`blog-cognition-auto-triage.md` Claim 3, `blog-cognition-devin-cli-terminal.md`
  Claims 11-14) describe fan-out triggered within a single session, not
  fan-out composed with a separate recurring-schedule trigger.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add this source alongside
  `blog-anthropic-claude-code-routines.md` in any discussion of managed
  scheduling infrastructure for background agent automation. Specifically
  contrast the two vendors' framing: Anthropic's Routines present a
  three-axis taxonomy (scheduled/API-triggered/webhook-triggered) the user
  explicitly configures; this source presents scheduling as an extension of
  ordinary task delegation ("the same way you would for any other task"),
  with Devin inferring the cadence from a natural-language request. Flag
  that neither source discloses failure/retry behavior for a missed or
  failed scheduled run — a gap in both vendors' public documentation the
  guide should note rather than paper over.

- **Chapter 04 (Context Engineering)**: Add Claim 3 (state persistence via
  Devin reading/writing its own notes across scheduled runs, explicitly
  positioned as the property distinguishing this from "a scheduled
  script") as a citable example of cross-session context accumulation
  applied specifically to recurring automation. Pair with
  `blog-cognition-auto-triage.md` Claims 6-7 to show the same
  state-persistence pattern used across two different Devin features
  (triage and scheduling), while flagging that neither source discloses
  the underlying storage/retrieval mechanism — this is a described
  behavior, not a documented architecture, in both cases.

- **Chapter 01 (Daily Workflows)**: Add Claim 2 (the "run it once
  interactively, then convert to a schedule" onboarding pattern) as a
  concrete, low-risk workflow for adopting recurring agent automation: the
  first run is reviewed by a human before recurrence is turned on, rather
  than configuring a recurring task blind. This is a specific, actionable
  practice independent of which vendor's scheduling feature a reader uses.

- **Chapter 05 (Team Adoption)**: Add Claim 6 (Scheduled Devins composing
  with Managed Devins for a weekly parallel QA sweep posted to Slack) as a
  concrete example of a single scheduled automation serving a whole team
  through a shared notification channel, in the same pattern already
  flagged for Anthropic's Routines in `blog-anthropic-claude-code-routines.md`'s
  Guide Impact section (webhook routine → shared Slack channel). Note that
  Managed Devins itself has no corpus source note (issue #2073 closed as
  `extraction-rejected`), so this composition claim currently rests only on
  this one sentence and worked example — flag as thin evidence if cited.

## Extraction Notes

- The full article was fetched via WebFetch and returned complete,
  section-by-section verbatim text on the first attempt (headings, body
  paragraphs, and all three "Try it now" prompts) — unlike several other
  Cognition source notes in this corpus which required repeated
  curl/raw-HTML fetches to get past WebFetch's summarizing pass (e.g.
  `blog-cognition-devin-in-windsurf.md`, `blog-cognition-ai-productivity.md`
  Extraction Notes). The returned text was checked for internal
  consistency (heading order, paragraph boundaries, prompt text) and used
  directly as the verbatim source for all quotes above.
- The article is short (~450 words across an intro paragraph and four named
  sections). No sub-pages were followed: the fetched text contained no
  inline hyperlinks to other Cognition posts or documentation pages within
  the body copy itself (unlike, e.g., `blog-cognition-devin-in-windsurf.md`,
  which linked to a companion post). The "Managed Devins" feature named in
  Claim 6 is referenced only by name and launch timing ("earlier this
  week"), with no link followed or found in the fetched text — this is
  flagged in Claim 6's assessment, where I also confirmed by search that no
  corpus source note documents Managed Devins directly (issue #2073 for
  that companion announcement is closed with an `extraction-rejected`
  label, no source note exists).
- The Prospector's triage comment on this issue references
  `blog-cognition-devin-cli-terminal.md`'s extraction notes, which
  explicitly deferred mining this exact URL and named it "a candidate for
  a future, separate source note if queued." This note is that follow-up
  extraction, as the Prospector's second triage comment states directly.
- No contradiction meeting the MINER.md §4a filing bar was identified — see
  Cross-References → Contradicts for the one candidate considered and
  rejected (a framing-emphasis difference between this source and
  `blog-anthropic-claude-code-routines.md`, not a same-claim mechanical
  disagreement). No contradiction issue filed.
- Cross-references verified before writing: re-read
  `blog-anthropic-claude-code-routines.md` in full and confirmed Claims 1
  and 3 by number and content; re-read `blog-cognition-auto-triage.md` in
  full and confirmed Claims 6 and 7 by number and content; re-read
  `blog-cognition-devin-in-windsurf.md` in full and confirmed Claim 4 by
  number and content; re-read `blog-cognition-devin-cli-terminal.md` in
  full and confirmed Claims 11-14 by number and content (cited in Claim 6's
  assessment to distinguish Managed Devins from Devin CLI's separately
  documented subagent system, not to equate them). No claim number was
  guessed or approximated.
- Confidence is rated `emerging` overall: this is a first-party product
  announcement for a shipped, publicly usable feature (not a research
  preview or a hypothetical), which is more than pure marketing intent —
  but it carries zero named customers, zero adoption or reliability
  metrics, and only illustrative (not observed) worked examples, so it does
  not reach `settled`. This matches the confidence tier already assigned to
  the two closest sibling sources in this corpus's Cognition cluster,
  `blog-cognition-devin-in-windsurf.md` and `blog-anthropic-claude-code-routines.md`.
