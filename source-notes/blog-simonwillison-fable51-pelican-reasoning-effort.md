---
source_url: https://simonwillison.net/2026/Sep/1/claude-fable-5-1/
source_type: blog-post
title: "Claude Fable 5.1 made me a really nice animated pelican"
author: Simon Willison
date_published: 2026-09-01
date_extracted: 2026-09-06
last_checked: 2026-09-06
status: current
confidence_overall: emerging
issue: "#3267"
---

# Claude Fable 5.1 made me a really nice animated pelican

> Simon Willison re-runs his "pelican riding a bicycle" SVG benchmark against
> all five of Claude Fable 5.1's reasoning effort levels (low, medium, high,
> xhigh, max), finding that low and medium skip reasoning entirely for this
> prompt, high adds only a token summary of planning, and xhigh/max trigger a
> dramatic, non-linear jump in tokens, latency, and cost ($0.10 → $0.13 →
> $1.83 → $3.30) while producing visibly more deliberate design choices in
> the reasoning trace.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, 1 September 2026 — a short,
  ~880-word hands-on post built around one running benchmark, with embedded
  SVG/reasoning-transcript links and a follow-up animation experiment
  prompted by a Hacker News comment)
- **Author credibility**: Simon Willison is the creator of Django, Datasette,
  and the `llm` Python CLI, and a trusted-feed source in this corpus with
  multiple prior first-day model evaluations (`blog-simonwillison-claude-fable-5.md`,
  `blog-simonwillison-kimi-k3-pelican-benchmark.md`). All token/cost/latency
  figures in this post are from his own API calls via `llm-anthropic`, not
  vendor-supplied. He explicitly fixed a bug in `llm-anthropic` (his own
  plugin) that had been preventing reasoning traces from being recorded
  correctly, before running the tests in this post — a methodological detail
  that increases confidence the reasoning-trace absence at low/medium is a
  real model behavior and not a logging artifact. No vendor affiliation with
  Anthropic.
