---
source_url: https://claude.com/blog/product-management-on-the-ai-exponential
source_type: blog-post
title: "Product Management on the AI Exponential"
author: Cat Wu (Head of Product, Claude Code — Anthropic)
date_published: 2026-03-19
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#176"
---

# Product Management on the AI Exponential

> A first-person insider account from Anthropic's Head of Product for Claude Code
> documenting how exponentially improving models reshape PM workflows: replacing
> roadmaps with "side quests," prototypes with demos instead of docs, and producing
> the most specific published METR capability-growth figure (41x task-completion
> horizon over 16 months).

## Source Context

- **Type**: blog-post (practitioner insider — author runs the Claude Code product
  team at Anthropic)
- **Author credibility**: Cat Wu is Head of Product for Claude Code at Anthropic.
  Prior roles: product engineer at Scale AI and Dagster, venture capitalist. Joined
  Anthropic's Research PM team August 2024. She is a direct observer of model
  capability improvement from inside the team building it — as close to primary
  source as exists for "how model progress changes work patterns." The post is
  first-person, based on her own workflows and examples. Vendor-adjacent (she
  works at Anthropic), but the content is observational, not promotional.
- **Scope**: PM-specific workflow account covering: three-tool division of labor,
  the "side quest" experiment cadence, prototype-first planning, model-release
  feature revisitation, the simplicity principle, and organizational role blurring.
  Does NOT cover harness engineering, context management, or code review patterns.
  The METR citation is a reference to external data, not original research.

## Extracted Claims

### Claim 1: AI task-completion horizon has grown 41x over 16 months (METR data)
- **Evidence**: METR benchmark data cited by Wu. Specific comparison:
  Sonnet 3.5 (new, Oct 2024) handled ~21-minute human software tasks;
  Opus 4.6 (Mar 2026) completes ~12-hour tasks approximately 50% of the time.
  21 minutes → 12 hours = ~34x by raw hours; Wu states "41x" (likely accounting
  for methodology differences or a different baseline figure).
- **Confidence**: emerging (METR is a credible external benchmark, but the
  specific citation is indirect — Wu quotes it, not linking to the original
  METR paper)
- **Quote**: "METR found that [Opus 4.6] can complete tasks that would take a
  human software engineer about 12 hours, roughly 50% of the time."
- **Our assessment**: This is the most precise publicly-cited capability-growth
  figure in our corpus. It makes concrete what "exponential improvement" means
  in practitioner terms: not percentage improvements but order-of-magnitude jumps
  in task duration. For Ch01 and Ch05, this number is load-bearing: it justifies
  why planning horizons must shorten and why workarounds become obsolete quickly.
  Treat as emerging rather than settled because Wu's citation does not directly
  link to the METR source and the 41x vs. ~34x discrepancy is unresolved.

### Claim 2: Excalidraw table test shows concrete model-by-model capability progression
- **Evidence**: Wu's direct experimental observation across three model generations.
  She ran the same test (add table functionality to Excalidraw) against successive
  models and recorded the results.
- **Confidence**: anecdotal (single test, insider account, not independently
  verified)
- **Quote**: "Sonnet 3.5 (new), October 2024: Claude failed at adding table
  functionality. Opus 4, June 2025: Occasional success, sufficient for pre-recorded
  demo. Opus 4.6, March 2026: 'Reliable enough that we feel comfortable doing it
  live, in front of thousands.'"
- **Our assessment**: This is the best concrete example in the corpus of what
  "model improvement changes the product" looks like in practice. The progression
  from "fails" → "occasionally works" → "reliable live demo" maps directly to the
  PM planning implication: features that were prototypes six months ago are product
  features today. Cite as the canonical illustration for "why planning horizons
  must shrink."

### Claim 3: A three-tool workflow covers the full PM workday — Claude.ai for strategy, Claude Code for building, Cowork for admin
- **Evidence**: Wu's stated personal workflow at Anthropic.
- **Confidence**: anecdotal (one practitioner; but a highly-informed one with access
  to all tools in their most developed form)
- **Quote**: (paraphrased) Claude.ai: "thought partnership," bouncing ideas. Claude
  Code: prototyping, evals, scripts, API integration. Claude Cowork: admin tasks,
  documentation, travel booking.
