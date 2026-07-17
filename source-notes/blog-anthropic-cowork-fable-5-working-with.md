---
source_url: https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork
source_type: blog-post
title: "Working with Claude Fable 5 in Claude Cowork"
author: Josefina Albert (Anthropic, Education team)
date_published: 2026-07-16
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: emerging
issue: "#1955"
---

# Working with Claude Fable 5 in Claude Cowork

> First-party Anthropic usage guide for Fable 5 specifically inside Claude Cowork:
> Fable is not the Cowork default (Sonnet 5 is), model choice is a distinct lever
> from the effort setting, delegation should shift from step-by-step instruction to
> outcome-plus-context (approach / procedure / timing), and a new pair of
> cybersecurity/bio-chem misuse classifiers silently reroutes triggered chats to
> Opus 4.8 — with a "users are informed whenever this occurs" claim that a prior
> corpus source's documented silent downgrade directly contradicts.

## Source Context

- **Type**: blog-post (official claude.com blog, "Enterprise AI" category, Claude
  Cowork product tag, dated July 16, 2026, ~5-minute read).
- **Author credibility**: Josefina Albert, credited at the foot of the post as
  writing "on Anthropic's Education team" — first-party, but not a Claude Code/Cowork
  product-team byline (contrast with `blog-anthropic-fable-finding-unknowns.md`,
  written by a Claude Code team member). The post itself states it draws on "our
  prompting guide for Claude Fable 5" (linked but not followed — see Extraction
  Notes) and folds those recommendations into the Cowork-specific setting. Feature
  and behavior claims (model defaults, effort mechanics, classifier fallback) are
  first-party product descriptions; the worked examples (budget project, data
  scientist dashboard anecdote) are illustrative, unnamed, and unverifiable beyond
  the post's own text.
- **Scope**: Covers how to work with Fable 5 specifically inside Claude Cowork:
  when to select it over Sonnet 5/Opus, how the effort setting interacts with model
  choice, the new misuse classifiers and their fallback behavior, three delegation
  strategies (approach/procedure/timing), starting a task from an unformed idea,
  context vs. constraints, reviewing Claude's plan and work in-product, and Cowork
  setup recommendations (tool connections, voice tuning, auditing old skills/memory).
  Does NOT cover: pricing or token costs, Fable's benchmark scores, the enterprise
  governance controls already documented in `blog-anthropic-cowork-enterprise.md`,
  or any content from the linked general "prompting guide for Claude Fable 5" beyond
  what this post restates.

## Extracted Claims

### Claim 1: Claude Fable 5 is Anthropic's most capable generally available model, built for long-running, complex, asynchronous multi-step work, and it tests and evaluates its own results as it goes
- **Evidence**: Opening product-positioning paragraph, with three named example
  workflow types.
- **Confidence**: settled (first-party model positioning)
- **Quote**: "Claude Fable 5 is Anthropic’s most capable generally available model, built for long-running, complex and asynchronous work. Claude Fable 5 is particularly effective carrying out multi-step workflows (such as conducting deep research that it incorporates in a first-draft memo, performing due diligence before generating board presentations, or going through a folder to redline multiple contracts, to name a few) on its own for extended periods of time, testing and evaluating its results as it goes."
- **Our assessment**: The three named workflow examples (research→memo, due
  diligence→board deck, folder→redlined contracts) are useful as citable canonical
  Cowork+Fable use cases, distinct from the engineering-flavored examples already in
  the corpus (`blog-simonwillison-claude-fable-5.md`, `blog-simonwillison-fable-relentlessly-proactive.md`).
  This post is squarely about non-engineering knowledge work, consistent with the
  quantified split in `blog-anthropic-cowork-usage-taxonomy.md` Claim 4 (developers
  use Cowork for the connective work around coding, not coding itself).

### Claim 2: Existing prompting/context/skills best practices still apply to Fable 5 and the model performs even better when they're in place — capability gains do not obsolete prompting discipline
- **Evidence**: Direct framing statement bridging the intro to the rest of the post.
- **Confidence**: settled (first-party framing claim)
- **Quote**: "Those practices still matter with Claude Fable 5, in fact, the model performs even better with them in place."
- **Our assessment**: This is a direct rebuttal-in-advance of a "bigger model means
  you can prompt less carefully" assumption. It's consistent with, and reinforces,
  this corpus's general stance (e.g. `blog-anthropic-fable-finding-unknowns.md`)
  that prompting/context discipline compounds with model capability rather than
  being superseded by it — worth citing whenever the guide risks implying that a
  more capable model reduces the need for context engineering.

