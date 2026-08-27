---
source_url: https://claude.com/blog/claude-in-chrome-generally-available
source_type: blog-post
title: "Claude in Chrome is generally available"
author: Anthropic (Claude.com blog)
date_published: 2026-08-26
date_extracted: 2026-08-27
last_checked: 2026-08-27
status: current
confidence_overall: emerging
issue: "#2993"
---

# Claude in Chrome is generally available

> Anthropic's GA announcement for Claude in Chrome — available on every paid
> plan, with autonomous (no per-step approval) browser actions gated by a new
> action-verification safety classifier, plus updated red-team attack-success
> metrics across Opus 4.5, Sonnet 5, Opus 5, Mythos 5, and Fable 5 that show
> 0% (0.3% for Fable 5) attack success with the full defense stack, down from
> 17.6% (Opus 4.5) and 3.8% (Opus 5) with no safeguards.

## Source Context

- **Type**: blog-post (first-party Anthropic product announcement, claude.com,
  August 26, 2026)
- **Author credibility**: Unbylined first-party Anthropic post on the official
  product blog. Authoritative on stated plan availability, shipped safety
  architecture, and Anthropic's own internal evaluation results. As vendor
  communication and self-reported red-team data (methodology described only
  at a high level: "our internal automated attackers, external red-teamers,
  and real-world monitoring"), the attack-success percentages should be read
  as Anthropic's own measurement, not independently reproduced.
- **Scope**: Covers general availability of Claude in Chrome on every paid
  plan, the shift to autonomous (non-per-step-approved) browser actions, the
  three-layer defense-in-depth description (training, probes, action
  verification), and a detailed prompt-injection attack-success-rate
  comparison across five model versions (Opus 4.5, Sonnet 5, Opus 5, Mythos 5,
  Fable 5) with and without safeguards. Does NOT cover pricing, the
  cross-surface Cowork session-continuity feature (covered in the Aug 12
  companion post), admin domain-restriction UI details beyond a single
  sentence, or independent/third-party red-team verification of the reported
  percentages.

## Extracted Claims

### Claim 1: Claude in Chrome is now generally available on every paid Claude plan, and Claude can take browser actions autonomously instead of requiring approval for each one

- **Evidence**: Opening two sentences of the post, stated as the headline
  product change from the prior (Aug 12) partial rollout.
- **Confidence**: settled (first-party statement of shipped availability as of
  publication date)
- **Quote**: "Claude in Chrome is now generally available on every paid Claude plan. Claude can now also take actions autonomously in the browser, instead of needing approval for every one."
- **Our assessment**: This supersedes the tiered rollout documented in
  `blog-anthropic-cowork-chrome-side-panel.md` Claim 10 (Max/Team available
  Aug 12, Pro "rolling out over the coming weeks") — as of Aug 26, availability
  is universal across paid plans, not tiered. It also marks a default-behavior
  change: the Aug 12 post described "automatically approve" as an opt-in mode
  a user could switch to (per that note's Concrete Artifacts, Layer 2); this
  post frames autonomous action as the new default experience, gated by a
  new classifier rather than by the user's permission-mode choice alone.

### Claim 2: A safety classifier validates each browser action before it executes, checking that the action is safe and matches the user's request

- **Evidence**: Third sentence of the post's opening paragraph, stated as the
  mechanism that makes autonomous action safe to ship.
- **Confidence**: settled (first-party statement of a shipped safety
  mechanism, later elaborated in the "Actions are verified before they run"
  section)
- **Quote**: "A safety classifier validates each action before it's performed to ensure it's safe and matches your request."
- **Our assessment**: This is the headline safety claim justifying autonomous
  action. It corroborates and appears to be the production form of the
  "pre-action consistency check" already documented in
  `blog-anthropic-cowork-chrome-side-panel.md` Claim 4 (a check that "reviews
  the action against what you originally asked for and blocks anything that
  doesn't match"). This post adds the detail that the same mechanism is
  described as "the same mechanism as auto mode in Claude Code" (see Claim 4
  below) — a detail absent from the Aug 12 post.

### Claim 3: Three layers of defense underlie Claude in Chrome's prompt-injection resistance — model training against a growing attack library, probes that screen tool-result content before Claude acts on it, and action verification before consequential actions run

- **Evidence**: Three named, bolded sub-sections in the "Safeguarding against
  prompt injection" portion of the post, each with its own mechanism
  description.
- **Confidence**: settled (first-party description of shipped defense-in-depth
  architecture, structured explicitly as three distinct layers)
- **Quote**: "Claude recognizes more attacks. ... Probes screen web content before Claude acts on it. ... Actions are verified before they run."
- **Our assessment**: This is a cleaner, more explicit three-layer framing than
  the six-layer breakdown inferred in `blog-anthropic-cowork-chrome-side-panel.md`
  Concrete Artifacts (which combined training, probes, permission mode, the
  consistency check, hard-coded approval gates, and admin controls into one
  list). This post's own structure maps onto that prior breakdown as: Layer 1
  (training) = prior Layer 1; probes = a distinct, newly-detailed mechanism
  not named as such in the Aug 12 post, first deployed "with Claude Opus 4.5"
  per this post; action verification = prior Layer 2/3 (automatic approval +
  consistency check), now merged into one classifier per Claim 2.

### Claim 4: Claude in Chrome's automatic action-approval now uses the same underlying mechanism as "auto mode" in Claude Code, and users can switch back to manual per-action approval in settings

- **Evidence**: Direct statement in the "Actions are verified before they run"
  section, naming the shared mechanism with a separate Claude product.
- **Confidence**: settled (first-party statement naming a specific
  cross-product mechanism)
- **Quote**: "In Claude in Chrome, Claude will now automatically approve actions it determines to be safe, using the same mechanism as auto mode in Claude Code. (You can switch this off in your settings if you'd prefer to continue to approve Claude's actions manually.)"
- **Our assessment**: This is a novel detail not present in the Aug 12 post or
  any other note in the corpus — it explicitly ties the Chrome
  action-verification classifier to the same underlying safety mechanism used
  for autonomous coding-agent actions in Claude Code's "auto mode." For a
  guide chapter comparing autonomy/approval models across Claude surfaces,
  this is evidence that Anthropic is standardizing one action-verification
  mechanism across products rather than building bespoke gates per surface.
  Manual per-step approval remains available as an opt-out, consistent with
  the Aug 12 post's framing (that note's Layer 2).

### Claim 5: Probes that screen tool-result content for prompt injection were first deployed with Claude Opus 4.5, and their attack-type coverage has expanded since

- **Evidence**: Direct statement in the "Probes screen web content" paragraph,
  giving a specific model-version deployment milestone.
- **Confidence**: settled (first-party statement of a named deployment
  milestone) — though the specific coverage expansion is not quantified
- **Quote**: "We first deployed these probes with Claude Opus 4.5, and have since expanded the types of attacks they cover."
- **Our assessment**: This dates the probe mechanism precisely (tied to the
  Opus 4.5 release) and is new specificity beyond the Aug 12 post, which
  described injection scanning generically without a deployment milestone.
  Useful for a guide timeline of Claude's browser-agent safety evolution.

### Claim 6: On the original (now-retired) evaluation harness, no prompt-injection attack succeeded against Claude Fable 5, Opus 5, or Sonnet 5, even without probes or the safety classifier — so Anthropic retired that evaluation as saturated and moved to a harder one sourced from professional red-teamers

- **Evidence**: Direct statement plus explicit methodology rationale for
  retiring and replacing the evaluation.
- **Confidence**: settled (first-party description of an internal evaluation
  and the reason for changing it) — the underlying 0% result should be read
  with the caveat that Anthropic itself judged it saturated/uninformative
- **Quote**: "On our initial evaluation testing Claude Cowork's resilience against prompt injection attacks (first developed when we released the Claude in Chrome pilot), no attack succeeded against Claude Fable 5, Claude Opus 5, or Claude Sonnet 5 in the Cowork harness, even without the probes and classifiers discussed above."
- **Our assessment**: This is methodologically important context that a guide
  citing "0% attack success" figures must carry: Anthropic explicitly
  discloses that this particular evaluation was retired for being too easy
  ("saturated") before reporting the newer, harder numbers in Claim 7. A
  reader who only sees "0% success, no safeguards needed" without this
  caveat would be misled about how meaningful that figure is.

### Claim 7: On Anthropic's current (harder, red-team-sourced) evaluation, prompt-injection attacks succeeded against Opus 4.5 17.6% of the time and against Opus 5 3.8% of the time with no additional safeguards; with probes and the safety classifier, 0% of attacks succeeded against Sonnet 5, Opus 5, and Mythos 5, and 0.3% succeeded against Fable 5

- **Evidence**: Explicit percentage figures given per model, per safeguard
  configuration, described as sourced from "stronger attacks sourced by
  professional red-teamers."
- **Confidence**: emerging (specific, quantified first-party red-team results,
  but self-reported, self-graded — "we moved to a more capable grading
  pipeline combined with manual review of successful attacks" — with no
  independent/third-party reproduction, and Anthropic controls both the
  attack corpus and the grading methodology)
- **Quote**: "attacks that reached the model succeeded against Opus 4.5 17.6% of the time and against Opus 5 3.8% of the time, before any additional safeguards... Against every model from Opus 4.8 onwards, when running with probes and the safety classifier, no attacks succeeded against Claude Sonnet 5, Claude Opus 5, or Claude Mythos 5. We saw a 0.3% attack success rate against Fable 5."
- **Our assessment**: This is the single most citable, specific security
  metric in the post and a substantial upgrade in specificity over the Aug 12
  post's single aggregate figure (see Cross-References → Extends below). It
  shows a clear generational safety improvement trend (Opus 4.5 → Opus 5:
  17.6% → 3.8% with no safeguards) and demonstrates that the safeguard stack
  (probes + classifier) closes the remaining gap to 0% for three of four
  current-generation models, with Fable 5 as the one model that still shows
  measurable (0.3%) residual risk. Anthropic's own footnote (Concrete
  Artifacts) clarifies "attacks that reached the model" excludes cases where
  Claude's own behavior prevented the malicious instruction from ever being
  seen — so the reported percentages are conditional on exposure, not on
  attempted-attack volume.

### Claim 8: With the strongest safeguards available in November 2025 (an earlier probe-only configuration), attacks against Opus 4.5 still succeeded 16.7% of the time — showing the November 2025 defenses were only marginally better than no safeguards at all against the newer, harder attack set

- **Evidence**: Direct comparison sentence contrasting old-safeguard
  performance against the new evaluation's harder attacks.
- **Confidence**: emerging (self-reported comparison against a retrospectively
  re-run older configuration)
- **Quote**: "With the strongest safeguards available in November 2025, attacks against Opus 4.5 running with probes succeeded 16.7% of the time."
- **Our assessment**: This is a striking admission: against the harder,
  current attack set, the November 2025 defenses (probes only, no action
  classifier) barely reduced Opus 4.5's attack-success rate (17.6% unsafeguarded
  → 16.7% with probes) — a ~1 percentage point improvement. The dramatic drop
  to 0%–0.3% only appears with the newer safety classifier added on top of
  probes (per Claim 7), for current-generation models. This substantially
  qualifies any guide claim that "probes alone meaningfully reduce prompt
  injection risk" — on this evidence, probes alone were a weak layer against
  sophisticated attacks, and the action-verification classifier is doing most
  of the risk reduction.