- **Our assessment**: This is the most explicit tool-division-of-labor framework
  in our corpus. Notably, it separates *strategic/discursive* work (Claude.ai)
  from *construction* work (Claude Code) from *administrative* work (Cowork).
  The division is not by capability but by workflow phase. For Ch01 (daily
  workflows): this is the practitioner-grounded answer to "which tool for which
  task" — the PM equivalent of what the Sentry CLAUDE.md provides for engineers.
  Caveat: Cowork is an Anthropic-internal tool, so this part of the workflow
  does not generalize. Claude.ai and Claude Code as a two-tool setup does generalize.

### Claim 4: "Side quests" replace long-term roadmaps as the primary planning unit when capabilities change rapidly
- **Evidence**: Wu's description of her PM methodology at Anthropic.
- **Confidence**: anecdotal (practitioner account; but it produces verifiable
  evidence: named features that emerged this way)
- **Quote**: (paraphrased) Self-directed afternoon experiments replaced locked
  roadmaps; features that emerged: Claude Code on Desktop, AskUserQuestion tool,
  todo lists.
- **Our assessment**: "Side quest" is Wu's named methodology for rapid capability
  exploration. The key mechanism: keep roadmap commitments short enough that a new
  model release can change the plan. The fact that three specific shipped features
  (AskUserQuestion, todo lists, Claude Code on Desktop) came from this process
  is the strongest evidence this is a real methodology and not just a framing.
  For Ch01: this is the PM-specific analog of the "prototype before planning"
  pattern. It is the most concrete "how does AI change planning cadence" answer
  in the corpus.

### Claim 5: Prototype-first thinking replaces documentation-first approaches — "wrong bets are cheap"
- **Evidence**: Wu's stated workflow shift. Internal validation: send spec to
  Claude Code, generate working prototype, test with internal users, let engagement
  determine polish level.
- **Confidence**: anecdotal
- **Quote**: "Wrong bets are cheap when prototyping takes an afternoon."
- **Our assessment**: This claim has direct implications for Ch01's coverage of
  spec writing and prototyping. The traditional PM workflow (write spec → get
  approval → hand to eng → build → test) is replaced by: write prompt → get
  prototype → test engagement → decide whether to polish. The bottleneck shifts
  from "can we build it?" to "is it worth polishing?" This is the prototyping
  complement to Osmani's "good spec" piece — Osmani argues for better specs; Wu
  argues specs become prototypes. The two are compatible: a spec-quality prompt
  produces a prototype-quality artifact.

### Claim 6: Each new model release should trigger revisiting existing features for improvement opportunities
- **Evidence**: Wu's stated practice.
- **Confidence**: anecdotal
- **Quote**: (paraphrased) Every new model release prompts reviewing existing
  features for improvement. Example: Claude Code with Chrome browser integration
  emerged from observing users manually switching between Claude Code and browser
  to test web applications.
- **Our assessment**: This is a novel planning heuristic not documented elsewhere
  in our corpus: the model release is itself a planning trigger, not just a
  deployment event. The Chrome integration example is excellent — a user workaround
  (tab-switching) becomes a feature signal, addressed at the next model release
  when it became feasible. For Ch05 (team adoption): this translates to "your
  team should have a standing "model release review" ritual that revisits the
  workaround list."

### Claim 7: "Do the simple thing that works" — workarounds for model limitations become obsolete and should be removed
- **Evidence**: Specific example: initial Claude Code todo lists required system
  reminders to update progress; Opus 4.6 made these reminders redundant.
- **Confidence**: anecdotal
- **Quote**: "Do the simple thing that works."
- **Our assessment**: This is the complement to the "model-release revisitation"
  claim — if revisitation adds features, this claim argues for actively pruning
  complexity that was added to work around old model limitations. For Ch02
  (harness engineering): this is the anti-accumulation principle. Harnesses built
  on early-model workarounds will become expensive scaffolding. The operational
  implication: build in a simplification review tied to model releases. Do not
  let the harness grow indefinitely.

### Claim 8: Capability-first, cost-second prototyping — validate function before optimizing tokens
- **Evidence**: Wu's stated approach.
- **Confidence**: anecdotal
- **Quote**: (paraphrased) "Optimize for capability first before cost reduction.
  Use more tokens than initially calculated. Cost optimization comes after
  capability validation."
- **Our assessment**: This is direct guidance that partially contradicts the
  "minimize token use" framing that appears in harness engineering discussions.
  Wu's point is about the *prototyping phase* specifically: in early exploration,
  token cost is not the binding constraint — capability discovery is. This is
  consistent with the broader "side quest" methodology. For Ch01: add a note
  distinguishing the exploration/prototyping phase (capability-first, cost-second)
  from the production phase (both matter).

