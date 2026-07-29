---
source_url: https://blog.jetbrains.com/ai/2026/07/ponytail-skill-claude-tested/
source_type: blog-post
title: "Ponytail Skill for Claude Code: Does It Really Cut Agent Code by 54%?"
author: Denis Shiryaev (JetBrains AI)
date_published: 2026-07-28
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: emerging
issue: "#2297"
---

# Ponytail Skill for Claude Code: Does It Really Cut Agent Code by 54%?

> Part 3 of JetBrains AI's paired A/B benchmark series testing vendor
> "token/code saving" tools against real agentic work: Ponytail, a Claude
> Code plugin that injects a "write-the-minimum-code" ruleset via a
> SessionStart hook, advertises −54% code / −22% tokens / −20% cost / −27%
> time and measures out to −15.4% code (p=0.088, not quite significant) and
> −10.3% cost (p=0.004, significant) across 80 paired SkillsBench tasks — the
> first tool in the series to show a statistically solid cost saving, though
> still far below the vendor's advertised figures and concentrated almost
> entirely on tasks where the baseline agent over-built.

## Source Context

- **Type**: blog-post (practitioner empirical benchmark / vendor blog,
  JetBrains AI, published 2026-07-28). Explicitly the third entry in a
  series: Part 1 tested the "Caveman" prompt-compression skill
  (`blog-jetbrains-caveman-token-savings-test.md`), Part 2 tested the "rtk"
  Bash-output-compression hook (`blog-jetbrains-rtk-token-savings-test.md`),
  and this post applies the same paired A/B methodology to "Ponytail," a
  code-minimization skill.
- **Author credibility**: Denis Shiryaev, same author/blog as Parts 1 and 2.
  The post discloses a named sandbox platform (Harbor 0.18), a named
  agent/version (Claude Code 2.1.201, headless, pinned in both arms), a
  named model and reasoning effort (`claude-sonnet-5`, medium effort), a
  named benchmark suite (SkillsBench, 80 paired tasks, auto-graded 0-1), a
  named tool version (Ponytail v4.8.4), an exact trial count (251 billed
  agent trials), and a total dollar cost (USD 246.09). This level of
  methodology disclosure matches Parts 1 and 2 and is independently
  checkable in principle.
- **Scope**: Covers a single code-minimization skill (Ponytail v4.8.4)
  tested against a single benchmark suite (SkillsBench, data/analysis/repair
  tasks) on a single model (`claude-sonnet-5`, medium reasoning effort) via
  Claude Code 2.1.201 in a Harbor-sandboxed environment. Does NOT cover:
  front-end-heavy codebases (which the authors say are where the vendor's
  benchmark and largest claimed wins concentrate), other models, other
  reasoning-effort levels, or Ponytail's effect on security/accessibility
  preservation (the post explicitly says it tests task completion only).

## Extracted Claims

### Claim 1: Ponytail's advertised savings do not hold at face value — measured code and cost reductions are roughly a third of the advertised figures, though cost savings are statistically significant
- **Evidence**: Full 80-paired-task A/B run, Claude Code 2.1.201 on
  `claude-sonnet-5` at medium reasoning effort, comparing stock Claude Code
  against Ponytail v4.8.4 with its ruleset injected via SessionStart hook.