### Claim 9: Opus 4.5 had the highest percentage of successful attacks among tested models despite fewer attacks reaching the model in the first place, due to differences in model behavior

- **Evidence**: Direct explanatory sentence following the headline result
  numbers, offered as Anthropic's own interpretation of why Opus 4.5 scores
  worse despite a lower attack-exposure rate.
- **Confidence**: anecdotal (a qualitative interpretive claim — "model
  behavior resulted in a lower number of attacks reaching the model" — with
  no supporting mechanism or data given for what that behavioral difference is)
- **Quote**: "Opus 4.5's model behavior resulted in a lower number of attacks reaching the model, but it still had the highest percentage of successful attacks."
- **Our assessment**: Interesting but underspecified — Anthropic asserts a
  behavioral difference in Opus 4.5 without explaining what it is (e.g.,
  does Opus 4.5 avoid opening/reading certain suspicious content more often,
  reducing exposure, while being more susceptible once exposed?). Worth
  flagging in the guide as an open question rather than a settled mechanism.

### Claim 10: All prompt-injection "successful breaks" observed in this evaluation round were manually verified by Anthropic to be low-severity scenarios, and Anthropic is working to mitigate them

- **Evidence**: Direct statement following the percentage results.
- **Confidence**: emerging (self-reported severity classification; no
  definition of "low-severity" given, no examples provided)
