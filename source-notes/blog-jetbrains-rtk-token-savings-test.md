---
source_url: https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/
source_type: blog-post
title: "Does \"rtk\" Skill Really Cut Agent Tokens by 60–90%? We Tested It"
author: Denis Shiryaev (JetBrains AI)
date_published: 2026-07-20
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2095"
---

# Does "rtk" Skill Really Cut Agent Tokens by 60–90%? We Tested It

> Part 2 of JetBrains AI's paired A/B benchmark series testing vendor "token
> saving" tools against real agentic work: rtk ("Rust Token Killer"), a
> Claude Code `PreToolUse` hook that compresses Bash command output, advertises
> 60–90% token savings but measures out to a +7.6% cost *increase* at low
> reasoning effort (p=0.004) and a flat 0% at high effort — because the hook
> only ever touches Bash output, which the authors calculate caps its
> theoretical ceiling at ≈3% of input tokens, and because rtk's own
> self-reported "tokens saved" scoreboard counts a counterfactual (uncompressed,
> uncached, untruncated output) that Claude Code's own truncation and caching
> already eliminate.

## Source Context

- **Type**: blog-post (practitioner empirical benchmark / vendor blog, JetBrains
  AI, published 2026-07-20). Explicitly framed as "Part 2 of a series where we
  take public 'token saving' add-ons for coding agents and run the same paired
  A/B benchmark against each of them," with Part 1 being the Caveman skill test
  (`blog-jetbrains-caveman-token-savings-test.md`).
- **Author credibility**: Denis Shiryaev, same author/blog as Part 1. The post
  discloses a named harness (Harbor 0.18), a named agent/version (Claude Code
  2.1.201), a named model (`claude-sonnet-5`), a named benchmark suite
  (SkillsBench, 86 of 87 tasks), exact trial counts (425 billed trials), and a
  total dollar cost (≈USD 320). It also discloses per-arm instrumentation (rtk's
  own audit log and `history.db` persisted on every with-rtk trial) specifically
  to distinguish "rtk saved nothing" from "rtk never ran." This level of
  methodological disclosure is independently verifiable in principle (harness,
  benchmark, and rtk are all stated to be Apache-2.0) even without knowing the
  author's personal credentials.
- **Scope**: Covers a single token-compression tool (rtk v0.43.0) tested against
  a single benchmark suite (SkillsBench) on a single model (`claude-sonnet-5`)
  via Claude Code 2.1.201 in a Harbor-sandboxed environment, at two reasoning
  effort levels (low and high). Does NOT cover: other shell-output compression
  tools, other models, non-Claude-Code harnesses, or rtk's behavior on
  non-benchmark real-world repositories.

## Extracted Claims

### Claim 1: rtk's advertised 60–90% token savings does not hold on real agentic work — measured impact is a cost *increase* at low reasoning effort and a wash at high effort
- **Evidence**: Full 86-task paired A/B run at both low and high reasoning
  effort, using Claude Code 2.1.201 with `claude-sonnet-5`.
- **Confidence**: settled (first-party measured result with disclosed p-values)
- **Quote**: "TL;DR: rtk advertised saving: 60–90%. Measured on real agent
  work: +7.6% more expensive at low reasoning effort (p=0.004), ±0% at high
  effort. Setup: Claude Code 2.1.201 · claude-sonnet-5 low and high efforts ·
  SkillsBench. Task quality: unchanged in both arms, at both effort levels."
- **Our assessment**: This is the headline finding and it is stronger than
  Part 1's result: the Caveman skill (Part 1) at least showed a real, if much
  smaller than advertised, savings (measured 8.5% vs. claimed 65%). rtk shows
  no savings at all in either tested condition — a net cost increase at low
  effort, and a statistical null at high effort. The vendor claim doesn't just
  overshoot; on this benchmark it never materializes as savings anywhere.

### Claim 2: rtk works by installing a Claude Code `PreToolUse` hook that rewrites eligible shell command output before the model sees it, transparently to the model
- **Evidence**: Description of the mechanism and a live worked example (`git
  status` and `pytest` output compression) captured from the authors' test
  container.