### Claim 3: Fable 5 applies context, preferences, and skills across entire multi-day tasks, whereas previous models could lose track over long stretches and need reminding
- **Evidence**: Direct capability comparison against "previous models," stated
  without benchmark data.
- **Confidence**: emerging (first-party comparative claim, no measurement given)
- **Quote**: "Claude Fable 5 applies your context, preferences, and skills across entire tasks, even those that take days to complete, while previous models may have lost track over long stretches and needed reminding."
- **Our assessment**: This is the stated mechanism behind the "delegate whole jobs,
  not steps" advice in Claim 8 below — if the model reliably keeps context over a
  multi-day task, checkpoint-heavy delegation becomes less necessary. No
  quantification of "days" or a failure-rate comparison is given, so this should be
  cited as vendor characterization, not a measured retention benchmark.

### Claim 4: Cowork decomposes large jobs into concurrently-run subagent parts and sets an upfront plan it checks its own results against, letting it catch and correct an early error (e.g., a misread figure) before it propagates through the rest of the job
- **Evidence**: Architecture description plus a worked, if unnamed, example (a
  next-year budget built from this year's actuals).
- **Confidence**: settled for the architecture description (first-party); emerging
  for the "catches the misread number while the job runs" claim (illustrative,
  unverified example rather than a measured error-correction rate)
- **Quote**: "A big job gets broken into parts that run at the same time, each with its own subagent, a separate instance of Claude that takes one part of the job to complete and reports back." / "Claude Fable 5 plans the workflow before starting and checks results as it goes, so it can catch the misread number while the job runs and correct it."
- **Our assessment**: The budget worked example (spreadsheets → run rates →
  per-line projections → reconciliation → summary, with an early misread run rate
  propagating into every downstream projection if uncaught) is a concrete,
  citable illustration of self-checking plan execution as a defense against
  compounding errors in long agentic chains. It corroborates the plan-and-checkpoint
  architecture already described for Cowork generally in
  `blog-anthropic-cowork-deploy-guide.md`, applied here specifically to the
  case for choosing Fable over other models on tasks with error-propagation risk.

### Claim 5: Fable 5 is not the default model in Claude Cowork — Sonnet 5 is the default for everyday tasks, Opus is recommended for well-defined deep work, and Fable should be reserved for the most complex or ambiguous jobs, especially those using multiple tools and requiring a series of judgment calls
- **Evidence**: Direct model-selection guidance with named alternatives and their
  recommended use cases.
- **Confidence**: settled (first-party product configuration and recommendation,
  as of publication date)
- **Quote**: "Claude Fable 5 isn’t the default model in Claude Cowork; you need to select it. As of the time of publication, the default is Claude Sonnet 5, and it is the right choice for everyday tasks you yourself would handle in quick passes. Claude Opus is a dependable choice for deep work with a clear shape, where you know what the end result looks like. Claude Fable 5 is for the projects that feel the most complex or ambiguous, and may have been out of reach for prior models." / "We recommend that you reserve Claude Fable 5 for your most important work, especially jobs that use multiple tools and require a series of judgment calls."
- **Our assessment**: This gives a concrete three-tier model-selection heuristic
  specific to Cowork (Sonnet = everyday/quick, Opus = well-defined deep work, Fable
  = complex/ambiguous/multi-tool) that is new to the corpus's Cowork-specific
  guidance — prior Cowork sources describe governance and adoption maturity but not
  a per-task model-selection rule of thumb. The "as of the time of publication"
  qualifier on the Sonnet-5-default claim should be carried into any guide citation,
  since Cowork's default model is stated as time-bound, not an architectural
  constant.

### Claim 6: The effort setting is a separate lever from model choice — higher effort makes Fable plan more upfront and check in more during a run, and Fable at lower effort often matched or exceeded earlier models running at their highest effort levels
- **Evidence**: Direct guidance on effort-level tuning plus an unquantified
  internal-testing comparative claim.
- **Confidence**: emerging for the effort-mechanics description (settled feature
  description); anecdotal/unquantified for the cross-model effort comparison (no
  benchmark, task set, or numbers given)
- **Quote**: "At higher effort, Claude Fable 5 plans more before it kicks off a job and checks in more throughout its run. Keep effort higher for complex or multi-step projects you expect Claude to complete from beginning to end. At lower effort, you’ll get a faster response, while still taking advantage of Claude Fable 5 intelligence." / "In our testing, Claude Fable 5 at lower effort often matched or exceeded the performance of earlier models at their highest effort levels."
- **Our assessment**: The "lower effort Fable ≥ highest effort prior models" claim
  is the strongest capability claim in the post, but it is stated with no benchmark,
  task category, or "often" quantification — treat as a directional marketing claim
  rather than a citable performance figure. The mechanically useful part is the
  orthogonality claim itself: effort and model choice are two independent dials
  (which model, how much it plans/checks before/during a run), useful to distinguish
  clearly in any guide section on Cowork model configuration.

### Claim 7: Fable 5 ships with new cybersecurity and biology/chemistry misuse classifiers; when triggered, Anthropic states the response is automatically handled by Opus 4.8 instead and users are informed every time this happens, though the safeguards are tuned conservatively and can trigger on harmless requests that only touch on related topics
- **Evidence**: Direct first-party description of the classifier/fallback mechanism
  and its known false-positive behavior.
- **Confidence**: settled for the mechanism's existence (first-party feature
  description); the "users are informed whenever this occurs" sub-claim is
  corroborated as *stated policy* by Anthropic's own June 2026 reversal statement
  (`blog-simonwillison-fable-silent-interventions.md` Claims 6–7 — see
  Cross-References → Corroborates) yet contradicted at the level of *observed
  behavior* by a dated first-person session — see Cross-References → Contradicts.