### Claim 9: Role blurring — designers ship code, engineers make product decisions, PMs build prototypes and evals
- **Evidence**: Wu's description of her team's operating model at Anthropic.
- **Confidence**: anecdotal
- **Quote**: "Designers ship code, engineers make product decisions, product
  managers build prototypes and evals."
- **Our assessment**: This is the most explicit description of AI-enabled role
  dissolution in our corpus. For Ch05 (team adoption): the mechanism is clear —
  when prototyping and evals become cheap and accessible, the skills that used
  to differentiate role boundaries become commodity. The implication is that
  team hiring and onboarding models (hiring people for roles defined by pre-AI
  capability gaps) may need to change. Treat as a forward-looking claim — it
  describes Anthropic's current state, which is an outlier; most teams are earlier
  in this trajectory.

### Claim 10: Organizational handoffs disappear when every function uses AI — "the whole organization moves at the same speed"
- **Evidence**: Wu's account of how the methodology spread from engineering to
  data science, finance, marketing, legal, and design at Anthropic.
- **Confidence**: anecdotal
- **Quote**: "The whole organization moves at the same speed instead of waiting
  on handoffs."
- **Our assessment**: This is the organizational-velocity claim that complements
  the role-blurring claim. The elimination of handoffs is not just faster delivery;
  it changes the *dependency graph* of work. For Ch05: this is the long-term
  aspiration that justifies the short-term investment in cross-functional AI
  adoption. Pair with Shopify's similar framing (Claim 4 in
  blog-bvp-shopify-ai-playbook) about organizational velocity as the organizational
  adoption end-state.

### Claim 11: Industry partners describe AI as raising the "ceiling" on product team capability, not just floor
- **Evidence**: Direct quotes from Bihan Jiang (Director of Product, Decagon) and
  Kai Xin Tai (Senior PM, Datadog).
- **Confidence**: anecdotal (quotes sourced by Anthropic for the piece; selection
  bias)
- **Quote (Jiang)**: "Claude has raised the ceiling on what good product teams
  can build, and dramatically shortened the distance between idea and prototype."
- **Quote (Tai)**: "Being a PM in an AI-native world is both creative and
  academic...a PM's craft has shifted from defining certainty upfront to
  accelerating discovery."
- **Our assessment**: These quotes are useful rhetorical support but should be
  treated as curated testimonials, not independent evidence. Kai Xin Tai's
  framing ("accelerating discovery" over "defining certainty") is the cleanest
  articulation of the shift Wu describes throughout the post. Can be cited as
  supporting color, but do not use as primary evidence for any claim.

## Concrete Artifacts

**Model capability progression (Excalidraw table test):**
```
Test: Add table functionality to Excalidraw using Claude
- Sonnet 3.5 (new), Oct 2024: Failed
- Opus 4, Jun 2025: Occasional success (sufficient for pre-recorded demo only)
- Opus 4.6, Mar 2026: Reliable live demo in front of thousands
```

**METR capability-growth benchmark:**
```
Task-completion horizon (software engineering tasks, ~50% completion rate):
- Sonnet 3.5 (new), Oct 2024: ~21 minutes
- Opus 4.6, Mar 2026:          ~12 hours
- Ratio:                        ~41x growth in 16 months
Source: METR benchmark (cited by Wu; direct link not provided in post)
```

**Three-tool PM workflow:**
```
Claude.ai    → Thought partnership, strategy, idea bouncing
Claude Code  → Prototyping, evals, scripts, API integration
Claude Cowork→ Admin tasks, documentation, travel booking
             (Cowork is Anthropic-internal; not publicly available)
```

**Features that emerged from "side quest" methodology:**
```
- Claude Code on Desktop
- AskUserQuestion tool
- Todo lists
```

**Wu's prototyping workflow:**
```
1. Write spec
2. Send to Claude Code → working prototype
3. Test with internal users
4. Measure engagement
5. If high engagement → polish
6. If low engagement → wrong bet was cheap, discard
```

## Cross-References

- **Corroborates**: `research-anthropic-ai-transforming-work.md` — Wu's insider
  account provides the PM-layer complement to the engineering-layer data in that
  study. The Anthropic internal research covers engineering teams broadly; this
  covers one specific team (Claude Code PM) in first-person detail. Both point to
  the same direction: AI adoption at Anthropic is deep, multifunctional, and
  accelerating.