- **Confidence**: settled (first-party description of the tool's documented
  mechanism, corroborated by a live captured example)
- **Quote**: "A Claude Code PreToolUse hook rewrites eligible shell commands
  transparently, so the model doesn't even have to know rtk exists. The
  README promises 60–90% less token consumption and walks through a
  30-minute session where 118k tokens of command output become 24k."
- **Our assessment**: The mechanism is a clean, low-risk integration point
  (a hook, not a model-visible instruction or system-prompt change), which is
  why the authors credit rtk's engineering as sound even while disputing the
  savings claim (see Claim 9/Verdict). This is architecturally distinct from
  Caveman (Part 1), which worked by instructing the model to write tersely —
  rtk's compression happens entirely outside the model's control.

### Claim 3: rtk can only ever touch Bash tool output — Claude Code's built-in Read and Grep tools bypass the hook entirely, and rtk's own documentation acknowledges this
- **Evidence**: Structural analysis of what a `PreToolUse` Bash hook can and
  cannot intercept, citing rtk's own README footnote.
- **Confidence**: settled (architectural fact about Claude Code's tool
  surface, corroborated by the vendor's own documentation)
- **Quote**: "Claude Code reads files with its built-in Read/Grep tools,
  which bypass the Bash hook entirely; rtk's own README admits this in a
  footnote."
- **Our assessment**: This is the single most transferable, guide-relevant
  finding in the post: it is not specific to rtk but to *any* tool built as a
  Bash-only `PreToolUse` hook. Whatever fraction of a session's tokens flow
  through Read/Grep instead of Bash is permanently outside such a tool's
  reach, no matter how good its compression algorithm is. Any practitioner
  evaluating a similar shell-output-compression skill should ask what
  fraction of their own agent's token consumption is Bash output at all.

### Claim 4: Replaying baseline transcripts before spending any money predicted a theoretical ceiling of roughly 3% of input tokens for rtk's maximum possible impact — and that back-of-envelope number correctly predicted the measured outcome
- **Evidence**: Replay of 83 existing baseline transcripts (same model, same
  benchmark) to estimate, without running any paid trials, what fraction of
  agent bytes rtk could even touch: 33% of Bash calls were eligible for
  rewriting, carrying under 20% of tool-result characters, further discounted
  because tool-result characters are only a slice of total input tokens
  (context is re-read every turn).
- **Confidence**: settled (first-party disclosed calculation, later validated
  against the paid measured result)
- **Quote**: "What's left, 33% of Bash calls, carries just under 20% of
  tool-result chars; and tool results are themselves only a slice of what a
  session bills as input, because the same context is re-read on every turn.
  Squeeze rtk's whole share by 70% and the cap works out to ≈3% of input
  tokens. This number cost nothing to compute, and it predicted the outcome."
- **Our assessment**: This is a valuable methodological pattern independent
  of rtk specifically: before running expensive paired trials, a cheap
  transcript-replay analysis of "what fraction of tokens could this
  intervention possibly touch" can predict whether a tool's advertised
  savings are even structurally plausible. A ≈3% theoretical ceiling made the
  measured near-zero/negative result unsurprising in hindsight.

### Claim 5: On the full 86-task run at low reasoning effort, the with-rtk arm was significantly *more* expensive (median +7.6% per task, p=0.004), with more turns and more cache reads, while the only token class rtk actually compresses moved by a statistically insignificant amount
- **Evidence**: Paired comparison across 80 clean pairs (of 86 tasks) at low
  reasoning effort, using Wilcoxon signed-rank tests on per-task deltas.
- **Confidence**: settled (disclosed statistical test with p-values across
  multiple metrics)
- **Quote**: "Across 80 clean pairs the with-rtk arm came out a median
  +7.6% more expensive per task (p=0.004, after correcting a cost-accounting
  gap we found along the way), on +13.8% more turns (p=0.03) and +14.3% more
  cache reads (p=0.008). Meanwhile "new input"; the only token class rtk
  actually compresses, moved just +3.2% (p=0.23): a flat null precisely where
  the ceiling analysis said the entire benefit had to live."
- **Our assessment**: The +3.2% (non-significant) movement in "new input" —
  the specific token class rtk's compression targets — is the most damning
  single data point in the post: even in the one metric where rtk's mechanism
  should show an effect, none was detected. The cost increase instead shows
  up in turns and cache reads, i.e., second-order effects of the compression
  changing agent behavior, not in the compression itself delivering savings.

### Claim 6: The cost penalty scaled with how much of the hook fired — heavily-rewritten task pairs cost ~24% more than baseline vs. ~5% for lightly-touched pairs — but this wasn't explained by task difficulty, and forensics found no single root cause beyond one broken rewrite and ordinary variance
- **Evidence**: Sub-analysis splitting task pairs by degree of hook exposure,
  plus a controlled check for task-difficulty confounding, plus manual
  transcript forensics on the extreme pairs.
- **Confidence**: settled (first-party sub-analysis with a named specific
  failure mode identified)
- **Quote**: "The more commands the hook rewrote, the larger the penalty. On
  the same corrected cost basis as the headline result, heavily exposed task
  pairs cost about 24% more than baseline, versus 5% for pairs the hook
  barely touched. Controlling for task difficulty did not reproduce this
  pattern, so harder tasks using more Bash does not appear to explain it.
  Transcript forensics found no single villain: one genuinely broken rewrite
  (compound find predicates turned into usage errors and retries), a few
  compression-induced re-reads, and a lot of ordinary variance on the extreme
  pairs. A thin, systematic tax rather than a dramatic failure."
- **Our assessment**: This rules out the more benign hypothesis that the cost
  increase is just measurement noise from a handful of difficult tasks. The
  dose-response relationship (more hook activity → more cost) is real, even
  though the authors could not pin it to one dominant mechanism — a mix of a
  genuine bug (compound `find` rewrites), induced re-reads, and variance.

### Claim 7: At high reasoning effort, the cost penalty disappears entirely — median delta +0.1% (p=0.99) — and rtk never produces a savings at any point in the study
- **Evidence**: Repeat of the full 86-task run at high reasoning effort, run
  specifically to address the anticipated critique that the low-effort result
  alone wasn't representative.
- **Confidence**: settled (disclosed statistical test, second independent
  full run)
- **Quote**: "Result: the cost penalty does not replicate there. Median
  paired delta +0.1% (p=0.99), turns +0.0 (p=0.74), quality still tied. At
  high effort, the model seems to waste fewer turns reacting to compressed
  output; though at k=1 all we can say is that the penalty didn't show up
  there, not that the two effort regimes probably differ. Either way, at no
  point did rtk save anything."
- **Our assessment**: The authors are appropriately cautious about
  over-interpreting the low-vs-high-effort difference (explicitly noting this
  is a single run per condition, not a replicated comparison of effort
  regimes) while still being unambiguous about the bottom line: across both
  tested conditions, rtk's net effect ranges from "costs more" to "costs the
  same" — never "costs less."

### Claim 8: Task quality was statistically indistinguishable between the rtk and baseline arms at both effort levels
- **Evidence**: Sign test over paired task outcomes at both low and high
  reasoning effort, on the full 86-task runs.
- **Confidence**: settled (disclosed statistical test with p-values)
- **Quote**: "On the full runs, task scores landed at 5 better / 4 worse / 71
  tie at low effort and 5 / 4 / 62 at high (sign test p=1.0 both); showing
  the arms are statistically indistinguishable on quality, with partial
  credit counted."
- **Our assessment**: This matters because it isolates the finding cleanly:
  rtk's cost increase is not a "you get what you pay for" quality tradeoff —
  quality is flat while cost rises. That makes the cost increase a pure
  inefficiency rather than a quality-for-cost exchange, which is a worse
  outcome for the tool than if it had at least traded cost for quality.

### Claim 9: rtk's own built-in analytics dramatically overstated its impact — reporting 96.2 million "tokens saved" (99.8% of everything touched) in the low-effort run even as the measured bill for the same trials went up — due to three specific accounting flaws in its self-reported metric
- **Evidence**: Comparison of rtk's own `rtk gain` self-reported savings
  dashboard against the paired measured billing data for the same trials,
  with three named mechanisms explaining the gap.
- **Confidence**: settled (first-party comparison of vendor tool's own
  self-reported metric against independently measured billing data)
- **Quote**: "Across the low-effort full run, rtk's built-in analytics (rtk
  gain) reported 96.2 million tokens saved — 99.8% of everything it touched;
  while the measured bill for the same trials went up. Three mechanisms make
  the scoreboard read high: First, rtk counts the full raw output as its
  counterfactual. One cat of a 1.2 MB CSV logged 320k tokens "saved", but
  Claude Code truncates any tool result long before 320k tokens; so the
  agent would have received a few thousand either way. The full run logged
  190 of such giant reads at an average of ~506k "saved" tokens each. Second,
  rtk estimates tokens as chars÷4 at the moment of execution, while most of a
  session's input cost is cached re-reads billed at a tenth of the price.
  Third, the hook simply never sees the majority of context. The scoreboard
  is grading its own homework."