- **Confidence**: settled (first-party measured result with disclosed
  p-values, directly comparable to the vendor's own advertised numbers)
- **Quote**: "We ran 80 paired tasks to test the ponytail skill for Claude
  Code. Advertised: −54% code, -22% tokens, -20% cost, -27% time. Measured:
  −15% code, −10.3% cost and -11% time."
- **Our assessment**: This is the headline finding and fits the pattern
  established by Parts 1 and 2: an advertised percentage collapses under
  paired measurement. Unlike Caveman (real but modest savings) and rtk (no
  savings / a cost increase), Ponytail is the first of the three to land a
  measured, statistically significant (p=0.004, see Claim 4) cost reduction
  — see Claim 8 for the series-wide comparison.

### Claim 2: Ponytail only activates reliably when installed as a plugin with a SessionStart hook that force-injects its ruleset — dropping the bare SKILL.md into a skills folder and letting the model decide produced zero self-activations
- **Evidence**: A disclosed ten-session test of the "obvious" install path
  (copying SKILL.md into a skills folder, no hook), contrasted with the
  hook-based install path actually used for the benchmark arm.
- **Confidence**: settled (first-party disclosed test of the alternate
  install path)
- **Quote**: "Across all ten sessions it self-activated zero times."
- **Our assessment**: This directly corroborates a near-identical finding in
  Part 2 about rtk's install mechanism (a PreToolUse hook, not a
  model-visible instruction — see `blog-jetbrains-rtk-token-savings-test.md`
  Claim 2) and extends the general pattern that these efficiency skills
  depend on forced instruction-injection at the harness level; a skill that
  merely sits in a skills folder for the model to discover on its own may
  never fire in practice, regardless of how good its ruleset is once active.

### Claim 3: Ponytail's mechanism is a decision ladder the model climbs before writing any code — checking whether the code needs to exist, is already present, or is covered by the standard library/platform/a dependency — before writing the minimum that works, while explicitly leaving validation, error handling, security, and accessibility untouched
- **Evidence**: Description of the injected ruleset's decision procedure,
  as disclosed in the post.
- **Confidence**: settled (first-party description of the tool's documented
  mechanism)
- **Quote**: "Mechanically it is a ladder the model climbs before writing
  anything. Does this need to exist at all? Is it already in the codebase?
  Does the standard library do it? A native platform feature? An installed
  dependency? Can it be one line? Only then: write the minimum that works."
- **Quote (scope carve-out)**: "validation, error handling, security and
  accessibility are explicitly off the chopping block."
- **Our assessment**: This is architecturally distinct from both prior
  tools in the series: Caveman instructs terser narration (Part 1), rtk
  compresses Bash output post-hoc via a hook (Part 2), while Ponytail
  intervenes upstream at the point of code-writing decisions themselves.
  This is the first tool in the series targeting the actual code artifact
  rather than surrounding narration or tool output, which plausibly explains
  why it is the first to show a real, if modest, cost effect.

### Claim 4: A typical task cost 10.3% less with Ponytail installed, a statistically significant result across 80 paired tasks
- **Evidence**: Paired per-task cost comparison across the full 80-task run.
- **Confidence**: settled (disclosed statistical test with p-value)
- **Quote**: "A typical task cost 10.3% less with ponytail installed: p=0.004
  across 80 pairs, cheaper on 46 tasks and dearer on 34."
- **Our assessment**: The headline positive result of the series so far.
  Notably the effect is not universal even within this benchmark — 34 of 80
  tasks were more expensive with Ponytail installed — meaning the aggregate
  saving is a net effect across a distribution, not a saving realized on
  every task.

### Claim 5: Median code reduction was 15.4% (10,205 lines became 8,756 across the full run), short of statistical significance at conventional thresholds
- **Evidence**: Paired per-task lines-of-code comparison across the full
  80-task run.
- **Confidence**: settled (disclosed measurement with p-value), though the
  authors' own p-value (0.088) sits above the conventional 0.05 significance
  threshold
- **Quote**: "Across 80 paired tasks a typical task shed 15.4% of the code
  the agent wrote; in total, 10,205 lines became 8,756."
- **Our assessment**: Worth flagging precisely because this is the metric
  the vendor's 54% claim is about, and even the directionally-supportive
  measured value (15.4%) does not clear p<0.05 (reported elsewhere in the
  post as p=0.088). Practitioners should read the code-reduction claim as
  suggestive, not confirmed, on this benchmark — in contrast to the cost
  result (Claim 4), which does clear significance.

### Claim 6: Savings are highly concentrated — big-build tasks saw code cut by up to 31%, while tasks where the baseline agent already wrote little code saw no measurable change
- **Evidence**: Sub-analysis splitting task pairs by how much code the
  baseline (non-Ponytail) arm wrote.
