---
source_url: https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
source_type: blog-post
title: "Better Models: Worse Tools"
author: Armin Ronacher
date_published: 2026-07-04
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: emerging
issue: "#1575"
---

# Better Models: Worse Tools

> Armin Ronacher documents a tool-calling regression specific to Opus 4.8 and Sonnet 5:
> the models emit syntactically-plausible-but-schema-invalid edit calls with invented
> trailing JSON keys against Pi's nested `edits[]` tool schema, a failure absent in
> every older Claude model tested. His hypothesis is that post-training on Claude
> Code's own forgiving, closed-source harness has made newer models strongly adapted
> to Claude Code's specific (and only partially documented) tool shape — making
> alternative, semantically-equivalent tool schemas increasingly off-distribution.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~1,350 words; six named
  sections: "Tool Calls Are Text", "The Failure", "Why It's Getting Worse", "The
  Slop Harness", "Strictness", "What This Means For Harnesses"; published 2026-07-04)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2, Click, and
  Sentry, and the author of the Pi coding agent (see `blog-ronacher-pi-oss.md`,
  `blog-ronacher-the-coming-loop.md`). His blog is a designated `trusted-feed` source
  in this repo. This post is a first-person investigation triggered by a bug report
  from another Pi contributor (Petr Baudis) in the public Pi issue tracker
  (github.com/earendil-works/pi/issues/6278), which Ronacher then investigated over
  "the last two days." The post is explicitly hypothesis-forming ("My strongest
  hypothesis is...", "I'm not *entirely sure* that this is how it works"), not a
  definitive root-cause disclosure — Anthropic has not confirmed the mechanism.
- **Scope**: Covers a specific tool-calling failure mode (invented trailing keys in
  a nested JSON array parameter) observed against Pi's edit tool schema on Opus 4.8
  and Sonnet 5; a mechanistic hypothesis involving ANTML serialization and
  grammar-constrained sampling; a training-artifact theory tied to RL on Claude
  Code's own harness; and a comparison against OpenAI's documented Harmony tool-call
  format. Does NOT cover: Anthropic's own account of the bug (no first-party
  confirmation exists), a fix or workaround recommendation from Ronacher himself
  (the post is diagnostic, not prescriptive), or the resolution status of the
  underlying Pi issue (open at time of extraction — see Extraction Notes for the
  post-publication continuation of the investigation).

## Extracted Claims

### Claim 1: Newer Claude models (Opus 4.8, Sonnet 5) call Pi's edit tool with extra, invented fields inside the nested `edits[]` array, a failure not observed in older Anthropic models

- **Evidence**: Direct first-hand investigation triggered by a Pi GitHub issue.
  Ronacher names the two affected models explicitly and contrasts them with "none
  of the older models."
- **Confidence**: emerging (reproduced by the author and corroborated independently
  by other Pi contributors in the linked issue thread; mechanism is hypothesized,
  not confirmed by Anthropic)
- **Quote**: "What surprised me is that this is getting worse with newer Anthropic
  models as both Opus 4.8 and Sonnet 5 show it but none of the older models. In
  other words, the SOTA models of the family are worse at this specific tool schema
  than their older siblings."
- **Our assessment**: This is a striking and counterintuitive claim — capability
  improvements coinciding with a *narrower* regression in schema fidelity for one
  specific tool shape. It is the load-bearing empirical claim of the whole post. The
  linked Pi issue thread (github.com/earendil-works/pi/issues/6278) provides
  substantially more quantified data than the blog post itself and is extracted in
  Claims 9–11 below; it both strengthens (via a controlled 50-trials-per-config
  replay experiment) and complicates (via later community-submitted production
  data showing non-zero rates on some older models too) this "clean regression"
  framing. See Claim 11 and Extraction Notes for the complication.

### Claim 2: The actual edit payload (`oldText`/`newText`) is byte-correct in the invalid calls; the only defect is nonsense appended after it

