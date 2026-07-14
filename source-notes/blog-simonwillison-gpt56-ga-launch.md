---
source_url: https://simonwillison.net/2026/Jul/9/gpt-5-6/
source_type: blog-post
title: "The new GPT-5.6 family: Luna, Terra, Sol"
author: Simon Willison
date_published: 2026-07-09
date_extracted: 2026-07-14
last_checked: 2026-07-14
status: current
confidence_overall: emerging
issue: "#1847"
---

# The new GPT-5.6 family: Luna, Terra, Sol

> Simon Willison's general-availability writeup of GPT-5.6 (Luna/Terra/Sol):
> GA pricing matches the June 26 preview exactly, OpenAI's Agents' Last Exam
> claims put Sol ahead of Claude Fable 5 while Fable 5 wins SWE-Bench Pro by a
> wide margin (a result OpenAI pre-emptively undercut with its own benchmark-
> validity audit), Willison's personal coding tests still favor Fable 5, and
> three new API primitives ship: Programmatic Tool Calling (sandboxed
> JS orchestration of tool calls), a native Multi-agent API, and explicit
> prompt-cache breakpoints — the last two independently confirmed against
> OpenAI's own developer docs.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, "notes" format — first-person
  commentary with embedded blockquotes of OpenAI's own announcement text,
  ~600 words)
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and the most consistently cross-referenced practitioner source in
  this corpus (see `blog-simonwillison-gpt56-sol-launch.md`,
  `blog-simonwillison-gpt55-codex-plugin.md`,
  `blog-simonwillison-claude-fable-5.md`, and dozens more). He had early
  access to GPT-5.6 Sol ahead of the GA announcement and tested it personally
  against Claude Fable 5 on his own coding tasks, adding independent
  first-person signal on top of OpenAI's marketing claims. No disclosed
  OpenAI or Anthropic affiliation.
