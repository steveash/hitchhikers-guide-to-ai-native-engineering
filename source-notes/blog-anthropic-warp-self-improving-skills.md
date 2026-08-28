---
source_url: https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
source_type: blog-post
title: "How Warp builds self-improving agents on Claude"
author: Anthropic (customer case study, quoting Zach Lloyd, Warp founder/CEO)
date_published: 2026-08-26
date_extracted: 2026-08-28
last_checked: 2026-08-28
status: current
confidence_overall: emerging
issue: "#2995"
---

# How Warp builds self-improving agents on Claude

> A first-party Anthropic customer case study documenting Warp's two-skill
> self-improvement pattern — an inner/base skill that does the work and an
> outer/improver skill that runs on a schedule to turn accumulated human
> feedback into PR-reviewed edits to the base skill — illustrated end-to-end
> with Warp's GitHub issue-triage agent, plus a named set of design
> heuristics and an FAQ-style troubleshooting section covering feedback
> trust, verifiability, and measuring whether the system is actually
> improving.

## Source Context

- **Type**: blog-post (customer case study, claude.com/blog, published
  August 26, 2026; part of an unnamed Anthropic customer-story series —
  the article opens "In our series, , we highlight how startups are
  transforming their industries with AI," with the series name apparently
  dropped from the rendered page).
- **Author credibility**: Published under Anthropic's own blog, so this is
  first-party vendor content promoting a customer's use of the Claude
  Platform — the same credibility profile as this corpus's other
  claude.com customer case studies (e.g. `blog-anthropic-datadog-temper-machine-tool.md`,
  `blog-anthropic-hebbia-financial-diligence.md`). The technical content is
  attributed to Zach Lloyd, Warp's founder and CEO, with direct quotes
  throughout — a named, on-record practitioner source rather than an
  anonymous or composite account. Warp is described in the article's "quick
  pitch" sidebar with specific figures (founded 2020, $73M raised, 800K
  monthly developers, 56% of the Fortune 500, 10M Claude Code sessions run
  inside Warp to date, 400K+ per week, 40M total Warp Agent conversations),
  which is a real, named, sizeable production deployment — stronger
  evidentiary footing than a hypothetical or small-scale pilot. No
  independent (non-Anthropic, non-Warp) verification of any claim is
  available in the article itself.
