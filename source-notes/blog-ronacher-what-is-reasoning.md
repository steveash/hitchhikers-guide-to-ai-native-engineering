---
source_url: https://lucumr.pocoo.org/2026/8/19/what-is-reasoning/
source_type: blog-post
title: "What Is Reasoning"
author: Armin Ronacher
date_published: 2026-08-19
date_extracted: 2026-08-20
last_checked: 2026-08-20
status: current
confidence_overall: emerging
issue: "#2807"
---

# What Is Reasoning

> Armin Ronacher explains reasoning traces as ordinary generated text routed
> into a separate channel by trained convention rather than by hard
> architectural boundary: reasoning effort is baked into the system prompt
> (not a sampling parameter), the analysis/final channel split is a learned
> behavior that can be tricked into leaking, and different model families
> (GPT-OSS vs. DeepSeek's DwarfStar) implement the enable/disable mechanism
> differently — with concrete implications for KV cache invalidation and
> prompt-injection-style reasoning leakage.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; short technical explainer,
  ~600 words; published 2026-08-19)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2, Click,
  Sentry, and the Pi coding agent (Earendil). His blog is a designated
  `trusted-feed` source in this repo (see `blog-ronacher-pi-oss.md`,
  `blog-ronacher-the-coming-loop.md`, and others already in the corpus). This
  post is a first-person technical investigation prompted by "a paper was
  shared" (an arXiv preprint on extracting reasoning traces from closed-weight
  APIs, https://arxiv.org/html/2608.09867v1) and by "online discussions about
  tricking models into leaking them." Ronacher states his motive explicitly:
  "Twitter seems full of half-truths and confusion about how this works, so
  perhaps this helps some to understand what is happening." He is a
  practitioner explaining publicly documented model behavior (GPT-OSS's Harmony
  format, DeepSeek's DwarfStar system-prompt scaffolding) rather than reporting
  novel first-party research; the credibility rests on his direct familiarity
  with agent-harness internals (he ships a coding agent, Pi, that has to
  interoperate with these reasoning-control mechanisms) plus the fact that the
  code artifacts he cites (Harmony channel tokens, DwarfStar system prompt
  text) are independently checkable against the linked GitHub repos.
- **Scope**: Covers three things narrowly: (1) what a reasoning trace
  mechanically is (routed scratchpad text, illustrated with GPT-OSS's Harmony
  format), (2) how "reasoning effort" is controlled (system-prompt text, not a
  sampling parameter, illustrated with GPT-OSS and DeepSeek's DwarfStar), and
  (3) how thinking is enabled/disabled per model family and how that
  mechanism can be tricked into leaking reasoning tokens. Does NOT cover:
  training methodology for how models learn the channel convention, the
  extraction attack from the linked arXiv paper in technical detail (Ronacher
  references it as motivation but does not walk through its method), benchmark
  or quality data on reasoning effort levels, or non-GPT-OSS/non-DeepSeek model
  families (e.g., no direct claims about Claude's or Gemini's thinking
  implementation, beyond what other corpus notes already establish).

## Extracted Claims

### Claim 1: Reasoning traces are not an architecturally special mechanism — they are ordinary generated text that the model is trained to emit into a scratchpad before its final answer

- **Evidence**: Direct assertion, illustrated in the next claim by GPT-OSS's
  Harmony format code example.
- **Confidence**: settled (consistent with publicly documented GPT-OSS/Harmony
  behavior; not a contested claim)
- **Quote**: "The industry has done a good job at making reasoning traces sound
  special and exotic, but they really are just text: the model is trained to
  emit its thinking into a scratchpad as part of its response, before its
  final answer."
- **Our assessment**: This is the framing claim for the whole post and is
  well-supported by the concrete Harmony example that follows. It is a useful
  corrective for practitioners who treat "reasoning" as a categorically
  different kind of model output (e.g., assuming it cannot be prompt-injected
  or manipulated the same way visible text can) — Claim 8 below shows that
  assumption is specifically wrong.

### Claim 2: GPT-OSS's Harmony response format makes the channel-based separation of reasoning from final output explicit via special tokens

- **Evidence**: Verbatim code example from the post showing the token sequence.
- **Confidence**: settled (Harmony is GPT-OSS's documented, publicly released
  response format; the token sequence is directly reproduced from the source)
- **Quote**: (see Concrete Artifacts — GPT-OSS Harmony channel example)
- **Our assessment**: This is the clearest piece of primary evidence in the
  post. Because GPT-OSS is open-weight, the channel markers are directly
  observable rather than inferred — this is why Ronacher singles it out ("Open-weight
  models thankfully reveal them"). It grounds the more speculative closed-model
  claim (Claim 4) by showing what the underlying mechanism looks like when it
  isn't hidden.

### Claim 3: When the model samples the `analysis` channel token, a parser routes the following text into a separate stream exposed through the Responses API

- **Evidence**: Direct mechanistic description following the Harmony code
  example.
- **Confidence**: emerging (plausible and consistent with how the Harmony
  format is documented to work, but Ronacher does not cite Harmony's own spec
  or OpenAI documentation directly in this post — the claim rests on his
  authority as a practitioner rather than a cited primary source)
- **Quote**: "When the model samples the `analysis` channel token, a parser
  routes the following text into a separate stream exposed through the
  Responses API."
- **Our assessment**: This is the load-bearing mechanistic claim: it explains
  reasoning-trace separation as a post-hoc parsing decision by the inference
  stack (token-triggered stream routing), not a distinct generation mode inside
  the model. That framing directly supports Claim 8's leak-vector argument —
  if separation is just "which stream a parser routes text into based on a
  token it already saw," then getting the parser to misroute is a plausible
  attack surface, not a hypothetical one.

### Claim 4: For closed-weight models, reasoning traces are presumably redacted and summarized by a secondary, simpler model before being shown to the user

- **Evidence**: Speculative inference by the author, not a cited primary
  source — explicitly hedged.
- **Confidence**: anecdotal (author's own word: "presumably")
- **Quote**: "For closed models, presumably a simple model redacts and
  summarizes it."
- **Our assessment**: This is the weakest claim in the post — Ronacher flags
  his own uncertainty with "presumably," and no evidence is offered. We should
  treat this as an informed guess rather than a documented fact. It is
  plausible (matches how OpenAI and Anthropic describe showing "abridged" or
  "summarized" reasoning for some models) but should not be cited in the guide
  without an independent, more authoritative source.

### Claim 5: Reasoning effort is not a property of the sampling process — it is baked into the system prompt as trained behavior, not exposed as a token-budget parameter

- **Evidence**: Direct claim, illustrated with GPT-OSS's literal system-prompt
  directive.
- **Confidence**: emerging (true for the two model families demonstrated —
  GPT-OSS and DeepSeek's DwarfStar — via concrete system-prompt text; framed
  by the author as a general statement about "reasoning effort," which is a
  broader claim than the two examples fully establish)
- **Quote**: "Earlier APIs exposed reasoning token budgets, making it seem like
  a property of the sampling process. In reality, reasoning effort is baked
  into the system prompt."
- **Our assessment**: This should be read as "system-prompt-text is *a*
  mechanism providers use to implement reasoning effort," not "reasoning
  effort is *never* a true sampling-level parameter for any provider." Some
  APIs (e.g., a fixed `thinking_budget`/`budget_tokens` integer parameter, as
  documented for Claude Opus 4.6 in `blog-anthropic-opus47-best-practices.md`
  Claim 5) genuinely are numeric sampling-time controls at the API surface,
  even if the underlying model behavior is still shaped by trained
  conventions. Notably, Anthropic's own move away from that fixed-budget
  parameter toward adaptive, prompt-steered thinking in Opus 4.7 (same note,
  Claims 6–8) is independent corroboration of Ronacher's broader point: the
  industry trend is toward prompt-based effort control replacing numeric
  budget parameters, even where numeric parameters existed before. This is a
  conditioning-variable nuance (which providers, which API generation), not a
  contradiction — no contradiction issue filed.

### Claim 6: Changing reasoning effort invalidates the KV cache, because the system-prompt text itself changes

- **Evidence**: Direct causal claim following from Claim 5's system-prompt
  mechanism.
- **Confidence**: emerging (logically follows from Claim 5 — if effort is
  encoded as literal system-prompt text, changing it changes the cached prefix
  — but Ronacher does not independently verify this with a measurement; it is
  presented as an explanatory inference)
- **Quote**: "This also explains why changing the effort invalidates the KV
  cache."
- **Our assessment**: This is a genuinely new, specific, and actionable
  mechanism for the corpus. The guide (`04-context-engineering.md`) already
  documents that compaction destroys the KV cache
  (`research-wasnotwas-context-compaction.md`) — this claim adds a second,
  independent trigger for cache invalidation that harness engineers should
  account for: switching a session's reasoning-effort level mid-conversation
  (e.g., escalating from "low" to "high" reasoning for a hard step) pays the
  same full-prefix re-read cost as a compaction event, because the effort
  directive lives in the same cached system-prompt region. Teams building
  effort-escalation logic ("try cheap first, escalate if it fails") should
  budget for this cache miss explicitly.

### Claim 7: DeepSeek's DwarfStar implementation encodes maximum reasoning effort as an elaborate, multi-sentence system-prompt directive, not a simple keyword

- **Evidence**: Verbatim system-prompt text from the DwarfStar project
  (https://github.com/antirez/ds4), reproduced in the post.
- **Confidence**: settled (directly reproduced from a linked, publicly
  inspectable open-source repository)
- **Quote**: "Reasoning Effort: Absolute maximum with no shortcuts permitted.
  You MUST be very thorough in your thinking and comprehensively decompose the
  problem to resolve the root cause, rigorously stress-testing your logic
  against all potential paths, edge cases, and adversarial scenarios."
- **Our assessment**: This is a striking contrast with GPT-OSS's terse
  `Reasoning: low` directive (Concrete Artifacts). It shows that "reasoning
  effort" is not a standardized string across providers — DwarfStar's authors
  found that a long, imperative, almost coaching-style instruction produces
  the desired maximum-effort behavior from DeepSeek, while GPT-OSS's training
  apparently makes a two-word directive sufficient. This is directly useful
  prompt-engineering evidence: verbosity and imperative framing in a
  reasoning-effort directive appears to be provider/model-specific tuning, not
  a universal requirement.

### Claim 8: The routing of reasoning tokens into the hidden scratchpad channel (vs. the visible final channel) is a learned convention, not a hard boundary — models can be tricked into leaking reasoning tokens by making them believe they are in the final channel

- **Evidence**: Direct claim plus a concrete historical example (bash-tool
  echo trick).
- **Confidence**: emerging (the underlying mechanism claim is plausible and
  consistent with Claim 3's parser-routing model; the specific bash/dev-null
  example is asserted as an observed phenomenon, "we have even seen," without
  a citation to a specific incident or reproduction)
- **Quote**: "The destination of reasoning tokens is therefore a learned
  convention: the model is trained to keep scratch work out of the `final`
  channel. Trick it into thinking it is in that channel and it may leak
  tokens. We have even seen older models, when thinking is disabled, reason
  into the bash tool and echo their thoughts to `/dev/null`."
- **Our assessment**: This is the security-relevant core of the post. It
  directly corroborates the mechanism behind `blog-simonwillison-prompt-injection-role-confusion.md`
  Claim 2 ("CoT Forgery" — crafting text that mimics chain-of-thought format
  raises attack success rates from near-zero to ~60% and generalizes across
  every tested LLM) and Claim 7 (models identify their own role/channel by
  text *style*, not by a structurally enforced tag). Ronacher's framing
  ("trick it into thinking it is in that channel") and Willison's framing
  ("attacker-controlled text formatted like internal reasoning is perceived as
  internal reasoning by the model") describe the same underlying failure mode
  from two different angles — one about reasoning-trace leakage, one about
  prompt-injection role confusion. Together they establish that channel/role
  boundaries in current LLMs are a soft, learned convention exploitable by
  format-mimicry, not an enforced architectural wall. This has direct
  Ch06 (security threat model) implications: reasoning-trace visibility
  settings should not be treated as a hard confidentiality boundary for
  secrets or sensitive scratch-work.

### Claim 9: Model families disable "thinking" through different mechanisms — DeepSeek's DwarfStar uses token prefilling (`</think>` to disable, `<think>` to enable), while GPT-OSS does not prefill and lets the model decide on its own

- **Evidence**: Direct comparative claim, citing the DwarfStar repository by
  name for the prefill behavior.
- **Confidence**: settled for the DwarfStar half (directly attributable to a
  named, linked open-source project) / emerging for the GPT-OSS half (asserted
  without a specific citation, but consistent with GPT-OSS's known behavior of
  making reasoning effort adjustable via the `Reasoning: <level>` system-prompt
  directive rather than a hard prefill)
- **Quote**: "In DwarfStar, disabled thinking uses the prefill `</think>`,
  while enabled thinking uses `<think>`, which are the tokens that close and
  start thinking. GPT-OSS doesn't prefill but lets the model decide either way
  on its own."
- **Our assessment**: This is a concrete, checkable implementation detail
  (DwarfStar's source is public) that shows disabling thinking is not a
  single, standardized operation across the industry — some inference stacks
  force it mechanically (prefilling the closing token so the model literally
  cannot sample the opening token), while others rely on the model's trained
  disposition. This distinction matters directly for Claim 10's security
  implication: a model that "decides" whether to think (GPT-OSS) has more
  behavioral surface area to manipulate than one that is mechanically
  prevented from starting a thinking block.

### Claim 10: A custom "think" tool can trick a model into placing reasoning where it should not go, but only when the model's native reasoning is disabled

- **Evidence**: Reference to a specific, linked code artifact — a
  browser-inspectable gist implementing a "think" tool extension for the Pi
  coding agent (https://gist.github.com/mitsuhiko/0904a3d89741e8e3bcca1ca93ea076de)
  — plus a causal explanation for why the trick works.
- **Confidence**: emerging (the causal mechanism is offered as a hypothesis —
  "But presumably... This may explain why" — not confirmed as fact; the
  existence and mechanics of the linked `think` tool extension itself are
  directly verifiable)
- **Quote**: "But presumably, some inference APIs prefill the opening token
  when reasoning is enabled, so the model never samples it itself and might
  prevent the sampling of the reasoning token when disabled since it can be
  trivially detected. This may explain why a custom think tool can trick
  models into putting some reasoning where it should not go — but only when
  native reasoning is disabled."
- **Our assessment**: This is the most concrete, guide-actionable claim in the
  post because it is backed by an inspectable artifact. The linked gist
  (Ronacher's own Pi coding agent extension) implements exactly this pattern:
  when native provider reasoning is disabled and a `think` tool is registered
  in the active toolset, the extension forces `tool_choice` to the `think`
  tool on the first turn of an agent run (see Concrete Artifacts below,
  `forceThinkToolChoice` / `before_agent_start` handler) — giving the model an
  explicit, sanctioned scratchpad to reason into via a tool call instead of
  the (blocked) native reasoning channel. This is a defensive/legitimate use
  of the same underlying vulnerability class Claim 8 describes: because models
  have a trained disposition to externalize reasoning somewhere, if you deny
  them the native channel they will find another one (a tool call) — and a
  harness can either exploit that constructively (this gist, to preserve
  reasoning quality when native thinking is off) or an attacker could exploit
  it adversarially (to smuggle reasoning content past a filter that only
  inspects the final-channel output).

### Claim 11: This blog post itself triggered safety filters in GPT-5.6 Terra, forcing the author to switch to Kimi for spell-checking

- **Evidence**: First-person anecdote, included by the author as a closing
  aside with a screenshot.
- **Confidence**: anecdotal (single, unreplicated incident, self-reported)
- **Quote**: "Hilariously enough I was unable to use GPT 5.6 terra for spell
  and grammar checking on this blog post because of safety filters. Had to
  switch to Kimi."
- **Our assessment**: Low evidentiary weight on its own, but a useful data
  point for the guide's existing discussion of overzealous safety filtering
  as a practitioner friction point: an article *about* reasoning-trace
  mechanics and leak vectors was apparently flagged as unsafe content by
  GPT-5.6 Terra's own safety layer, illustrating that safety classifiers can
  false-positive on security-research-adjacent writing about the model's own
  internals — a self-referential edge case worth a passing mention if the
  guide discusses safety-filter false positives.

## Concrete Artifacts

### GPT-OSS Harmony response format — channel markers

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/8/19/what-is-reasoning/ (2026-08-19)

<|channel|>analysis<|message|>
I need to work this out ...
<|end|><|start|>assistant<|channel|>final<|message|>
The answer is ...
<|return|>
```

### GPT-OSS reasoning-effort system-prompt directive

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/8/19/what-is-reasoning/ (2026-08-19)

Reasoning: low
```

### DwarfStar (DeepSeek) max-reasoning system-prompt directive

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/8/19/what-is-reasoning/ (2026-08-19)
Attributed to: https://github.com/antirez/ds4

Reasoning Effort: Absolute maximum with no shortcuts permitted.
You MUST be very thorough in your thinking and comprehensively decompose the
problem to resolve the root cause, rigorously stress-testing your logic against
all potential paths, edge cases, and adversarial scenarios.
```

### Pi coding agent "think" tool extension — forcing a scratchpad when native reasoning is disabled

```
Source: mitsuhiko (Armin Ronacher), linked from the blog post as evidence for
Claim 10. Gist: https://gist.github.com/mitsuhiko/0904a3d89741e8e3bcca1ca93ea076de
(TypeScript, Pi extension API — @earendil-works/pi-coding-agent)

Key excerpts (reproduced verbatim from the gist):

  const THINK_TOOL_NAME = "think";

  const THINK_GUIDELINES = [
    "Use think as your scratchpad: it is where your reasoning happens, and its content is private rather than part of the answer.",
    "Call think before the first action of a turn, and again before any step that is expensive to undo: an edit, a destructive command, or a final answer.",
    ...
  ];

  function forceThinkToolChoice(payload: Payload): Payload {
    // Do not replace an explicit directive from the user or another extension.
    // Codex emits `auto` by default, so that value is safe to replace.
    if (payload.tool_choice !== undefined && payload.tool_choice !== "auto")
      return payload;

    return {
      ...payload,
      tool_choice: { type: "function", name: THINK_TOOL_NAME },
    };
  }

  function disableProviderReasoning(
    payload: unknown,
    model: ReasoningModel | undefined,
  ): unknown {
    // ... strips/disables native provider reasoning fields across API shapes:
    // OpenAI Responses `reasoning`/`reasoning_effort`, Anthropic/DeepSeek/Z.AI
    // `thinking`, Google `thinkingConfig`, Bedrock `additionalModelRequestFields`, etc.
  }

  // Arm one eager scratchpad call for each user-initiated agent run.
  pi.on("before_agent_start", (_event, ctx) => {
    forceThinkOnNextResponsesRequest =
      pi.getActiveTools().includes(THINK_TOOL_NAME) &&
      isResponsesModel(ctx.model);
  });

Behavior: when native provider reasoning is disabled for a model AND a
`think` tool is registered, the extension forces the model's very first tool
call of an agent run to be `think`, giving it an explicit private scratchpad
tool instead of the (blocked) native reasoning channel.
```

### Linked motivating research (not independently verified — see Extraction Notes)

```
Paper referenced by Ronacher as the trigger for this post:
https://arxiv.org/html/2608.09867v1 ("a paper was shared that showed how to
extract reasoning traces from closed-weight models")

Per a WebFetch summary (not independently confirmed against the paper's own
text by the Miner — see Extraction Notes): the paper reportedly demonstrates
that encrypted reasoning blocks from closed-weight provider APIs
(Anthropic/OpenAI/Google) are portable across sessions/users/models within a
provider's ecosystem, and that injecting a stronger model's encrypted
reasoning block into a weaker, less-restricted model from the same provider
can be used to have the weaker model decode and transcribe it in plaintext.
The summary reports recovery of PII and credentials from reasoning blocks
found in public repositories. This is NOT a claim of Ronacher's post itself —
it is background motivation he cites — and its specifics should be treated as
unverified until a Miner reads the paper directly (see Extraction Notes).
```

## Cross-References

- **Extends**: `docs-github-copilot-1m-context-reasoning-levels.md` (Claims 2,
  3, 4). That note documents GitHub Copilot's user-facing "configurable
  reasoning levels" and "extended thinking" as a product feature ("dial in the
  right balance of speed and depth") but explicitly notes it could not
  determine "how 'extended thinking' differs technically from 'higher
  reasoning' settings" and that "the specific level options (names, count, or
  increments)" were never enumerated by GitHub. This source fills exactly that
  gap at the mechanism level: reasoning levels/effort are (at least for
  GPT-OSS and DeepSeek's DwarfStar) implemented as system-prompt text the
  model was trained to respond to, not a black-box sampling knob — and
  changing that level has a concrete side effect (KV cache invalidation,
  Claim 6) that the Copilot note could not have surfaced from a product
  changelog.

- **Corroborates**: `blog-anthropic-opus47-best-practices.md` (Claims 5, 6, 7,
  8). That note documents Anthropic's Opus 4.6 → 4.7 migration: a fixed,
  numeric `thinking_budget` parameter ("Extended Thinking with a fixed
  thinking budget is not supported in Opus 4.7") was replaced by adaptive
  thinking steered via prompt text ("Think carefully and step-by-step before
  responding; this problem is harder than it looks."). This is independent,
  first-party corroboration of this source's Claim 5 (reasoning effort control
  trending toward system/user-prompt text rather than numeric sampling
  parameters) from a different provider and a different mechanism (adaptive
  per-step allocation vs. GPT-OSS/DwarfStar's static system-prompt directive).
  See Claim 5's "Our assessment" for the nuance: Opus 4.6's old parameter *was*
  a genuine sampling-level control, so the corroboration is about the
  direction of the industry trend, not an identical mechanism.

- **Corroborates**: `blog-simonwillison-prompt-injection-role-confusion.md`
  (Claims 2 and 7). That note documents "CoT Forgery" — text crafted to mimic
  chain-of-thought/reasoning formatting raises prompt-injection attack success
  rates from near-zero to ~60% and "generalized across every LLM tested" —
  and the underlying mechanism, that "models identify roles from an insecure
  feature (style)" rather than structural position. This source's Claim 8
  (channel destination is "a learned convention... trick it into thinking it
  is in that channel and it may leak tokens") describes the identical failure
  mode — style-based channel/role identification — applied specifically to
  the reasoning/final channel split rather than to system/user role
  confusion generally. The two sources together show this is one failure
  mode (format-mimicry defeats learned-convention boundaries) manifesting in
  two guide-relevant places: role confusion (Willison) and reasoning-trace
  leakage (this source).

- **Extends**: `blog-ronacher-pi-oss.md` (same author; no direct claim-level
  content overlap — that note covers OSS maintenance and issue-triage
  patterns in Pi, not reasoning-trace mechanics). The connection is
  incidental but concrete: the `think` tool extension in this source's Claim
  10 / Concrete Artifacts is a real extension for the same Pi coding agent
  that note documents operationally (the `.pi` folder, `/is`/`/wr` commands).
  Both sources are first-hand accounts from Pi's own maintainer/author.

- **Novel**: The GPT-OSS Harmony channel-token mechanism, the system-prompt
  implementation of "reasoning effort" (with two concretely differing
  provider examples), the KV-cache-invalidation-on-effort-change claim, the
  DwarfStar prefill-based enable/disable mechanism, and the `think`-tool
  leak-vector explanation are all new to the corpus — no existing source note
  documents reasoning-trace implementation mechanics at this level of detail
  for any model family.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add reasoning-effort changes as a
  second, independent KV-cache-invalidation trigger alongside compaction
  (currently documented via `research-wasnotwas-context-compaction.md` around
  the "Compaction is a budget item, not a rescue mechanism" section). Cite
  Claim 6: changing a session's reasoning-effort level mid-conversation
  re-writes the cached system-prompt prefix (at least for providers that
  implement effort via system-prompt text) and forces a full-prefix re-read at
  base pricing, the same way compaction does. Practitioners building
  cost-escalation logic ("start cheap, escalate reasoning effort on failure")
  should budget for this cache miss.

- **Chapter 02 (Harness Engineering)**: Document the `think`-tool pattern
  (Claim 10, Concrete Artifacts) as a legitimate harness design for preserving
  reasoning quality on models/providers where native reasoning is disabled —
  registering an explicit `think` tool and forcing it as the first tool call
  of a turn when provider reasoning is off. This is a concrete, reusable
  extension pattern (not hypothetical — it is shipped code) for any harness
  that needs to support both reasoning-capable and reasoning-disabled model
  configurations behind one interface.

- **Chapter 06 (Security Threat Model)**: Add reasoning-trace channel
  confusion as a named vulnerability class, citing Claim 8 alongside the
  existing "CoT Forgery" findings from `blog-simonwillison-prompt-injection-role-confusion.md`.
  Currently Chapter 06 documents prompt injection defenses and gradual-trust
  rollout patterns but does not discuss reasoning-trace confidentiality or
  channel-based role confusion. State plainly: reasoning/thinking traces are
  separated from final output by a *learned convention*, not an enforced
  architectural boundary, and format-mimicry attacks that generalize across
  model families (per Willison's corroborating data) can defeat that
  separation. Practitioners should not treat "hidden reasoning" as a
  confidentiality guarantee for secrets that might appear in scratch-work
  (e.g., credentials or internal reasoning about access decisions) — this is
  reinforced by the linked-but-unverified arXiv paper's reported finding of
  recovered credentials in leaked reasoning blocks (see Concrete Artifacts;
  flagged as unverified, worth an independent Miner pass — see Extraction
  Notes).

## Extraction Notes

- Full post text was fetched directly from
  `https://lucumr.pocoo.org/2026/8/19/what-is-reasoning.md` (the site's own
  markdown mirror, linked from the HTML page's "copy as markdown" control) and
  cross-checked against the rendered HTML at the canonical URL. All quotes in
  this note were copied character-for-character from that markdown fetch, not
  reconstructed from a WebFetch summary. The post is short (~600 words); no
  content was skimmed or omitted.
- Two links were followed as substantive related pages: (1)
  https://gist.github.com/mitsuhiko/0904a3d89741e8e3bcca1ca93ea076de (Pi's
  `think` tool extension — fetched in full, code reproduced verbatim in
  Concrete Artifacts and used as direct evidence for Claim 10); (2)
  https://arxiv.org/html/2608.09867v1 (the motivating arXiv paper — fetched
  via WebFetch, which returned a *summarized* rendering rather than the raw
  paper text). Because the paper summary was model-generated rather than a
  verbatim fetch, I have NOT extracted its claims as first-class Claims in
  this note (per MINER.md §2a, no fabricated/reconstructed quotes) — it is
  presented only as unverified background context in Concrete Artifacts and
  flagged there. **Recommendation for the Prospector**: the linked paper
  (reasoning-trace extraction from closed-weight APIs, reportedly recovering
  PII and credentials at scale) looks independently source-worthy and directly
  relevant to Chapter 06; consider filing it as its own source-submission
  issue for a dedicated Miner pass that reads the primary paper text.
- Two other links (https://earendil.com/posts/session-portability/, cited only
  as "We have lamented this" in passing, and the second
  https://github.com/antirez/ds4 reference, which duplicates the first) were
  not followed in full — the DwarfStar repo link is already substantively
  covered via the two system-prompt excerpts quoted directly in the post
  itself, and the earendil.com link is a single incidental aside with no
  additional claims attributable to this source.
- No contradiction issue filed. The closest candidate — this source's "reasoning
  effort is baked into the system prompt, not a sampling parameter" (Claim 5)
  vs. Anthropic's documented fixed numeric `thinking_budget` parameter for
  Opus 4.6 (`blog-anthropic-opus47-best-practices.md` Claim 5) — is a
  conditioning-variable difference (which provider, which API generation), not
  a real contradiction: both can be true simultaneously (some providers use a
  true numeric parameter, others use prompt text), and Anthropic's own 4.6→4.7
  migration away from the numeric parameter toward prompt-steered adaptive
  thinking is directionally consistent with, not opposed to, Ronacher's claim.
  See MINER.md §4a "When NOT to file."
- Confidence rated `emerging` overall: the post mixes settled, directly
  verifiable facts (the Harmony token sequence, the two providers' literal
  system-prompt text, the `think` tool gist's actual code) with several
  explicitly hedged inferences ("presumably," "may explain," "we have even
  seen") that the author himself does not claim to have confirmed. Individual
  claim confidence levels above reflect this split rather than treating the
  whole post uniformly.