- **Our assessment**: This is the mechanistic explanation for why a tool
  can honestly report huge savings while the bill goes up: its counterfactual
  (full uncompressed, uncached, untruncated output) is not what the agent
  would actually have paid for, because Claude Code's own truncation already
  caps pathological outputs, and because most repeated context is billed at
  cached rates (0.1× base) regardless of rtk's involvement. A tool's
  self-reported "tokens saved" dashboard measures against an inflated
  counterfactual, not against the actual bill.

### Claim 10: rtk's binary failed to start in one benchmark task's Docker image due to a glibc version incompatibility, causing the with-rtk arm to score zero at setup on that task in both full runs
- **Evidence**: A disclosed compatibility failure on one specific task
  (`dialogue-parser`), excluded from paired analysis but reported as a real
  finding rather than discarded as noise.
- **Confidence**: settled (first-party disclosed and specifically diagnosed
  failure)
- **Quote**: "on one task (dialogue-parser) rtk's own binary refused to start
  inside the task's image (it needs a newer glibc), so the with-rtk trial
  died at setup in both full runs while the plain arm scored 0.667. Paired
  analysis excludes that task from both arms, but it's a real compatibility
  failure, not Docker noise. Even scoring every errored trial as zero, the
  arms stay tied (sign test p=1.0)."