- **Evidence**: Direct inspection of failing tool calls by the author.
- **Confidence**: emerging (first-hand inspection; corroborated independently in the
  linked issue by multiple other investigators using different sessions and models)
- **Quote**: "The most annoying part is that the actual `oldText` and `newText`
  payloads were byte-correct in the invalid calls I inspected. The model had in fact
  produced the right invocation but then added nonsense at the end of the object."
- **Our assessment**: This rules out the simplest explanation (the model doesn't
  understand the edit operation) and points toward a narrower, more mechanical
  failure: something about *closing* the JSON object goes wrong, not something
  about composing the edit itself. This detail is what makes Ronacher's later
  entropy-at-closing-brace hypothesis (Claim 6) plausible rather than speculative.

### Claim 3: The failure is heavily context-dependent — a fresh single-turn "edit this file" prompt does not reproduce it, but an agentic multi-turn history (read files, diagnose, compose a multi-line edit) does, at up to ~20% of edit calls in one user's session

- **Evidence**: Direct experimentation contrasting prompt types; a specific
  external contributor's real session used to reproduce the bug reliably.
- **Confidence**: emerging (reproduced with a named external contributor's
  transcripts; rate is session-specific and the author notes inconsistency across
  transcripts)
- **Quote**: "A fresh single-turn prompt like 'edit this file' did not reproduce it
  at all for me. An agentic history where the model had read files, diagnosed a
  problem and then composed a multi-line edit could reproduce it. And more
  annoyingly, not all transcripts will show that behavior. In fact, I needed Petr
  Baudis's transcripts to reproduce this for me at all! In that user's session
  continuing the session caused Opus 4.8 to fail around 20% of the time."
- **Our assessment**: The context-dependence is the reason this bug is hard to
  detect via standard testing — it requires a realistic, lengthy agentic history to
  surface, not a synthetic unit test of the tool schema. This mirrors the
  "intersection bug" pattern in `blog-anthropic-claudecode-quality-postmortem.md`
  (Claim 9): a defect that only manifests under the combination of specific
  conditions (long context + multi-turn tool use + a particular tool schema), not
  in any single component tested in isolation.

### Claim 4: Stripping thinking blocks from session history roughly halves the failure rate; enabling Anthropic's `strict` tool-invocation mode eliminates it entirely in the author's runs

- **Evidence**: Direct ablation testing by the author on the reproducing session.
- **Confidence**: emerging (first-hand ablation results from one practitioner;
  numbers refined further in the linked issue thread — see Claim 10)
- **Quote**: "Stripping thinking blocks from history reduced the failure rate by
  half. Turning on strict tool invocation eliminated it in my runs."
