---
source_url: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
source_type: blog-post
title: "Choosing a Claude model and effort level in Claude Code"
author: Lydia Hallie (Anthropic, member of technical staff, Claude Code team)
date_published: 2026-07-07
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1668"
---

# Choosing a Claude model and effort level in Claude Code

> First-party Anthropic explainer separating "model" (which frozen weights answer
> the request) from "effort" (how much work Claude does before checking back in)
> as two independent axes, giving a mechanistic account of both, a diagnostic
> framework for which to adjust when Claude gets something wrong, and a
> specialist/expert/generalist metaphor (Fable/Opus/Sonnet) for reasoning about
> cost and quality tradeoffs.

## Source Context

- **Type**: blog-post (official claude.com/blog explainer, published July 7, 2026;
  long-form conceptual post, not a changelog or feature announcement)
- **Author credibility**: Lydia Hallie, member of technical staff on the Claude
  Code team at Anthropic — first-party, and a member of the team that ships the
  effort-level and model-selection UI being explained. Authoritative for how the
  mechanism works (tokenization, frozen weights, effort as a request parameter)
  and for Anthropic's own recommended mental model. Not independently verified:
  the Opus 4.8 vs. Opus 4.7 "about the same number of tokens" comparison is
  described as internal Anthropic testing with no published methodology, sample
  size, or task set.
- **Scope**: Covers the conceptual distinction between model selection and effort
  level in Claude Code, the token-prediction mechanics of model selection, how
  effort is passed as a request parameter and affects thoroughness, a diagnostic
  framework for choosing what to change when Claude gets something wrong, a
  three-model metaphor (Fable as specialist, Opus as expert, Sonnet as generalist),
  and general cost/token guidance for routine vs. complex work. Does NOT cover:
  specific effort-level tier names (the piece never uses labels like "low",
  "medium", "high", "max", or "xhigh" in the body text), the `ultracode` setting,
  pricing/dollar figures, Haiku (mentioned only in site navigation, not discussed),
  or benchmark data for any of its claims.

## Extracted Claims

### Claim 1: Model selection and effort level are two independent axes — model chooses which frozen weights answer the request, effort controls how much work is done before Claude checks back in
- **Evidence**: This is the organizing distinction for the entire post, stated in
  the "Key Takeaways" section and restated in the "Claude Code Effort Levels and
  Model Selection" section.
- **Confidence**: settled (this is Anthropic's own stated conceptual framework for
  a shipping product feature, not a benchmarked claim)
- **Quote**: "Effort level controls how much work Claude does on your request
  overall."
- **Quote (files/verification)**: "Effort controls how much work Claude does on
  your request overall including the number of files read, tools used, and how
  many steps it takes before it checks back in with you."
- **Our assessment**: This is the single most useful framing in the post for
  practitioners who conflate "bigger model" with "more effort." The two dials are
  orthogonal: a practitioner can run a small model at high effort (thorough but
  capability-bounded) or a large model at low effort (capable but shallow). The
  guide currently has no explicit statement of this orthogonality.

### Claim 2: Effort means more than "thinking time" — at higher effort Claude takes more actions (reads more files, runs tests, double-checks) before returning to the user; at lower effort it asks for clarification sooner
- **Evidence**: Direct explanatory sentence in the "Claude Code Effort Levels and
  Model Selection" section.
- **Confidence**: settled (product-behavior description from the team that built it)
- **Quote**: "At a higher effort, Claude will take more of those actions (for
  example, read files, run tests, and double-check) before it comes back to you."
- **Our assessment**: This directly extends the corpus's prior effort-level
  mentions, which mostly treated "effort" as a synonym for reasoning depth (see
  Cross-References). This source is explicit that effort also governs autonomy
  and checking-in cadence — a low-effort session asks for clarification sooner,
  a high-effort session pushes further before surfacing to the user. That is an
  actionable distinction for harness design: effort level is partly a proxy for
  how much unsupervised work a practitioner is willing to let Claude do in one
  turn.

### Claim 3: Model weights are frozen at training time and read-only at inference; your prompt and context steer prediction but do not add anything to the weights themselves
- **Evidence**: Mechanistic explanation in "How Model Selection Works," grounded
  in the tokenization → next-token-prediction pipeline.