- **Quote**: "It’s also worth noting that Claude Fable 5 comes with a new set of classifiers: separate AI systems that detect potential misuse in requests related to cybersecurity or to biology and chemistry. When they trigger, the response is automatically handled by Claude Opus 4.8 instead, and users are informed whenever this occurs. Opus 4.8 is a highly capable model in its own right, and the chat stays on Opus from there; start a new one to get back to Claude Fable 5. We tuned these safeguards conservatively so we could release a Mythos-class model for general use both safely and quickly, so they'll sometimes catch harmless requests, including phrases in Claude Cowork that only touch on related topics."
- **Our assessment**: This is the most operationally important claim in the post for
  practitioners running long Cowork sessions: a mid-session model swap to Opus 4.8
  can happen transparently and persist for the rest of that chat, with a stated (but
  contradicted, see below) guarantee of user notification, and known false-positive
  risk on merely-adjacent topics. Practitioners should not assume every claimed
  cybersecurity/bio-chem trigger reflects genuinely risky content, but they also
  should not assume they will always notice the switch — see the filed
  contradiction.

### Claim 8: Delegating "complete jobs" rather than step-by-step instructions to Fable 5 in Cowork takes one of three forms — delegating the approach (goal + material, not method), delegating the procedure (naming no skills, letting Fable pick the right skill at the right moment), or delegating the timing (describing a recurring outcome and letting Claude set up the schedule)
- **Evidence**: Named three-way taxonomy with one example prompt per category.
- **Confidence**: anecdotal (practitioner-facing framework, illustrated with
  invented example prompts, not measured outcomes)
- **Quote**: "Delegate the approach: Give Claude the material and describe the outcome you want, for example, \"Here is last quarter's customer feedback. Find out why cancellations rose and what we should change.\"" / "Delegate the procedure: A skill teaches Claude a procedure your team uses—how you build a report, format a deck, run an analysis. You don't need to say which skills to use or in what order. Say \"put together the quarterly review the way we always do it,\" and Claude Fable 5 picks the right skills at the right moment." / "Delegate the timing: For work you want repeated, describe the outcome and Claude will set up the schedule and turn it into a recurring task: \"I want to start every Monday knowing what changed in the pipeline and what needs a decision.\""
- **Our assessment**: This taxonomy is a directly reusable delegation vocabulary —
  distinct from, and more Cowork-specific than, the general "delegate vs. don't
  delegate" framework already in `01-daily-workflows.md`'s "When NOT to Delegate"
  section. "Delegating the procedure" in particular assumes skills already exist
  and are well-scoped enough for Fable to pick correctly without being told which
  one — an assumption worth flagging rather than taking at face value, since skill
  quality/coverage is exactly the governance gap `blog-anthropic-cowork-enterprise.md`
  Claim 7 already identifies as unaddressed.