- **Quote**: "We have manually verified that all successful breaks are in low-severity scenarios and are working to mitigate them."
- **Our assessment**: This softens the residual risk (0.3% for Fable 5, plus
  whatever fraction of the 16.7%/17.6%/3.8% figures represent scenarios not
  covered by the final safeguard stack) but the claim is unfalsifiable as
  stated — "low-severity" is undefined and no example breaks are described.
  A guide citing this figure should note the severity claim is asserted, not
  demonstrated.

### Claim 11: Not all prompt-injection attacks in the evaluation corpus actually reach the model — Claude's own actions sometimes prevent it from ever encountering the malicious instructions

- **Evidence**: A footnote attached to the results, clarifying what "attacks
  that reached the model" means in the percentage denominators of Claim 7.
- **Confidence**: settled (first-party methodological clarification)
- **Quote**: "Not all attacks reach—i.e., are seen by—the model. In some cases, the actions Claude takes result in it never encountering the malicious instructions."
- **Our assessment**: This is an important denominator caveat for anyone
  citing the Claim 7 percentages: they are conditioned on exposure, not
  computed over the full attack corpus. A guide summarizing "0% attack
  success for Sonnet 5 and Opus 5" should note this is 0% of attacks that
  reached the model, not 0% of all attempted attacks — a materially different
  (and more favorable to Anthropic) statistic.

