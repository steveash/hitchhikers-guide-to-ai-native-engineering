---
source_url: https://claude.dev/blog/how-we-made-claude-ai-faster/
source_type: blog-post
title: "How we made claude.ai 3x faster in two weeks"
author: Raymond Wang, Sam Attard, and Issac G. (Anthropic)
date_published: 2026-09-23
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: emerging
issue: "#3949"
---

# How we made claude.ai 3x faster in two weeks

> Anthropic's retrospective on a two-week, Slack-channel-driven performance sprint in which Claude (via Claude Tag) hill-climbed deterministic lab metrics, shipped 3,000+ flag-gated changes, and locked each win in with CI ratchets, with humans supplying ambition, taste, and direction.

## Source Context

- **Type**: blog-post (engineering retrospective, first-party)
- **Author credibility**: Three engineers on the claude.ai / desktop team at Anthropic, writing about their own sprint; named colleagues are quoted in the Slack excerpts. Internal first-party account, so results are self-reported and unaudited. Thread excerpts are labelled "Recreated from a real conversation."
- **Scope**: Covers the August 2026 sprint on four user journeys (launch, start conversation, load conversation, send message), the measurement hierarchy, the thread-per-problem loop, guardrails, human steering roles, and a streaming-render sidequest. It does not cover cost/token spend of the sprint, the p95 tail, or the upstream Electron/Chromium/Node contributions (promised for a separate post). Model used: Claude Tag (beta) running "an internal research model roughly comparable to Opus 5.5", so results may not transfer to current public models.

## Extracted Claims

### Claim 1: A two-week sprint produced a ~3.1x geometric-mean speedup across 13 measurements on four journeys, with more than 3,000 merged changes and no customer-facing incident or rollback
- **Evidence**: Field RUM before/after (Aug 13 vs Aug 27) per platform and product, e.g. claude.ai fresh load 3,085 → 550 ms (5.6x), Cowork cloud send 928 → 48 ms (19x), desktop cold start 6,310 → 3,328 ms (1.9x); p75.
- **Confidence**: emerging
- **Quote**: "we merged more than three thousand changes without a single customer-facing incident or rollback"
- **Our assessment**: Specific, field-measured numbers make this stronger than typical claims, but it is self-reported, from the vendor of the tool, with an internal model and a team with unusually strong guardrails. Treat the speedups as an upper-end existence proof, not an expected rate.

### Claim 2: "With Claude, measuring something makes it tractable" — measurement shifts from step zero to step one of the climb, so the highest-leverage human work is finding more things to measure
- **Evidence**: Narrative across the sprint; each new instrument (instruction counts, layout-shift events, hook census, style-recalc counts) spawned new threads and fixes.
- **Confidence**: emerging
- **Quote**: "With Claude, measuring something makes it tractable."
- **Our assessment**: Compelling framing consistent with verification-loop guidance elsewhere in the corpus; the evidence is anecdotal-but-concrete (many examples) rather than controlled.

### Claim 3: Prefer deterministic lab metrics (instruction counts, V8 call counts, React commits, style recalcs, DOM mutations) over wall-clock time as both optimization target and CI gate, but make each prove it correlates with wall-clock before keeping it
- **Evidence**: Two hot paths: message-tree assembly cut instructions 48% / wall-clock 78%; status-line scanner 31% / 44%. Unproven benches were to be unshipped.
- **Confidence**: emerging
- **Quote**: "Wall-clock time is what users feel, but it’s noisy, and milliseconds are too flaky to use as a CI gate."
- **Our assessment**: Sound engineering and an important guard against Goodhart-style hill climbing. Only two hot paths were shown as proof, so "the count tracks the clock" is demonstrated, not established generally.

### Claim 4: Every new benchmark has two jobs — a metric the agent can move in the lab and a CI guardrail that can only ratchet down — and flaky or uncorrelated benchmarks are discarded
- **Evidence**: Description of the ratchet mechanism: PRs raising instruction counts fail CI; a daily job lowers each ceiling when counts drop.
- **Confidence**: emerging
- **Quote**: "a guardrail in CI with a number that could only ratchet down"
- **Our assessment**: A reusable pattern (ratchet = locked-in gain). Note that ceilings that only decrease can create friction on legitimate feature work; the post does not discuss how exceptions are handled.