### Claim 9: Brainstorming with Fable 5 in the same Cowork conversation that later executes the task lets the model carry forward the goal, constraints, and decisions made during the brainstorm into the task itself, without re-stating them
- **Evidence**: Direct workflow description plus one specific, named-but-anonymized
  internal example (an Anthropic data scientist building a dashboard).
- **Confidence**: anecdotal (single internal anecdote, no outcome metric beyond a
  qualitative "shortlist of metrics" and "clickable prototype")
- **Quote**: "And when the task begins in the same conversation, Claude Fable 5 already carries the goal you settled on, the constraints you named, and the decisions you made along the way." / "For example, a data scientist at Anthropic came to Claude Cowork with an idea for a new analytics dashboard while the team was still figuring out what it should show. Because Claude Fable 5 could read the team's usage data during the conversation, it knew which problems take weeks to get noticed, and it ranked the metrics that would have caught them sooner. By the end of the conversation, the data scientist had a shortlist of metrics worth adding and a clickable prototype."
- **Our assessment**: The operational takeaway — don't start a fresh conversation
  once brainstorming concludes — is a small, concrete, and easy-to-miss piece of
  Cowork-specific advice; it's in mild tension with Claim 11 below (long
  conversations use more usage because the whole history is re-read each turn), so
  the guide should present both together: staying in one conversation preserves
  carried context but costs more usage on long sessions, and the practitioner has to
  weigh that tradeoff rather than treat "same conversation" as a free win.

### Claim 10: Context (prompt, shared files/folders, connected tools) tells Fable 5 what the work is *for*, letting it make good calls in situations a fixed set of constraints didn't anticipate; constraints alone only say what not to do
- **Evidence**: Direct framing distinction with example constraint language.
- **Confidence**: anecdotal (author's framing principle, not measured)
- **Quote**: "Constraints are still useful: \"keep it under two pages and use plain language\" is a fine instruction. But a constraint only tells Claude what not to do. Context tells it what the work is for, so it can make the right call in situations your constraints didn't anticipate."
- **Our assessment**: This is a clean, quotable articulation of a context-vs-rules
  distinction the guide's context-engineering chapter could use directly: rules
  (constraints) bound the *how*, context supplies the *why*, and the *why* is what
  lets a capable model improvise correctly outside the literal rule set. It pairs
  naturally with the map/territory framing already sourced from
  `blog-anthropic-fable-finding-unknowns.md` Claim 2.

### Claim 11: Long, context-heavy Cowork conversations use more of a user's usage allowance because Claude re-reads the entire conversation on every new message; starting new tasks in fresh conversations, and periodically turning off unneeded scheduled tasks (which also count against the limit), are the recommended mitigations
- **Evidence**: Direct operational/cost caveat.
- **Confidence**: settled (first-party mechanism description)
- **Quote**: "One thing to note about chats with lots of context: in order to stay caught up, Claude reads the whole conversation again with every new message you send, so a long conversation may use more of your usage. It helps to start new tasks in a fresh conversation. Scheduled tasks count towards your limit too, so check yours occasionally and turn off any you no longer need."
- **Our assessment**: This is a concrete, actionable usage-management tip specific
  to Cowork's conversation model, and it directly qualifies Claim 9's "stay in the
  same conversation" advice — the guide should present them as a tradeoff (context
  continuity vs. usage cost) rather than two independent tips. No cost multiplier or
  quantified usage-consumption rate is given, so this should be cited as a
  qualitative mechanism, not a quantified cost claim.

### Claim 12: Cowork surfaces Fable 5's live plan and file/tool activity in a side panel during a run, letting a user redirect a wrong step mid-task with a single correction rather than restarting, and after the run review it like a colleague's work — reading outputs, scrolling the step record, expanding reasoning, or asking directly where a figure came from
- **Evidence**: Direct product-behavior description of the in-Cowork review UI and
  suggested review workflow.