## Concrete Artifacts

```
Claude in Chrome — attack-success-rate results (blog.claude.com,
"Claude in Chrome is generally available," Aug 26, 2026)

Retired evaluation (Cowork harness, original attack set):
  Fable 5, Opus 5, Sonnet 5 — 0% attack success, even with NO probes/classifier
  → judged saturated, retired

Current evaluation (harder attacks, sourced by professional red-teamers):
  No additional safeguards:
    Opus 4.5 ....... 17.6% attack success
    Opus 5 .......... 3.8% attack success
  With probes only (Nov 2025 configuration, re-run against current attacks):
    Opus 4.5 ........ 16.7% attack success
  With probes + safety classifier (current, Opus 4.8 and later):
    Sonnet 5 ......... 0% attack success
    Opus 5 ........... 0% attack success
    Mythos 5 ......... 0% attack success
    Fable 5 .......... 0.3% attack success

Footnote: "Not all attacks reach—i.e., are seen by—the model. In some
cases, the actions Claude takes result in it never encountering the
malicious instructions."

All successful breaks manually verified by Anthropic as "low-severity
scenarios," per the post; mitigation described as ongoing, not complete.
```

```
Claude in Chrome — three-layer defense description (same source)

1. Training: "We train Claude against a growing library of prompt
   injection attacks, sourced from our internal automated attackers,
   external red-teamers, and real-world monitoring." New successful
   attacks are added to the training library for future models.

2. Probes: scan tool-result content (page/email text returned to
   the model) for likely injection; on detection, "Claude is warned
   to treat the content with suspicion and, if needed, to check with
   you before taking an action." First deployed with Opus 4.5;
   coverage since expanded.

3. Action verification: a classifier reviews proposed actions (e.g.
   navigating to a new site, entering text) against the user's
   original request before the action executes; non-matching actions
   are blocked. Uses "the same mechanism as auto mode in Claude Code."
   Manual per-step approval remains available as an opt-out in settings.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-chrome-side-panel.md` Claim 4 (a "pre-action
    consistency check" that blocks actions not matching the user's original
    request, layered on the permission-mode toggle): this post's Claim 2 and
    Claim 4 describe the production/GA form of that same mechanism, now named
    a "safety classifier" and tied explicitly to Claude Code's "auto mode."
  - `blog-anthropic-cowork-chrome-side-panel.md` Claim 6 (Anthropic frames
    prompt injection defense as an ongoing arms race, not a solved problem):
    corroborated directly by this post's closing section, "Prompt injection
    remains a moving target... we also need to ensure our safeguards stay
    ahead of the evolving methods of attackers."
  - `blog-anthropic-dispatch-computer-use.md` Claim 3 (three-safeguard safety
    model for computer use generally: consent gating, activation-level
    injection scanning, app denylist): this post's three-layer framing
    (training, probes, action verification) is the Chrome-specific,
    more-detailed successor description of the same defense-in-depth
    philosophy, six months later.
  - `blog-anthropic-computer-use-best-practices.md` Claim 7 (the official
    `computer_20251124` tool type provides automatic classifier protection;
    "classifiers are one layer of defense, not a complete solution"): this
    post's own framing — three distinct layers, with the classifier as only
    the last of them — is consistent with that "one layer, not a complete
    solution" caveat.