- **Confidence**: settled (first-party sub-analysis)
- **Quote**: "On big builds the cut reaches −31%. On tasks where the plain
  agent already wrote almost nothing, the typical task moved by zero."
- **Our assessment**: This is the mechanistic explanation for why the
  aggregate 15.4%/10.3% figures undersell the technique's value in the right
  context and oversell it in the wrong one: Ponytail's benefit is
  concentrated entirely in over-building scenarios and vanishes to zero
  where there's nothing to trim. This mirrors the concentration pattern in
  Part 1 (Caveman's savings capped by narration share) and Part 2 (rtk's
  savings capped by Bash-call share) — every tool in this series has an
  architectural or behavioral ceiling that determines where its
  measured-average number actually comes from.

### Claim 7: The benchmark used (SkillsBench) is a conservative test of the code-reduction claim specifically, because it contains data/analysis/repair tasks rather than the front-end over-building scenarios where the vendor's own claimed figures concentrate
- **Evidence**: The authors' explicit statement contrasting SkillsBench's
  task composition with the vendor's own benchmark composition, plus a
  direct quote from the vendor's own writeup about where its savings
  concentrate.
- **Confidence**: settled (first-party disclosed benchmark-composition
  caveat, corroborated by a quoted vendor admission)
- **Quote**: "SkillsBench is data, analysis and repair work; it contains few
  of the front-end over-build traps that produce ponytail's largest wins.
  This is a fair test of the cost, speed and quality claims and a
  conservative test of the code claim."
- **Quote (vendor's own admission)**: their own writeup is explicit that the
  figure "reaches 94% where an agent over-builds and is near zero where the
  code is already minimal."
- **Our assessment**: This is an important interpretive caveat the authors
  volunteer against their own headline finding: the 15.4%/54% gap may partly
  reflect a genuinely conservative benchmark choice, not only vendor
  overstatement. A team whose actual workload is front-end-heavy and prone
  to over-building might plausibly see savings closer to the vendor's
  figure than to this post's 15.4%. This nuance should travel with the
  headline number whenever it's cited.

### Claim 8: Ponytail is the first tool in this three-part series to produce a clear, statistically solid cost saving — Caveman showed modest real savings, rtk showed none (or a cost increase)
- **Evidence**: The authors' own explicit series-wide comparison across all
  three tested tools.
- **Confidence**: settled (first-party synthesis directly citing each prior
  post's own headline numbers)
- **Quote**: Ponytail is "the first tool in this series that clearly saved
  money."
- **Our assessment**: Read alongside `blog-jetbrains-caveman-token-savings-test.md`
  Claim 1 (measured −8.5% vs. advertised −65%) and
  `blog-jetbrains-rtk-token-savings-test.md` Claim 1 (measured +7.6% cost at
  low effort, ±0% at high effort, vs. advertised −60–90%), this establishes
  a three-point series trend: vendor-advertised percentages for agentic
  token/cost/code-saving skills have so far ranged from "real but far
  smaller than claimed" (Caveman, Ponytail) to "illusory or negative" (rtk).
  Ponytail is the strongest positive result of the three, but even its
  strongest metric (cost, −10.3%) is roughly half the vendor's own claimed
  cost figure (−20%).

### Claim 9: A ten-task pilot run gave a misleading result in the opposite direction from the eventual finding — showing a cost increase and a quality collapse that did not hold up at the full 80-task scale
- **Evidence**: The authors' own reported smoke-test-vs-full-run comparison.
- **Confidence**: settled (first-party reported result of their own
  two-stage testing process)
- **Quote**: "Our ten-task smoke run said ponytail cut code by 3% and made
  things 9.6% more expensive, with mean task scores collapsing from 0.51 to
  0.31."
- **Our assessment**: This is the third instance across the series of a
  small-sample pilot producing a result that reverses or evaporates at full
  scale — Part 1's Claim 6 (a 10-task pilot showed −30% savings that
  dissolved to −8.5%) and Part 2's Claim 11 (a k=1 smoke showed +35% cost
  that evaporated to noise at k=3) both document the same trap. Notably,
  here the pilot mirage pointed in the *worst possible* direction (implying
  Ponytail both cost more and produced markedly worse task scores), which
  would have been a strong reason to abandon the tool if the authors had
  stopped at the pilot. This strengthens the series-wide lesson: escalate
  small-sample agentic A/B pilots to full scale before drawing conclusions,
  regardless of which direction the pilot points.