- **Confidence**: settled (standard LLM-architecture fact, stated authoritatively
  by an Anthropic engineer)
- **Quote**: "The weights of each model are set during training, and by the time
  you're sending requests they're read-only."
- **Quote (context vs. weights)**: "Your prompt and context can still steer the
  prediction, but they don't add anything to the weights themselves."
- **Our assessment**: This is a correctness-relevant clarification worth citing
  directly: practitioners sometimes act as though a long, detailed session
  "teaches" the model something durable. This source states plainly that nothing
  in a session changes the weights — all steering is prompt/context-based and
  vanishes with the session. Useful grounding for any guide section on why
  context engineering (not fine-tuning) is the practitioner's actual lever.

### Claim 4: Effort level is sent to the model as an explicit request parameter alongside the prompt, considered on every turn, and produces exponentially more tokens for higher-confidence answers as effort increases
- **Evidence**: Mechanistic explanation in "How Effort Works."
- **Confidence**: settled for the mechanism (effort as a request parameter,
  considered per-turn); "exponentially more tokens" is stated as a description of
  the scaling shape, not backed by a chart or numbers in this post
- **Quote**: "The effort level is sent to the model as part of the request, right
  alongside your prompt."
- **Quote (per-turn/scaling)**: "This is considered on every turn and results in
  more tokens to produce higher confidence answers."
- **Our assessment**: The "considered on every turn" detail matters operationally:
  effort is not a session-level setting that's applied once and then drifts — it's
  re-evaluated per turn, meaning a practitioner who changes effort mid-session
  should expect the new setting to apply from the very next turn, not require a
  fresh session. The "exponentially more" token-scaling claim is qualitative here;
  no concrete multiplier is given, so treat the cost-scaling shape as directional
  rather than a number practitioners can budget against.

### Claim 5: In Anthropic's internal testing, Opus 4.8 at default effort produces better results for about the same number of tokens as Opus 4.7 at default effort, for the same task
- **Evidence**: Stated as an internal-testing finding in "Picking an Effort
  Level," used to support the recommendation to use default effort rather than
  manually tuning per task.
- **Confidence**: emerging (vendor-internal comparison; no published methodology,
  task set, or sample size)
- **Quote**: "in our testing we found when you use the default effort setting for
  Opus 4.8, it will produce better results for about the same number of tokens when
  compared to using the default effort setting of Opus 4.7 for the same task."
- **Our assessment**: This is the closest thing to a quantitative claim in the
  post, and it's notably soft — "better results" and "about the same number of
  tokens" are not defined with a benchmark, task category, or effect size. Its
  practical use is narrow: it supports the "trust the default, don't hand-tune
  effort per task" recommendation (Claim 9) by implying that model upgrades
  already improve the default operating point, rather than practitioners needing
  to compensate with manual effort increases after a model bump.

### Claim 6: The diagnostic question for fixing a wrong answer is "did it not try hard enough, or did it not know enough?" — insufficient effort shows up as skipped files, unrun tests, or missing double-checks; genuine difficulty (with full context and real effort already applied) calls for a larger model
- **Evidence**: Named diagnostic framework in "What to Change When Claude Gets It
  Wrong," with explicit example failure modes for each branch.
- **Confidence**: settled (this is Anthropic's stated recommended troubleshooting
  heuristic for a shipping feature, though it is a heuristic, not a measured
  decision rule)
- **Quote**: "did it not _try_ hard enough, or did it not _know_ enough?"
- **Quote (effort branch)**: "Pick a higher effort level if Claude got it wrong by
  skipping a file, not running the tests, or not double-checking its work."
- **Quote (model branch)**: "If Claude has all the pertinent context and clearly
  tried and still got it wrong, that's a signal to pick a larger model."
- **Quote (scope caveat)**: "This is most relevant if you selected an effort level
  below the model's default."
- **Our assessment**: This is the most directly actionable content in the post —
  a two-branch decision tree practitioners can apply immediately after a bad
  result, without needing to understand the underlying mechanics. The scope
  caveat on the effort branch is important and easy to miss: the "raise effort
  first" advice is explicitly framed as most relevant when you're already below
  the model's default effort — it is not a claim that raising effort indefinitely
  fixes capability gaps once you're at or above default.