- **Contradicts**: None filed. The <0.08% aggregate attack-success figure in
  `blog-anthropic-cowork-chrome-side-panel.md` Claim 8 (from the linked Aug 12
  safety guide) and this post's 0%–0.3% per-model figures (Claim 7) are not
  presented as measuring the same thing: the Aug 12 figure is a single
  aggregate number "against internal testing combining known effective
  techniques," while this post explicitly describes replacing the prior,
  saturated evaluation with a harder, red-team-sourced one and reports
  per-model breakdowns. Anthropic discloses the methodology change itself
  (Claim 6), so this reads as evaluation evolution rather than a competing
  claim — not a contradiction under MINER.md §4a's bar ("materially opposes
  ... on the same topic" and "would lead to different guide advice"). Both
  figures point the same direction (very low measured attack success with
  full safeguards) and neither claims the other is wrong.

- **Extends**:
  - `blog-anthropic-cowork-chrome-side-panel.md` Claim 8 (single aggregate
    <0.08% figure): this post supersedes it with a per-model, per-safeguard
    breakdown (Claim 7) that is far more specific and should be preferred in
    the guide going forward — it shows the safeguard stack does NOT reduce
    all models equally (Fable 5 retains 0.3% vs 0% for the other three) and
    that probes alone were nearly ineffective against the current attack set
    (Claim 8: 17.6% → 16.7%).
  - `blog-anthropic-cowork-chrome-side-panel.md` Claim 10 (tiered plan
    availability: Max/Team now, Pro rolling out): this post's Claim 1
    (available on every paid plan) is the completion of that rollout.
  - `blog-anthropic-computer-use-best-practices.md` Claim 7 (official tool
    type ships classifier protection): this post names the Chrome-specific
    classifier and, new to the corpus, ties it explicitly to Claude Code's
    "auto mode" (Claim 4) — evidence of a shared action-verification
    mechanism across at least two Claude products.

- **Novel** (not in prior corpus):
  - The specific per-model attack-success percentages (Claim 7): 17.6%
    (Opus 4.5, unsafeguarded), 3.8% (Opus 5, unsafeguarded), 16.7% (Opus 4.5,
    probes only), 0% (Sonnet 5 / Opus 5 / Mythos 5, full stack), 0.3%
    (Fable 5, full stack). No prior source note has model-by-model
    prompt-injection metrics for Claude's browser agent.
  - The disclosure that an earlier evaluation was retired for being
    saturated (Claim 6), and that the Nov 2025 probe-only defenses were
    nearly ineffective (16.7%) against the newer, harder attack set (Claim 8)
    — a rare first-party admission that a previously-touted safeguard
    generation underperformed against stronger attacks.
  - The explicit statement that Chrome's action-verification classifier uses
    "the same mechanism as auto mode in Claude Code" (Claim 4) — new evidence
    of a shared safety mechanism across Claude Code and Claude in Chrome.
  - The exposure-conditioning footnote (Claim 11) — a methodological
    disclosure not present in any prior computer-use/Cowork source note.

## Guide Impact