- **Our assessment**: A concrete, disclosed real-world deployment risk for
  teams considering rtk: a glibc-version dependency can silently fail the
  tool's binary in a constrained/minimal container image, with the practical
  effect of the agent losing the task entirely rather than merely losing the
  compression benefit. The authors' choice to report this rather than quietly
  exclude it is a marker of methodological transparency worth noting.

### Claim 11: The authors used a staged "run ladder" (transcript replay → 1-trial wiring check → 10-task k=1 smoke → 10-task k=3 → full 86-task runs) specifically because a k=1 pilot on Bash-heavy tasks produced a misleading +35% cost signal that evaporated into noise at k=3
- **Evidence**: The authors' own reported progression of run stages and the
  specific pilot-vs-repeated-sampling comparison.
- **Confidence**: settled (first-party reported methodology and result of
  their own staged testing process)
- **Quote**: "We ran the ladder the caveman eval taught us to run. The k=1
  smoke on ten deliberately Bash-heavy tasks (rtk's best case) showed the rtk
  arm a median +35% more expensive. Alarming, until you know that identical
  attempts of the same task in the same arm differ by a median 22% in cost
  anyway. At k=3 most of the scare evaporated into noise (Wilcoxon p≈0.65),
  exactly as a k=1 mirage should."
- **Our assessment**: This directly corroborates and extends Part 1's
  small-sample-pilot lesson (`blog-jetbrains-caveman-token-savings-test.md`
  Claim 6): here the pilot mirage ran in the *opposite* direction (a false
  alarm of harm, rather than a false signal of savings), showing the same
  methodological trap applies symmetrically — small-N agentic pilots can
  manufacture a misleadingly large effect in either direction, and the fix
  in both cases was to keep sampling (k=3, then full-N) rather than trust
  the first read.

### Claim 12: The generalizable lesson is that a tool's self-reported savings metric is a claim about its own counterfactual assumption, not a claim about the actual bill — evaluators should measure the paired bill directly rather than trusting the tool's internal "diff"
- **Evidence**: The authors' closing synthesis, generalizing beyond rtk
  specifically.
- **Confidence**: emerging (this is the authors' own interpretive conclusion,
  though directly supported by the disclosed Claim 9 mechanism)
- **Quote**: "The deeper lesson generalizes beyond rtk: a tool's
  self-reported savings are a claim about its counterfactual, not about your
  bill. rtk's scoreboard said 96 million tokens saved while the invoice went
  up. If you evaluate any context-compression tool, measure the paired bill,
  not the tool's diff."
- **Our assessment**: This is the most durable, transferable claim in the
  post for the guide's purposes — more durable than the specific 7.6%/3%
  figures, since it prescribes a concrete evaluation discipline applicable to
  any future token/cost-optimization tool: don't trust a vendor's or a tool's
  own internal savings dashboard; measure your actual paired bill.

## Concrete Artifacts

```
# Benchmark setup (from post's "Setup" section)
# Source: https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/

Harness:    Harbor 0.18 – Docker sandboxes, task verifiers, paired runs
Agent:      Claude Code 2.1.201, headless, bypassPermissions, pinned in both arms
Model:      claude-sonnet-5 – full run twice: at low and at high reasoning effort
Benchmark:  SkillsBench, 86 of 87 tasks, auto-graded 0-1 with partial credit
Arm A:      stock Claude Code
Arm B:      rtk v0.43.0 exactly as `rtk init -g` ships it: binary + PreToolUse hook + RTK.md
Volume:     4 paired runs (10-task smoke, same 10 at k=3, full 86 at low effort,
            full 86 at high effort) — 425 billed trials, ~USD 320
            (Harbor-recorded USD 317 plus reconstructed subagent spend)

# Results summary
Theoretical ceiling (transcript replay, pre-spend):  ~3% of input tokens
k=1 smoke (10 Bash-heavy tasks):                     +35% more expensive (did not replicate)
k=3 (same 10 tasks):                                 penalty dissolved into noise (Wilcoxon p~0.65)
Full 86 tasks, low effort:                           +7.6% cost (p=0.004), +13.8% turns (p=0.03),
                                                      +14.3% cache reads (p=0.008),
                                                      "new input" tokens +3.2% (p=0.23, not significant)
Full 86 tasks, high effort:                          +0.1% cost (p=0.99), +0.0 turns (p=0.74)
Quality (low effort):                                5 better / 4 worse / 71 tie (sign test p=1.0)
Quality (high effort):                               5 better / 4 worse / 62 tie (sign test p=1.0)
rtk's own self-reported savings (low-effort run):    96.2 million tokens "saved" (99.8% of touched)
Hook exposure (share of Bash calls rewritten):       33-50% depending on run
Compatibility failure:                               dialogue-parser task — rtk binary would not
                                                      start (needs newer glibc); scored 0 at setup
                                                      in both full runs vs. 0.667 for the plain arm
```

```
# Worked example of rtk's compression (captured by authors from a live test container)
# Source: https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/

# git status                              # rtk git status
On branch master                          * master
Changes not staged for commit:             M a.txt
(use "git add <file>..." to update...)    ?? b.txt
        modified:   a.txt
Untracked files:
(use "git add <file>..." to include...)
        b.txt
no changes added to commit ...

# python -m pytest  (19 lines)             # rtk pytest
...full pytest output...                  Pytest: 2 passed, 1 failed
                                           Failures:
                                           1. [FAIL] test_fail
                                              test_demo.py:3: in test_fail
                                              E  AssertionError: one is not two
```

```
# Methodology notes (from post's "Methodology notes" section)
# Source: https://blog.jetbrains.com/ai/2026/07/rtk-claude-code-token-savings/

Run ladder:        free transcript replay -> 1-trial wiring check -> 10 Bash-heavy
                    tasks at k=1 -> same 10 at k=3 -> full 86 at k=1, twice (low/high effort)
Paired analysis:   every number compares the same task across arms under the same job;
                    errored tasks excluded from both arms
Statistical tests: quality = exact sign test over non-ties; token/cost deltas =
                    per-task medians + Wilcoxon signed-rank (arm totals are
                    outlier-dominated by long-context pricing-tier crossings)
Pre-registration:  primary endpoints (per-task paired delta in cost and in "new
                    input" tokens) and the adoption-stratified split were decided
                    before any paid run
Adoption tracking:  every with-rtk trial persists rtk's own hook audit log + history.db,
                    to distinguish "rtk saved nothing" from "rtk never ran"
Provenance:        rtk v0.43.0 release binary (sha256-pinned), Claude Code 2.1.201
                    pinned in both arms, claude-sonnet-5, Harbor 0.18, SkillsBench
                    with bike-rebalance excluded (allow_internet=false crashes local Docker)
```

## Cross-References

- **Corroborates**:
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 1 (8.5% measured vs.
    65% claimed savings for the Caveman skill): rtk pushes the same
    "vendor-claimed savings collapse under paired A/B measurement" pattern
    even further — where Caveman still showed *some* real savings, rtk shows
    none at all (a cost increase or a wash). Two independent tools tested by
    the same team with the same methodology now support the same general
    skepticism-of-headline-claims pattern.
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 6 (a 10-task pilot
    showed a misleading -30% savings that dissolved at the full 82-task run):
    this source's Claim 11 reports the same pilot-instability trap firing in
    the opposite direction — a misleading +35% *cost increase* signal at k=1
    that evaporated at k=3. Together the two notes show the small-sample
    trap is symmetric (can manufacture false alarms of harm, not just false
    signals of benefit), reinforcing that k=1 agentic benchmark results
    should never be trusted regardless of which direction they point.
  - `docs-ghaw-effective-tokens-specification.md` Claim 3 (cached input is
    weighted 0.1× vs. 1.0× for regular input, output/reasoning at 4.0×): this
    source's Claim 9 mechanism #2 ("most of a session's input cost is cached
    re-reads billed at a tenth of the price") is an empirical instance of
    exactly the 0.1× cache weighting the ET spec formalizes as a normative
    default. This corroboration also explains part of *why* rtk's raw
    chars÷4 self-reported savings estimate diverges so far from the actual
    bill — it is not applying any cache discount at all.
  - `blog-bswen-mcp-token-cost.md` Claim 8 ("Cache read costs 0.1x compared
    to base input"): same 0.1× cache-pricing corroboration as the ET spec,
    from an independent practitioner source — both are consistent with this
    source's stated cache-pricing mechanism.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about rtk specifically or about Bash-hook-based compression tools that this
  source's findings dispute. No contradiction issue filed.

- **Extends**:
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 3 (Caveman's savings
    are capped by the narration share of output tokens, since it leaves
    code/diffs/tool calls untouched): this source's Claim 3 identifies the
    analogous but architecturally distinct ceiling for a Bash-hook-based tool
    — capped not by *content type* (narration vs. code) but by *tool surface*
    (Bash calls vs. Read/Grep calls). Together the two notes establish a
    general pattern: every token-compression technique tested so far has a
    hard architectural ceiling determined by what the technique's
    interception point can and cannot see, and that ceiling — not the
    vendor's demo — determines the realistic savings.
  - `blog-jetbrains-caveman-token-savings-test.md` Claim 8 (realistic
    savings ceiling for prompt-compression skills tops out in the "high
    single digits"; recommendation to treat Caveman as low-risk/optional):
    this source shows a second data point where even that modest ceiling
    does not hold — rtk's realistic ceiling (Claim 4, ≈3% of input tokens)
    was smaller still, and the measured result went negative rather than
    merely underwhelming. This suggests the "high single digits" framing
    from Part 1 should not be read as a floor that compression tools
    generally clear; some tools underperform even a single-digit-percent
    ceiling.

- **Novel**:
  - The pre-spend transcript-replay methodology (Claim 4) that computes a
    theoretical savings ceiling *before* running any paid trials, and
    validates that cheap estimate against the eventual paid result. No prior
    corpus note documents this cost-avoidance benchmarking technique.
  - The specific three-mechanism breakdown of why a tool's self-reported
    "tokens saved" metric can overstate reality by two orders of magnitude
    (counting truncation-exempt raw output, ignoring cache pricing, and
    having no visibility into non-Bash context) — Claim 9 is the first
    corpus source to dissect a vendor tool's own internal savings dashboard
    against independently measured billing data.
  - The finding that a token-compression tool can produce a *net cost
    increase* (not just underwhelming savings) via second-order effects
    (more turns, more cache reads) even while the specific token class it
    targets shows no significant change (Claim 5) — this is a qualitatively
    different (and worse) outcome than anything documented in Part 1.
  - The disclosed binary-compatibility failure mode (Claim 10, glibc
    incompatibility) as a concrete deployment risk for shell-hook-based
    tooling in containerized agent environments.

## Guide Impact

- **Chapter 02 (Foundations — LLM Cost Measurement) / Chapter 03 (Cost and
  Efficiency)**: Add Claim 12 ("measure the paired bill, not the tool's diff")
  as a concrete evaluation discipline for any token/cost-optimization tool a
  team is considering adopting: do not trust the tool's own self-reported
  savings metric (Claim 9 shows exactly how such a metric can be honestly
  computed yet wildly overstate reality). Pair with Claim 4's pre-spend
  transcript-replay technique as a cheap way to sanity-check a vendor's
  savings claim before running any paid A/B trial.

- **Chapter 02/Chapter 04 (Tool choice and context cost)**: Add Claim 3 (Bash
  hooks cannot see Read/Grep-tool traffic) as a generalizable caveat for
  evaluating any shell-output-compression skill or hook: ask what fraction of
  a typical session's tokens flow through tools the hook cannot intercept.
  This extends the existing `blog-jetbrains-caveman-token-savings-test.md`
  Claim 3 guidance (which covers narration-only prompt compression) to the
  separate category of Bash-output compression, so Ch04's token-compression
  guidance should cover both "what content type does this technique touch"
  and "what tool surface does this technique's interception point cover."

- **Chapter 04 (Benchmarking methodology)**: Add Claim 11 (the k=1 → k=3 →
  full-N run ladder, and the finding that k=1 pilots can manufacture false
  alarms in either direction) as a second, symmetric data point supporting
  the existing small-sample-pilot caution already recommended from Part 1.
  Recommend the specific run-ladder structure (transcript replay, wiring
  check, k=1 smoke, k=3, full-N) as a reusable methodology for any team
  running their own agent-behavior-change A/B test.

## Extraction Notes

- The source was retrieved two ways: an initial WebFetch pass (which returned
  a competent but non-verbatim summary), followed by a direct `curl` fetch of
  the raw HTML and a script-based HTML-tag strip to recover the article's
  exact text. All quotes in this note were copied from that raw-HTML
  extraction and spot-verified against the underlying HTML source (grepping
  for each quoted passage in the raw markup) to confirm character-for-character
  accuracy, including punctuation and em-dashes, before inclusion.
- The post is a self-contained single-page benchmark write-up; the only
  substantive linked page is Part 1 (the Caveman test), which is already a
  separate source note in this corpus (`blog-jetbrains-caveman-token-savings-test.md`)
  and was read in full for cross-referencing rather than re-extracted here.
  The rtk GitHub repo itself (linked in the post) was not fetched — this note
  extracts only what the blog post itself states about rtk, not independent
  verification of rtk's README or source code.
- No paywall or access issues; the full article was readable.
- No contradiction issue was filed. This source corroborates and extends the
  existing corpus pattern (vendor token-savings claims collapse under paired
  measurement) rather than opposing any existing claim.