### Claim 7: Fable, Opus, and Sonnet are characterized as a specialist, an expert, and a generalist respectively — effort adjusts how much time each gets on a problem, not which kind of expertise is applied
- **Evidence**: Extended metaphor in the "Fable vs. Opus vs. Sonnet" section,
  applied to explain why effort and model are separate axes rather than
  substitutes for one another.
- **Confidence**: anecdotal (an explanatory metaphor, not a measured claim; useful
  for intuition-building, not a technical specification)
- **Quote**: "Opus is the expert, and Sonnet is a really good generalist."
- **Quote (Fable recognition)**: "Fable, even at low effort, is that specialist
  glancing at the problem everyone else is stuck on."
- **Quote (effort as time, not expertise)**: "Opus at low effort is like getting
  five minutes with an expert" / "Sonnet at high effort is like giving a really
  good generalist the whole afternoon."
- **Our assessment**: The metaphor's real content is the claim that effort and
  model select different things: effort selects *how long* a given kind of
  expertise gets applied; model selects *which* expertise (specialist pattern
  recognition vs. deep expert reasoning vs. broad generalist competence) is
  applied. This reframes "just raise effort" as not always the fix — if the
  problem needs specialist recognition that Sonnet/Opus don't have regardless of
  time spent, only switching to Fable helps, no matter the effort level.

### Claim 8: On routine work, smaller and larger models generally reach the same correct result at the same effort level, but the larger model spends more tokens on extra verification at a higher per-token price — so dropping to the smaller model on routine work saves money at no quality cost; on harder multi-step work, the larger model reaches the same quality bar in fewer steps while the smaller model burns iterations grinding toward the limit of its ability
- **Evidence**: Cost/quality comparison in "Effort, Model, and Token Consumption,"
  contrasting routine and complex-work token economics.
