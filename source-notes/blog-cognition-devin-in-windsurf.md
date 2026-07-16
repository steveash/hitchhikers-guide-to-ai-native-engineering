---
source_url: https://cognition.com/blog/devin-in-windsurf
source_type: blog-post
title: "Devin in Windsurf"
author: The Cognition Team
date_published: 2026-04-15
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1929"
---

# Devin in Windsurf

> Cognition's short product-philosophy post arguing local and cloud agents are
> not competing options but complementary roles (local = plan/think,
> cloud = delegate/execute), instantiated as a shipped, one-click handoff from
> Windsurf 2.0 (local agentic IDE) to Devin (cloud agent), with PR review
> looped back into Windsurf.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  2026-04-15; byline "By The Cognition Team," no individual author named)
- **Author credibility**: Published directly by Cognition, the company that
  builds Devin (autonomous cloud coding agent) and, as of this post, also
  writes about Windsurf (the agentic IDE) as its own product — a companion
  Cognition post (`cognition.com/blog/swe-grep`) refers to "the combined
  Cognition+Windsurf," confirming the two products now share a vendor. This
  is a first-party product-philosophy and feature-announcement post, not an
  independent or customer-side account. No named individual, no customer
  quote, and no metric of any kind appears anywhere in the post.
- **Scope**: Covers Cognition's stated philosophy of local vs. cloud agent
  roles (attention ceiling vs. independent execution), a brief history of
  Devin's push toward operating without a human in the loop, and the
  concrete Windsurf 2.0 mechanics for delegating a locally-planned task to
  Devin and reviewing the resulting PR back in Windsurf. Does NOT cover: any
  metric (adoption, session duration, success rate, cost), any named
  practitioner or customer using the integration, exact technical
  implementation of the "single click" handoff, what happens on delegation
  failure, or any comparison data versus not using the integration. This is
  the thinnest kind of source in this corpus's Cognition cluster by
  evidentiary density — a product-philosophy post with one shipped feature
  described only at the level of user-visible mechanics.

## Extracted Claims

### Claim 1: A local agent is bound to the developer's own session and machine and stops when the laptop closes — its capability ceiling is the developer's own attention, not the model
- **Evidence**: Opening framing statement distinguishing local from cloud
  agents by execution lifetime and the limiting resource.
- **Confidence**: emerging (first-party framing of a real architectural
  distinction — local processes do stop when the machine sleeps/closes —
  presented as product philosophy rather than a measured claim)