- **Scope**: Covers the GPT-5.6 family's GA pricing, specs (context window,
  output limit, knowledge cutoff), two headline benchmark comparisons against
  Claude Fable 5 (Agents' Last Exam and SWE-Bench Pro), OpenAI's same-week
  audit of SWE-Bench Pro's validity, Willison's own early-access coding
  impressions, and four new API features (Programmatic Tool Calling,
  Multi-agent, explicit prompt-cache breakpoints, `detail: original` image
  handling). Does NOT cover: a formal benchmark suite run by Willison himself,
  pricing/latency comparisons for the new API features, or hands-on testing of
  Programmatic Tool Calling / Multi-agent (Willison explicitly says these are
  features he "need[s] to explore" and has not yet used).

## Extracted Claims

### Claim 1: GPT-5.6's GA pricing (Luna $1/$6, Terra $2.50/$15, Sol $5/$30 per 1M input/output tokens) is unchanged from the June 26 preview announcement

- **Evidence**: Willison's post states the GA pricing directly; this figure is
  identical to the pricing table in `blog-simonwillison-gpt56-sol-launch.md`
  Concrete Artifacts (Sol $5.00/$30.00, Terra $2.50/$15.00, Luna $1.00/$6.00),
  which was sourced from OpenAI's June 26 preview announcement.
- **Confidence**: settled (published GA pricing, directly checkable, and
  consistent across two independent posts six weeks apart)
- **Quote**: "The new models are priced per 1M input/output tokens as Luna
  $1/$6, Terra $2.50/$15, Sol $5/$30."
- **Our assessment**: This closes the loop on `blog-simonwillison-gpt56-sol-launch.md`
  Claim 2, which only had preview pricing to go on. OpenAI held pricing flat
  from preview to GA — worth noting since pricing sometimes shifts between
  preview and general availability for other vendors in this corpus. This is
  the strongest possible confirmation available (same numbers, independent
  post, six weeks later) short of Willison explicitly saying "unchanged."

### Claim 2: OpenAI's per-token pricing across vendors is a weak comparison signal because reasoning-token volume varies so much between models for the same task

- **Evidence**: Willison's own editorial aside while listing comparison
  pricing (Claude Opus series $5/$25, Claude Fable 5 $10/$50).
- **Confidence**: emerging (a practitioner's methodological caveat, not a
  measured claim)
- **Quote**: "but price-per-million tokens doesn't tell us much now that the
  number of reasoning tokens can differ so much between models for the same
  task"
- **Our assessment**: This is a durable methodological point for Ch03 cost
  guidance: as reasoning-token budgets diverge across vendors and effort
  settings, sticker price-per-token becomes a less reliable predictor of
  actual task cost than a per-task or per-effort-level cost benchmark (see
  Claim 9's pelican cost table, which is exactly this kind of measurement).

### Claim 3: All three GPT-5.6 models share a February 16, 2026 knowledge cutoff, a 1M-token context window, and a 128,000-token maximum output

- **Evidence**: Stated directly in the post as a spec summary.
- **Confidence**: settled (published spec, directly checkable)
- **Quote**: "All three models have a February 16th 2026 knowledge cutoff, a
  million token context window, and 128,000 maximum output tokens."
- **Our assessment**: A uniform context/output/cutoff spec across a
  three-tier family (rather than the largest model getting a bigger context
  window) is consistent with the tiering-by-price-not-by-context pattern this
  corpus has already seen in `blog-simonwillison-gpt56-sol-launch.md` — tiers
  differentiate on price and (per Claim 4 below) benchmark score, not on
  context window size.

### Claim 4: On Agents' Last Exam, GPT-5.6 Sol scores 53.6 — 13.1 points ahead of Claude Fable 5 — with Terra and Luna also beating Fable 5 at a fraction of the cost

- **Evidence**: A direct blockquote of OpenAI's own announcement, embedded by
  Willison without independent verification.
- **Confidence**: emerging (this is OpenAI's own self-reported benchmark
  claim, presented via a named benchmark — Agents' Last Exam — but not
  independently reproduced by Willison or any other corpus source)
- **Quote**: "On Agents' Last Exam, an evaluation of long-running professional
  workflows across 55 fields, GPT-5.6 Sol sets a new high of 53.6, eclipsing
  Claude Fable 5 (adaptive reasoning) by 13.1 points. Even at medium
  reasoning, it beats Fable 5 by 11.4 points at roughly one-quarter the
  estimated cost. That efficiency extends to smaller models, which are
  essential to making intelligence more abundant and affordable: GPT-5.6
  Terra and GPT-5.6 Luna outperform Fable 5 at around one-sixteenth the
  cost."
- **Our assessment**: This is the first corpus mention of "Agents' Last Exam"
  as a named benchmark. Treat the score and the cost-efficiency multipliers
  (one-quarter, one-sixteenth) as vendor-reported until an independent source
  reproduces them — OpenAI is both the model developer and the party
  reporting the comparison. Willison presents it as OpenAI's "biggest
  benchmark claim" without endorsing or disputing the number himself.

### Claim 5: On SWE-Bench Pro, Claude Fable 5 scores 80% versus GPT-5.6 Sol's 64.6% — the inverse of the Agents' Last Exam result

- **Evidence**: Willison's own framing of a "self-reported benchmark" result,
  contrasted directly against the Agents' Last Exam claim in Claim 4.
- **Confidence**: emerging (self-reported per-vendor benchmark figures, but
  corroborated by an independent figure for Fable 5 specifically — see
  Cross-References)
- **Quote**: "Amusingly, one self-reported benchmark that Fable 5 crushed the
  GPT-5.6 family on was SWE-Bench Pro, where Fable 5 got 80% compared to
  GPT-5.6 Sol getting 64.6%."
- **Our assessment**: A 15.4-point gap in Fable 5's favor on SWE-Bench Pro,
  set directly against a 13.1-point gap in Sol's favor on Agents' Last Exam,
  is a genuinely useful "benchmark choice determines the winner" data point
  for Ch03 — practitioners choosing a model on the strength of one benchmark
  should be aware both leading vendors can point to a benchmark that favors
  them. Fable 5's 80% figure corroborates `blog-latentspace-fable-5-mythos-launch.md`
  Claim 2 (80.3% on SWE-Bench Pro, reported in June) — two independent
  sources six weeks apart put Fable 5's SWE-Bench Pro score at ~80%, which
  raises confidence in that specific number even though the GPT-side
  comparison figures differ between sources (58.6% for GPT-5.5 in June vs.
  64.6% for GPT-5.6 Sol here — a plausible generational improvement, not a
  conflict).

### Claim 6: OpenAI published an audit the day before the GPT-5.6 GA announcement estimating that ~30% of SWE-Bench Pro tasks are broken

- **Evidence**: A direct blockquote from an OpenAI article Willison links to
  and explicitly connects, by timing, to the SWE-Bench Pro result in Claim 5.
- **Confidence**: emerging (OpenAI's own self-audit of a benchmark it
  performed worse on; the methodology behind the "~30% broken" estimate is
  not detailed in Willison's post, and the audit article itself could not be
  independently verified during this extraction — see Extraction Notes)
- **Quote**: "In light of these results, we estimate that ~30% of SWE-bench
  Pro tasks are broken, and advise that model developers carefully examine
  results"
- **Our assessment**: Willison's own framing — "This may help explain why
  OpenAI chose to publish this article yesterday specifically calling out
  SWE-Bench Pro for problems they found while auditing that benchmark" — is
  itself worth preserving as a practitioner's skeptical read: a vendor
  publishing a benchmark-validity critique one day before losing badly on
  that same benchmark is a conflict-of-interest pattern worth flagging in any
  guide passage that cites SWE-Bench Pro results. This doesn't mean the ~30%
  broken-task estimate is wrong, but it should be weighted as a source with a
  clear incentive, not a neutral third-party audit.

### Claim 7: Willison's own early-access testing found GPT-5.6 Sol "definitely very competent" but not better than Claude Fable 5 on the complex coding tasks he uses day to day

- **Evidence**: Willison's first-person assessment, based on early access
  granted ahead of the public GA announcement.
- **Confidence**: anecdotal (single practitioner, unspecified number and type
  of tasks, no controlled comparison methodology described)
- **Quote**: "I've had some early access to GPT-5.6 Sol—it's definitely very
  competent, though so far it hasn't struck me as better than Fable at the
  kind of complex coding tasks I've been using with Anthropic's model."
- **Our assessment**: This is the highest-value single claim in the post for
  Ch03 model-selection guidance: an experienced practitioner's real-task
  comparison, made independently of both vendors' benchmark claims, and it
  directly undercuts OpenAI's Agents' Last Exam framing (Claim 4) for at
  least one task category (complex coding). Treat as anecdotal-but-credible
  given Willison's track record of consistent, detailed cross-model testing
  elsewhere in this corpus (e.g. `blog-simonwillison-claude-fable-5.md`).

### Claim 8: Programmatic Tool Calling lets GPT-5.6 write and run JavaScript in an isolated, ephemeral sandbox to orchestrate tool calls, with per-tool `allowed_callers` controlling whether a tool is reachable directly, only from generated code, or both

- **Evidence**: Willison's blog quote, independently confirmed and extended
  against OpenAI's own developer documentation
  (developers.openai.com/api/docs/guides/tools-programmatic-tool-calling),
  fetched directly during this extraction.
- **Confidence**: settled (first-party API documentation, directly fetched
  and checked, not just a secondhand summary)
- **Quote**: "Programmatic Tool Calling allows the models to "compose and run
  JavaScript that orchestrates tool calls"" (Willison, quoting OpenAI's
  feature description). From OpenAI's own docs: "Programmatic Tool Calling
  lets a model write and run JavaScript that coordinates the tools in a
  Responses API request. A program can call tools in parallel, use loops and
  conditions, and keep intermediate results in the hosted runtime." And on
  the sandbox: "OpenAI runs each generated program in a fresh, isolated V8
  runtime. The runtime supports JavaScript with top-level await, but it does
  not provide Node.js, package installation, direct network access, a
  general-purpose filesystem, subprocess execution, a console, or persistent
  JavaScript state between program executions."
- **Our assessment**: This is a formalized, hosted, harness-agnostic version
  of a pattern this corpus has already documented twice under Anthropic's
  branding — see Cross-References. The key architectural difference from
  Anthropic's version: OpenAI's runtime is a request-scoped, stateless V8
  sandbox with no filesystem/network/subprocess access and explicit
  per-tool `allowed_callers` gating (direct vs. programmatic vs. both),
  whereas Anthropic's pattern (per `blog-anthropic-harnessing-claude-intelligence.md`
  Claim 2) is Claude using the bash/text-editor tools it already has. OpenAI's
  version trades flexibility for a tighter security boundary — useful context
  for Ch05 guidance on when to reach for sandboxed code-orchestration tools
  vs. giving the model a general-purpose shell.

### Claim 9: The Multi-agent API lets a GPT-5.6 model spin up subagents for parallel, focused work as a native part of the Responses API, not a harness-level pattern

- **Evidence**: Willison's blog quote of OpenAI's feature description. The
  dedicated docs page Willison links
  (developers.openai.com/api/docs/guides/tools-multi-agent) returned a
  "Page not found" response when fetched directly during this extraction —
  see Extraction Notes.
- **Confidence**: emerging (confirmed only via Willison's secondhand quote of
  OpenAI's own description; the linked primary-source docs page could not be
  independently verified)
- **Quote**: "Multi-agent lets the model "spin up subagents for parallel,
  focused work"—the sub-agent pattern now baked into the core API."
- **Our assessment**: Willison's own framing — "baked into the core API" — is
  the useful signal here: this corpus has extensively documented subagent
  spawning as a harness-level feature (Claude Code's subagents, gh-aw's
  agent orchestration, etc.); this is the first corpus mention of a model
  vendor exposing subagent orchestration as a first-class, model-native API
  primitive rather than something the calling application has to build.
  Should be flagged for re-verification once the docs page is reachable or
  Willison (or another source) tests it directly, since the only confirmation
  available is a short vendor-sourced description quoted secondhand.

### Claim 10: GPT-5.6 formalizes explicit prompt-cache breakpoints — request-scoped, up to four new cache writes per request, a fixed 30-minute TTL, and a 1.25x uncached-rate cache-write cost that applies only to GPT-5.6 and later models

- **Evidence**: Willison's blog quote plus direct verification against
  OpenAI's prompt-caching developer documentation
  (developers.openai.com/api/docs/guides/prompt-caching), fetched during this
  extraction.
- **Confidence**: settled (first-party API documentation, directly fetched
  and checked against Willison's summary and against the preview-stage
  numbers in `blog-simonwillison-gpt56-sol-launch.md`)
- **Quote**: Willison: ""Prompt cache breakpoints brings the Claude model of
  prompt caching to OpenAI, letting you be explicit about where the cache
  breakpoints are rather than relying on the API to detect them
  automatically. Personally I much prefer automatic detection (still
  supported by OpenAI), but presumably there are optimization cost savings to
  be had here if you put the work in."" From OpenAI's docs: "Cache writes
  have no additional fee on models before the GPT-5.6 family. For GPT-5.6
  models and later model families, cache writes cost 1.25× the uncached
  input token rate." And: "All breakpoints use the request-wide
  prompt_cache_options.ttl, which currently defaults to 30m and is the only
  supported value. Each request can create up to four new cache writes."
- **Our assessment**: This confirms and extends `blog-simonwillison-gpt56-sol-launch.md`
  Claims 5-6 (announced at preview stage: explicit breakpoints, 30-minute
  minimum cache life, 1.25x write rate) — the GA docs show those preview
  figures shipped unchanged, and add mechanics the preview announcement
  didn't cover: `mode: implicit` (default, one breakpoint auto-placed on the
  latest message plus any explicit ones) vs. `mode: explicit` (only explicit
  breakpoints count, and a request with none gets no caching at all), a
  1,024-token minimum prefix to be cacheable, and up to the latest 50
  breakpoints considered for cache reads. Note the 1.25x write surcharge is
  GPT-5.6-and-later-specific — pre-5.6 models still write to cache for free,
  per the docs quote above.