- **Corroborates**: `blog-bvp-shopify-ai-playbook.md` Claims 4 and 5 — Wu's
  "whole organization moves at the same speed" and Shopify's organizational-velocity
  framing describe the same end-state from different vantage points (PM insider at
  a small team vs. VP Eng at a large org). Both identify handoff elimination as
  the organizational benefit, not just individual speedup.
- **Corroborates**: `blog-osmani-good-spec.md` (if it covers spec quality as a
  constraint on AI output) — Wu's "prototype-first" and Osmani's "spec quality
  determines output quality" are compatible frameworks for different stages of the
  same workflow.
- **Extends**: `research-anthropic-ai-transforming-work.md` — the broader Anthropic
  study shows AI adoption trajectories for engineering; Wu adds the PM-specific
  layer and the product-side workflow patterns (side quests, model-release
  revisitation, simplicity principle) that the research study does not cover.
- **Novel**: The 41x METR capability-growth figure is the most specific
  capability-trajectory number in our corpus. The "side quest" methodology (named,
  with three specific shipped-feature examples) is original. The "model release as
  planning trigger and pruning trigger" framing is not present elsewhere. The
  three-tool workflow for PM daily work is original.
- **No direct contradictions identified**: The prototype-first claim is compatible
  with Osmani's spec quality claim (different phases); the capability-first-cost-
  second prototyping claim is not in conflict with harness efficiency discussions
  (which focus on production, not exploration).

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add a "PM workflow" section drawing on Wu's
  three-tool division (Claude.ai for strategy, Claude Code for building). Cite
  the side-quest methodology as the AI-native PM planning unit — explicitly
  contrast with traditional sprint/roadmap planning. Use the Excalidraw progression
  as the concrete "why" behind shorter planning horizons.

- **Chapter 01 (Prototype-first thinking)**: Wu's "wrong bets are cheap" framing
  is the sharpest articulation in our corpus of why the spec-to-prototype cycle
  has shortened. Add alongside or after the Osmani spec-quality discussion:
  prototype-first replaces spec-approval gating when prototypes take an afternoon.

- **Chapter 02 (Harness Engineering — Simplicity Principle)**: Wu's Claim 7
  ("do the simple thing that works; workarounds become obsolete") is a direct
  recommendation to build in a simplification review tied to model releases. Add
  this as a recurring harness maintenance ritual alongside the "update CLAUDE.md
  on model upgrade" recommendation.

- **Chapter 05 (Team Adoption)**: Three specific additions:
  1. The role-blurring claim (Claim 9) as a forward-looking organizational state
     to aim toward, with the caveat that Anthropic is an outlier.
  2. The "model release as planning trigger" pattern (Claim 6) as a standing
     ritual recommendation.
  3. The 41x capability figure (Claim 1) as the empirical anchor for "why
     adoption must be dynamic, not a one-time rollout."

- **Chapter 05 (Measuring Impact)**: Wu's emphasis on capability-first,
  cost-second (Claim 8) is a useful check on teams that reject AI prototyping
  because the first pass was expensive. Add as guidance for distinguishing
  exploration economics from production economics.

## Extraction Notes

- The METR citation is the most important data point but is indirect — Wu cites
  the 41x figure without linking to the original METR report. Cross-referencing
  with paper-miller-speed-cost-quality or other benchmark sources to verify the
  ~21 min → ~12 hour progression would strengthen the chapter's use of this claim.
- Wu's account is about her personal workflow; it is not a survey or study. The
  "side quest" methodology is one PM's approach, not an industry survey finding.
  Use as a named, concrete illustration rather than as a prevalence estimate.
- Cowork is an Anthropic-internal tool and is not publicly available as of
  publication date. The three-tool workflow should be described in the guide as
  a principle (separate tools for strategy / construction / admin) rather than as
  a specific tool recommendation. Claude.ai + Claude Code is the generalizable
  two-tool version.
- The two external quotes (Jiang, Tai) were solicited by Anthropic for the post.
  They carry selection bias and should not be cited as independent validation.
- Wu's background (Scale AI, Dagster, VC) means she brings both engineering and
  investment-side perspectives to the PM role. Her emphasis on prototyping as
  the primary planning tool likely reflects this hybrid background; it may be
  more natural for technical PMs than for non-technical ones.