- **Scope**: Covers Claude Fable 5.1's five reasoning effort levels tested
  against a single fixed prompt ("Generate an SVG of a pelican riding a
  bicycle"), with token counts, wall-clock time, and dollar cost for each
  level, excerpts from the model's own reasoning transcripts, Anthropic's
  self-reported Terminal-Bench-Science 0.1 score, and a follow-up animation
  request run at `high` effort. Does NOT cover: any prompt other than the
  pelican SVG and its animation follow-up; formal benchmark reproduction;
  coding-agent or long-horizon agentic tool-use behavior; enterprise
  deployment; or system-prompt/safety changes in Fable 5.1.

## Extracted Claims

### Claim 1: Fable 5.1 exposes five reasoning effort levels — low, medium, high, xhigh, max — with no way to disable reasoning entirely

- **Evidence**: Willison's direct statement after testing all five levels.
- **Confidence**: settled (first-hand observation of the model's exposed
  configuration surface)
- **Quote**: "Fable 5.1 has five reasoning levels: low, medium, high, xhigh, max—and no option to turn off reasoning entirely."
- **Our assessment**: The "no option to turn off reasoning" detail is
  operationally significant — unlike models that offer a true zero-reasoning
  mode, every Fable 5.1 request pays at least the `low`-tier reasoning
  overhead. This matches the pattern in `docs-github-copilot-1m-context-reasoning-levels.md`
  Claim 2, where configurable reasoning levels are framed as a dial rather
  than an on/off switch, but this source is the first in the corpus to name
  Claude's specific five-level naming scheme (low/medium/high/xhigh/max).

### Claim 2: For the pelican SVG prompt, low and medium effort produced no visible reasoning tokens at all, and used almost identical output token counts (1,998 vs. 1,977) despite the different effort setting

- **Evidence**: Willison's side-by-side comparison of the `low` and `medium`
  transcripts, both of which showed no summarized reasoning text.
- **Confidence**: settled (specific first-person measurement, cross-checked
  against two separate transcripts)
- **Quote**: "The transcript doesn't show any summarized reasoning tokens, and the output token count is 1,998. With Claude that output token count includes reasoning tokens. It took 23.8 seconds and cost 10.017 cents."
- **Quote (medium)**: "Weirdly, that one also shows no reasoning text  and used 1,977 output tokens—21 tokens less than low. It took 23 seconds and cost 9.912 cents."
- **Quote (conclusion)**: "So for this particular prompt (\"Generate an SVG of a pelican riding a bicycle\") Fable 5.1 appeared to skip reasoning entirely at both low and medium settings."
- **Our assessment**: This is a concrete, falsifiable finding that the
  low→medium step buys nothing for at least some prompts — medium is not
  simply "a bit more reasoning than low," it can be functionally identical.
  Willison flags the 21-token *decrease* from low to medium as "weirdly"
  non-monotonic, echoing the non-monotonic effort/output relationship
  already documented for Fable 5 in `blog-simonwillison-claude-fable-5.md`
  Claim 11 (that note's `high` tier produced fewer tokens than `medium`).
  Practitioners should not assume effort level and output verbosity/quality
  scale monotonically without testing their own prompt.

### Claim 3: High effort added a short visible reasoning summary but was still close in cost/tokens to low and medium

- **Evidence**: Willison's transcript excerpt and cost figure for the `high`
  setting.
- **Confidence**: settled (first-person measurement)
- **Quote**: "Here's high—29.6 seconds, 2,612 output tokens, 13.087 cents:"
- **Quote (reasoning summary)**: "I'm planning the SVG layout for a pelican riding a bicycle, with a sky and ground background, a bicycle with two spoked wheels, frame, seat and handlebars, and a white-bodied pelican with a long neck and orange beak positioned on top."
- **Quote (Willison's comparison)**: "Really not much difference from low and medium, though."
- **Our assessment**: `high` is the first tier to show any visible planning
  text, but the actual cost/token delta from `low` (2,612 vs. 1,998 output
  tokens, $0.131 vs. $0.100) is small relative to what comes next. This
  establishes low/medium/high as a cheap, low-variance cluster for this
  prompt — the real cost cliff is between `high` and `xhigh` (see Claim 4).

### Claim 4: Moving from high to xhigh effort caused output tokens to jump roughly 14x and cost to jump roughly 14x, described by Willison as "radically different"

- **Evidence**: Willison's direct token/time/cost measurement for the
  `xhigh` run.
- **Confidence**: settled (first-person measurement)
- **Quote**: "At xhigh things got radically different.  36,767 output tokens, 7 minutes 51 seconds, $1.83!" (the source renders "radically" in italics; quoted here as plain text since italics are not a literal character sequence)
- **Our assessment**: 36,767 tokens at xhigh vs. 2,612 at high is a ~14x
  token multiplier and cost multiplier ($1.83 vs. $0.131), for a single
  step up the effort ladder. Latency scaled even more sharply: ~16x (7m51s
  vs. 29.6s). This is the sharpest single-step discontinuity documented in
  this corpus's effort-level data (compare to Fable 5's smoother scaling in
  `blog-simonwillison-claude-fable-5.md` Concrete Artifacts, where xhigh was
  only ~3x high's tokens). Practitioners choosing between `high` and `xhigh`
  for Fable 5.1 should treat it as a large, deliberate cost/latency
  commitment, not an incremental dial turn.

### Claim 5: Max effort produced 65,927 output tokens over nearly 14 minutes for $3.30 — the best pelican Willison has seen from any Anthropic model, though still less visually flairful than a competing non-Anthropic model

- **Evidence**: Willison's direct measurement and qualitative visual
  assessment of the `max`-effort SVG output.
- **Confidence**: settled for the token/time/cost figures (first-person
  measurement); anecdotal for the qualitative "best pelican" and
  flair-comparison judgment (single evaluator, subjective aesthetic call)
- **Quote**: "Setting effort to max gave me the best pelican I've seen from any of Anthropic's models. 65,927 output tokens, 13 minutes and 54 seconds, $3.30:"
- **Quote (assessment)**: "There's a lot to like about this. The  background is tasteful, the legs are clearly on either side of the frame, the feet are on the pedals, the wing is on the handlebars, the pelican has a cute blue hat and there's a basket with a fish."
- **Quote (flair comparison)**: "It's still not showing nearly the same level of flair as Gemini 3.7 Flash, but I didn't ask for flair—I asked for an SVG, and that's what I got."
- **Our assessment**: The max→xhigh delta (65,927 vs. 36,767 tokens, $3.30
  vs. $1.83, 13m54s vs. 7m51s) is roughly another 1.8x on every axis — large,
  but proportionally much smaller than the high→xhigh jump in Claim 4. The
  cost curve across all five levels is therefore front-loaded-flat then
  back-loaded-steep: ~$0.10 → ~$0.10 → ~$0.13 → ~$1.83 → ~$3.30. The
  Gemini 3.7 Flash comparison is a single-evaluator aesthetic judgment, not
  a scored benchmark, and should be weighted accordingly.

### Claim 6: The xhigh and max reasoning transcripts show the model making and revising specific, checkable design decisions rather than generic planning restatement

- **Evidence**: Direct excerpts from the reasoning trace Willison published
  inline in the post.
- **Confidence**: settled (verbatim reasoning-trace text, first-hand
  publication)
- **Quote (xhigh)**: "Adding the eye, wings stretching down to the handlebar grip, orange legs reaching to the pedals, and a small tail feather, while keeping the pelican intentionally oversized compared to the bike for comic effect."
- **Quote (max, helmet/beak collision)**: "I realize the beak at (484,84) would overlap with the dome helmet, so I need to shrink the helmet so it only covers the top of the head, adjusting its arc endpoints to sit higher and narrower so the beak can attach cleanly at the front without collision."
- **Quote (max, fork correction)**: "I decide skipping a handlebar bell and tire highlights since they're unnecessary additions. Now I'm reconsidering the front fork's curve — the current control point pulls the shape backward when it should bow forward for a proper rake, so I need to shift the control point rightward to fix the fork's lean."
- **Our assessment**: These are coordinate-level, self-correcting design
  decisions (catching a specific overlap at named SVG coordinates, then
  computing a geometric fix) rather than restated boilerplate — the kind of
  visible, checkable reasoning trace that supports treating extended
  thinking output as an audit trail, consistent with the extended-thinking
  verification pattern documented in `docs-github-copilot-1m-context-reasoning-levels.md`
  Claim 3 (Copilot's "extended thinking" positioned for "hardest
  architectural and debugging challenges"). Here the same pattern shows up
  for a purely visual/generative task, not just code debugging.

### Claim 7: Anthropic's own announcement reports Fable 5.1 scoring 52.6% on the new Terminal-Bench-Science 0.1 benchmark, up from 24.7% for Fable 5, versus 29.0% for Opus 5 and 22.4% for GPT-5.6 Sol

- **Evidence**: Willison relays Anthropic's announcement figures; not an
  independent benchmark run by Willison himself.
- **Confidence**: emerging (vendor-reported benchmark score, relayed but not
  independently reproduced by the author)
- **Quote**: "Their announcement spends a notable amount of time on scientific research, boasting of a 52.6% score on the brand new Terminal-Bench-Science 0.1 benchmark (first announced on August 27th), up from 24.7% for Fable 5, 29.0% for Opus 5 and 22.4% for GPT-5.6 Sol. Other benchmarks show slightly improved scores, but none as impressive as the Science one."
- **Our assessment**: A jump from 24.7% to 52.6% (more than doubling) on a
  benchmark introduced only days earlier (27 August 2026) is a large claimed
  gain, and Willison explicitly frames it as Anthropic's own framing choice
  ("spends a notable amount of time on") rather than something he verified.
  Treat as a vendor-asserted headline number pending third-party
  reproduction, per this corpus's standard treatment of self-reported
  benchmark claims (e.g. `blog-simonwillison-kimi-k3-pelican-benchmark.md`
  Claim 2's treatment of Moonshot's self-reported K3 rankings).

### Claim 8: Willison explicitly frames his own pelican benchmark as no longer a general quality signal, but still useful for within-model-family comparisons across reasoning effort levels — and this post is that methodology in action

- **Evidence**: Willison's own stated rationale for why he still runs this
  specific comparison, referencing his own July 2026 reassessment of the
  benchmark.
- **Confidence**: emerging (editorial framing by the benchmark's creator,
  consistent with his earlier stated position)
- **Quote**: "Back in July I wrote about how I was losing faith in the pelican benchmark—its connection to how good the models were at other tasks didn't seem to hold as strongly as it did back in 2025. The most interesting insights I get from it now are comparisons within model families, and particularly comparisons for the same prompt at different reasoning effort levels."
- **Our assessment**: This post is a direct, named continuation of the
  position Willison set out in `blog-simonwillison-kimi-k3-pelican-benchmark.md`
  (Claims 5, 6, 12: the benchmark's cross-model-quality signal is "mostly
  severed," but it retains value as a cheap forcing-function / cost-and-
  tokenization probe). Here Willison narrows that residual value further,
  to specifically "comparisons within model families... at different
  reasoning effort levels" — exactly the exercise this post performs. The
  guide should treat this post's numbers as evidence for effort-level cost
  scaling, not as a Fable 5.1 vs. other-vendor capability ranking.

### Claim 9: Willison animated the max-effort pelican SVG by piping the prior output back into the model at the default `high` effort level, at a cost of $1.37, prompted by a Hacker News comment

- **Evidence**: Willison's own follow-up experiment and the exact
  command-line invocation he used.
- **Confidence**: settled (first-person action with an exact reproducible
  command and cost figure)
- **Quote (trigger)**: "Now that it's a solved benchmark, can we get the animated version?" (Hacker News user swalsh, quoted by Willison)
- **Quote (Willison's response)**: "I didn't want to spend another $3 so I took the Max pelican and piped it into the default thinking level of High:"
- **Quote (cost)**: "6,121 input, 26,201 output = $1.37."
- **Our assessment**: The explicit "I didn't want to spend another $3" line
  is a direct practitioner signal that `max`-effort cost ($3.30 for the
  static SVG) was treated as prohibitive enough to deliberately downgrade to
  `high` for a related follow-up task, even though the follow-up (animating
  an existing design) arguably required less fresh design reasoning than
  the original generation. This is a concrete, named instance of a
  practitioner actively managing reasoning-effort cost mid-workflow rather
  than defaulting to the highest tier throughout a session.

## Concrete Artifacts

### Fable 5.1 pelican-on-a-bicycle SVG benchmark — full effort-level table

```
Prompt: "Generate an SVG of a pelican riding a bicycle"
Model: Claude Fable 5.1 (via llm-anthropic)

Effort   Output tokens   Wall time      Cost
------   -------------   -----------    -------
low      1,998           23.8s          $0.10017
medium   1,977           23s            $0.09912
high     2,612           29.6s          $0.13087
xhigh    36,767          7m 51s         $1.83
max      65,927          13m 54s        $3.30

Follow-up: animate the Max SVG, run at default (High) effort
  6,121 input tokens, 26,201 output tokens = $1.37

Source: Simon Willison, simonwillison.net/2026/Sep/1/claude-fable-5-1/
```

### Reasoning trace excerpts (verbatim, from the article)

```
[xhigh]
"Adding the eye, wings stretching down to the handlebar grip, orange legs
reaching to the pedals, and a small tail feather, while keeping the pelican
intentionally oversized compared to the bike for comic effect. [...]
I'll accept the slight thickness as charming rather than overengineering it."

[max]
"Adding pedal shapes near both feet, with the far foot on the second leg
partially visible behind the frame. I'm considering whether to add a small
scarf or cap for extra character, but leaning toward keeping it simple to
avoid clutter."

"Now I'm debating a bicycle helmet on the head versus the pelican's
signature crest—the beak and pouch already read clearly as "pelican," so a
helmet could reinforce the bicycle theme without losing identity, though it
might compete with the crest for visual space."

"I realize the beak at (484,84) would overlap with the dome helmet, so I
need to shrink the helmet so it only covers the top of the head, adjusting
its arc endpoints to sit higher and narrower so the beak can attach cleanly
at the front without collision. [...]"

"I'm adding a darker tip region to represent the primary feathers, then
reconsidering the trailing edge to include scalloped feather curves instead
of one smooth line for a more natural look. [...]"

"Now I'm checking the vent line placements on the helmet, making sure they
sit far enough inside the helmet's edge given the stroke width and rounded
caps, and confirming each vent stays within the helmet's circular
boundary. [...]"

"I decide skipping a handlebar bell and tire highlights since they're
unnecessary additions. Now I'm reconsidering the front fork's curve — the
current control point pulls the shape backward when it should bow forward
for a proper rake, so I need to shift the control point rightward to fix
the fork's lean."

Source: Simon Willison, simonwillison.net/2026/Sep/1/claude-fable-5-1/
```

### Animation command (verbatim)

```
llm logs -cx | llm -m claude-fable-5.1 -s 'animate this'

Source: Simon Willison, simonwillison.net/2026/Sep/1/claude-fable-5-1/
```

### Terminal-Bench-Science 0.1 scores (Anthropic's announcement, as relayed by Willison)

```
Model            Terminal-Bench-Science 0.1
--------------   ---------------------------
Fable 5.1        52.6%
Opus 5           29.0%
Fable 5          24.7%
GPT-5.6 Sol      22.4%

Benchmark first announced 27 August 2026.
Source: Simon Willison, simonwillison.net/2026/Sep/1/claude-fable-5-1/,
citing Anthropic's announcement at anthropic.com/claude-fable-and-mythos-5-1
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-choosing-claude-model.md` Claim 7 (effort level is a
    second, independent axis from model class; higher-class models at
    lower effort can sometimes beat a smaller model class on cost): this
    source supplies the first concrete, measured cost/token/latency curve
    across all five of Claude's effort levels for a single frontier model
    (Fable 5.1), turning that qualitative claim into a citable numeric
    example — including the finding that two adjacent tiers (low, medium)
    can be functionally identical for a given task (Claim 2).
  - `blog-anthropic-cowork-fable-5-working-with.md` Claim 6 (effort setting
    is a separate lever from model choice; higher effort makes Fable plan
    more upfront): this source's reasoning-trace excerpts (Claim 6) are a
    concrete illustration of "planning more upfront" — the xhigh/max traces
    show explicit upfront design planning and self-correction that the
    low/medium/high traces do not.

- **Contradicts**: None identified. No existing note makes a claim that
  materially conflicts with this source's measurements. No contradiction
  issue required.

- **Extends**:
  - `blog-simonwillison-claude-fable-5.md` Claim 11 (Fable 5's pelican
    benchmark across effort levels: low 1,929 tokens/9.67c → max 14,430
    tokens/72.175c, a ~7.5x token/cost multiplier top-to-bottom, with a
    non-monotonic dip at `high`): this source runs the identical benchmark
    against Fable 5.1 and finds a much steeper multiplier (low 1,998 tokens/
    10.017c → max 65,927 tokens/$3.30, a ~33x token multiplier and ~33x cost
    multiplier). The two posts, same author and same fixed prompt, five
    months apart, show Fable 5.1's top reasoning tiers burning roughly
    4.5x-6x more output tokens than Fable 5's did at the equivalent xhigh/max
    tiers (36,767 vs. 5,992 at xhigh; 65,927 vs. 14,430 at max), while the
    low/medium/high tiers stayed roughly comparable in scale. This is a
    citable data point that newer-generation reasoning-effort scaling is not
    simply "the same curve, shifted" — the top of the curve got much steeper
    in absolute terms even as low/medium/high stayed cheap.
  - `blog-simonwillison-kimi-k3-pelican-benchmark.md` Claims 5, 6, 12
    (Willison's own reassessment that the pelican benchmark's cross-model
    quality signal is "mostly severed," but it retains value as a "hello
    world" forcing function and a cost/tokenization probe): this source is
    Willison explicitly acting on that narrowed methodology (Claim 8 above),
    applying the benchmark specifically to compare effort levels within one
    model family rather than to rank Fable 5.1 against competing vendors.
  - `docs-github-copilot-1m-context-reasoning-levels.md` Claims 2 and 5
    (configurable reasoning levels let practitioners "dial in the right
    balance of speed and depth," and both extended context and higher
    reasoning "consume more AI credits per interaction," without a stated
    multiplier): this source supplies the multiplier that GitHub's
    changelog left unspecified — a concrete ~14x-33x token/cost jump between
    adjacent tiers at the top of Claude's five-level scale, and a
    near-zero (or even negative) difference between the bottom two tiers for
    at least one prompt type.
  - `blog-simonwillison-pelicanmaxxing.md` (Dylan Castillo's systematic
    48-prompt factorial study finding no statistically significant
    per-lab pelican- or bicycle-specific benchmark gaming): this source's
    within-family, cross-effort-level use of the pelican prompt (Claim 8) is
    consistent with that study's implicit conclusion that the pelican
    prompt's main remaining value is as a fixed, comparable stimulus for
    relative comparisons rather than as an absolute or cross-vendor quality
    signal.

- **Novel**:
  - **First in-corpus documentation of Claude Fable 5.1 as a model**: no
    prior source note covers Fable 5.1's reasoning-level behavior, cost
    curve, or Terminal-Bench-Science score.
  - **First concrete, measured cost/token/latency table across all five
    Claude effort levels for a single fixed prompt**: prior effort-level
    data in the corpus (Fable 5, GPT-5.5, Kimi K3) covered other models;
    this is the first Fable-5.1-specific dataset, and the first to show two
    adjacent tiers (low, medium) producing statistically indistinguishable
    output for the same prompt.
  - **A concrete example of a practitioner mid-session downgrading effort
    level to control cost** (Claim 9: "I didn't want to spend another $3"):
    not documented elsewhere in the corpus as an explicit, quoted
    cost-driven effort-level decision.

## Guide Impact

- **Chapter on Models and Reasoning (effort-level selection)**: Add this
  source's effort-level table as the primary citable evidence that Claude's
  reasoning-effort scale is not linear or even monotonic in cost/output for
  all tasks: low/medium/high form a cheap, low-variance cluster (roughly
  $0.10-$0.13, within 30% of each other), while xhigh and max represent
  large, deliberate cost/latency commitments (14x and 33x over `high`,
  respectively, for this prompt). Recommend explicit guidance: default to
  `high` for most generative/creative tasks, and only escalate to
  `xhigh`/`max` when the task specifically benefits from deeper, checkable
  deliberation (Claim 6) — verified per-task rather than assumed, since
  `medium` bought nothing over `low` for this prompt (Claim 2).

- **Chapter on Prompting Strategies / Cost Optimization**: Cite Claim 9 (the
  Hacker-News-prompted animation follow-up run at `high` instead of `max` to
  avoid "spend[ing] another $3") as a concrete, reproducible pattern:
  practitioners can deliberately downgrade effort level for a follow-up
  request that builds on prior output, rather than re-running the most
  expensive tier for every step of a multi-turn task.

- **Chapter on Evaluation and Quality (benchmark skepticism)**: Reinforce
  the guide's existing treatment (informed by `blog-simonwillison-kimi-k3-pelican-benchmark.md`)
  that informal creative benchmarks like the pelican SVG should be used for
  relative, within-family comparisons (effort levels, model generations) —
  exactly as this source uses it — not as a cross-vendor capability ranking.
  Keep Anthropic's self-reported Terminal-Bench-Science score (Claim 7)
  flagged as vendor-asserted until independently reproduced.

## Extraction Notes

- WebFetch's default (LLM-summarized) pass on this URL returned a
  serviceable but imprecise summary and, on follow-up targeted-quote
  requests, one quote with altered punctuation (a period substituted for a
  comma mid-sentence). To get character-exact quotes, the article's raw HTML
  was fetched directly (`curl`) and the entry body was extracted and
  stripped of markup programmatically. All quotes in this note are taken
  from that raw-HTML extraction, not from the summarized WebFetch passes.
- The post links to several external resources that were not fetched in
  full: two `gist.github.com` transcripts (via a `tools.simonwillison.net`
  SVG/reasoning-transcript renderer) for each effort level, the Hacker News
  thread, and Anthropic's own Fable/Mythos 5.1 announcement page. These were
  not needed for extraction because the article's own prose states every
  token/time/cost figure and reproduces the relevant reasoning-trace
  excerpts inline. The linked GitHub issue (`simonw/llm-anthropic#88`,
  titled "Reasoning traces should be requested, displayed, and stored by
  default") was checked only for its title, cited in Source Context as
  supporting evidence that the low/medium reasoning-trace absence (Claim 2)
  reflects real model behavior rather than a pre-existing logging bug that
  Willison had already fixed before running these tests.
- The article's link for "Back in July I wrote about..." resolves to
  `simonwillison.net/2026/Jul/16/kimi-k3/`, which matches the existing
  corpus note `blog-simonwillison-kimi-k3-pelican-benchmark.md` — confirmed
  by reading that note's frontmatter `source_url` before citing it in
  Cross-References.
- No contradictions identified against any existing source note. No
  contradiction issue filed.