### Claim 5: A repeatable per-thread loop (open thread → benchmark → risk-sized PRs behind flags → watch deploy and field data → ratchet or flag off → next slow spot) is the unit of work
- **Evidence**: Six-step loop description with a diagram; sidebar-jank example where a test went "red 20 of 20 runs on main, and green 20 of 20 on the PR".
- **Confidence**: emerging
- **Quote**: "Claude would trace the flow, then find or build a benchmark that demonstrated the problem."
- **Our assessment**: Nicely concrete: reproduce-before-fix with a repeated-run red/green criterion. Closely mirrors the loop literature already in the corpus, with a perf-specific instantiation.

### Claim 6: Existing aggregate metrics miss user-perceived problems; going to the underlying browser API (Layout Instability API) exposed that 31% of web page loads moved content after the page was usable
- **Evidence**: Each shift scored ~0.008 CLS (under the 0.1 "good" threshold), so no monitor fired; Claude built a telemetry event mapping shift sources to named regions and phases, then read the field data.
- **Confidence**: emerging
- **Quote**: "Claude read the field data and found that 31% of web page loads moved something after the page was usable"
- **Our assessment**: Strong illustration that agent-built bespoke telemetry can surface blind spots of standard dashboards. Human provided the lead (Issac's idea), so it is human-agent collaboration rather than autonomous discovery.

### Claim 7: Horizontal scaling is just opening more narrow threads (150+ at once); threads keep going after the original request, and increasingly Claude opens threads itself from nightly jobs or other investigations
- **Evidence**: Up to 50–100 PRs per thread, 200+ changes on the busiest days; ~a third of PRs added telemetry or guardrails.
- **Confidence**: emerging
- **Quote**: "During the sprint, we ran more than a hundred and fifty at a time."
- **Our assessment**: Notable throughput claim; review capacity (human approval on every PR) is the implicit bottleneck and the post gives no data on reviewer load.

### Claim 8: Measurement cascades — each probe found surprising root causes (6,900 hooks in the typing path, a `:root:has()` selector costing 24 ms per DOM change, a leftover `location.reload()` causing ~500k hidden reloads/day, em dashes forcing UTF-16 strings and slow regex highlighting)
- **Evidence**: Specific root causes with numbers; highlighting freeze reduced from ~1.0 s to 0.35 s main-thread blocking via a ~20-line change (4-vCPU container, headless Chrome, 2–3 runs per value).
- **Confidence**: anecdotal
- **Quote**: "If a reply’s markdown contained any non-Latin-1 character, like an em dash or a curly quote, V8 stored the entire string as UTF-16"
- **Our assessment**: Technically plausible and specific; the benchmark sample size (2–3 runs) is small, noted by the authors.

### Claim 9: Safety stack for moving fast on hot paths: automated review plus at least one human approval, tests before optimizations, short-lived feature flags for anything user-visible, and incremental rollout (employees → 1% → everyone)
- **Evidence**: Nearly 200 flags introduced, more than half cleaned up by sprint end; Claude classified each flag as kill switch or ramp and retired them; dogfooding caught a layout shift four hours after internal release.
- **Confidence**: emerging
- **Quote**: "Every PR went through automated review with at least one human approval, unit tests always came before optimizations"
- **Our assessment**: Standard but well-executed practices; the flag-lifecycle management delegated to the agent is the interesting extension. The zero-rollback claim depends on this stack, not on the model alone.

### Claim 10: Performance wins decay in a fast-moving codebase, so each proven win should be protected by layered guardrails (drift tests, cross-viewport alignment tests, keystroke tests, field reporting that opens a thread on any non-zero movement)
- **Evidence**: Static-composer example: HTML copy rendered from the real React component in jsdom, 14 viewport sizes asserted within 1 px, a keystroke test that fails on lost/reordered keys, field shift reporting to a tenth of a pixel.
- **Confidence**: emerging
- **Quote**: "performance wins decay in a fast-moving codebase"
- **Our assessment**: Good argument that brittle-by-design optimizations require agent-authored guardrails as the price of admission.

### Claim 11: Agents can diagnose edge cases outside the codebase from user evidence — a screen recording led Claude to trace a layout shift to Chrome's speculative prerender plus a 56 px managed-browser footer
- **Evidence**: Claude's Slack reply explains the 0.18 × 56 ≈ 10 px shift matching the video, why it only occurs on new tabs, and why headless-Chrome layout tests could not see it; a prerender-simulation test was added.
- **Confidence**: anecdotal
- **Quote**: "Our layout tests can’t see it because headless Chrome has no browser UI to retract"
- **Our assessment**: Illustrates a limit of lab guardrails (they cannot see environment chrome) and why staged rollouts to humans remain necessary.

### Claim 12: Humans' three roles in an agent-driven sprint are ambition, taste, and direction — Claude defaults to caution (ticketing, hedging, padding estimates) and has to be pushed to be bolder
- **Evidence**: Slack exchange where Raymond tells Claude "please be braver" and the PR lands within the hour; Sam repeatedly told threads "the targets are not the stopping point"; a 900-line PR rejected with one line because 2 ms per send did not justify the maintenance burden.
- **Confidence**: anecdotal
- **Quote**: "By default, Claude is careful about scope. It tickets findings, hedges on feasibility, and pads its estimates."
- **Our assessment**: Valuable and unusual: a vendor admitting default agent behavior needed correcting. Also shows threads slowed once targets were hit, i.e. targets act as stopping conditions. The "be braver" prompting is only safe because of the guardrails in Claim 9.

### Claim 13: A single Slack channel with standing instructions, a named human owner per thread, and Claude present in every thread serves as the coordination layer; others brought changes in for performance review and wrote faster code by default thanks to the introduced guardrails and skills
- **Evidence**: Verbatim standing-instruction brief (see artifacts); the post says working in one channel meant everything happened in the open.
- **Confidence**: emerging
- **Quote**: "The ultimate goal for this channel is for you to become as autonomous as possible, but today we know that isn’t yet possible."
- **Our assessment**: Standing instructions that include monitoring deploys, maintaining dashboards, and proposing projects define a durable role rather than a one-off task.

### Claim 14: Making frame budgets deterministic (120 Hz headless Chrome via DevTools begin-frame control) turned smoothness into an exact lab read and a nightly regression job; the resulting ~60 PRs cut long-reply main-thread blocking from ~750 ms to ~200 ms
- **Evidence**: Claude stepped through frames at 8.33 ms; "exactly 240 frames for 240 begin-frames"; held 120 fps on a 120 Hz MacBook.
- **Confidence**: emerging
- **Quote**: "But it turned out we could count them — and anything we could count, Claude could climb."
- **Our assessment**: Strong example of the human proposing a stretch target and the agent building the measuring rig to make it tractable.

## Concrete Artifacts

Standing instructions given to Claude in the channel (excerpt, as published):

```
@Claude Your job is to facilitate all things related to the performance of the claude.ai website and desktop app. Your responsibilities include monitoring deploys for performance regressions, assessing the accuracy and comprehensiveness of existing telemetry, maintaining well-curated observability dashboards, proactively implementing solutions for observed issues and low-hanging fruit, proposing performance project opportunities, and communicating with your human teammates. […]
```

Project-refresh prompt (verbatim fragment):

```
@Claude we’ve ended up funding nearly every project in the original projects list and more. let’s do a refresh […] what have we not explored, what can we hill climb on, where is the most opportunity at this point? […] i am open to WACKY ideas
```

Benchmark-validation prompt:

```
@Claude please prove that hill climbing against each of these can result in measurable wall clock perf wins. we’ll unship the benches for any candidates that cannot prove that
```

Measurement ladder suggested by Claude (Slack, paraphrased from source): pure-JS paths under Valgrind with `node --predictable` against a checked-in baseline (instruction counts, "one run, no statistics needed"); for browser paths, React commits per interaction, V8 precise-coverage function call counts, layout/style-recalc counts, DOM mutations.

Core journey results (p75, RUM, Aug 13 → Aug 27, from the source):

```
claude.ai web fresh load      3,085 -> 550 ms   (5.6x)
Desktop cold start            6,310 -> 3,328 ms (1.9x)
Chat web start                  416 -> 273 ms   (1.5x)
Claude Code desktop start       837 -> 347 ms   (2.4x)
Cowork desktop cloud load     2,566 -> 728 ms   (3.5x)
Cowork desktop cloud send       928 -> 48 ms    (19x)
Claude Code desktop send        250 -> 52 ms    (4.8x)
13 measurements, geometric mean 3.1x
```

Loop (source, bulleted list): open thread on slow stretch → trace flow / build benchmark → PR(s) sized for risk, user-visible behind a flag → watch deploy and read field data → if faster, ratchet benchmark down; if not, turn flag off and iterate → find next slow spot.

## Cross-References

- **Corroborates**: `blog-anthropic-getting-started-with-loops.md` Claim 10 (self-verification skills should be quantitative so Claude can measure the result) and Claim 6 (encoding failures into system-wide fixes) — this sprint is a large-scale instance of both. `blog-anthropic-ci-test-impact-analysis-scaling.md` Claim 11 (instrument services so Claude can act as "eyes and ears" for incremental hill-climbing) — same pattern from another Anthropic team. `blog-cursor-app-stability.md` Claim 12 (rules acting as regression guards in CI) and Claim 4 (feature flags to attribute regressions) — independent corroboration that CI regression guards and flags are the answer to agent-driven velocity.
- **Contradicts**: None found. (Tension, not contradiction: the Slack "be braver" steering in Claim 12 vs. cautious-scope guidance elsewhere; it is conditioned on strong guardrails, so no contradiction issue was filed.)
- **Extends**: `blog-anthropic-claude-tag-employee-workflows.md` (Claude Tag in dedicated channels, with standing instructions in Claims 9–10) — extends it from document/review work to a multi-engineer, 150-thread engineering effort. `blog-anthropic-claude-tag-context-awareness.md` Claim 6 (plain-language per-channel instructions) — here those instructions are an engineering role brief. `blog-thoughtworks-singh-shaik-performance-engineering.md` — a concrete performance practice rather than a mindset piece.
- **Novel**: Deterministic-metric hierarchy (instruction counts → call counts → React commits → layout/DOM counts) with a wall-clock correlation proof requirement; ratchet-down CI ceilings lowered automatically by a daily job; thread-per-problem coordination at 150 concurrent threads; the "ambition / taste / direction" human-role taxonomy; agent-managed feature-flag lifecycle (kill switch vs ramp); deterministic 120 Hz frame-budget rig.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the "benchmark = lab metric + ratchet guardrail" pattern and the rule that a deterministic proxy metric must be shown to track the user-facing metric before being adopted as an agent's optimization target (Claims 3, 4). Cite as evidence that guardrails, not model care, carry the safety burden.
- **Chapter 03 (Verification)**: Use the red 20/20 on main, green 20/20 on PR criterion and the Layout Instability example (Claims 5, 6) as a concrete reproduce-before-fix standard; note the limit that lab tests could not see browser-environment effects (Claim 11).
- **Chapter 04 (Concurrent development / rollouts)**: Add the flag lifecycle (nearly 200 flags, over half retired; kill switch vs ramp) and employees → 1% → 100% rollouts as the safety layer for high-concurrency agent work (Claim 9).
- **Chapter 07 (Workflow patterns)**: Add the Slack channel + standing-instructions + thread-per-problem pattern, and the human steering roles (ambition, taste, direction) including narrow-scope threads and closing at diminishing returns (Claims 7, 12, 13).
- Caveat for any guide text: results come from an internal model and a vendor's own team; present as emerging evidence.

## Extraction Notes

- Read the full article (fetched HTML, text-extracted) including the results table, all Slack excerpts, and the embedded ClaudeDevs post; video figures (FIG A, FIG B) are not extractable. Related-post sidebar links (e.g. "Automating eval design and hillclimbing with Claude") were not followed and may be worth a separate issue.
- Slack conversations are labelled "Recreated from a real conversation," so they are reconstructions rather than transcripts.
- Quotes copied character-for-character from the source (curly apostrophes preserved); cross-reference claim numbers verified against the cited notes' numbered claims.