- **Confidence**: emerging (directional claim from Anthropic, consistent with the
  post's overall recommendations, but no benchmark numbers, task examples, or
  cost figures are given to substantiate "generally will get it right" or "burning
  iterations")
- **Quote**: "On routine work at the same effort level, both models generally will
  get it right."
- **Quote (larger-model cost)**: "The larger model consumes more tokens with extra
  verification steps at a higher per-token price."
- **Quote (savings)**: "That's why dropping to the smaller model for routine
  stretches saves real money at no quality cost."
- **Quote (complex work)**: "The smaller model has to grind toward the limit of
  its ability, burning iterations, while the larger model reaches the same quality
  bar in fewer steps."
- **Our assessment**: This is the core cost-management guidance of the post and
  matches the "right model for the job" heuristic already documented elsewhere in
  the corpus for other vendors' tools (see Cross-References). The claim that a
  larger model "reaches the same quality bar in fewer steps" on hard problems is
  the more interesting half — it implies the token-cost comparison between model
  tiers is not simply per-token price times a fixed step count; the step count
  itself shrinks with a more capable model on genuinely hard tasks, partially
  offsetting the higher per-token price. No numbers are given to show at what
  problem difficulty this offset becomes net-favorable for the larger model.

### Claim 9: Practitioners should start with default model and effort settings for most tasks and only adjust the dials when the default result disappoints — most of the time neither setting should require active thought
- **Evidence**: Closing recommendation in "Start with the Defaults, Then Reach for
  the Dials," and echoed earlier in "Picking an Effort Level" ("use the default
  effort level for most of your tasks").
- **Confidence**: settled (explicit, direct recommendation from the product team)
- **Quote**: "Most of the time, you shouldn't be thinking about either setting."
- **Our assessment**: This is the post's practical bottom line and directly
  contradicts a "power user" instinct to manually tune effort per task. Combined
  with Claim 5 (Opus 4.8 default already outperforms Opus 4.7 default at similar
  token cost), the implicit argument is that Anthropic is tuning the *default*
  operating point across model releases, so hand-tuning effort per task is
  increasingly unnecessary busywork for routine cases — the diagnostic framework
  in Claim 6 is offered as the fallback for when defaults visibly underperform,
  not as a routine practice.

## Concrete Artifacts

```
# Diagnostic framework for fixing a wrong Claude Code result
# Source: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
# Section: "What to Change When Claude Gets It Wrong"

QUESTION: did it not try hard enough, or did it not know enough?

BRANCH 1 — Insufficient effort (symptoms):
  - Skipped a file
  - Did not run the tests
  - Did not double-check its work
  FIX: raise the effort level
  CAVEAT: "most relevant if you selected an effort level below the model's default"

BRANCH 2 — Genuine difficulty (symptoms):
  - Claude had all the pertinent context
  - Claude clearly tried
  - Still got it wrong
  FIX: pick a larger model
```

```
# Fable / Opus / Sonnet metaphor
# Source: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
# Section: "Fable vs. Opus vs. Sonnet"

Fable  = specialist  ("even at low effort, is that specialist glancing at the
                       problem everyone else is stuck on")
Opus   = expert      ("Opus at low effort is like getting five minutes with an
                       expert")
Sonnet = generalist  ("Sonnet at high effort is like giving a really good
                       generalist the whole afternoon")

AXIS SEPARATION: model = which kind of expertise; effort = how much time that
expertise gets on the problem.
```

```
# Cost/quality tradeoff by task type
# Source: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
# Section: "Effort, Model, and Token Consumption"

ROUTINE WORK (same effort level):
  Small model:  gets it right
  Large model:  gets it right, but burns extra tokens on verification at a
                higher per-token price
  -> Recommendation: use the smaller model; "saves real money at no quality cost"

HARD / MULTI-STEP WORK:
  Small model:  "has to grind toward the limit of its ability, burning
                iterations"
  Large model:  "reaches the same quality bar in fewer steps"
  -> Recommendation: larger model is worth the higher per-token price because
     step count drops
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-1m-context-reasoning-levels.md` (Claim 4): "We recommend
    using the default context window and reasoning level for everyday tasks, and
    reaching for extended context or higher reasoning when you're tackling
    complex, multi-file problems." Independently, GitHub's own reasoning-level
    guidance for Copilot lands on the identical default-first, escalate-for-
    complexity heuristic this source states for Claude Code's effort dial (Claim
    9). Two vendors converging on the same "don't touch the dial by default"
    guidance for an analogous feature strengthens the case that this is sound
    general advice, not an Anthropic-specific quirk.
  - `blog-cursor-bugbot-effort-billing.md` (Claim 6): "From our internal runs,
    Bugbot with high effort finds 35% more bugs while resolution rate stays
    constant at 80%." This is a different product (a code-review agent, not a
    coding agent) but the same underlying pattern as this source's Claim 2:
    higher effort buys more thoroughness (more bugs found / more files read and
    verified) at a real cost, without necessarily changing the character of the
    output. Cursor's number is the more quantified version of the qualitative
    claim this source makes.
  - `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 9: "Low remains a
    fast, cost-efficient default for straightforward work like docs and small
    repositories"): matches this source's Claim 8 routine-work guidance (use the
    cheaper tier/model for straightforward work) almost exactly, in a different
    vendor's code-review product rather than a coding agent.

- **Extends**:
  - `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 5): that note
    documents the `ultracode` setting, which "sets effort level to 'xhigh'" —
    naming a specific effort tier absent from this source. This source never uses
    tier names (no "low"/"medium"/"high"/"xhigh"/"max" appear in the body) and
    never mentions `ultracode`; it is a conceptual explainer of what effort *does*,
    not a reference for the tier names or the `ultracode` shortcut. Practitioners
    should read this source for the mental model and the other note for the
    concrete setting name.
  - `blog-anthropic-fable-finding-unknowns.md` (Claim 11): that note documents
    Thariq Shihipar's claim that "Claude Fable is the first model where I find the
    quality of the work is bottlenecked by my ability to clarify its unknowns" —
    a single practitioner's account of working with Fable specifically. This
    source's Fable-as-specialist framing (Claim 7) is a complementary, more
    general characterization from a different Anthropic author: Fable's value is
    in recognition/pattern-matching on problems "everyone else is stuck on,"
    which is consistent with (but does not repeat) the "bottlenecked by my
    ability to clarify" framing — one describes what Fable is good at, the other
    describes the practitioner skill needed to get the most out of it.