- **Our assessment**: This is the single most actionable finding for harness
  engineers: `strict` mode (Anthropic's grammar-constrained tool-call sampling) is
  a practical mitigation available today, at the cost of the complexity limits
  Anthropic imposes on tool definitions in strict mode (Claim 5). Thinking-block
  volume as a contributing factor also connects this bug to a distinct class of
  context-management defects already in the corpus (see Cross-References).

### Claim 5: Claude Code's own client is deliberately permissive of malformed tool calls — it does not use `strict` mode, silently filters unknown keys, applies per-tool parameter aliases, and repairs broken Unicode escapes

- **Evidence**: Author's inspection of Claude Code's minified client code (described
  as "the minified code" available for inspection despite Claude Code being
  closed-source).
- **Confidence**: emerging (based on reverse-engineering a closed-source client;
  not confirmed by Anthropic, but the specific mechanisms named — alias list, escape
  repair — are concrete enough to be falsifiable)
- **Quote**: "It has explicit Unicode escape repair which fixes broken `\uXXXX`
  sequences and lone surrogates in string values. It also has per-tool aliases for
  parameters. For instance, `Edit` accepts `old_str` (presumably from the times when
  the models were trained on the officially documented text editor tool), the newer
  `old_string` from the schema, `new_str`/`new_string`, `path` as an alias for
  `file_path`, and some more."
- **Additional quote**: "It also silently filters out unexpected keys and it does
  not use `strict` mode either. The issue with `strict` mode is that Anthropic
  applies complexity limits to the tool definitions that cause API requests to
  fail, so presumably that's why Claude Code does not attempt to use it."
- **Our assessment**: This is the mechanism underlying the "training artifact"
  hypothesis (Claim 7): if the harness that shapes post-training reward is this
  forgiving, malformed-but-repairable tool calls incur no training penalty. The
  detail that Anthropic's own flagship client does not use its own `strict` mode
  feature — because strict mode's complexity limits break Claude Code's actual tool
  definitions — is a concrete, citable data point about a real tension between
  schema strictness and tool complexity in the current Anthropic API.

### Claim 6: The invented keys cluster at the highest-entropy point in the tool-call encoding — immediately after closing a long escaped multi-line string, where the model must decide between a closing brace and another field

- **Evidence**: Author's structural analysis of where in the generated JSON the
  spurious keys appear, combined with his account of how ANTML-style tool-call
  serialization likely encodes nested-array parameters (top-level string params are
  inlined; array-of-object params are serialized as literal JSON text inside one
  parameter tag).
- **Confidence**: anecdotal (explicitly hedged by the author: "While I'm not
  *entirely sure* that this is how it works, there are some indications that this
  is not too far off")
- **Quote**: "For a nested array parameter, that JSON includes escaped multi-line
  file content inside string literals, inside one tag. The unexpected, made-up keys
  appear exactly at the highest-entropy point of that task: after closing a
  several-hundred-token escaped `newText` string, where the model must decide `}`
  vs `, \"...\"`."
- **Our assessment**: This is the most technically specific — and most speculative
  — claim in the post. It is plausible and consistent with Claim 2 (payload itself
  is correct, only the closing sequence is wrong) but Ronacher himself flags it as
  uncertain, and it is contradicted in part by a later comment in the linked issue
  (Claim 12: renaming the `edits` parameter made no difference, and Claude Code's
  own `MultiEdit` tool also uses arrays without showing the bug, per mitsuhiko's
  comment of 2026-07-04 — "What I get least of all of this is that seemingly going
  by the strings in claude code is that it also has a `MultiEdit` tool. So the JSON
  explanation from tool calls for arrays does not fully explain it."). Treat this
  mechanistic claim as an unresolved hypothesis, not a settled explanation.

### Claim 7: The most likely explanation is a training artifact — newer models' post-training includes Claude Code or a harness resembling it, so slightly malformed tool calls that Claude Code's harness silently absorbs and repairs receive no training penalty, while alternative (semantically equivalent but differently-shaped) schemas become increasingly off-distribution

- **Evidence**: Author's synthesis connecting Claude Code's permissive client
  (Claim 5) to reinforcement learning dynamics, plus the observed generational
  trend (Opus 4.5 adapted well to other tool shapes; Opus 4.8 and Sonnet 5 do not).
- **Confidence**: anecdotal (explicitly labeled "my strongest hypothesis"; not
  confirmed by Anthropic; Ronacher has no visibility into Anthropic's actual RL
  environments)
- **Quote**: "If reinforcement learning happens in a harness like that, or a
  simulation of one, then slightly malformed tool calls can still complete the task
  and receive reward. The harness fully absorbs the error and there is little
  gradient against inventing an alias, adding a stray field or using a nearby
  parameter name."
- **Additional quote**: "Worse, the model may become very strongly adapted to the
  canonical Claude Code edit tool shape. A different harness can present a tool
  with the same semantic intent but a different schema. Such a tool can
  increasingly be off-distribution. The better-trained model might actually fight
  you harder because its prior is stronger."
- **Our assessment**: This is the central thesis of the post and the reason it
  matters for harness engineering: it reframes "the model should generalize to any
  well-specified schema" as an assumption that may no longer hold once a model's
  post-training is dominated by one specific, closed-source, and only
  partially-documented harness. The claim that "this ecology is not documented"
  and diverges from Anthropic's own published `text_editor_tool` API spec (Ronacher
  links platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool and
  states Claude Code "does not follow" that documented format) is a specific,
  checkable assertion about a documentation/implementation gap.

### Claim 8: Anthropic's `strict` mode functions similarly to OpenAI's Harmony format's in-band JSON-constraint marker — both make grammar-constrained sampling explicit — but Anthropic's version imposes complexity limits on tool definitions that Harmony's does not appear to

- **Evidence**: Comparative analysis against OpenAI's documented, open Harmony
  response format, including a concrete Harmony function-call example.
- **Confidence**: anecdotal (comparative technical analysis; Ronacher notes
  Anthropic's actual internal mechanism "is not known" and this is inference from
  observed effects)
- **Quote**: "The marker in harmony helps the sampler to detect when it needs to
  sample with a specific grammar, and because it is part of the transcript, it
  makes that rather easy to do... Anthropic appears different from that, though
  maybe not entirely."
- **Our assessment**: This comparison is valuable context for why the regression is
  Anthropic-specific: OpenAI's tool-calling format is openly documented (Harmony is
  public, with a public grammar spec via LARK for custom tools), giving practitioners
  visibility Anthropic's ANTML-based format does not provide. Ronacher separately
  reports (in the section "Strictness") that Codex models did not show this
  regression across all versions he tested except one he lacked access to (Codex
  5.6) — a useful negative result, though tested by one practitioner on one set of
  prompts, not systematically.

### Claim 9 (from the linked Pi issue thread — github.com/earendil-works/pi/issues/6278): Anthropic's own flagship `Edit` tool definition, captured via mitmproxy from a live Claude Code request, does not use `strict` mode and uses a flat `file_path`/`old_string`/`new_string`/`replace_all` schema

- **Evidence**: mitsuhiko (Ronacher) posted the literal JSON tool definition
  intercepted from Claude Code's own wire traffic in the Pi issue thread, as direct
  evidence for what Claude Code actually sends versus what Anthropic's public
  `text_editor_tool` docs describe.
- **Confidence**: settled (a raw captured API payload is about as close to
  ground truth as this investigation gets, though it reflects one point-in-time
  capture, not a documented guarantee)
- **Quote**: "I ran a claude code request through mitmproxy on my machine and it
  definitely does not use strict tool calling. Here is the tool definition for the
  edit tool in the request that it sent" — followed by the tool definition JSON
  (see Concrete Artifacts).
- **Our assessment**: This is the strongest piece of direct evidence in the entire
  investigation (blog post plus linked issue) because it is not an inference about
  training dynamics — it is literally what Claude Code sends over the wire. It
  directly substantiates Claim 5's assertion that Claude Code doesn't use strict
  mode, sourced from live traffic rather than static code inspection.

### Claim 10 (from the linked issue thread): A controlled 50-trials-per-configuration replay of a real user's frozen session context found a 20% failure rate on Opus 4.8, dropping to 8% with thinking blocks stripped and 0% with `strict` mode enabled; Sonnet 5 showed a ~7% failure rate under the same conditions, while Opus 4.5, Opus 4.6, Opus 4.7, Sonnet 4.5, and Haiku 4.5 showed no failures in any tested configuration

- **Evidence**: mitsuhiko's most rigorous experiment in the issue thread (posted
  2026-07-04, after the blog post's initial publication): a "minimal harness that
  resamples the assistant turn from @pasky's exported session (context frozen: same
  system prompt, tools, messages) against the live API, 50 trials per
  configuration with opus-4-8 primarily."