### Claim 10: Task quality was statistically indistinguishable between arms, but the authors are explicit this is a null result, not proof of equivalence
- **Evidence**: Paired quality-score comparison across the full 80-task run.
- **Confidence**: settled for the measured result; the authors' own framing
  of its interpretive limits is itself worth preserving
- **Quote**: "Nine tasks scored slightly worse, six slightly better, 65
  identical — statistically indistinguishable."
- **Our assessment**: The authors' own caveat about this finding (see Claim
  11) is as important as the number itself, and this note preserves both
  rather than treating "no significant difference" as "proven equivalent."

### Claim 11: The authors explicitly caution that their quality finding is a null result, not a clean bill of health, because the study was not powered to detect small quality degradations and does not test security or accessibility preservation
- **Evidence**: The authors' own methodological caveat about the limits of
  their quality measurement.
- **Confidence**: settled (first-party disclosed limitation)
- **Quote**: this "is a null result, not a clean bill of health." They
  explicitly state tests measure task completion, not security or
  accessibility preservation.
- **Our assessment**: Directly relevant given Claim 3's ruleset explicitly
  carves out validation, error handling, security, and accessibility as
  "off the chopping block" in principle — but the benchmark's own verifier
  only scores task completion, so it cannot independently confirm that
  carve-out is actually honored in the code Ponytail produces. This is a
  meaningful gap between what the tool claims to preserve and what this
  particular study is capable of verifying.

### Claim 12: Ruleset adherence to Ponytail's own self-marking convention was almost nonexistent — the skill asks the model to flag deliberate shortcuts with a `ponytail:` comment, but this happened once across 80 trials despite the ruleset being confirmed present in context every time
- **Evidence**: Disclosed count of how often the model actually followed the
  skill's own self-annotation instruction, despite confirming the ruleset
  was in context for all treatment trials.
- **Confidence**: settled (first-party disclosed adherence count)
- **Quote**: "Across 80 trials with the ruleset demonstrably in context,
  that happened once."