### Claim 11: GPT-5.6 adds a `detail: original` option on image inputs to skip automatic resizing before processing

- **Evidence**: Stated directly in the post as one of the four new API
  features.
- **Confidence**: settled (a documented, checkable API parameter)
- **Quote**: "You can now set detail: original on image requests to avoid
  resizing the image at all before it is processed."
- **Our assessment**: A minor but concrete feature — relevant for any Ch05
  guidance on vision-input fidelity tradeoffs (resizing can lose detail
  needed for OCR-heavy or fine-grained visual tasks; this option trades that
  loss against higher token/compute cost for full-resolution processing, cost
  not quantified in this source).

### Claim 12: Across reasoning-effort levels and the three GPT-5.6 tiers, the pelican-SVG cost benchmark ranged from 0.71 cents (Luna, no reasoning) to 48.55 cents (Sol, max reasoning) — a roughly 68x cost spread within a single model family

- **Evidence**: Willison's own cost-tracked test — an 18-pelican gallery
  (3 models × 6 reasoning-effort levels) with token counts and calculated
  per-image cost, independently fetched and confirmed during this extraction
  at static.simonwillison.net/static/2026/gpt-5.6-pelicans.html.
- **Confidence**: settled (Willison's own measured token counts and computed
  costs against published pricing, directly reproduced by this Miner from the
  linked results page)