- **Scope**: Covers Warp's motivating problem (a noisy, low-quality internal
  code-review agent), the two-skill self-improvement architecture (inner/base
  + outer/improver), a named set of best practices for writing
  self-improving skills, one worked example (the GitHub issue-triage agent)
  walked through end-to-end, and a closing FAQ section with six named design
  questions and terse answers. Does NOT cover: any code, YAML, or SKILL.md
  file contents (no artifacts of this kind are shown — everything is prose
  description); a metric or benchmark showing the pattern actually improved
  output quality (e.g., no before/after accuracy numbers for the code-review
  agent are given); Oz (Warp's internal agent-orchestration platform) beyond
  naming it as where the improver skill runs; or any discussion of cost,
  latency, or failure/rollback handling for a bad skill-update PR.

## Extracted Claims

### Claim 1: A first-pass agent prompt that gets 80% of a recurring task right creates a noisy, annoying user experience, not an acceptable one
- **Evidence**: Author's framing of the general problem, illustrated by Warp's own internal code-review agent, which "generated unhelpful comments and low-quality output" before the fix.
- **Confidence**: anecdotal (a framing claim backed by one internal example; no accuracy or satisfaction metric is given for "80%" or for the before/after state)
- **Quote**: "Agents need to handle recurring tasks reliably and effectively. A first-pass prompt that gets 80% of the task correct can create a noisy and annoying experience for the user."
- **Our assessment**: This is the article's motivating thesis and it is stated as received wisdom rather than measured — no data backs the specific "80%" figure or ties it to the code-review agent's actual accuracy. It is nonetheless a useful framing for practitioners: a recurring-task agent's failure mode is not "sometimes wrong," it is "wrong often enough that users start distrusting or ignoring it," which is a qualitatively different bar than one-shot task accuracy.

### Claim 2: The root cause of degrading agent quality was that feedback disappears when a session ends, removing critical context from future runs — not a prompting or context-file problem per se
- **Evidence**: Author's stated diagnosis after describing two stopgap fixes that "didn't scale": manual prompt rewrites and improving context files like AGENTS.md.
- **Confidence**: anecdotal (a single team's retrospective diagnosis; no comparison data on how much manual rewriting vs. AGENTS.md improvements helped before being judged insufficient)
- **Quote**: "the real issue was that feedback to an agent, no matter what its purpose, typically disappears when the session ends, removing critical context from the agentic loop"
- **Our assessment**: This is the load-bearing causal claim that motivates the whole two-skill architecture: if the diagnosis is right, no amount of upfront prompt or CLAUDE.md/AGENTS.md engineering fixes a recurring-task agent, because the missing ingredient is a mechanism for capturing and replaying *session-to-session* feedback, not better one-time authoring. This is a different failure mode than the "auto-generated AGENTS.md is redundant/harmful" finding in `blog-addyosmani-code-agent-orchestra.md` (Claim 7) — Warp is not claiming their context files were low-quality, but that even good context files go stale without a feedback-ingestion mechanism.

### Claim 3: The self-improvement architecture is two skills — an inner/base skill holding domain knowledge and instructions, and an outer/improver skill that functions as a scheduled observer agent comparing agent output to human responses and proposing edits to the base skill
- **Evidence**: Author's direct architectural description, illustrated with the code-review example (inner skill executes when a PR opens) and restated by Zach Lloyd in his own words.
- **Confidence**: emerging (a named, implemented architecture from a real production deployment, but described only in prose — no file structure, YAML, or code is shown)
- **Quote**: "Warp evolved a self-improving agent architecture consisting of two skills, with human feedback in between." / "The outer/improver skill functions as an observer agent that runs on a schedule rather than per-task. It pulls the accumulated human feedback, compares what the agent suggested against how humans responded, and proposes a small, focused edit to the base skill."
- **Additional quote (Zach Lloyd)**: "File-based skills are a way of encoding knowledge for agents without putting that knowledge directly in the prompt, as something the agent can simply look up in the course of doing its job. The framework is really simple actually: there's the base domain-specific skill and then there's the improver skill that refines that domain-specific skill. This simplicity is the beauty of this approach."
- **Our assessment**: This is the article's central, most citable claim. It is architecturally distinct from the platform-level "dreaming" feature documented in `blog-anthropic-managed-agents-dreaming-outcomes.md` (Claim 1–3): dreaming is a Claude Managed Agents platform capability that reviews session traces and memory stores to curate memory automatically; Warp's improver skill is a DIY pattern built on ordinary file-based Agent Skills, driven specifically by *human* feedback comments (not session-trace pattern-mining), and its output is a reviewable PR editing a skill file rather than an automatically curated memory store. The two are complementary self-improvement mechanisms at different layers (platform memory curation vs. skill-file editing via human feedback), not competing implementations of the same idea — the guide should present them as two distinct patterns, not variants of one.

### Claim 4: Explicit, specific human feedback ("you suggested renaming this variable, but our convention is X") gives the improver skill more to work with than a binary thumbs up/down
- **Evidence**: Zach Lloyd's direct quote describing the range of feedback Warp collects on code-review comments.
- **Confidence**: anecdotal (a stated preference with one illustrative example; no comparison of outcomes from binary vs. explicit feedback is given)
- **Quote**: "A human could affirm, 'this was a good, useful comment,' But the human could also give detailed reasons why a code review wasn't good. Specifics like 'you suggested renaming this variable, but our code base convention is this type of global variable uses this particular naming context' tell the agent how to do it right next time."
- **Our assessment**: This is a concrete instance of the "feedback quality > volume" principle named later in the article (Claim 6) and is consistent with the general "specificity beats vagueness" thread already in this corpus (e.g., `blog-addyosmani-code-agent-orchestra.md` Claim 10 on the specification imperative). The naming-convention example is small enough to be a template for what "good feedback" looks like in practice: it names the exact wrong output, the exact rule violated, and the exact correction — three components a vague "not helpful" comment lacks.

### Claim 5: Because skills are plain files, agent-proposed updates to them flow through the team's normal PR/code-review workflow, and this is what keeps the improvement loop human-controlled
- **Evidence**: Author's structural claim about why file-based skills specifically (as opposed to some other self-improvement mechanism) were chosen.
- **Confidence**: emerging (a design-rationale claim, directly demonstrated by the triage-agent worked example later in the article, where the improver skill's edit does go through PR review and merge)
- **Quote**: "Because skills are plain files, agents are extremely good at updating them. These updates, which are reviewable, approvable, and mergeable, can flow through a normal PR/code-review workflow; once merged, the next run of the inner skill inherits the improvement."
- **Our assessment**: This is the governance mechanism that answers the FAQ's own "what happens when feedback is wrong" question (Claim 9) — the answer is structural, not algorithmic: bad or premature skill edits are supposed to be caught the same way bad code is caught, by a human reviewing the PR before merge. This is consistent with the file-based-skills-as-PR-reviewable-artifact pattern already documented in `blog-anthropic-claude-code-skills-lessons.md` (skills as folders checked into repos) and is the single clearest practical answer in this corpus to "how do you keep an agent from unsupervised-ly rewriting its own instructions."

### Claim 6: Six named best practices for writing self-improving skills — write principles not rules, explain the why, make feedback effortless to give, keep skills small with progressive disclosure, prioritize feedback quality over volume, and invest extra effort in the improver skill because it is highly reusable across use cases
- **Evidence**: Author's structured list of Warp's "tried and true tips," each with a Zach Lloyd quote.
- **Confidence**: emerging (prescriptive design advice from one practitioner team, presented as validated by their own experience but without a controlled comparison against alternative approaches)
- **Quote (principles not rules)**: "Construct the skill as though you're instructing a smart person, not like you're programming a computer. Including direction in the skill like 'Look for repeated code' provides better direction than exhaustive variable naming rules."
- **Quote (low-friction feedback)**: "Low friction is what keeps signal flowing. If you make it too hard you're not going to get the feedback and you're not going to be able to improve the skill."
- **Quote (feedback quality)**: "You can get really good signal even from a relatively small sample size if it's very detailed feedback from a person around domain specific knowledge that the agent otherwise would have no way of getting. That said, the bigger the corpus of quality signal, the better. At Warp we're using a loop to manage our whole open source repo. We have hundreds of people contributing and we're doing thousands of code reviews."
- **Quote (improver skill reusability)**: "Outside of the domain specific knowledge component, this is a fairly reusable mechanism—the improver skill for a code review agent is not that different from the improver skill for any other agent."
- **Our assessment**: The "principles, not rules" and "explain the why" practices directly corroborate `blog-anthropic-claude-code-skills-lessons.md` Claim 8 (avoid railroading Claude with overly specific instructions — give it flexibility to adapt) from an entirely independent source (a customer rather than the Claude Code team itself), which strengthens the case that this is a convergent, cross-organization best practice rather than one team's house style. The "invest in the improver skill because it's reusable across agents" point is the most operationally significant of the six for teams scaling this pattern beyond one agent: it argues for treating the improver skill as shared infrastructure, not a bespoke one-off per agent — directly anticipated by Claim 8 below (one improver loop vs. one per agent).

### Claim 7: Warp's issue-triage agent demonstrates the pattern end-to-end: an inner skill triages new GitHub issues by label, a maintainer's specific feedback about a missed label ("ready to spec") was captured directly on the issue, and the improver skill later authenticated to GitHub, pulled and summarized recent feedback via a bundled Python script, and opened a PR with the minimal skill edit needed to apply the fix going forward
- **Evidence**: A single, detailed worked example walked through step by step: trigger (GitHub Action on new issue), inner-skill behavior (label assignment, feasibility analysis, fix direction), the specific missed label and the maintainer's feedback, and the improver skill's mechanics (runs in Oz on a schedule, authenticates to GitHub, runs a bundled script to pull recent issues with feedback, summarizes to JSON, reads that back into context, proposes the smallest edit).
- **Confidence**: emerging (one specific, detailed, named example from the vendor; no metric is given for how the triage agent performed before vs. after the fix, or how many other feedback signals were pending at the time)
- **Quote**: "A maintainer on the Warp team caught the gap and left feedback directly on the issue, exactly where the work was happening. Critically, he explained both what he expected and why he expected it: actionable feedback easy for the agent to absorb later." / "It opened a PR editing the inner skill to apply the 'ready to spec' label when an issue describes a real problem, even though the exact UI or UX shape is not yet defined."
- **Our assessment**: This is the article's most concrete evidence for the pattern actually working end-to-end, though it remains a single anecdote (one label, one PR) rather than a measured before/after study across many triage decisions. The mechanical detail that the improver skill "ran a Python script bundled with the skill to pull recent issues carrying feedback, summarized them into a JSON file, and read that back into context" is a specific implementation pattern — a bundled helper script doing deterministic data-gathering work, with the LLM reasoning only over the pre-summarized JSON — that is a concrete instance of the general "helper scripts reduce boilerplate, let Claude compose rather than reconstruct" principle in `blog-anthropic-claude-code-skills-lessons.md` (Claim 12), applied specifically to the improver skill's own data-collection step.

### Claim 8: Choosing between one improver loop per agent and one shared improver loop across many agents is a scale decision — a templated base loop with domain-specific weights layered on, a handful of improvers can each own their own, a hundred should share
- **Evidence**: A terse FAQ-style answer, one of six closing design questions.
- **Confidence**: anecdotal (a heuristic rule of thumb with a "handful vs. hundred" threshold, given without justification or data on where exactly the crossover point lies)
- **Quote**: "Meet in the middle: a templated base loop captures the overlap across your agents, with domain-specific weights layered on. A handful of improvers can each own one; a hundred should share."
- **Our assessment**: This directly operationalizes Claim 6's "improver skill is reusable across use cases" point into an actual architectural decision rule. The "templated base + domain-specific weights" framing suggests Warp treats the improver skill itself as a parameterized template rather than either a fully bespoke skill per agent or a single monolithic shared skill — a middle path not discussed in either of this corpus's existing Claude Code skills posts, which describe skill reuse (marketplace distribution) but not this specific pattern of one skill *type* (the improver) being templated across many domain-specific instances.

### Claim 9: Feedback should be assumed wrong by default — an improver skill needs context to sanity-check incoming feedback, a way to filter whose input counts, and a human retained in the loop at either the filtering stage or the final-review stage
- **Evidence**: A terse FAQ-style answer to "What happens when the feedback is wrong?"
- **Confidence**: anecdotal (a stated design principle without a described mechanism for how sanity-checking or filtering is actually implemented at Warp, and no example of a case where bad feedback was caught or missed)
- **Quote**: "Assume it will be. Don't let the agent accept feedback blindly — give it context to sanity-check, filter whose input counts, and keep a human in the loop at either the filtering or final-review stage."
- **Our assessment**: This is the article's only explicit acknowledgment that the feedback-ingestion mechanism itself is a new attack surface for bad or malicious input — a real gap, since the worked triage example shows a single trusted maintainer's feedback with no discussion of what happens if multiple contributors give conflicting or low-quality feedback on the same issue. The recommended mitigations (context to sanity-check, a filter on whose feedback counts, human review as a backstop) are named but not shown in the triage example, which used a maintainer's feedback and relied on the standard PR-review step (Claim 5) as the actual safeguard — the article does not show the "filter whose input counts" mechanism in action anywhere.

### Claim 10: For a domain that can be made verifiable, the recommended sequence is to build the verification harness first, then tune the agent against it — generate a reference corpus, compare output to reference, fix, repeat; where the domain is not verifiable, lean on deterministic evals against golden outputs where they exist, and restrict human feedback specifically to domain experts rather than opening it to everyone
- **Evidence**: Two paired FAQ-style answers addressing "Is your domain verifiable?" and "And if it isn't domain verifiable?"
- **Confidence**: anecdotal (prescriptive sequencing advice, no worked example of building such a harness is given anywhere in the article — the triage example is presented as feedback-driven, not harness-verified)
- **Quote**: "Build the verification harness first, then let the agent tune against it: generate a reference corpus, compare output to reference, fix, repeat." / "Lean on deterministic evals against golden outputs wherever they exist. Where you must use human feedback, restrict it to domain experts — don't open the floodgates."
- **Our assessment**: This is a notable internal tension worth flagging for the guide: the article's own worked example (issue triage) is a *human-feedback-driven* improvement loop, not a verification-harness-driven one, yet the FAQ recommends building a verification harness "first" wherever a domain is verifiable. Issue-label triage is arguably not cleanly verifiable (there is no ground-truth reference corpus for "which label is correct"), which may explain why Warp used the feedback path for it — but the article does not name which of Warp's agents (if any) use the harness-first approach instead, leaving the verifiable-domain recommendation untested by any example in the piece itself. "Restrict [human feedback] to domain experts" also stands in some tension with Claim 6's volume point ("the bigger the corpus of quality signal, the better... hundreds of people contributing... thousands of code reviews") — the reconciliation is presumably that quantity from a broad contributor base is fine as *signal volume* while the improver skill's actual trust weighting should be expert-restricted, but the article does not state this reconciliation explicitly.

### Claim 11: The success metric for a self-improvement loop should be the same global metrics humans already track — time to merge, contributor count, cost — fed back into the improver agents, deployed incrementally ("crawl-walk-run")
- **Evidence**: A terse FAQ-style answer to "How do you know the whole system is improving?"
- **Confidence**: anecdotal (names three example metrics without specifying which ones Warp actually tracks for which agent, or showing any trend data)
- **Quote**: "Track the global metrics humans already eyeball—time to merge, contributor count, cost—and feed them back into the improver agents. Go crawl-walk-run on deployment."
- **Our assessment**: This is the weakest-evidenced claim in the article — no metric trend, dashboard, or before/after number is shown anywhere for any of Warp's agents, despite the FAQ implying these are actively tracked. It is useful only as a checklist prompt ("what should I measure") rather than as evidence that Warp has actually validated improvement. The "crawl-walk-run" deployment caution is generic risk-management advice, consistent with but not adding detail to the standard incremental-rollout practice already implicit in this corpus's CI/PR-gate guidance.

## Concrete Artifacts

### Warp company profile (as stated in the article's "quick pitch" sidebar)

```
Source: claude.com/blog/how-warp-builds-self-improving-agents-on-claude (2026-08-26)

Name:      Warp
Founded:   2020
Founders:  Zach Lloyd (CEO)
Stack:     Rust, Golang, GitHub Actions, internal agent orchestration
           platform (Oz), Claude Platform
Growth:    $73M raised. 800K monthly developers build on Warp.
           56% of the Fortune 500 uses Warp.
           10M Claude Code sessions run inside Warp to date, 400K+ per week.
           40M total Warp Agent conversations.
```

### The two-skill self-improvement loop (as described in the article)

```
Source: claude.com/blog/how-warp-builds-self-improving-agents-on-claude (2026-08-26)

INNER / BASE SKILL
  - Holds functional domain knowledge and instructions
  - Executes per-task (e.g., runs when a PR opens, for code review)
  - Produces the agent's actual output (comments, labels, etc.)

HUMAN FEEDBACK (in between)
  - Captured on the agent's output where the work happens
    (PR comments, issue comments)
  - Ranges from binary (thumbs up) to detailed, specific corrections
  - "the more explicit the better"

OUTER / IMPROVER SKILL
  - Runs as an observer agent ON A SCHEDULE, not per-task
  - Pulls accumulated human feedback
  - Compares agent suggestions against human responses
  - Proposes a small, focused edit to the base skill
  - Update flows through normal PR/code-review workflow
  - Once merged: next run of inner skill inherits the improvement
```

### Worked example: Warp's issue-triage agent feedback loop

```
Source: claude.com/blog/how-warp-builds-self-improving-agents-on-claude (2026-08-26)

TRIGGER:    New GitHub issue filed -> GitHub Action fires triage agent
INNER SKILL: Domain knowledge on label meanings, codebase-research steps
             before acting; analyzes issue for complexity/feasibility,
             assigns labels, suggests a fix direction

GAP OBSERVED: Missed the "ready to spec" label (signals a contributor can
             start building product/technical specs against the issue)
FEEDBACK:    Maintainer left a comment directly on the issue, explaining
             both what he expected AND why

IMPROVER SKILL MECHANICS (runs in Oz, Warp's agent orchestration platform,
as a scheduled "update triage" agent):
  1. Authenticates to GitHub
  2. Runs a bundled Python script (shipped with the skill) to pull recent
     issues carrying feedback
  3. Summarizes signals into a JSON file
  4. Reads the JSON back into context
  5. Identifies concrete feedback signals in maintainer comments
  6. Proposes the smallest edit capturing them
  7. Opens a PR editing the inner skill: apply "ready to spec" when an
     issue describes a real problem, even if exact UI/UX shape is
     undefined
  8. PR includes a description of which signals prompted the change
  9. Human reviews, approves, merges
  10. Next triage run inherits the new knowledge

SCALE: Same mechanism now runs across Warp's entire open-source repo,
       with separate spec-writing, review, and triage agents, each
       carrying its own self-improvement loop.
```

### Six best practices for self-improving skills (verbatim list, as titled in the article)

```
Source: claude.com/blog/how-warp-builds-self-improving-agents-on-claude (2026-08-26)

1. Write principles, not rules.
2. Explain the why.
3. Make feedback effortless to give.
4. Keep skills small and use progressive disclosure.
5. Feedback quality > volume, but volume helps.
6. Put extra effort into the improver skill.
```

### FAQ: six named design questions (as titled/answered in the article's closing section)

```
Source: claude.com/blog/how-warp-builds-self-improving-agents-on-claude (2026-08-26)

Q: Are you conflating skills with memory?
A: Skills are procedural and stable — "how to do X," run-agnostic, changed
   deliberately. Memory is auto-written by the agent at inference time and
   never stops changing.

Q: Do you need one improver loop, or one per agent?
A: Meet in the middle: a templated base loop captures the overlap across
   your agents, with domain-specific weights layered on. A handful of
   improvers can each own one; a hundred should share.

Q: What happens when the feedback is wrong?
A: Assume it will be. Don't let the agent accept feedback blindly — give
   it context to sanity-check, filter whose input counts, and keep a
   human in the loop at either the filtering or final-review stage.

Q: Is your domain verifiable?
A: Build the verification harness first, then let the agent tune against
   it: generate a reference corpus, compare output to reference, fix,
   repeat.

Q: And if it isn't domain verifiable?
A: Lean on deterministic evals against golden outputs wherever they
   exist. Where you must use human feedback, restrict it to domain
   experts — don't open the floodgates.

Q: How do you know the whole system is improving?
A: Track the global metrics humans already eyeball — time to merge,
   contributor count, cost — and feed them back into the improver
   agents. Go crawl-walk-run on deployment.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-skills-lessons.md` (Claim 8: avoid
    railroading Claude with overly specific instructions — give it
    information and flexibility rather than a fixed sequence). Claim 6 here
    ("Write principles, not rules... provides better direction than
    exhaustive variable naming rules") is an independent, cross-organization
    (customer vs. Anthropic-internal) convergence on the same skill-authoring
    principle.
  - `blog-anthropic-claude-code-skills-lessons.md` (Claim 12: helper scripts
    let Claude compose rather than reconstruct boilerplate). Claim 7 here's
    detail that the improver skill runs "a Python script bundled with the
    skill to pull recent issues carrying feedback" and summarizes to JSON
    before the LLM reasons over it is a concrete, named instance of exactly
    this pattern, applied specifically to an improver skill's own
    data-gathering step.
  - `blog-addyosmani-code-agent-orchestra.md` (Claim 10: the specification
    imperative — vague thinking multiplies errors, specificity is the
    leverage point). Claim 4 here's naming-convention feedback example
    ("you suggested renaming this variable, but our code base convention
    is...") is a concrete instance of the same specificity-over-vagueness
    principle, applied to human feedback on agent output rather than to
    upfront task specs.

- **Extends**:
  - `blog-anthropic-managed-agents-dreaming-outcomes.md` (Claim 1–3:
    dreaming — a scheduled, platform-level process that reviews session
    traces and memory stores to curate memory between sessions). This
    source documents a structurally different, DIY self-improvement
    mechanism built on ordinary file-based Agent Skills rather than the
    Managed Agents platform's dreaming feature: Warp's improver skill is
    driven by explicit human feedback comments (not automated session-trace
    pattern mining), and its output is a human-reviewed PR editing a skill
    file (not an automatically curated memory store). The guide should
    present dreaming and Warp's improver-skill pattern as two distinct
    self-improvement layers — platform memory curation vs. skill-file
    editing via human feedback — not as the same mechanism described twice.
    Notably, the FAQ's own answer to "Are you conflating skills with
    memory?" (skills are stable/deliberately-changed, memory is
    auto-written and never stops changing) is Warp's own explicit statement
    of this same layering distinction.
  - `blog-anthropic-claude-code-verification-loops-skills.md` (the four
    deployment patterns for verification skills — standalone, embedded,
    chained, on-every-PR). That source documents how to deploy a
    verification *check* as a skill; this source documents a different
    but complementary problem — how to keep a non-verification (e.g.,
    code-review commentary, triage labeling) skill accurate over time via
    a second, scheduled skill. The two sources are both about skill
    lifecycle management but address different lifecycle stages: deploying
    a check (verification-loops post) vs. maintaining and correcting an
    existing skill's judgment over time (this source).

- **Contradicts**: None filed. Two internal-tension observations are noted
  above under Claim 10's assessment (the article's own worked example is
  feedback-driven rather than harness-verified, despite the FAQ
  recommending harness-first for verifiable domains; and "restrict human
  feedback to domain experts" sits in some tension with Claim 6's
  volume-helps framing) — these are internal to this single source, not
  disagreements with another corpus source or a claim that would drive
  opposite guide advice, so no contradiction issue was filed per MINER.md
  §4a.

- **Novel**:
  - **The named inner/base + outer/improver two-skill pattern itself**: no
    existing corpus source documents a specific, implemented pattern of
    one skill producing output and a second, scheduled skill that
    consumes human feedback on that output and proposes edits to the
    first skill's file. This is the article's central contribution and is
    new to the corpus.
  - **A bundled helper script performing an improver skill's own
    feedback-gathering step (GitHub API pull + JSON summarization) before
    the LLM reasons over the result**: a specific implementation detail
    for how an improver skill itself should be built, extending the general
    "use helper scripts" principle with a self-improvement-specific
    example.
  - **The "templated base loop + domain-specific weights" answer to
    whether to run one improver skill per agent or share one across many**:
    not addressed in either existing Claude Code skills source note.
  - **The FAQ's explicit skills-vs-memory distinction, stated by a
    practitioner customer rather than by Anthropic's own product
    documentation**: an independent corroboration, from outside Anthropic,
    of the skills/memory layering already implicit in
    `blog-anthropic-managed-agents-dreaming-outcomes.md`.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Skills Design**: Add Warp's
  inner/base + outer/improver two-skill pattern as a named, concrete
  self-improvement architecture, alongside the existing skills-design
  content from `blog-anthropic-claude-code-skills-lessons.md`. Present it
  specifically as the pattern to reach for when a recurring-task skill's
  output quality degrades over many runs and the fix is not a one-time
  prompt rewrite — distinguishing it from platform-level dreaming
  (`blog-anthropic-managed-agents-dreaming-outcomes.md`), which is a
  different, non-DIY mechanism available only on the Managed Agents
  platform.

- **Chapter 02 (Harness Engineering) — Governance for self-modifying
  skills**: Add Claim 5 (updates flow through the normal PR/code-review
  workflow) as the guide's concrete answer to "how do you let an agent
  change its own instructions safely" — the mechanism is not a special
  approval gate, it is treating a skill-file edit exactly like any other
  code change. Pair with Claim 9's caution (assume feedback is wrong by
  default; sanity-check, filter, keep a human at filtering or final
  review) as the risk this governance step is meant to catch.

- **Chapter 03 (Verification/Practitioner Patterns)**: Add the FAQ's
  verifiable-vs-not-verifiable branch (Claim 10) as a decision point for
  teams building a self-improvement loop: build a verification harness and
  reference corpus first if the domain supports it; fall back to
  deterministic evals against golden outputs or expert-restricted human
  feedback if it does not. Flag explicitly (per this note's Cross-References
  → Contradicts discussion) that the article's own worked example (issue
  triage) does not follow the harness-first path, so this recommendation
  should be presented as untested-by-example guidance from the source, not
  as a validated case study.

- **Chapter 05 (Multi-Agent Orchestration / Team Adoption)**: Add Claim 8's
  "templated base loop, handful vs. hundred" heuristic as a scaling
  decision point for teams running this pattern across more than one
  agent — a handful of agents can each own a bespoke improver skill; at
  Warp's scale (an entire open-source repo, separate spec/review/triage
  agents), a shared, templated improver skill with domain-specific
  parameters is the recommended shape.