- **Confidence**: emerging (a controlled, repeated-trials experiment — stronger
  methodology than casual reproduction attempts — but confined to one frozen
  session context and primarily one model)
- **Quote**: "Basic failure rates on Opus 4.8: exact replay of the session has a
  fail rate of 20% / thinking blocks stripped from history drops it to 8% /
  `strict` on the edit tool makes it 0% of failures / minimal repro case averages
  around 7%." "Model specific failures: Opus 4.5, Opus 4.6, Opus 4.7, Sonnet 4.5
  and Haiku 4.5 do not show failures in no configuration / Sonnet 5 has a failure
  rate of roughly 7%." "Fascinatingly the failure is a clean regression: 0/250 on
  every model up to and including opus-4-7/sonnet-4-5, present on opus-4-8 and
  sonnet-5."
- **Our assessment**: This is the strongest quantified support for Claim 1's "clean
  regression" framing, and it is more rigorous than the number quoted in the blog
  post itself (which references informal early testing). It also adds a specific,
  actionable detail beyond the blog post: `additionalProperties` set to `true` or
  `false` on the schema has no effect on whether the model emits the extra keys
  ("just changes sdk side validaiton [sic]") — meaning schema laxness on the
  harness side does not reduce the underlying generation-time error, only its
  visibility. Also notable: the ~40 distinct invented key names observed
  (enumerated in Concrete Artifacts) are always trailing fields after `newText`
  with trivial values, and OAuth/subscription auth causes Pi to rename its tools to
  Claude-Code style on the wire (`edit` becomes `Edit`) — a detail the issue thread
  flags as still under investigation for whether it changes the failure rate.