- **Quote**: "the least expensive was gpt-5.6-luna at effort none for 0.71
  cents, the most expensive was gpt-5.6-sol at max reasoning level for 48.55
  cents."
- **Our assessment**: This is exactly the kind of per-task cost measurement
  that Claim 2's "price-per-token doesn't tell us much" caveat calls for —
  a concrete illustration that reasoning-effort setting, not just model tier,
  dominates real task cost. The full table (Concrete Artifacts, below) shows
  the spread isn't monotonic with model size alone: at `high` effort,
  gpt-5.6-luna produced more output tokens than gpt-5.6-terra (4,098 vs.
  2,486) yet cost less per image (2.46 vs. 3.74 cents), because Terra's
  per-token rate is 2.5x Luna's. Output token *count* also varies
  unpredictably by model+effort combination (it isn't monotonically
  increasing with effort level for every model), so neither model tier nor
  effort level alone predicts cost; both the token count and the per-token
  rate must be looked up.

## Concrete Artifacts

### GPT-5.6 GA pricing (per 1M tokens), confirmed unchanged from June 26 preview
```
Model    Role          Input     Output
Luna     Fast/cheap     $1.00     $6.00
Terra    Balanced       $2.50    $15.00
Sol      Flagship       $5.00    $30.00

Comparison cited in the post:
Claude Opus series:    $5/$25
Claude Fable 5:         $10/$50

Source: simonwillison.net/2026/Jul/9/gpt-5-6/
```