## Extraction Notes

- **Fetch method**: WebFetch's summarizing pass on this URL (like several
  other claude.com/blog articles in this corpus, e.g. the Extraction Notes
  in `blog-anthropic-claude-code-skills-lessons.md`) returned a condensed,
  non-verbatim summary rather than the article's own wording. Because this
  particular claude.com blog page is server-rendered static Webflow HTML
  (not a client-side-rendered app), the full article text was recoverable
  directly via `curl` on the raw page HTML, followed by stripping HTML tags
  with a plain Python script — the same higher-confidence verbatim-fetch
  method used in `blog-addyosmani-loop-engineering.md`. All quotes in this
  note are copied from that raw-HTML extraction, not from the WebFetch
  summary, and are therefore character-for-character from the source page
  (verified against `/tmp/warp_article.txt`, the stripped output of the
  `u-rich-text-blog` article container div).
- **Full source read**: The entire article body was read (quick pitch
  sidebar through the closing FAQ and CTA). No sub-pages or linked content
  were present to follow — a "View the full webinar" reference is
  mentioned at the end but no URL for it was recoverable from the fetched
  HTML (it appears to be a dynamically-inserted CMS link that did not
  resolve to static markup), and it was not pursued further since the
  article's own text already covers the technical content in full prose.
- **No code/config artifacts in the source**: Unlike
  `blog-anthropic-claude-code-verification-loops-skills.md`, which
  reproduces full SKILL.md examples verbatim, this article contains no
  file contents, YAML frontmatter, or code — every technical detail is
  conveyed in prose or as Zach Lloyd quotes. This is reflected in the
  Concrete Artifacts section above, which is a structured restatement of
  prose content rather than literal source code.
- **Confidence rated `emerging`**: a single named practitioner (Zach
  Lloyd) speaking on the record about a large, real production deployment
  (10M+ Claude Code sessions, 40M Warp Agent conversations) is more
  credible than an anonymous or synthesized account, but the article
  provides no before/after metric for any claim — no accuracy figure for
  the code-review agent's improvement, no time-series data for the FAQ's
  suggested "time to merge, contributor count, cost" metrics, and only one
  detailed worked example (the triage agent's single missed label). This
  is consistent with how this corpus rates other single-customer,
  first-party vendor case studies without independent benchmark data.
- Cross-references verified: `blog-anthropic-managed-agents-dreaming-outcomes.md`,
  `blog-anthropic-claude-code-skills-lessons.md`,
  `blog-anthropic-claude-code-verification-loops-skills.md`, and
  `blog-addyosmani-code-agent-orchestra.md` were each re-read in full
  before citing; no claim numbers were guessed.