- **Our assessment**: This is a distinct and separately valuable finding
  from the aggregate cost/code numbers: even when a skill successfully
  activates (unlike Claim 2's zero-self-activation finding) and its
  instructions are demonstrably present in the model's context, the model
  can still largely ignore a specific sub-instruction (the self-marking
  convention) while still following the broader spirit of the ruleset
  (writing less code). This is a caution for anyone relying on an injected
  ruleset's self-reporting/self-flagging behavior as a compliance signal —
  the aggregate behavioral effect (less code) and adherence to a specific
  textual instruction within the same ruleset are not the same thing and
  should be measured separately.

### Claim 13: The authors' closing verdict is that Ponytail works and is worth installing-and-forgetting for a modest net benefit, but that the advertised 54% should not be expected outside over-building-prone workloads
- **Evidence**: The post's closing "Verdict" section, synthesizing the cost
  result (Claim 4), the code result (Claim 5), the quality null result
  (Claim 10), and the concentration finding (Claim 6) into a practitioner
  recommendation.
- **Confidence**: anecdotal (this is the authors' own bottom-line judgment
  call and adoption recommendation, not an additional measurement —
  consistent with how the equivalent verdict was graded in
  `blog-jetbrains-caveman-token-savings-test.md` Claim 8)
- **Quote**: "Ponytail works. Across 80 paired tasks, it cut the typical bill
  by 10.3% and reduced code written by 15%, with no quality difference we
  could detect. It is the first tool in this series that clearly saved money.
  If you install it and forget about it, you should be modestly better off."
- **Quote (caveat attached to the verdict)**: "Do not expect the advertised
  54% everywhere. Ponytail's benchmark uses tasks with obvious over-building
  traps. Ours did not. In our runs, code fell 31% on larger builds and barely
  moved on tasks that were already lean. The more over-building your agent
  does, the more ponytail can cut."
- **Our assessment**: This is the first unambiguously *positive* adoption
  recommendation in the three-part series, and it is worth contrasting with
  the Part 1 verdict on Caveman ("use it if you like it" — a low-risk
  optional extra, `blog-jetbrains-caveman-token-savings-test.md` Claim 8) and
  the implicit Part 2 verdict on rtk (no savings / a cost increase). The
  authors' framing is carefully bounded, though: "modestly better off" and
  "install it and forget about it" describe a set-and-forget background
  saving, not a cost-optimization lever worth engineering effort — and the
  second half of the verdict re-attaches the task-composition condition from
  Claim 6/Claim 7 directly to the recommendation. Any guide language citing
  this as a "yes, adopt" data point should carry the conditioning clause with
  it; the recommendation is genuinely workload-dependent, by the authors'
  own statement.

## Concrete Artifacts

```
# Benchmark setup (from post's Methodology/Setup section)
# Source: https://blog.jetbrains.com/ai/2026/07/ponytail-skill-claude-tested/

Platform:    Harbor 0.18 (Docker sandboxes with task verifiers)
Harness:     Claude Code 2.1.201, headless, pinned in both arms
Model:       claude-sonnet-5 at medium reasoning effort
Benchmark:   SkillsBench, 80 paired tasks, auto-graded 0-1
Arm A:       stock Claude Code
Arm B:       Ponytail v4.8.4, ruleset injected via SessionStart hook
Volume:      251 total billed agent trials; USD 246.09 total cost

# Results
Advertised:  -54% code, -22% tokens, -20% cost, -27% time
Measured:    -15.4% code (p=0.088, 10,205 -> 8,756 lines),
             -10.3% cost (p=0.004, cheaper on 46 tasks, dearer on 34),
             -11% time
Concentration: up to -31% on big-build tasks; ~0% where baseline already wrote little
Quality:     9 worse / 6 better / 65 tied (statistically indistinguishable;
             authors call this a null result, not proof of equivalence)
Ruleset self-marking adherence (`ponytail:` comments on deliberate shortcuts):
             1 occurrence across 80 trials, despite ruleset confirmed present
             in context on every treatment trial
Install path check: SKILL.md dropped into a skills folder with no hook ->
             self-activated 0 times across 10 sessions
Pilot (10-task smoke run): -3% code, +9.6% cost, mean quality 0.51 -> 0.31
             (did not replicate at full 80-task scale)

# Series comparison (as stated in this post)
Caveman (Part 1):  advertised -65%, measured -8.5%
rtk (Part 2):      advertised -60-90%, measured +7.6% cost increase (low effort), +-0% (high effort)
Ponytail (Part 3): advertised -54% code/-22% tokens/-20% cost/-27% time,
                   measured -15% code/-10.3% cost/-11% time
```

## Cross-References

- **Corroborates**:
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 1 (measured 8.5%
    vs. advertised 65%) and `blog-jetbrains-rtk-token-savings-test.md`
    Claim 1 (measured +7.6%/±0% vs. advertised 60–90%): this source's
    Claim 1 continues the same series-wide pattern of vendor-advertised
    percentages collapsing under paired A/B measurement, though Ponytail is
    the first of the three where the collapsed number still clears
    statistical significance on the cost dimension.
  - `blog-jetbrains-rtk-token-savings-test.md` Claim 2 (rtk requires a
    PreToolUse hook; the model doesn't need to know it exists): this
    source's Claim 2 (Ponytail self-activates zero times without a
    SessionStart hook) is an independent, corroborating instance of the
    same broader pattern — these efficiency skills function as
    harness-level forced injections, not as skills the model reliably
    discovers and opts into on its own.
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 6 (a 10-task pilot
    showing −30% savings that dissolved to −8.5% at 82 tasks) and
    `blog-jetbrains-rtk-token-savings-test.md` Claim 11 (a k=1 smoke showing
    +35% cost that evaporated to noise at k=3): this source's Claim 9 (a
    10-task pilot showing worse cost AND worse quality, both of which
    reversed at the full 80-task run) is a third, independent instance of
    the same small-sample-pilot instability trap — now demonstrated to
    manufacture misleading signals in both individual metrics (cost,
    quality) simultaneously, not just one metric at a time.

