---
source_url: https://news.ycombinator.com/item?id=47295954
source_type: failure-report
platform: hn
title: "I was \"early\" in agentic coding. Here's my story"
author: noemit (anonymous HN user)
date_published: 2026-03-08
date_extracted: 2026-04-15
last_checked: 2026-04-15
status: current
confidence_overall: anecdotal
issue: "#54"
---

# Failure Report: Early Agentic Coding Adoption Friction — Medical Necessity, >50% Rejection Rate, Naming Convention Violations

> An anonymous HN practitioner who adopted Cursor under medical necessity (Guillain-Barré
> Syndrome requiring voice-to-text coding) documents early agentic coding as genuinely
> difficult — >50% rejection rate, requirement for extreme prompt granularity, and
> persistent naming-convention violations — before reaching pragmatic neutral acceptance
> after ~18 months as model capabilities improved. The post's primary guide value is not
> the failure itself but what it reveals: adoption-friction reports are filtered by who
> stayed to complain, and accessibility-driven adoption produced a rare data point from
> someone who could not abandon the tool when the friction peaked.

## Source Context

- **Platform**: Hacker News self-post, 4 points, 2 comments (one reply thread), 2026-03-08
- **Author credibility**: noemit is an anonymous HN account. The post is credible as a
  lived-experience account — the Guillain-Barré Syndrome diagnosis, hospitalization, and
  six-month recovery timeline are specific and biographical rather than constructed. The
  author is not a researcher or tool vendor; they are a working programmer forced into the
  adoption path by medical necessity rather than by choice. This distinction matters: the
  post documents friction that was tolerated rather than abandoned, a data point most
  adoption narratives cannot provide. Low HN engagement (4 points) means the post has
  not been crowd-validated.
- **Community response**: Only one substantive reply (actionfromafar), asking how the
  workflow has evolved from early adoption to the present. noemit's reply describes the
  shift from high rejection rate to substantially higher acceptance, and names the specific
  improvement: the model no longer renames things. The thread is primarily biographical
  narrative with one constructive follow-up exchange.

## What Was Attempted

- **Goal**: Resume software development during and after recovery from Guillain-Barré
  Syndrome, which caused progressive paralysis and loss of fine motor control (hand
  dexterity and typing ability).
- **Tool/approach**: Cursor IDE with voice-to-text as the primary input modality. Also
  experimented with ChatGPT in early 2024 and tried Claude Code at some point, but
  returned to Cursor.
- **Setup**: Individual developer. The paid Cursor subscription began October 2024; earlier
  experimentation with ChatGPT and a first Cursor attempt predated this. Language and
  project type not specified.

## What Went Wrong

### Failure Mode 1: Pre-illness voluntary adoption — early tools too unreliable to overcome
initial friction

- **Symptoms**: Author tried ChatGPT and Cursor in early 2024, found them unreliable,
  described the experience as "a chore to use them," and abandoned Cursor after one
  attempt.
- **Severity**: Adoption deterrent — the tools were not good enough to overcome voluntary
  friction at that stage.
- **Reproducibility**: Consistent with the general state of code-generation tools in early
  2024. The "chore" framing reflects model capabilities at that time, not current state.

### Failure Mode 2: Early forced-adoption phase — >50% rejection rate, extreme granularity
required

- **Symptoms**:
  1. Required outlining "in detail really small chunks of code" for the model to produce
     usable output
  2. Required repeating naming conventions on each prompt to prevent the model from
     overwriting them ("I had to repeat how I named things")
  3. Rejection rate exceeded 50% of generated code during the first few months (Oct–Dec
     2024)
- **Severity**: High productivity cost. More than half of generated code was discarded,
  requiring rework and re-prompting effort. Under normal conditions this friction would
  likely have driven abandonment; the medical necessity context prevented that.
- **Reproducibility**: Author describes this as a sustained pattern over "the first few
  months," not a one-off incident.

### Failure Mode 3: Naming convention violations — model overwriting author-defined naming

- **Symptoms**: The model would rename things despite the author attempting to establish
  naming conventions. Required behavioral compensation: explicitly re-stating conventions
  on every prompt session.
- **Severity**: Not blocking, but a consistent drag requiring repeated effort. Named as
  a specific historical failure in the follow-up reply: "it doesn't make mistakes like
  renaming things" — the framing implies this was a recurrent past failure now largely
  resolved.
- **Reproducibility**: Persistent enough to be cited explicitly and contrasted with current
  behavior.