- **Confidence**: settled (first-party feature/workflow description)
- **Quote**: "In Claude Cowork, you can see that plan while Claude works: the panel beside the conversation lists what it intends to do, then the files it's reading and writing and the tools and skills it's using." / "That panel is your chance to catch problems and redirect early. A mistake you'd otherwise find in the finished output instead shows up as one wrong step in the plan. You can correct the plan in one sentence and Claude adjusts without starting over." / "Or ask directly: \"Where did this figure come from?\" and Claude will point you to the source."
- **Our assessment**: This is a concrete, Cowork-specific human-in-the-loop
  mechanism — mid-run plan correction without restart — distinct from the
  supervised-then-scheduled autonomy-building pattern already documented in
  `blog-anthropic-cowork-deploy-guide.md` Claim 10 (which is about *removing*
  validation once trust is built). This claim is about the *shape* of validation
  while it's still in place: catch a wrong plan step early rather than discovering
  the consequence in the finished output. The "start with work you know how to
  verify" framing (not separately quoted above) reinforces the guide's existing
  verification-ramp advice in `05-team-adoption.md`.

### Claim 13: As part of a Cowork setup investment, practitioners should connect their daily tools first, actively tune Fable 5's default writing voice (which the post says trends terser/harder-to-follow in long sessions) via prompting/project instructions/skills, and explicitly audit old Skills and memory files for corrections that were written for a less capable prior model and may now unnecessarily constrain Fable 5
- **Evidence**: Three named setup recommendations, the last with a suggested audit
  prompt.
- **Confidence**: emerging for the tool-connection and voice-tuning advice (first-party
  recommendations, logically grounded but not measured); anecdotal for the specific
  "terser or hard to follow" writing-default observation (stated without examples or
  a comparison baseline)
- **Quote**: "You may notice Claude Fable 5 has certain defaults, such as more terse or hard to follow writing style in longer sessions." / "We've found Claude Fable 5 follows standing instructions more closely than earlier models, and is better at using saved material when needed." / "Revisit what you set up for earlier models: Saved instructions, like Skills and memory files, written for an earlier model often carry corrections that model needed. Carried forward, old corrections can constrain a new model. Ask Claude Fable 5 to do an audit: 'Go through my skills and saved memory. Which still fit, and which were written for an older model?'"
- **Our assessment**: The "audit your skills/memory for model-specific corrections
  that no longer apply" recommendation is the most concretely actionable claim in
  this section — it names a specific, reusable audit prompt and a specific failure
  mode (accumulated corrections written for a weaker model becoming unnecessary
  constraints on a stronger one). This is a direct maintenance counterpart to the
  claim (Claim 2) that context-engineering discipline compounds with capability:
  discipline that compounds also needs periodic pruning as the underlying model
  changes, or the accumulated rules become a ceiling rather than a floor.

## Concrete Artifacts

### Delegation and interview prompts (verbatim from the post)

```
Interview prompt (start with an idea):
"Before you start, ask me everything you need to know to get this right."

Directions prompt (start with an idea):
"Here is roughly what I want. Give me three ways you could take it, with a
quick sample of each."

Delegate the approach:
"Here is last quarter's customer feedback. Find out why cancellations rose
and what we should change."

Delegate the procedure:
"put together the quarterly review the way we always do it"

Delegate the timing:
"I want to start every Monday knowing what changed in the pipeline and what
needs a decision."

Constraint example (contrasted with context, not a replacement for it):
"keep it under two pages and use plain language"

Post-run comprehension check:
"Where did this figure come from?"

Skills/memory audit prompt (setup recommendation):
"Go through my skills and saved memory. Which still fit, and which were
written for an older model?"
```
*Source: claude.com/blog/working-with-claude-fable-5-in-claude-cowork*

### Model-selection and effort guidance summary (paraphrased structure, quotes verbatim per Claims 5-6)