- **Chapter on browser automation / agentic browser risk (risk management)**:
  Replace or supplement any citation of the Aug 12 post's <0.08% aggregate
  figure with this post's per-model breakdown (Claim 7, Concrete Artifacts).
  Explicitly carry three caveats when citing it: (1) percentages are
  conditional on the attack reaching the model at all (Claim 11); (2)
  "low-severity" breaks are asserted, not defined or exemplified (Claim 10);
  (3) probes alone were nearly ineffective against the current attack set —
  17.6% → 16.7% for Opus 4.5 (Claim 8) — so guide language should attribute
  the safety improvement specifically to the action-verification classifier
  layer, not to probes generally.

- **Chapter on tool/plan selection (Ch07 per Prospector triage)**: Update the
  plan-availability note from `blog-anthropic-cowork-chrome-side-panel.md`
  (Max/Team now, Pro rolling out as of Aug 12) — as of Aug 26, Claude in
  Chrome is available on every paid plan (Claim 1). No more tiered-rollout
  caveat is needed for plan availability, though the "Chrome only, no other
  Chromium browsers, no mobile" platform limitation from the Aug 12 note is
  unchanged (this post repeats it verbatim in "Getting Started").

- **Chapter on agent autonomy / approval models (Ch04 per Prospector triage)**:
  Add Claim 4 — Chrome's autonomous-action default now uses the same
  verification mechanism as Claude Code's "auto mode." For a guide section
  comparing autonomy levels across Claude surfaces, this is evidence Anthropic
  is standardizing one action-verification primitive across products rather
  than building bespoke per-surface gates, worth naming explicitly rather than
  treating Chrome and Claude Code autonomy as unrelated design decisions.

## Extraction Notes

- Read the full post via WebFetch first, then re-fetched and parsed the raw
  HTML directly with `curl` + a Python tag-stripping pass to obtain the
  unmodified page text, because WebFetch's AI-summarized output restructured
  the attack-rate paragraph into a bulleted table not present in the source's
  actual prose. All quotes in this note were verified against the raw
  HTML-derived text (including correcting curly-quote characters to plain
  ASCII quotes), not the WebFetch summary. The raw-text extraction is saved
  at the time of writing; the summary/table framing in Claim 7-adjacent
  Concrete Artifacts is my own structuring of the source's prose numbers, not
  a quoted table from the source.
- The post includes an inline chart with a caption describing methodology
  changes (grader model swap, extended-thinking normalization across models)
  between the November 2025 and current evaluations; this is summarized in
  Claim 7/8's "Our assessment" but not separately quoted since it is chart-
  caption prose describing methodology rather than a standalone claim.
- Followed the "Getting Started" and footnote text but did not follow the
  Chrome Web Store listing link or the admin setup guide link (product/install
  pages without additional claims relevant to this note's scope), consistent
  with the same decision made in `blog-anthropic-cowork-chrome-side-panel.md`.
  Did not follow the linked November 2025 blog post or the Aug 12 "Claude
  gets its own browser in Cowork" related post, since companion Aug 12
  coverage already exists in the corpus as
  `blog-anthropic-cowork-chrome-side-panel.md` and this note cross-references
  it directly rather than re-extracting overlapping claims.
- Checked `source-notes/` for existing Chrome/Cowork/computer-use/prompt-
  injection coverage before writing (directory listing filtered for those
  terms) and reviewed `CONTRADICTIONS.md` (grepped for "Claude in Chrome",
  "Cowork", "browser" — no existing entries). No contradiction meeting
  MINER.md §4a's bar was found; the evaluation-methodology difference between
  this post and the Aug 12 post's aggregate figure is addressed under
  Cross-References → Contradicts above and judged not to qualify, since
  Anthropic discloses the methodology change itself and both figures point
  the same direction.
- Confidence calibration: **emerging** overall. Claims about what shipped and
  is available (Claim 1, plan availability) and the qualitative defense
  architecture (Claim 3) are settled first-party product facts. But the
  headline evidence — the attack-success percentages (Claims 6-9) — are
  self-reported, self-graded internal red-team results with no independent
  verification, which is why this note (like the Aug 12 note it extends)
  is graded emerging rather than settled.