### Benchmark scorecard (both figures self-reported by the winning vendor)
```
Benchmark              GPT-5.6 Sol   Claude Fable 5   Gap
Agents' Last Exam      53.6          40.5 (implied)   +13.1 (Sol)
SWE-Bench Pro          64.6%         80%              +15.4 (Fable 5)

Source: simonwillison.net/2026/Jul/9/gpt-5-6/, quoting OpenAI's own
announcement for both figures.
```

### Prompt-cache mechanics for GPT-5.6 and later (from OpenAI developer docs, developers.openai.com/api/docs/guides/prompt-caching, fetched 2026-07-14)
```
- Cache write cost: 1.25x the uncached input token rate (GPT-5.6+ only;
  free on pre-5.6 models)
- TTL: fixed at 30m (prompt_cache_options.ttl, only supported value)
- Writes per request: up to 4 new cache writes
- Minimum cacheable prefix: 1,024 tokens
- mode: "implicit" (default) — auto-breakpoint on latest message + any
  explicit breakpoints you add; up to 3 additional explicit writes
- mode: "explicit" — only explicit breakpoints count; a request with none
  gets no caching and no cache-write charge
- Cache reads consider up to the latest 50 breakpoints in a conversation
- Supported content blocks: Responses API — input_text, input_image,
  input_file; Chat Completions API — text, image_url, input_audio, file,
  refusal
```