### Claim 11 (from the linked issue thread, post-dating the blog post): Community-submitted production session data (posted 2026-07-05/06, after the blog's publication) shows non-zero extra/invented-property tool-call error rates on Sonnet 4.6 (~3.0–3.5%) and Opus 4.8 (~5.2–6.7%), complicating the blog's "clean regression" (zero on pre-4.8/5 models) framing

- **Evidence**: A Pi user (eyalroth) shared an analysis of 3,976 real production
  `edit` tool calls across their own sessions (both direct Anthropic API and Amazon
  Bedrock), broken down by model and error type, at mitsuhiko's request to classify
  errors by model.
- **Confidence**: anecdotal (self-reported, LLM-assisted classification of one
  user's session logs across two API providers — not independently audited, and
  posted after the blog article was written)
- **Quote**: "Extra/invented properties vs. missing required property, by model" —
  "claude-opus-4-8 | 1451 | 75 | 5.17%" / "claude-sonnet-5 | 537 | 19 | 3.54%" /
  "claude-sonnet-4-6 | 2034 | 61 | 3.00%" / "claude-haiku-4-5 | 24 | 0 | 0%" (from
  eyalroth's comment of 2026-07-06).
- **Our assessment**: This is the most important nuance the blog post itself does
  not capture, because the data postdates publication — the investigation
  continued in the issue thread after Ronacher wrote the article. Two production
  datasets (from `pasky` and `eyalroth`, using both direct Anthropic API and
  Bedrock) show measurable extra/invented-key rates on Sonnet 4.6, a model
  mitsuhiko's own controlled 50-trial replay (Claim 10) found zero failures on. This
  does not necessarily contradict Claim 10 — different sessions, prompts, and
  possibly routing/provider paths could produce different rates, and mitsuhiko's
  test used one frozen session context while the production data spans many
  organic ones — but it means the "clean regression, zero before Opus 4.8/Sonnet
  5" claim should be treated as provisional rather than settled. No contradiction
  issue is filed for this: it is the same ongoing investigation surfacing
  additional, messier data after the blog post's snapshot, not two established
  corpus sources disagreeing (see Extraction Notes).

### Claim 12 (from the linked issue thread): Renaming the `edits` array parameter to something other than "edits" made no measurable difference to the failure rate, weakening a proposed "conceptual overload of the word 'edit'" hypothesis

- **Evidence**: A community member (robinwander) hypothesized that the term "edit"
  being overloaded across the tool name, the array name, and prose descriptions
  might confuse the model; mitsuhiko tested the specific proposed fix.
- **Confidence**: anecdotal (single practitioner's negative test result on one
  proposed hypothesis)
- **Quote**: "what if you call the parameter something besides `edits`?" (robinwander,
  2026-07-04) — "Does not seem to make any difference." (mitsuhiko, 2026-07-04)
- **Our assessment**: This is a useful negative result: it rules out a
  simple naming/terminology fix and is consistent with Ronacher's own hedged
  entropy-at-closing-brace hypothesis (Claim 6) rather than a naming-confusion
  theory. It also reinforces that this bug resists the kind of quick harness-side
  patches teams might first reach for (renaming fields, loosening
  `additionalProperties`) — see Claim 10's related finding that
  `additionalProperties` toggling doesn't change generation-time behavior either.

## Concrete Artifacts

### The malformed tool-call pattern (blog post, "The Failure" section)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/

Intended payload:
{
  "path": "some/file.py",
  "edits": [
    {
      "oldText": "text to replace",
      "newText": "replacement text"
    }
  ]
}

Observed failing variants:
{
  "oldText": "...",
  "newText": "...",
  "requireUnique": true
}

{
  "oldText": "...",
  "newText": "...",
  "oldText2": "",
  "newText2": ""
}

Full observed zoo of invented trailing keys (blog post):
type, id, kind, unique, requireUnique, matchCase, in_file,
forceMatchCount, children, notes, cost, oldText2, newText2,
oldText_2, newText_2, and an "event.0.additionalProperties" key
inside the edit object itself.
```

### Claude Code's actual `Edit` tool schema, captured via mitmproxy (Pi issue #6278, mitsuhiko comment, 2026-07-03)

```
Source: github.com/earendil-works/pi/issues/6278 (comment by mitsuhiko)
Captured from a live Claude Code request via mitmproxy -- NOT from
Anthropic's public text_editor_tool documentation.

{
  "name": "Edit",
  "description": "Performs exact string replacement in a file.\n\n- You must Read the file in this conversation before editing, or the call will fail.\n- `old_string` must match the file exactly, including indentation, and be unique -- the edit fails otherwise. Strip the Read line prefix (line number + tab) before matching.\n- `replace_all: true` replaces every occurrence instead.",
  "input_schema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
      "file_path": {
        "description": "The absolute path to the file to modify",
        "type": "string"
      },
      "old_string": {
        "description": "The text to replace",
        "type": "string"
      },
      "new_string": { "description": "(truncated in source comment)" }
    }
  }
}