- **Quote**: "A local agent runs on your machine, in your session, but when you close your laptop, it stops. The ceiling on a local agent is your attention."
- **Our assessment**: "The ceiling on a local agent is your attention" is a
  compact, citable framing for why local IDE-based agents cannot scale past
  a single human's real-time supervision, regardless of model capability —
  the constraint is architectural (session-bound execution), not a model
  quality gap. This is the same underlying constraint Cursor's CEO states
  structurally in `blog-cursor-third-era.md` Claim 5 ("synchronous agents
  compete for resources on the local machine, means it is only practical to
  work with a few at a time"), though that source frames the ceiling as
  concurrency/resource contention while this source frames it as attention —
  two related but distinct articulations of the same local-execution limit.

### Claim 2: Devin is defined as a cloud agent that runs in its own infrastructure and environment, can work for minutes or hours "past the async valley of death," and independently opens PRs, runs tests, QAs its own work via computer vision, and notifies the user on completion
- **Evidence**: Direct definitional statement of Devin's product category and
  named capability list, including a reference (hyperlinked in the source)
  to Cognition's own "Semi-Async Valley of Death" concept from a separate
  post.
- **Confidence**: emerging (first-party capability description for a
  shipped, purchasable product; no session-duration data, success rate, or
  worked example accompanies the claim in this post)
- **Quote**: "Devin is a cloud agent. It runs in its own infrastructure and in its own environment. Devin can work for minutes or hours, past the async valley of death. It opens PRs, runs tests, QAs its own work using computer vision, and lets you know when it's done."
- **Our assessment**: The four named capabilities (open PRs, run tests, QA
  via computer vision, notify on completion) form a compact definition of
  what "done" looks like for a cloud agent session, consistent with and
  extending the self-verification workflow already documented in detail in
  `blog-cognition-verifying-agentic-development.md` (test-plan generation,
  computer-use QA, structured test report) — this post is the marketing-level
  summary of the same underlying capability that source documents at
  implementation depth. The "async valley of death" reference is unglossed
  in this article; the linked companion post
  (`cognition.com/blog/swe-grep`) names it "Semi-Async Valley of Death" and
  describes it only as a state to "avoid... at all costs," without a formal
  definition — see Extraction Notes.

### Claim 3: A local agent makes the developer faster; a cloud agent does the work while the developer is not there
- **Evidence**: Single-sentence summary statement immediately following the
  local/cloud definitions (Claims 1-2), functioning as the post's thesis
  line.
- **Confidence**: emerging (first-party philosophical framing, stated as a
  clean dichotomy rather than a measured comparison)
- **Quote**: "A local agent makes you faster, but cloud agents do the work while you're not there."
- **Our assessment**: This is the single most quotable sentence in the post
  for a guide chapter on choosing between agent modalities — it draws the
  line not on capability tier (weaker vs. stronger model) but on whether the
  human's presence is required for the work to proceed. Should be cited
  alongside Claim 5 (division-of-labor detail) rather than in isolation,
  since on its own it risks oversimplifying to "local = fast, cloud = slow,"
  which is not the distinction the source is actually making.

### Claim 4: Cognition frames Devin's entire release history as a progression toward operating without a human in the loop, naming four specific milestones: self-testing via computer use, reviewing and auto-fixing its own code, managing teams of sub-agents in parallel, and scheduling its own work
- **Evidence**: Direct retrospective statement naming four capability
  milestones as a single progression, with no dates or version numbers
  attached to any of the four.
- **Confidence**: anecdotal (retrospective self-narrative naming four
  capabilities with zero dates, version numbers, or release identifiers —
  each milestone is independently more fully documented elsewhere in this
  corpus, see Cross-References, but this post itself supplies no evidence
  beyond the list)
- **Quote**: "We've been building Devin to operate independently from the start. Each release has pushed it further toward working without you in the loop: self-testing with computer use, reviewing and auto-fixing its own code, managing teams of sub-agents in parallel, and scheduling its own work."
- **Our assessment**: Useful primarily as an index into this corpus's
  existing, better-evidenced Cognition sources: "self-testing with computer
  use" is documented in depth in
  `blog-cognition-verifying-agentic-development.md`; "managing teams of
  sub-agents in parallel" is documented in
  `blog-cognition-auto-triage.md` Claim 3 (sub-Devins investigating in
  parallel) and in the "10 to 20 Devins in parallel" anecdote in
  `blog-cognition-verifying-agentic-development.md` Claim 3. "Reviewing and
  auto-fixing its own code" and "scheduling its own work" are not
  independently documented elsewhere in this corpus at time of writing — see
  Cross-References → Novel.

### Claim 5: The recommended workflow explicitly composes both modalities: local agents are for planning, prototyping, and iterating work that requires hands on the keyboard; cloud agents are for delegated work that must get done but does not require being watched over the shoulder — specifically implementation, testing, QA, and deployment
- **Evidence**: Direct division-of-labor statement under the "Local and cloud
  agents" heading, naming the specific task categories assigned to each
  modality.
- **Confidence**: emerging (first-party workflow prescription; internally
  consistent with the rest of the post but not validated by any named
  practitioner's actual usage pattern)
- **Quote**: "A local agent is where you think. You use one or multiple local agents to plan, prototype, and iterate the work that requires your hands on the keyboard. A cloud agent is where you delegate work that needs to get done but doesn't need you watching over the shoulder: implementation, testing, QA, and deployment."
- **Our assessment**: This is the post's most concrete, actionable claim: a
  named four-item task list (implementation, testing, QA, deployment)
  assigned specifically to cloud agents, with planning/prototyping/iteration
  assigned to local agents. This is a specific instance of the general
  "start locally then delegate work to the cloud" deployment mode already
  named abstractly in `blog-cursor-cloud-agent-lessons.md` Claim 6 (an agent
  "might run on one machine, spawn async subagents across several, or start
  locally then delegate work to the cloud") — this source supplies the task
  taxonomy that determines *what* gets delegated and *why* (attention
  requirement, not just architectural flexibility), which Cursor's source
  does not name explicitly.

### Claim 6: With a local agent the developer works faster; with a cloud agent the developer can parallelize themselves
- **Evidence**: Second summary-line statement, immediately following the
  division-of-labor claim (Claim 5), restating the value proposition in
  terms of the developer's own multiplicative capacity rather than task type.
- **Confidence**: emerging (first-party framing; "parallelize yourself" is
  presented as a natural consequence of delegating rather than watching, not
  independently measured)
- **Quote**: "With a local agent, you're faster. With a cloud agent, you can parallelize yourself."
- **Our assessment**: "Parallelize yourself" is a distinct framing from
  Claim 3's "cloud agents do the work while you're not there" — this version
  emphasizes that the developer can be doing something else (including
  running another local or cloud agent) concurrently with a delegated cloud
  session, connecting directly to the "engineers running 10 to 20 Devins in
  parallel" anecdote already documented in
  `blog-cognition-verifying-agentic-development.md` Claim 3. Together the
  two sources describe the same underlying capacity-multiplication argument
  for cloud agents at two different scales: this post frames it as "you,
  personally, doing two things at once," while the other frames it as an
  observed extreme (one engineer running 10-20 sessions).

### Claim 7: Windsurf 2.0 ships a concrete, named integration: plan locally in Windsurf, send the plan to Devin with a single click for implementation, and Devin spins up its own machine while the developer keeps coding or steps away entirely
- **Evidence**: Direct product-mechanics description under the "Devin in
  Windsurf" heading, naming the trigger action (single click) and Devin's
  resulting behavior (spins up its own machine).
- **Confidence**: emerging (first-party description of a shipped,
  named-version feature — Windsurf 2.0 — with a specific trigger mechanism
  named; no detail on what happens if the click-to-delegate action fails, or
  how the plan is structured/passed to Devin)
- **Quote**: "You work locally in Windsurf to understand the codebase and put together a plan. With a single click, you send it to Devin for implementation. Devin spins up its own machine and gets to work. In the meantime, you keep coding, or you close your laptop and grab a coffee."
- **Our assessment**: This is the single concrete, named integration surface
  in the post — a specific product (Windsurf 2.0), a specific trigger (one
  click), and a specific handoff artifact (a plan produced locally). It is
  the shipped instantiation of the abstract division of labor stated in
  Claim 5. No detail is given on what the "plan" actually consists of
  (a written spec? a task description? a set of file references?) or on
  what user-visible feedback exists between the click and Devin's PR, beyond
  what Claim 8 covers for the return side of the loop.

### Claim 8: When Devin opens a PR, the developer reviews it inside Windsurf — checking the diff, running tests, or handing it to a local agent for touch-ups — closing the full plan → delegate → monitor → review loop in one tool
- **Evidence**: Direct product-mechanics description of the review side of
  the integration, naming three specific reviewer actions and an explicit
  closing statement about the loop being unified in one place.
- **Confidence**: emerging (first-party description of shipped review
  mechanics; no detail on review latency, what "hand it off to your local
  agent for touch-ups" looks like technically, or how often review actually
  triggers a local-agent touch-up versus a direct merge)
- **Quote**: "When Devin opens a PR, you review it right in Windsurf. You can check the diff, run tests, or hand it off to your local agent for touch-ups. The whole loop of planning, delegating, monitoring, and reviewing all happens in one place."
- **Our assessment**: "Hand it off to your local agent for touch-ups" is the
  most operationally interesting detail in the post: it describes a
  three-hop handoff chain (local plan → cloud implementation → local
  touch-up) rather than a one-way delegation, meaning the local agent's role
  is not only upstream planning but also downstream polishing of cloud
  output. This is a more granular loop than the general "local agent, cloud
  agent" binary stated in Claims 1-3 — the same tool (a local agent in
  Windsurf) appears on both ends of the delegation, with Devin doing the
  bulk implementation work in between. No detail is given on how common the
  touch-up path is relative to a direct merge of Devin's PR.

## Concrete Artifacts

### Full local/cloud agent framing (verbatim, from the article)

```
Source: cognition.com/blog/devin-in-windsurf, "By The Cognition Team," 04.15.26

"Most people treat local and cloud agents as the same thing, but they're
not. A local agent runs on your machine, in your session, but when you
close your laptop, it stops. The ceiling on a local agent is your
attention.

Devin is a cloud agent. It runs in its own infrastructure and in its own
environment. Devin can work for minutes or hours, past the async valley of
death. It opens PRs, runs tests, QAs its own work using computer vision,
and lets you know when it's done.

A local agent makes you faster, but cloud agents do the work while you're
not there."
```

### Devin/Windsurf handoff loop, as described (verbatim, from the article)

```
Source: cognition.com/blog/devin-in-windsurf, "Devin in Windsurf" section

Step 1 (local): "You work locally in Windsurf to understand the codebase
  and put together a plan."
Step 2 (handoff): "With a single click, you send it to Devin for
  implementation."
Step 3 (cloud): "Devin spins up its own machine and gets to work. In the
  meantime, you keep coding, or you close your laptop and grab a coffee."
Step 4 (review, back in the local tool): "When Devin opens a PR, you review
  it right in Windsurf. You can check the diff, run tests, or hand it off
  to your local agent for touch-ups."
Closing statement: "The whole loop of planning, delegating, monitoring, and
  reviewing all happens in one place."
```

### Companion-post context: "Semi-Async Valley of Death" (from a linked Cognition post, not the primary source)

```
Source: cognition.com/blog/swe-grep (linked from the "async valley of
death" phrase in the primary source's Claim 2 quote; fetched as a
substantive followed link per MINER.md §1)

"Our ultimate goal at the combined Cognition+Windsurf is to maximize your
software engineering productivity, and we are simultaneously researching
both the directions of pushing the frontier of coding agent autonomy -AND-
making them faster given a 'good enough' bar. The best mental model we've
found is the one we've arrived at below - avoid the Semi-Async Valley of
Death at all costs!"

Note: this companion post names but does not formally define the term; it
is presented as a mental-model heuristic, not a specified threshold. See
Extraction Notes.
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-third-era.md` Claim 5 ("synchronous agents compete for
    resources on the local machine, means it is only practical to work with
    a few at a time") — this source's Claim 1 ("the ceiling on a local agent
    is your attention") names the same local-execution ceiling from an
    independent vendor (Cognition vs. Cursor), framing it as an attention
    constraint rather than a resource-contention constraint, but both
    sources agree local/synchronous agents structurally cannot scale to many
    concurrent sessions the way cloud agents can.
  - `blog-cursor-cloud-agent-lessons.md` Claim 6 (an agent "might run on one
    machine, spawn async subagents across several, or start locally then
    delegate work to the cloud") — this source's Claim 5 and Claim 7 are a
    concrete, named, shipped instance of exactly this "start locally then
    delegate to the cloud" deployment mode, from a second, independent
    vendor (Cognition/Windsurf rather than Cursor), adding the specific task
    taxonomy (implementation, testing, QA, deployment → cloud; planning,
    prototyping, iteration → local) that the Cursor source states only as an
    architectural possibility without naming which tasks go where.
  - `blog-cognition-verifying-agentic-development.md` Claim 3 (engineers
    observed running "10 to 20 Devins in parallel, each with its own dev
    server") — this source's Claim 6 ("with a cloud agent, you can
    parallelize yourself") is the same capacity-multiplication argument
    stated as product philosophy here and as an observed extreme there;
    together they move the parallelization claim from a single anecdote
    toward a stated, repeated product thesis.
  - `blog-cognition-auto-triage.md` Claim 3 ("spin up sub-Devins to
    investigate in parallel") — corroborates this source's Claim 4 detail
    that Devin manages "teams of sub-agents in parallel," giving that
    specific milestone claim a concrete, previously-documented mechanism
    (parallel sub-Devin investigation) rather than leaving it as an
    unsupported list item.

- **Contradicts**: None filed. One candidate tension was considered and
  rejected: `blog-cursor-third-era.md` Claim 11 (Cursor's CEO predicts "the
  vast majority of development work" will be done by cloud agents within a
  year, implying local/synchronous agents recede toward a minority role)
  appears to sit in tension with this source's framing that local and cloud
  agents are stable, permanent complementary roles ("the best workflow isn't
  restricted to just local or cloud agents"). This does not meet the
  MINER.md §4a bar for filing: the two claims measure different things —
  Cursor's claim is about the proportion of total *implementation volume*
  that will run on cloud infrastructure, while this source's claim is about
  which *task types* (planning vs. execution) belong to which modality. A
  world where cloud agents execute the large majority of implementation
  work is fully consistent with local agents remaining the necessary
  front-end for planning that work — the two sources are not making
  opposing claims under matching conditions, they are answering different
  questions (volume share vs. workflow role).

- **Extends**:
  - `blog-cognition-verifying-agentic-development.md` — that source
    documents Devin's self-verification mechanics (test plans, annotation,
    skills, hard edges) at implementation depth; this source's Claim 2
    references the same self-testing capability only as a one-line summary
    ("QAs its own work using computer vision") within a broader
    product-philosophy post. Read together, this source supplies the
    workflow-level "why this matters" framing (local/cloud division of
    labor) that the verifying-agentic-development note does not cover, while
    that note supplies the mechanism depth this source lacks.
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 11 (Cognition's
    founding product bet — that agents should run in the cloud for hours at
    a time — "was not viable with the models available during the company's
    first year," with Fable 5 named as the model that "makes the full
    version of that bet viable") — this source's Claim 2 (Devin working "for
    minutes or hours, past the async valley of death") is the product-level
    manifestation of the model-capability threshold that source documents;
    together they connect a specific model-capability claim (Fable 5 enables
    multi-hour unattended runs) to the specific product feature (Devin as a
    cloud agent, shippable as a Windsurf integration) that depends on it.

- **Novel**: The explicit local/cloud task taxonomy (Claim 5: planning,
  prototyping, iteration → local; implementation, testing, QA, deployment →
  cloud) is new to this corpus — prior sources establish that local and
  cloud agents differ architecturally (concurrency, resource contention) but
  none previously named which specific task categories belong to which
  modality as product guidance. The "async valley of death" term (Claim 2)
  and its unglossed companion-post reference to a "Semi-Async Valley of
  Death" mental model are also new to this corpus. The specific three-hop
  handoff chain — local plan → cloud implementation → local touch-up (Claim
  8) — is a more granular loop than any prior source's local/cloud
  composition pattern, which stopped at a one-way "local then cloud"
  handoff (e.g. `blog-cursor-cloud-agent-lessons.md` Claim 6) without a
  documented return trip through a local agent for polishing.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add Claim 1 ("the ceiling on a local
  agent is your attention") and Claim 5 (the explicit task taxonomy: local
  for planning/prototyping/iteration, cloud for implementation/testing/
  QA/deployment) as a concrete, citable framework for readers deciding when
  to stay in a local IDE agent versus delegate to a cloud agent. This is
  more specific and actionable than the corpus's existing local/cloud
  coverage (`blog-cursor-third-era.md`'s resource-contention framing,
  `blog-cursor-cloud-agent-lessons.md`'s abstract "start locally then
  delegate" deployment mode) because it names the actual task categories,
  not just the architectural possibility. Flag clearly that this is vendor
  philosophy with zero adoption or outcome data behind it — not a
  practitioner-validated best practice.

- **Chapter 01 (Daily Workflows) / Chapter 02 (Harness Engineering)**: Add
  Claim 7 and Claim 8 (the concrete Windsurf 2.0 mechanics: single-click
  plan handoff, Devin spins up its own machine, PR review back in Windsurf
  with an optional local-agent touch-up step) as a named, shipped example of
  a local-IDE-to-cloud-agent integration surface — useful as a concrete
  reference point for teams building or evaluating similar
  plan-locally/execute-in-cloud/review-locally loops, regardless of which
  specific vendor tools they use. Flag that no detail is disclosed on plan
  format, failure handling, or how often the local-touch-up step is actually
  used versus a direct merge.

- **Chapter 04 (Context Engineering)**: If the guide discusses how planning
  artifacts are handed from a human-in-the-loop phase to an unattended
  execution phase, add Claim 7's "you work locally... to put together a
  plan... with a single click, you send it to Devin for implementation" as
  a named instance of plan-as-handoff-artifact, alongside the existing
  corpus's cloud-agent-environment material
  (`blog-cursor-cloud-agent-dev-environments.md`) on what a cloud agent
  needs to execute a delegated task successfully.

## Extraction Notes

- The primary article is very short (~350 words across an intro paragraph,
  two named sections — "Local and cloud agents" and "Devin in Windsurf" —
  and a closing "Try it out now" call-to-action with two outbound links).
  It was fetched in full via WebFetch, and specific sentences were
  independently re-fetched and cross-checked in three separate passes
  (the full-article pass, a targeted pass isolating the "valley of death"
  and "We've been building Devin" sentences, and a full outbound-link
  listing pass) to confirm verbatim accuracy before quoting, consistent
  with MINER.md §2a. All quotes above matched character-for-character
  across the repeated fetches.
- One substantive linked page was followed per MINER.md §1: the inline
  hyperlink on the phrase "async valley of death," which resolves (via a
  301 redirect from `cognition.ai/blog/swe-grep` to
  `cognition.com/blog/swe-grep`) to a separate Cognition post about a
  code-search tool. That post names a related but not identical term
  ("Semi-Async Valley of Death," not "async valley of death") and does not
  formally define it — it is used there as an unexplained mental-model
  heuristic. I did not attempt to independently define or resolve this term
  beyond what the swe-grep post itself states, since doing so would go
  beyond what either source actually says. The four other outbound links on
  the primary page (Windsurf 2.0 launch post, Windsurf download page, and
  the site's own nav/article footer links) were also checked: the Windsurf
  2.0 launch post (`windsurf.com/blog/windsurf-2-0`, redirecting to
  `devin.ai/blog/windsurf-2-0`) was fetched twice, but WebFetch returned
  only a paraphrased summary both times (on the second attempt, the
  fetching sub-model explicitly declined to reproduce verbatim text, citing
  an internal ~125-character quote-length constraint) — consistent with the
  verbatim-extraction difficulty already documented in several other
  Cognition/Thoughtworks source notes in this corpus (e.g.
  `blog-cognition-verifying-agentic-development.md` Extraction Notes). No
  quote from that page is used anywhere in this note; its content (a
  three-section structure: "The Agent Command Center," "Windsurf Spaces,"
  "Devin in Windsurf") is mentioned only as unquoted confirmation that the
  same Devin-Windsurf mechanics described in the primary source are also
  described on the Windsurf-branded launch post, not as an independent
  source of claims.
- Confidence is rated `emerging` rather than `anecdotal` because the post
  describes concrete, shipped, named-version (Windsurf 2.0) product
  mechanics with specific user-visible steps (single-click handoff, PR
  review location), which is more falsifiable than a pure statement of
  intent — but it is rated no higher than `emerging` because zero metrics,
  zero named practitioners, and zero customer validation appear anywhere in
  the post, unlike `blog-cognition-auto-triage.md`, which has one named
  customer quote (Modal) at the same overall confidence tier.
- Cross-references verified before writing: re-read
  `blog-cursor-third-era.md` in full and confirmed Claim 5 and Claim 11 by
  number and content; re-read `blog-cursor-cloud-agent-lessons.md` in full
  and confirmed Claim 6 by number and content; re-read
  `blog-cognition-verifying-agentic-development.md` in full and confirmed
  Claim 3 by number and content; re-read `blog-cognition-auto-triage.md` in
  full and confirmed Claim 3 by number and content; re-read
  `blog-anthropic-cognition-fable5-frontier-trust.md` in full and confirmed
  Claim 11 by number and content. No claim number was guessed or
  approximated.
- The source issue (#1929) carries three separate Prospector triage
  comments, apparently from repeated/duplicate triage runs, with mutually
  inconsistent chapter-numbering schemes (none of which match this guide's
  actual chapter files: `00-principles.md` through `06-security-threat-model.md`).
  This note's Guide Impact section cites the guide's actual chapter numbers
  and titles as read directly from the `guide/` directory, not the numbering
  used in any of the three triage comments.
- No contradiction meeting the MINER.md §4a filing bar was identified — see
  Cross-References → Contradicts for the one candidate considered and
  rejected as a conditioning-variable difference (volume share vs. workflow
  role), not a same-claim conflict. No contradiction issue filed.