### Programmatic Tool Calling sandbox constraints (from OpenAI developer docs, developers.openai.com/api/docs/guides/tools-programmatic-tool-calling, fetched 2026-07-14)
```
Runtime: fresh, isolated V8 instance per generated program
Supports: JavaScript with top-level await
Does NOT provide: Node.js, package installation, direct network access,
  general-purpose filesystem, subprocess execution, a console, or
  persistent state between program executions
Output: emitted only via text(...) or image(...) calls
Tool gating: allowed_callers on each tool = ["direct"] | ["programmatic"] |
  ["direct","programmatic"]
ZDR: Programmatic Tool Calling supports Zero Data Retention workflows
  without a persistent code-execution container (org/project-level ZDR
  must still be separately enabled)
```

### Pelican SVG cost benchmark, full table (from static.simonwillison.net/static/2026/gpt-5.6-pelicans.html, fetched 2026-07-14; prices per 1M tokens: Luna $1/$6, Terra $2.50/$15, Sol $5/$30)
```
Effort   gpt-5.6-luna                         gpt-5.6-terra                        gpt-5.6-sol
none     16 in, 1,176 out  = 0.71 cents       26 in, 1,731 out  = 2.60 cents       26 in, 1,961 out  = 5.90 cents
low      16 in, 1,258 out  = 0.76 cents       26 in, 2,312 out  = 3.47 cents       26 in, 2,772 out  = 8.33 cents
medium   16 in, 2,089 out  = 1.26 cents       26 in, 2,302 out  = 3.46 cents       26 in, 3,511 out  = 10.55 cents
high     16 in, 4,098 out  = 2.46 cents       26 in, 2,486 out  = 3.74 cents       26 in, 3,454 out  = 10.38 cents
xhigh    16 in, 7,072 out  = 4.24 cents       26 in, 9,776 out  = 14.67 cents      26 in, 8,033 out  = 24.11 cents
max      16 in, 13,040 out = 7.83 cents       26 in, 21,390 out = 32.09 cents      26 in, 16,180 out = 48.55 cents
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt56-sol-launch.md` Claims 1-2, 5-6, and Concrete
    Artifacts (pricing table, prompt-caching mechanics): GA pricing (Claim 1
    here) matches the June 26 preview pricing table exactly, and the prompt
    cache breakpoint mechanics OpenAI announced at preview (explicit
    breakpoints, 30-minute cache life, 1.25x write rate) shipped unchanged to
    GA (Claim 10 here) — see Extends below for the mechanics this note adds
    on top.
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 2 (Fable 5 scored 80.3%
    on SWE-Bench Pro vs. GPT-5.5's 58.6%, reported June 10, 2026): Claim 5
    here reports Fable 5 at 80% on SWE-Bench Pro (vs. GPT-5.6 Sol's 64.6%) six
    weeks later — two independent sources put Fable 5's SWE-Bench Pro score
    at ~80%, raising confidence in that specific figure even though it's
    still vendor-self-reported in both cases.

- **Contradicts**: None filed. The internal tension between OpenAI's Agents'
  Last Exam claim (Sol beats Fable 5 by 13.1 points, Claim 4) and its
  SWE-Bench Pro result (Fable 5 beats Sol by 15.4 points, Claim 5), and
  between both benchmark claims and Willison's own coding-task experience
  (Claim 7, favoring Fable 5), is presented in the source itself as
  "benchmark choice determines the winner" rather than as a factual dispute
  between two sources about the same claim — per MINER.md §4a this is a
  conditioning-variable/nuance situation (which benchmark, which task type),
  not a contradiction requiring a filed issue. Captured directly in Claims
  4, 5, and 7's "Our assessment" instead.

- **Extends**:
  - `blog-simonwillison-gpt56-sol-launch.md`: that note only had OpenAI's
    preview-announcement text to go on for prompt-caching mechanics (Claim 5:
    "explicit cache breakpoints and a 30-minute minimum cache life"). Claim 10
    here adds the GA-stage mechanical detail fetched directly from OpenAI's
    docs: implicit vs. explicit cache mode, the 4-writes-per-request cap, the
    1,024-token minimum cacheable prefix, and the 50-breakpoint read window —
    none of which appeared in the preview announcement.
  - `blog-anthropic-harnessing-claude-intelligence.md` Claim 2 ("Agent
    Skills, programmatic tool calling, and the memory tool are all
    compositions of bash and text editor") and `blog-anthropic-mcp-production-agents.md`
    Claim 11 ("Programmatic tool calling — processing tool results in a
    code-execution sandbox... reduces token usage by roughly 37% on complex
    multi-step workflows"): Claim 8 here documents OpenAI shipping a
    similarly-named "Programmatic Tool Calling" feature with a materially
    different architecture — a request-scoped, stateless, sandboxed V8
    runtime with explicit per-tool `allowed_callers` gating, rather than
    Claude's approach of using tools (bash/REPL) the model already has
    general access to. Same name, convergent motivation (reduce
    context spent on raw tool-result round-trips), different security model.
    Worth flagging in Ch05 as a vendor-terminology collision practitioners
    should not assume means "the same feature."

- **Novel**:
  - First corpus mention of "Agents' Last Exam" as a named benchmark
    (Claim 4), and the first corpus documentation of any model vendor's
    Multi-agent orchestration shipping as a native Responses-API primitive
    rather than a harness-level pattern (Claim 9).
  - First corpus documentation of a vendor publishing a benchmark-validity
    audit (Claim 6, "~30% of SWE-bench Pro tasks are broken") timed one day
    before a competing benchmark result unfavorable to that same vendor —
    worth flagging generally as a pattern to watch for when citing
    self-reported benchmark validity critiques in the guide.
  - First corpus per-effort-level, per-model-tier cost table for a single
    model family (Claim 12 / Concrete Artifacts) showing cost does not scale
    monotonically with either model size or effort level alone.

## Guide Impact

- **Chapter 03 (Model Selection — Cost Economics)**: Update the GPT-5.6
  pricing entry (sourced provisionally from `blog-simonwillison-gpt56-sol-launch.md`)
  to note pricing is now GA-confirmed, not preview-stage. Add Claim 2's
  methodological caveat directly: recommend per-task cost benchmarking (like
  Claim 12's pelican table) over raw price-per-token comparison, since
  reasoning-token volume varies unpredictably by model and effort level even
  within one vendor's family.

- **Chapter 03 (Model Selection — Benchmark Interpretation)**: Add Claims 4-7
  as a concrete case study for a "no single benchmark picks a winner" guidance
  passage: GPT-5.6 Sol leads Agents' Last Exam by 13.1 points; Claude Fable 5
  leads SWE-Bench Pro by 15.4 points; the practitioner who actually tested
  both (Willison) still preferred Fable 5 for his complex coding tasks.
  Explicitly flag Claim 6 (OpenAI's benchmark-validity audit, timed the day
  before its own weaker SWE-Bench Pro result) as a reason to treat
  self-reported benchmark-critique articles with the same skepticism as
  self-reported benchmark wins.

- **Chapter 05 (Tooling/API Capabilities — Sandboxed Code Orchestration)**:
  Add OpenAI's Programmatic Tool Calling (Claim 8, Concrete Artifacts) as a
  second, architecturally distinct implementation of the "let the model write
  code to orchestrate/filter tool calls" pattern already documented for
  Anthropic. Explicitly note the terminology collision (same name, different
  mechanism) so the guide doesn't conflate the two when discussing either
  vendor.

- **Chapter 05 (Tooling/API Capabilities — Prompt Caching)**: Add the GA-stage
  cache-breakpoint mechanics (Claim 10 / Concrete Artifacts) as a concrete,
  implementable reference alongside the existing Anthropic prefix-caching
  documentation — implicit/explicit modes, the 4-write-per-request cap, the
  1,024-token minimum, and the 1.25x write-cost multiplier that applies only
  from GPT-5.6 onward.

## Extraction Notes

- **Primary blog post fetched twice, two different ways**: WebFetch (the
  standard tool) returned reconstructed/paraphrased text on the first three
  attempts against this URL, close in meaning but not verbatim (e.g. it
  rendered Willison's "hasn't struck me as better than Fable at the kind of
  complex coding tasks I've been using with Anthropic's model" as "hasn't
  struck me as better at complex coding tasks compared to Anthropic's
  model"). All quotes in this note were instead sourced from a direct `curl`
  fetch of the raw HTML and hand-extracted from the article markup, then
  cross-checked character-for-character against that raw HTML.
- **Three linked pages fetched and confirmed directly**: the prompt-caching
  docs guide, the Programmatic Tool Calling docs guide, and the pelican-SVG
  cost-comparison results page all returned real, substantive HTML content
  via direct `curl` fetch (not JS-gated) and are quoted/tabulated above from
  that raw content, not from Willison's summary of them.
- **Two linked pages could NOT be independently verified**:
  - `developers.openai.com/api/docs/guides/tools-multi-agent` (the Multi-agent
    docs page Willison links) returned "Page not found" on direct fetch. Claim
    9 is sourced only from Willison's secondhand quote of OpenAI's
    description, not from the primary docs.
  - `openai.com/index/separating-signal-from-noise-coding-evaluations/` (the
    SWE-Bench Pro audit article behind Claim 6) returned a JavaScript-gated
    "Enable JavaScript and cookies to continue" page on direct fetch, and a
    403 Forbidden via WebFetch. Claim 6's quote is sourced only from
    Willison's blockquote of it, not independently re-verified against the
    original.
  - `openai.com/index/gpt-5-6/` (OpenAI's own GA announcement, linked at the
    top of the post) was not attempted directly given the above two OpenAI.com
    URLs both failed to load outside a browser; Claim 4's Agents' Last Exam
    blockquote is sourced from Willison's embedded quote of it, which is
    presented as a direct copy of OpenAI's own text.
  - The Anthropic docs page Willison links for "dynamic filtering" on the web
    search tool (platform.claude.com/docs/.../web-search-tool#dynamic-filtering)
    was not fetched — it's a passing comparison aside in Claim 8's source
    quote, not a claim in its own right, and no existing corpus note covers
    it, so no cross-reference could be made either way.
- **No contradiction issue filed**: see Cross-References → Contradicts above
  for the reasoning (benchmark-choice nuance, not a factual dispute between
  sources).