Note: strict mode is not enabled on this tool definition -- no
"strict": true field and no "additionalProperties": false constraint
at the top level of input_schema.
```

### Model-by-model failure rate summary (from the linked Pi issue thread, two independent datasets)

```
Source: github.com/earendil-works/pi/issues/6278

Dataset A -- mitsuhiko's controlled 50-trials-per-config replay
(one frozen session context, primarily opus-4-8):
  opus-4-5, opus-4-6, opus-4-7, sonnet-4-5, haiku-4-5:  0% (no config)
  opus-4-8, exact replay:                                20%
  opus-4-8, thinking blocks stripped:                     8%
  opus-4-8, strict mode on:                               0%
  opus-4-8, minimal repro case average:                   ~7%
  sonnet-5:                                               ~7%

Dataset B -- eyalroth's production session analysis, 3,976 edit
calls total, "extra/invented properties" error subclass only:
  claude-opus-4-8    (n=1451):  5.17%
  claude-sonnet-5    (n=537):   3.54%
  claude-sonnet-4-6  (n=2034):  3.00%
  claude-haiku-4-5   (n=24):    0%

Note: Dataset B postdates the blog post and shows non-zero rates on
sonnet-4-6, which Dataset A found 0/250 on. See Claim 11.
```

## Cross-References

- **Extends**: `blog-ronacher-pi-oss.md` and `blog-ronacher-the-coming-loop.md` —
  both prior Ronacher posts extracted in this corpus. This post is a narrower,
  more technical investigation than either: where `the-coming-loop.md` (Claims 3-5)
  documents newer models producing more *defensive, over-complex code*, this post
  documents a distinct failure category — schema-invalid *tool calls* — in the same
  generational window (Opus 4.8, Sonnet 5). The two failure modes are not the same
  mechanism (code-quality drift vs. tool-schema drift) but both are attributed by
  Ronacher to the same underlying cause category: training/RL dynamics specific to
  recent post-training, not a capability regression.

- **Extends**: `blog-anthropic-claudecode-quality-postmortem.md` Claim 9 (the
  "intersection bug" framing — "at the intersection of Claude Code's context
  management, the Anthropic API, and extended thinking"). This source's Claim 3
  documents a structurally similar intersection: the tool-schema failure only
  surfaces at the intersection of (a) a specific non-Claude-Code tool schema shape,
  (b) long agentic multi-turn history, and (c) the presence of thinking blocks.
  Neither bug is detectable by testing any one of those conditions in isolation.
  Unlike the postmortem (a first-party Anthropic account with a confirmed root
  cause and shipped fix), this source's root cause remains an outsider's hypothesis,
  unconfirmed by Anthropic.

- **Corroborates**: `docs-github-copilot-sonnet5-ga.md` and other corpus notes
  establish Opus 4.8 and Sonnet 5 as the current frontier model generation as of
  late June/July 2026 — consistent with the generational window this source
  identifies as when the regression appears.

- **Contradicts**: No existing corpus source note makes a claim that directly
  opposes this post's core finding. The closest tension is internal to this
  source's own underlying evidence base rather than between two corpus notes:
  Claim 10 (a controlled experiment finding zero tool-schema failures on
  Sonnet 4.6) is in tension with Claim 11 (production data showing ~3% extra-key
  error rates on Sonnet 4.6, submitted to the same GitHub issue thread one to two
  days after the blog post's publication). Per MINER.md guidance, this is not filed
  as a contradiction issue: both claims originate from the same ongoing
  investigation (the linked Pi issue), not from two independent, settled corpus
  sources, and the discrepancy is plausibly explained by differing test conditions
  (one frozen synthetic session vs. many organic production sessions) rather than a
  genuine factual disagreement about the same measurement. Flagged here so the
  Assayer and Smith are aware of the internal tension before citing either number
  as a precise rate.

- **Novel**:
  - **Tool schema shape as a training-distribution variable, not a neutral
    contract**: No existing corpus source frames tool schema design as something
    that can be "in-distribution" or "off-distribution" relative to a model's
    post-training, with direct consequences for tool-call reliability. This is the
    first source in the corpus to argue that alternative tool schemas may be
    actively fought by newer models regardless of how well-specified they are.
  - **A specific, named tool-calling regression tied to specific model versions**:
    No prior corpus source documents a concrete tool-calling defect (invented
    trailing JSON keys) isolated to Opus 4.8 and Sonnet 5 specifically, with
    quantified failure rates and a working mitigation (`strict` mode).
  - **Claude Code's internal tool schema and its divergence from Anthropic's
    published `text_editor_tool` docs**: No prior corpus source discloses the
    actual flat `file_path`/`old_string`/`new_string`/`replace_all` schema Claude
    Code sends over the wire (captured via mitmproxy) or notes that it diverges
    from Anthropic's own public tool-use documentation.
  - **A concrete comparison of Anthropic's `strict` mode against OpenAI's open
    Harmony format**: No prior corpus source compares the two providers'
    grammar-constrained tool-calling mechanisms, or notes that Anthropic's strict
    mode imposes tool-definition complexity limits that (per this source) prevent
    Claude Code itself from using it.

## Guide Impact

- **Chapter 02 (Harness Engineering — Tool Schema Design)**: This is a significant,
  actionable addition. Currently the guide (per `blog-ronacher-pi-oss.md` and
  related notes) treats tool schemas mostly as a design/documentation problem for
  humans. This source provides evidence that tool schema *shape* itself has become
  a model-performance variable on Anthropic models: schemas that are close to
  Claude Code's own flat, forgiving conventions are more reliably called than
  semantically-equivalent alternative shapes (particularly nested arrays of
  objects). Recommend adding: (1) a note that harness engineers building custom
  tool schemas for Claude models should prefer flat parameter structures over
  nested array-of-object parameters where possible, given the current evidence of
  degraded reliability for the latter shape on Opus 4.8/Sonnet 5; (2) `strict` mode
  as a concrete, currently-available mitigation, with the caveat that it imposes
  complexity limits on tool definitions (per Claim 5) — this is a real trade-off,
  not a free fix.

- **Chapter 03 (Verification)**: Add this bug as an example of a defect standard
  testing will miss: it requires realistic agentic multi-turn history with
  thinking blocks to surface (Claim 3), meaning short synthetic tool-call tests
  will pass while production sessions fail at up to 20%. This reinforces the
  guide's existing intersection-bug framing from
  `blog-anthropic-claudecode-quality-postmortem.md` — teams building custom
  harnesses around non-Claude-Code tool schemas should specifically test with long,
  realistic agentic transcripts, not just fresh single-turn prompts.

- **Chapter 00 (Principles)**: The core thesis — that tool schemas are not a
  neutral, model-agnostic contract but instead sit somewhere on a spectrum of
  training-distribution closeness to one dominant harness — is worth stating as an
  explicit principle: "assume nothing about how well a model will generalize to a
  tool schema shape it wasn't trained against, and verify empirically for schemas
  that diverge structurally (e.g., nested arrays) from Claude Code's own tool
  conventions."

## Extraction Notes

- Full blog post text fetched via direct HTTP request to
  https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/ and read from the
  raw HTML (not summarized by an intermediate model). All blog-post quotes were
  verified character-for-character against the fetched HTML (with HTML entities
  such as `&#8217;` and `&#8220;`/`&#8221;` resolved to their plain-text
  equivalents, and `&amp;` to `&`).