## Root Cause (if identified)

- **Author's diagnosis**: Not explicitly diagnosed for either failure mode. The author
  attributes improvement to two factors: getting "much better at prompting and organizing
  my thoughts" and implicit model capability improvements over time.

- **Our assessment (Failure Mode 2)**: The small-chunk requirement is consistent with
  late-2024 model limitations. Models at that time had shorter effective context windows
  and less robust instruction-following for code generation; working in small, explicitly
  scoped increments was a rational adaptation. This framing is now a best practice
  recommendation; at that time it was a hard constraint.

- **Our assessment (Failure Mode 3)**: Naming convention violations in 2024-era models
  are a well-documented behavior pattern. Without a persistent AGENTS.md or CLAUDE.md
  file (not mentioned by the author), naming context did not survive across sessions.
  The improvement over time reflects both better instruction-following in later models
  and, probably, the author's learned practice of establishing context more explicitly.
  The structural fix (persistent context files) is not one the author describes adopting.

- **Category**: expectation-mismatch + tool-limitation (2024 model capabilities) +
  workflow-design (no persistent context file described)

## Recovery Path

- **What they switched to**: Nothing — the author continued with Cursor throughout
  recovery and into 2026. Voice-to-text remained viable as the primary input modality
  even after partial typing recovery. Tried Claude Code at some point but returned to
  Cursor. The tool did not change; the model improved and the prompting practice improved.
- **Workaround**: Extreme prompt granularity (small chunks), explicit per-session
  repetition of naming conventions. Not formalized as an AGENTS.md / CLAUDE.md pattern
  — behavioral compensation rather than structural mitigation.
- **Current state**: Author accepts substantially more generated code than in the early
  phase. Continues using Cursor as primary IDE and prompts more than codes directly.
  Reports deep gratitude for the accessibility function: "I feel deep gratitude for this
  technology, which eclipses any anxiety or frustration that bubbles up."
- **Unresolved**: The author notes their Cursor unlimited legacy plan expires in May 2026,
  after which Cursor forces all legacy users to new plans with paid tokens. This is a
  near-term cost friction unrelated to agentic coding quality — a pricing transition
  concern, not a quality concern. Addressed in more depth in
  `failure-cursor-ultra-billing-cache-explosion.md`.

## Extracted Lessons

### Lesson 1: Early agentic coding (late 2024) required extremely granular, small-chunk prompting to produce usable output

- **Evidence**: Author's first-person account: "I had to outline in detail really small
  chunks of code for it to write." Sustained over "the first few months" (Oct–Dec 2024),
  not a one-off.
- **Confidence**: anecdotal (single practitioner, but specific and sustained)
- **Actionable as**: The "works best with well-scoped tasks" guidance in current guides is
  not merely a best practice — it was a hard requirement in late 2024. Knowing this
  history lets the guide document capability improvement as a concrete delta, not just an
  abstract claim.

### Lesson 2: Naming convention violations were a recurrent early failure mode for code-generation models; persistent context files are the structural fix

- **Evidence**: Author cites explicit per-session repetition of naming conventions as a
  required compensatory behavior, and contrasts with current state: "it doesn't make
  mistakes like renaming things." The framing implies this was a consistent historical
  failure now largely resolved by model improvements.
- **Confidence**: anecdotal (single source; but mechanism is consistent with
  `failure-claudemd-ignored-compaction.md` — models skip guidance that is not re-injected
  or enforced structurally)
- **Actionable as**: AGENTS.md / CLAUDE.md patterns that persist naming conventions and
  style rules across sessions are the structural solution to this failure mode. The guide
  should recommend persistent context files not only as a best practice but as a
  documented fix for a specific historical failure that developers actually experienced.

### Lesson 3: Voice-to-text as the primary coding modality with Cursor is viable, but
requires prompt structure adaptation

- **Evidence**: Author used voice-to-text as their sole input method during GBS recovery
  and continues using it post-recovery alongside partial typing ability. No documented
  failure of voice-to-text itself — the documented friction was in code-generation quality,
  not in the input modality.