- **Contradicts**: None identified. No existing source note makes a claim about
  Claude Code effort levels or model selection that this source opposes; the
  corpus's prior effort-level mentions (`blog-anthropic-dynamic-workflows-claude-
  code.md` Claim 5, naming `ultracode`/"xhigh") are narrower in scope (a specific
  setting) rather than in tension with this source's broader conceptual claims.

- **Novel**:
  - The explicit statement that model weights are read-only/frozen at inference
    and that effort is a per-turn request parameter (Claims 3–4) — no prior corpus
    source explains the mechanism this precisely for Claude Code specifically.
  - The "did it not try hard enough, or did it not know enough?" diagnostic
    framework (Claim 6) — no prior source gives a named, two-branch troubleshooting
    heuristic for choosing between raising effort and switching models.
  - The Fable/Opus/Sonnet specialist/expert/generalist metaphor (Claim 7) — new to
    the corpus; no prior source characterizes the three model tiers this way.
  - The Opus 4.8 vs. Opus 4.7 default-effort comparison (Claim 5) — first corpus
    mention of this specific internal comparison.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the "start with defaults, adjust only when
  disappointed" guidance (Claim 9) as the default recommendation for both model
  and effort selection in Claude Code sessions, alongside the parallel GitHub
  Copilot guidance already citable from `docs-github-copilot-1m-context-reasoning-
  levels.md` Claim 4 — this becomes a cross-vendor-corroborated default, not just
  an Anthropic assertion.
- **Chapter 02 (Harness Engineering)**: Add the two-branch diagnostic framework
  (Claim 6: "did it not try hard enough, or did it not know enough?") as a named,
  reusable troubleshooting step when a Claude Code session produces a wrong or
  incomplete result — before defaulting to "just switch to a bigger model,"
  practitioners should check whether the actual failure was skipped files, unrun
  tests, or a missed double-check, which is an effort-level fix, not a model fix.
- **Chapter 04 (Context Engineering / Model Selection)**: Add the model/effort
  orthogonality framing (Claim 1) as the organizing concept for any section on
  configuring Claude Code — currently the guide's mentions of effort levels
  (via `blog-anthropic-dynamic-workflows-claude-code.md`) are limited to the
  `ultracode` shortcut and don't establish that model and effort are independent,
  separately-tunable axes. Add the frozen-weights/read-only clarification (Claim
  3) to reinforce why context engineering, not accumulated session history,
  is the practitioner's actual lever on model behavior.
- **Chapter 05 (Team Adoption / Cost Management)**: Add the routine-vs-complex
  cost guidance (Claim 8) as a concrete cost-optimization heuristic: route
  routine, well-bounded work to smaller models at default effort; reserve larger
  models for tasks where a smaller model would need many more iterations to reach
  the same quality bar. Pair with the cross-vendor corroboration from Cursor
  Bugbot's 35%-more-bugs-at-high-effort finding to show this effort/cost tradeoff
  recurs across different agentic tools, not just Claude Code.

## Extraction Notes

- The source was read across seven separate WebFetch passes: one full structural
  map (all section headings and paraphrased content), five section-targeted
  passes to extract verbatim quotes (each kept under the tool's ~125-character
  quote limit to avoid triggering copyright-refusal behavior, which occurred on
  a first attempt to request the full verbatim text in one call), and one
  targeted pass confirming the byline (Lydia Hallie), publication date (July 7,
  2026), and the absence of explicit effort-tier names, `ultracode`, and any
  substantive Haiku/Mythos discussion (both appear only in the site's navigation
  menu, not the article body).
- All `Quote` fields above were returned by WebFetch inside quotation marks in
  response to targeted, section-scoped prompts; none were reconstructed from the
  structural-map paraphrase pass. Where a quote could plausibly be an
  AI-paraphrase artifact of the fetch tool rather than a true verbatim string
  (a known risk noted in other source notes' Extraction Notes for this same
  WebFetch behavior), the Assayer should spot-check directly against the source
  URL — this note's author was not able to view raw HTML/text directly and relied
  on the WebFetch tool's fidelity for character-level accuracy.
- No sub-pages were linked from the post that warranted following — this is a
  single, self-contained long-form explainer with no "read more" links to related
  docs pages.
- The post does not name specific effort-level tiers (no "low/medium/high/max/
  xhigh" in body text) despite the Prospector's triage key question asking about
  tradeoffs "between... effort levels (low/medium/high/max)". This note does not
  invent tier-specific guidance the source doesn't contain; the tier names remain
  documented only in `blog-anthropic-dynamic-workflows-claude-code.md` (the
  `ultracode`/"xhigh" mention).