- Per MINER.md's guidance to follow substantive linked pages, the post's primary
  link — the underlying Pi issue at github.com/earendil-works/pi/issues/6278 — was
  fetched in full via `gh issue view` (21 comments, spanning 2026-07-03 through
  2026-07-06). This issue is not a peripheral link; it is the actual investigation
  the blog post narrates and summarizes, and it contains substantially more
  quantified data (Claims 9-12) than the blog post itself, including data posted
  *after* the blog post's publication date that complicates its "clean regression"
  framing (Claim 11). All issue-thread quotes were verified character-for-character
  against the `gh issue view --json comments` output.
  Other links in the post (the Anthropic `text_editor_tool` docs page, the OpenAI
  `harmony` and `gpt-oss` GitHub repos, the LARK grammar docs) are documentation
  references supporting Claim 8's comparison; they were not independently fetched
  since the post's own description of them is what's being extracted here, not an
  independent claim about their contents.
- One PR was opened against Pi during the investigation
  (`legacy7838-create`, comment 2026-07-03) proposing to silently strip unrecognized
  keys client-side; mitsuhiko explicitly asked the contributor not to open such a
  PR ("we need data" before "making random changes") and it was not extracted as a
  claim since it was explicitly rejected as premature by the maintainer, not
  adopted as a mitigation.
- The investigation was still open and ongoing at time of extraction (issue
  #6278 unresolved, latest comment 2026-07-06, same day as this extraction). The
  `status: current` / `confidence_overall: emerging` ratings reflect that this is
  an active, unresolved investigation rather than a settled finding — the Assayer
  and Smith should treat specific failure-rate numbers as provisional and subject
  to revision as the issue thread continues.
- No contradiction issue filed against another corpus source note (see
  Cross-References "Contradicts" for the internal tension between Claim 10 and
  Claim 11, which is flagged but not filed as a formal contradiction per MINER.md's
  guidance, since it is one ongoing investigation's data evolving over time rather
  than two settled, independent sources disagreeing).