- **Contradicts**: None identified requiring a contradiction issue. This
  source does not dispute any existing corpus claim; it extends the same
  series' methodology to a third tool and reports a directionally different
  (more positive) result than Parts 1–2, which is a difference in measured
  outcome across distinct tools under the same methodology, not a
  contradiction between sources.

- **Extends**:
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 3 (Caveman's
    savings are capped by the narration share of output tokens) and
    `blog-jetbrains-rtk-token-savings-test.md` Claim 3 (rtk's savings are
    capped by the Bash-call share of tool traffic): this source's Claim 6
    (Ponytail's savings are capped by how much the baseline agent
    over-built) identifies a third, distinct ceiling mechanism — not
    content type, not tool surface, but the *baseline's own over-building
    tendency on a given task*. Together the three notes establish that
    every tested token/code/cost-saving technique in this series has some
    structural ceiling determining where its average measured effect
    actually comes from, and that ceiling is specific to the technique's
    point of intervention.
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 8 (recommended
    ceiling for prompt-compression skills is "high single digits"): this
    source's Claim 4 (−10.3% cost, p=0.004) shows a code-level intervention
    clearing a higher, statistically solid ceiling than the narration-level
    or Bash-output-level interventions tested in Parts 1–2 — suggesting
    that where a technique intervenes in the token/code-generation pipeline
    (upstream at code-writing decisions vs. downstream at narration or tool
    output) may matter more than the specific advertised percentage when
    predicting realistic savings.

- **Novel**:
  - The explicit vendor self-admission, quoted directly in this post, that
    the vendor's own claimed figure is task-composition-dependent ("reaches
    94% where an agent over-builds and is near zero where the code is
    already minimal") — no prior post in the series quotes the tested
    vendor conceding this directly, making Ponytail's advertised number the
    most self-qualified of the three claims examined so far.
  - The finding (Claim 12) that a ruleset's aggregate behavioral effect
    (less code written) and a model's adherence to a specific, checkable
    sub-instruction within that same ruleset (self-marking shortcuts with a
    `ponytail:` comment) can diverge almost completely — the model complied
    with the spirit of the instruction while all but ignoring one of its
    explicit, individually verifiable requirements.
  - The first tool in the series with a measured, statistically significant
    (p=0.004) net cost saving.

## Guide Impact

- **Chapter 02 (Harness Engineering — skills, hooks)**: Add Claim 2/Claim 3
  as concrete evidence that a "code-minimization" skill or ruleset needs to
  be force-injected via a SessionStart-style hook to reliably activate —
  extend the existing rtk-derived guidance (from
  `blog-jetbrains-rtk-token-savings-test.md`) that efficiency skills
  generally require harness-level injection rather than passive
  availability, now corroborated by a second, architecturally different
  tool. Add Claim 12 as a caution when designing any hook-injected ruleset:
  do not assume adherence to a specific sub-instruction (e.g. a
  self-flagging convention) just because the ruleset demonstrably activated
  and produced its intended aggregate effect — verify individually.