- **Confidence**: anecdotal (single practitioner's sustained experience)
- **Actionable as**: AI coding tools can function as accessibility tools for users with
  reduced fine motor ability. This use case is absent from existing guides, which assume
  keyboard-primary input. Voice-to-text + agentic coding is a viable combination, though
  it likely amplifies the need for explicit prompt structure (spoken language tends toward
  less precise technical phrasing than typed instructions).

### Lesson 4: Adoption driven by necessity surfaces friction that preference-driven adoption
abandons, creating a selection bias in reported friction

- **Evidence**: The author tried and abandoned Cursor before GBS, then used it
  successfully under medical necessity. The friction was the same; the tolerance changed
  when there was no alternative. The author explicitly frames the pre-illness attempt as
  a voluntary abandonment.
- **Confidence**: anecdotal (single data point, but structurally significant)
- **Actionable as**: Practitioner reports of early agentic tool adoption have a selection
  bias: those who found the friction intolerable left and did not report their experience.
  Reports from late 2024 that "AI coding was still hard" likely undercount the actual
  difficulty because the most-friction-affected practitioners were not present to report
  it. The noemit post provides a rare data point from someone who had to persist through
  the friction rather than exercise the exit option.

### Lesson 5: "Neutral on agentic coding" is a valid and underrepresented adoption outcome

- **Evidence**: Author's explicit summary: "It's a new modality. It has pros and cons."
  Despite deep daily usage, full workflow integration, and genuine gratitude for
  accessibility, the author explicitly does not endorse agentic coding as superior — only
  as different.
- **Confidence**: anecdotal
- **Actionable as**: The guide should represent the "pragmatic neutral" outcome as a
  legitimate and healthy endpoint, not only "enthusiastic convert" or "frustrated
  abandoner." Some practitioners will reach sustained, daily adoption without becoming
  advocates. This is not a failure of adoption — it is an honest assessment of the
  trade-offs.

## Concrete Artifacts

### noemit's early adoption friction pattern (reconstructed from post and reply)

```
Early adoption phase (Oct–Dec 2024):
  - Required: outline in detail "really small chunks of code" per prompt
  - Required: re-state naming conventions each session ("repeat how I named things")
  - Rejection rate: >50% of generated code discarded in first few months
  - Input modality: 100% voice-to-text (GBS paralysis of hands/fingers)

Current state (early 2026):
  - Acceptance rate: substantially higher ("I accept a lot more")
  - Named improvement: model no longer renames things
    ("it doesn't make mistakes like renaming things")
  - Continued behavior: "I still prompt more than code directly"
  - Primary IDE: Cursor
  - Perspective: "It's a new modality. It has pros and cons."
```

*Source: noemit, https://news.ycombinator.com/item?id=47295954, 2026-03-08,
and reply in same thread*

### Author's framing of the accessibility function (confirmed quote)

> "I feel deep gratitude for this technology, which eclipses any anxiety or frustration
> that bubbles up."

*Source: noemit reply, 2026-03-08*

### Adoption timeline

```
Early 2024:   Tried ChatGPT and Cursor, found them "a chore," abandoned Cursor after
              one attempt
Oct 2024:     Diagnosed with Guillain-Barré Syndrome after hand pain, weakness, loss
              of dexterity; hospitalized for one week
              Switched from VSCode to Cursor overnight; input modality: voice-to-text
              Rejection rate: >50%; required small-chunk prompting
Oct 2024–     GBS recovery; prompting-only workflow, improving prompting practice
~Apr 2025:    Partial typing ability regained after ~6 months
              (Typing speed and accuracy permanently reduced)
Early 2026:   Still using Cursor as primary IDE; prompts more than codes directly
              Acceptance rate substantially higher; naming violations resolved
              Tried Claude Code, returned to Cursor
              Perspective: "neutral" — "a new modality. It has pros and cons."
May 2026:     Cursor legacy unlimited plan expiry → transition to paid token plans
              (pricing concern only, unrelated to agentic quality)
```

## Cross-References

- **Corroborates**: `discussion-hn-agentic-coding-jobs.md` Claim 10 (codingdave: "a
  little more speed alongside a little more slop"): noemit's "neutral on agentic coding /
  pros and cons" framing is the accessibility-adoption version of the same pragmatic
  outcome. Two independent practitioners — one adopting for productivity, one forced by
  necessity — arrive at the same unsentimental acceptance. Neither abandons the tool;
  neither becomes an advocate.

- **Corroborates**: `failure-claudemd-ignored-compaction.md` (model ignoring
  CLAUDE.md-style guidance after compaction): noemit's naming violation failure mode
  (Failure Mode 3) is the same underlying mechanism without any persistent context file
  at all. If CLAUDE.md instructions can be silently skipped even when present, naming
  conventions stated only in the prompt would be even more fragile. Both failures point
  to the same structural fix: durable persistent context with enforcement.

- **Extends**: `research-anthropic-ai-transforming-work.md` (Anthropic report on AI
  transforming work): noemit's post is the clearest example of AI coding tools enabling
  participation that would otherwise be blocked. The Anthropic report discusses
  productivity gains; noemit's case is a participation gain — coding was not slower
  without AI, it was not possible. This is a stronger and categorically different claim
  than productivity improvement.

- **Novel**:
  - **Accessibility/disability as adoption driver**: No other source in our corpus
    describes AI coding tool adoption driven by physical necessity rather than
    productivity interest. The only documented case of voice-to-text + agentic coding as
    an accessibility accommodation.
  - **Selection bias in adoption-friction reports**: The observation (Lesson 4) that
    friction reports are filtered by who stayed to complain — and that medical necessity
    produced a rare unfiltered data point — is new to this corpus. No other note
    explicitly raises this structural issue with how adoption difficulty is reported.
  - **Naming convention violations as a named, recurrent historical failure mode**: Other
    notes recommend persistent context files as a best practice; this note provides the
    concrete practitioner failure that motivates that recommendation.

- **Contradicts**: None filed. The low-engagement, high-friction early adoption narrative
  is consistent with the late-2024 state of tools. No existing source claims models in
  2024 reliably honored naming conventions or that early adoption was frictionless.

## Guide Impact

- **Chapter 01 (Why Adopt / Adoption Framing)**: The accessibility angle belongs in any
  honest treatment of "who AI coding tools help and how." noemit's case is the clearest
  possible answer to "what does AI coding enable?" when framed not as productivity
  improvement but as participation recovery. Include alongside productivity-first framing
  as a distinct and compelling use case.

- **Chapter 02 (Harness Engineering / Persistent Context)**: Lesson 2 provides the direct
  practitioner motivation for AGENTS.md / CLAUDE.md naming conventions. Without a
  persistent context file, naming conventions stated in prompts were lost across sessions
  and violated recurrently. Use noemit's naming violation experience as the "before"
  example in any section introducing persistent context files: this is not an abstract
  risk, it is a documented failure mode that practitioners actually experienced.

- **Chapter 02 (Prompt Discipline / Task Scoping)**: Lesson 1 provides historical
  grounding for the small-task-scoping recommendation. In late 2024 this was a hard
  requirement for usable output, not a style preference. Knowing the historical baseline
  helps practitioners understand the recommendation's origin and the degree of capability
  improvement that has occurred since then.

- **Chapter 05 (Honest Adoption Outcomes / Setting Expectations)**: Lesson 5 ("neutral
  on agentic coding") should appear in any honest-objections section alongside success
  narratives and failure narratives. Not all sustained adoption ends in enthusiasm. The
  pragmatic-neutral outcome is healthy and should be modeled, not treated as a failure
  of adoption advocacy.

## Extraction Notes

- The post is a low-engagement personal narrative (4 points, 2 comments). Direct WebFetch
  returned summaries rather than verbatim quotes; the Firebase HN API returned a truncated
  text field; the Algolia API also returned summarized content. Verbatim quotes in this
  note appear consistently across all three fetch paths and are treated as reliable, but
  are marked as reconstructed from consistent synthesis rather than fully confirmed
  character-for-character transcriptions. The phrases "outline in detail really small
  chunks of code for it to write," "repeat how I named things," "it doesn't make
  mistakes like renaming things," and "It's a new modality. It has pros and cons." appear
  in all fetches.
- The Prospector labeled this low priority (4 points, 2 comments) and recommended
  skimming. The medical accessibility angle is the primary reason to include it: it
  surfaces a distinct failure mode (forced persistence through friction) and a use case
  (accessibility/disability accommodation) absent from all other corpus sources.
- The author's Cursor unlimited plan transition concern (May 2026 expiry) is noted in the
  timeline artifact but not developed into an extracted lesson. It is a pricing transition
  issue, not a quality issue.
- The Prospector's observation that the Oct 2024 experiences predate the Dec 2025
  relevance window is correct. The early friction patterns are documented as historical
  baseline, not as current-state claims. The "current state" observations (increased
  acceptance, naming violations resolved) are from early 2026 and within the relevance
  window. The historical patterns are retained because they motivate current guide
  recommendations (persistent context, task scoping) and document the capability
  improvement delta.
- The Prospector correctly noted there are no overlapping source notes — this is the
  only note in the corpus covering accessibility-driven adoption or the selection-bias
  framing of early adoption friction reports.