```
Claude Cowork model tiers (as of 2026-07-16 publication):
  Sonnet 5 — default; everyday tasks, "quick passes"
  Opus     — deep work with a clear shape / known end result
  Fable 5  — most complex or ambiguous work; multiple tools; a series of
             judgment calls; NOT the default, must be explicitly selected

Effort setting (independent of model choice):
  Higher effort — more upfront planning, more mid-run check-ins;
                  use for complex/multi-step projects run start-to-finish
  Lower effort  — faster response, still frontier-level judgment;
                  use for many-easy-steps agentic runs or easily-checked results
  Claimed (unquantified): Fable 5 at low effort often matched/exceeded prior
  models at their highest effort level, per Anthropic's internal testing.
```
*Source: claude.com/blog/working-with-claude-fable-5-in-claude-cowork*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-fable-finding-unknowns.md` Claim 2 (map/territory framing —
    the prompt/skills/context you give Claude is a map, not the territory) — this
    post's context-vs-constraints distinction (Claim 10) is the same underlying
    idea restated for Cowork specifically: constraints are a partial map of what
    not to do; context is what lets the model reason about the actual territory.
  - `blog-anthropic-cowork-usage-taxonomy.md` Claim 4 (developers use Cowork for
    connective work, not core coding; software dev + DevOps combined are only
    15.7% of Cowork sessions) — this post's three named example workflows (Claim 1:
    research memos, board due-diligence decks, contract redlines) are all
    non-engineering knowledge-work examples, consistent with that quantified split.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 10 (supervised-then-scheduled
    autonomy progression, Level 2→3) — this post's plan-review panel (Claim 12)
    describes the validation mechanism practitioners use *during* that supervised
    phase, before they've earned the confidence to remove the checkpoint.
  - `blog-simonwillison-claude-fable-5.md` Claim 2 (Anthropic states the Claude API
    "has new mechanisms for letting you know when you hit [guardrails]") — this
    post's classifier/fallback description (Claim 7) restates and specifies that
    general claim for the cybersecurity/bio-chem classifier case specifically
    ("users are informed whenever this occurs"). See Contradicts below for where
    this same claim conflicts with a different corpus source.
  - `blog-simonwillison-fable-silent-interventions.md` Claims 6–7 (Anthropic's
    2026-06-10/11 reversal of its silent frontier-LLM-development degradation
    policy) — this is the strongest first-party corroboration in the corpus for
    this post's Claim 7 notification guarantee, and it is the documented *origin*
    of that guarantee: after community backlash, Anthropic's June 11 statement
    committed that "Starting this week, flagged requests will visibly fall back to
    Opus 4.8—the same as our safeguards for cyber and bio" (Claim 6), and the
    reversal statement's notification language (Concrete Artifacts → Anthropic
    Reversal Statement) reads "You will see this every time it happens." This July
    16 post's cybersecurity/bio-chem classifier notification promise ("users are
    informed whenever this occurs") is the same commitment restated as settled
    Cowork policy roughly five weeks later. Note the timing relationship: the June
    reversal established the visible-fallback-with-notification standard; this post
    describes it as the shipped default. The corroboration and the Contradicts
    entry below are not in tension — Anthropic's *stated* policy (June reversal →
    this post) is consistent notification, while the contradiction concerns whether
    that stated policy held in a specific observed session (see Contradicts).
    Claim 7 of that note also names Anthropic's own rationale for why it originally
    chose *invisible* safeguards ("Invisible safeguards can be targeted more
    narrowly, allowing us to ship quickly with very few false positives... that was
    the wrong tradeoff"), which contextualizes this post's admission that the
    conservatively-tuned classifiers "sometimes catch harmless requests."

- **Contradicts**: Filed as
  [steveash/hitchhikers-guide-to-ai-native-engineering#1974](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1974).
  This post's Claim 7 states that when Fable 5's misuse classifiers trigger and the
  session falls back to Opus 4.8, "users are informed whenever this occurs."
  `blog-simonwillison-fable-relentlessly-proactive.md` Claim 5 documents a specific,
  first-person, dated instance (June 11, 2026, in Claude Code) of Fable "silently"
  downgrading itself to Opus mid-session with no notification Willison could
  observe — he had to infer the switch himself. No verdict is picked here; the
  filed issue notes a plausible but unstated reconciling variable (timing/product
  surface: Willison's session predates this post by five weeks and was in Claude
  Code rather than Cowork).

- **Extends**:
  - `01-daily-workflows.md`'s "When NOT to Delegate" framework and
    `blog-anthropic-fable-finding-unknowns.md`'s pre-implementation techniques
    (blind spot pass, interviews, references) — this post's three-way delegation
    taxonomy (Claim 8: approach / procedure / timing) and its "interview me" /
    "give me three directions" starting prompts (Claim 9, Concrete Artifacts) are a
    Cowork-specific, more product-integrated version of the same underlying
    practice: describe an outcome and let the model ask the clarifying questions,
    rather than pre-specifying every step.
  - `blog-anthropic-cowork-enterprise.md` Claim 7 (skills-as-shared-infrastructure;
    no enterprise skill lifecycle policy documented) — this post's "audit your
    skills/memory for stale model-specific corrections" recommendation (Claim 13)
    is a concrete, individual-level maintenance practice that partially fills the
    lifecycle gap that note flagged as ungoverned, though only at the level of a
    single user's own skills, not an organizational policy.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 1 (Chat/Cowork/Code three-surface
    decision framework) — this post is a worked example of choosing *within* the
    Cowork surface (which model, which effort) once a practitioner has already
    decided Cowork is the right surface; it does not revisit the surface-choice
    question itself.

- **Novel**:
  - **A Cowork-specific three-tier model-selection heuristic** (Claim 5: Sonnet 5
    default/everyday, Opus for well-defined deep work, Fable for complex/ambiguous
    multi-tool work) is not documented elsewhere in the corpus; prior Cowork
    sources cover governance and adoption maturity, not per-task model choice.
  - **Effort setting as a lever independent of model choice, specific to Fable 5 in
    Cowork** (Claim 6) is new — no prior corpus source documents the Cowork effort
    dial's interaction with model selection.
  - **The classifier/fallback-to-Opus-4.8 mechanism and its stated user-notification
    guarantee** (Claim 7) is the first corpus source to name these specific
    classifiers (cybersecurity, biology/chemistry) and state a notification
    guarantee — which a prior source then contradicts (see Contradicts).
  - **The three-way delegation taxonomy** (Claim 8: approach / procedure / timing)
    with matching example prompts is a new, reusable vocabulary not present
    elsewhere in the corpus.
  - **The mid-run plan-correction-without-restart mechanism** (Claim 12) is a new,
    concrete description of Cowork's live plan panel as a redirect point, distinct
    from post-hoc review.
  - **"Audit your skills/memory for prior-model-specific corrections" as a named
    maintenance practice** (Claim 13) with a reusable audit prompt is new to the
    corpus.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add the Sonnet-5/Opus/Fable-5 model-selection
  heuristic (Claim 5) as Cowork-specific guidance alongside the existing "Model
  Deprecation Is a Recurring Governance Event" section — note the "as of the time
  of publication" qualifier on Sonnet 5 being the default, since the post itself
  flags this as time-bound.
- **Chapter 05 (Team Adoption)**: In the "Verification Before Autonomy" /
  "verification ramp" sections, add the plan-panel mid-run correction mechanism
  (Claim 12) as a concrete Cowork-specific instance of catching errors before they
  reach the finished output, complementing the existing supervised-then-scheduled
  autonomy pattern already cited from `blog-anthropic-cowork-deploy-guide.md`.
- **Chapter 01 (Daily Workflows)**: In "When NOT to Delegate," add the three-way
  delegation taxonomy (Claim 8) and the "interview me" / "give me three directions"
  starting prompts (Claim 9) as a Cowork-flavored refinement of that framework —
  the taxonomy gives practitioners named categories (approach/procedure/timing)
  for what "delegate fully" can mean beyond a single fire-and-forget instruction.
- **Chapter 04 (Context Engineering)**: Add the context-vs-constraints framing
  (Claim 10) as a companion to the existing map/territory framing sourced from
  `blog-anthropic-fable-finding-unknowns.md` — cite both together as two
  complementary articulations of "why context outperforms a fixed rule list."
- **Chapter 04 (Context Engineering)**: Add the "audit skills/memory for
  stale model-specific corrections" practice (Claim 13) as a maintenance
  recommendation whenever a team upgrades its default coding/Cowork model — flag
  that this is currently an individual-level practice with no organizational
  tooling, per the unresolved gap in `blog-anthropic-cowork-enterprise.md` Claim 7.
- **Chapter 05 (Team Adoption) or a future security/guardrails section**: If the
  guide adds content on model-layer safety fallback behavior, cite this post's
  classifier/fallback claim (Claim 7) alongside the filed contradiction
  (#1974) rather than treating "users are informed whenever this occurs" as
  settled — the guide should not assert a notification guarantee without flagging
  the counter-evidence.

## Extraction Notes

- **WebFetch's summarization pass was insufficient and was not used for quotes.**
  An initial WebFetch call returned only a paraphrased summary (with a note that it
  was a summary, not verbatim text). I fetched the raw page HTML directly via
  `curl` with a browser user agent, stripped markup with a small Python
  `HTMLParser`-based script, and extracted the full article body (confirmed at
  `/tmp/fable5-cowork.txt` in the extraction session, lines 275–392 covering the
  headline through the closing byline). Every `Quote` field above was copied
  character-for-character from that raw-text extraction, not from the WebFetch
  summary.
- **The post links to a separate "prompting guide for Claude Fable 5"** ("Our
  prompting guide for Claude Fable 5 provides a detailed list of capability
  improvements and recommended behavior and prompting changes") and to "how model
  choice and effort interact in Claude Code" — neither link target was followed;
  both are described in the post as covering broader, non-Cowork-specific ground,
  and following them would extract a different source's content under this issue's
  URL. If either is independently submitted as a source later, this note's Claims
  5–6 should be cross-checked against it.
- **The post is by Josefina Albert of Anthropic's Education team**, not the Claude
  Code/Cowork product team byline seen on some other Cowork posts in the corpus —
  noted in Source Context; this does not change the settled/first-party grading of
  feature descriptions, since the post speaks in Anthropic's institutional voice
  throughout ("We recommend," "We tuned these safeguards," "In our testing").
- **Contradiction filed before this PR was opened**, per MINER.md §4a: see
  [#1974](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1974).
  No verdict is picked in this note. (Note: #1974's Side A originally cited a
  transposed filename `blog-anthropic-fable-5-cowork-working-with.md` that never
  existed; the citation has been corrected to this PR's actual filename
  `blog-anthropic-cowork-fable-5-working-with.md` and the issue reopened so a
  fresh contradiction assessment can run against the real note.)
- **Confidence calibration**: Feature/mechanism descriptions (model defaults,
  effort mechanics, classifier existence, usage-cost mechanism, plan-panel UI) are
  **settled** first-party product descriptions. Comparative capability claims
  (Claim 3's "previous models lost track," Claim 6's "matched or exceeded... at
  their highest effort levels") are **emerging** — directionally stated by the
  vendor but unquantified. The worked examples and delegation taxonomy (Claims 4,
  8, 9, 10, 13) are **anecdotal** — illustrative, unnamed or single-anecdote, not
  measured. Overall **emerging**: the post mixes settled feature description with
  enough unquantified comparative and anecdotal material, plus one claim now
  directly contradicted by an existing source, that it should not be graded
  settled overall.
- Cross-references verified against the cited source notes before writing:
  `blog-anthropic-fable-finding-unknowns.md` Claim 2 (map/territory quote
  confirmed at lines 67-69 of that note); `blog-anthropic-cowork-usage-taxonomy.md`
  Claim 4 (developer Cowork-usage split confirmed at lines 97-99);
  `blog-anthropic-cowork-deploy-guide.md` Claim 10 (supervised-then-scheduled
  progression confirmed at lines 238-241) and Claim 1 (three-surface framework
  confirmed at lines 57-58); `blog-simonwillison-claude-fable-5.md` Claim 2
  (guardrail notification mechanism confirmed at lines 58-59);
  `blog-simonwillison-fable-relentlessly-proactive.md` Claim 5 (silent downgrade
  confirmed at lines 124-125); `blog-anthropic-cowork-enterprise.md` Claim 7
  (skills-as-shared-infrastructure, no lifecycle policy, confirmed at lines
  166-183); `blog-simonwillison-fable-silent-interventions.md` Claim 6 ("Starting
  this week, flagged requests will visibly fall back to Opus 4.8..." reversal
  commitment confirmed at lines 176-177, and the "You will see this every time it
  happens" notification line confirmed in that note's Concrete Artifacts →
  Anthropic Reversal Statement at line 271) and Claim 7 (Anthropic's stated
  rationale for originally choosing invisible safeguards confirmed at lines
  193-195) — added as the primary first-party corroboration for this note's
  Claim 7 notification guarantee.