- **Chapter 04 (Context Engineering — token efficiency and optimization
  tactics that don't work in practice)**: Add this source as the third data
  point in the JetBrains series (alongside Caveman and rtk) for
  cost/token/code-saving vendor claims, specifically noting: (1) Ponytail is
  the first to clear statistical significance on cost (Claim 4), giving
  practitioners a rare positive example rather than only cautionary ones;
  (2) the savings are concentrated almost entirely in over-building
  scenarios (Claim 6) and vanish where baseline code is already minimal —
  guide language recommending this class of tool should qualify the
  recommendation by codebase/task type (front-end-heavy and over-building-
  prone workloads vs. data/analysis work); and (3) even the vendor's own
  writeup concedes this task-dependence (Claim 7), which is a useful
  template for how the guide should frame *any* vendor efficiency claim —
  look for the vendor's own scope qualifications, not just the headline
  number. Where the guide draws an explicit practitioner "should we adopt
  this" recommendation for this class of tool, cite Claim 13 (the authors'
  own closing verdict: "Ponytail works... If you install it and forget about
  it, you should be modestly better off") rather than the raw percentages —
  but carry its attached conditioning clause ("Do not expect the advertised
  54% everywhere") with it, and contrast it against the weaker Part 1 verdict
  on Caveman (`blog-jetbrains-caveman-token-savings-test.md` Claim 8, "use it
  if you like it") so the guide reflects that this series has now produced
  differently-strength recommendations for differently-performing tools.

- **Chapter 04 (Benchmarking methodology)**: Add Claim 9 as a third
  corroborating instance of the series' small-sample-pilot caution
  (alongside Caveman's Claim 6 and rtk's Claim 11) — now demonstrating the
  pilot-instability trap can produce a false *double* negative signal (both
  cost and quality look worse) that fully reverses at full scale, reinforcing
  that practitioners should not trust 10-task or k=1 agentic A/B pilots in
  either direction.

## Extraction Notes

- The source was retrieved via WebFetch. An initial general-summary pass
  was followed by four targeted passes, each requesting verbatim,
  character-for-character reproduction of a specific section (intro/TL;DR
  and methodology; results/findings; mechanism/pilot-run/benchmark-caveat
  passages; verdict/series-comparison/install-guidance passages). Several
  key figures and quotes (e.g. the 15.4%/10,205→8,756 line count, the
  10.3%/p=0.004/46-vs-34 cost result, the "self-activated zero times"
  sentence) were returned identically, word-for-word, across independent
  passes with different prompts, which is the basis for treating them as
  reliable verbatim extractions rather than model paraphrase. Quotes that
  were only paraphrased inconsistently across passes are not used as
  quoted material in this note. The closing "Verdict" passage (Claim 13) was
  re-fetched and confirmed in two further independent passes with different
  prompts, both returning the same contiguous four-sentence passage
  word-for-word; it is quoted here as one unbroken run of sentences rather
  than spliced.
- No sub-pages were followed: the post is a self-contained benchmark
  write-up. The two prior posts in the series (Caveman, rtk) are already
  separate source notes in this corpus and were read in full for
  cross-referencing rather than re-extracted here. The Ponytail vendor's
  own site/README (referenced but not linked with a URL in what was
  fetched) was not independently fetched — this note extracts only what
  the JetBrains post itself states about Ponytail's advertised claims and
  its own quoted admission, not independent verification of the vendor's
  original marketing page.
- No paywall or access issues; the article was fully readable via WebFetch.
- `confidence_overall` is set to "emerging" rather than "settled": while the
  cost result (Claim 4) is statistically significant and the methodology
  disclosure is strong (matching Parts 1–2), the code-reduction result
  (Claim 5, the metric closest to the post's own title claim) does not
  clear conventional significance (p=0.088), and this is a single benchmark
  suite / single model / single reasoning-effort-level test of one tool
  version — consistent with how the two prior posts in this same series
  were also graded "emerging" in this corpus.
- No contradiction issue was filed. This source does not oppose any
  existing corpus claim; it adds a third, structurally consistent data
  point to the same JetBrains benchmark series.
