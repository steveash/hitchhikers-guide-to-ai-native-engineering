---
source_url: https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/
source_type: blog-post
title: "Introducing Muse Glimmer"
author: Simon Willison (linking to and testing Meta's own announcement)
date_published: 2026-08-10
date_extracted: 2026-08-20
last_checked: 2026-08-20
status: current
confidence_overall: emerging
issue: "#2805"
---

# Introducing Muse Glimmer

> Simon Willison's link-blog post on Meta's Muse Glimmer, a 30B Apache-2.0
> open-weights model explicitly optimized for local agentic use. Read
> alongside Meta's own announcement page (fetched directly via its embedded
> React Server Component payload, not summarized) and three of Willison's own
> published test-session gists, this note surfaces a training-lineage detail
> absent from Willison's post — Glimmer is pretrained via logit distillation
> from Muse Spark's own outputs, not trained from scratch or built on a
> third-party base model — plus quantified local-inference numbers (55GB to
> under 20GB via 4-bit quantization; 1.5-3.1x decode speedup via speculative
> decoding) and a full multi-tool-call transcript of the model exploring a
> real codebase's authentication system.

## Source Context

- **Type**: blog-post (Willison's link-blog format — three short paragraphs,
  an inline SVG-pelican image, a coding-agent test description, and a
  multimodal vision test, auto-discovered via trusted feed `simon-willison`).
  Per MINER.md §1, this note follows four linked pages beyond Willison's own
  post: Meta's own announcement at
  `research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model`
  (fetched via its raw Next.js React Server Component text payload, since a
  plain browser-UA `curl` only returns unrendered JavaScript loader markup),
  the pelican-SVG gist, the Datasette-auth coding-agent transcript gist, and
  the vision-description gist. The LM Studio model listing page
  (`lmstudio.ai/models/muse-glimmer`) was also fetched but contained no
  extractable prose beyond a client-rendered model card shell — see
  Extraction Notes.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo (creator of Django, Datasette, `sqlite-utils`, `llm`)
  and the originator of the recurring "pelican riding a bicycle" SVG
  cross-model test used throughout this corpus (see
  `blog-simonwillison-kimi-k3-pelican-benchmark.md`,
  `blog-simonwillison-ornith.md`). For this post he is first-person
  hands-on tester (his own LM Studio session, his own `llm-coding-agent`
  run against his own Datasette checkout, his own `llm` CLI vision call) —
  not a passive quoter of vendor marketing. The architectural, training, and
  capability claims quoted from Meta's announcement are vendor self-report
  and should be read as such; Willison has no disclosed affiliation with
  Meta.
- **Scope**: Covers Muse Glimmer's licensing, Meta's own stated capability
  list and training methodology, quantization/speculative-decoding
  performance figures, and Willison's own local hands-on testing (one pelican
  SVG generation, one real-codebase agentic coding-navigation session, one
  vision/image-description call). Does NOT cover: independent third-party
  benchmark verification (Meta's announcement links to a separate
  methodology report that was not fetched — see Extraction Notes), any
  numeric benchmark scores for the four named agentic benchmarks, or
  production/multi-session deployment experience beyond Willison's single
  test session.

## Extracted Claims

### Claim 1: Meta released Muse Glimmer, a 30B-parameter open-weights model under a "clean" Apache 2.0 license, which Willison frames as a licensing improvement over Meta's earlier Llama releases

- **Evidence**: Willison's own direct statement, corroborated by the
  license terms being stated identically on Meta's own announcement page
  (Concrete Artifacts, below).
- **Confidence**: settled (a specific, checkable license designation)
- **Quote**: "Meta are back in the open weights game! Muse Glimmer is a brand new 30B model under a clean Apache 2.0 license (a step up from the janky Llama licenses of old)."
- **Our assessment**: This is the same rhetorical pattern Willison used for
  Gemma 4 in `blog-simonwillison-ornith.md` (Claim 2: Gemma 4 is "not bound
  by the janky additional Gemma Terms of Use that afflicted the previous
  Gemma models") — a practitioner-credible signal that major labs are
  moving away from custom, restriction-laden open-weight licenses toward
  plain Apache 2.0. For practitioners evaluating Glimmer for commercial use,
  Apache 2.0 removes the redistribution/use-case restrictions that made
  earlier Llama licenses a legal-review burden.

### Claim 2: Meta names four specific full-task agentic benchmarks as evidence for "End-to-end Agentic Task Completion," but the announcement's body text gives no numeric scores for any of them — only a link to a separate methodology report

- **Evidence**: Direct text from Meta's announcement's capability list, plus
  the following "Performance" section, which names only two comparison
  models in prose (no table or chart data present in the fetched text) and
  points to `research.meta.ai/static/muse-glimmer-methodology` for detail.
- **Confidence**: settled (a directly observable absence: the claim is
  named but not quantified in the fetched page)
- **Quote**: "Muse Glimmer achieves strong success rates on full-task benchmarks including DeepSearch QA, MCP-Atlas, 𝛕-Bench and SWE-Bench, which measure its ability to work within scaffolds, write and debug code, and resolve multi-turn requests from start to finish." / "Compared with Gemma4-31B and Qwen3.6-27B, Muse Glimmer performs strongly for its size class on several widely used LLM benchmarks. For more detail about our evaluations, see our report."
- **Our assessment**: "Strong success rates" and "performs strongly for its
  size class" are unquantified vendor characterizations, not numbers. This
  mirrors `blog-simonwillison-muse-code-spark-12.md` Claim 10, where Meta's
  Muse Code kernel-optimization case study was likewise described only via
  chart images with no extractable numeric values — a recurring pattern in
  Meta's Muse-family announcements of naming benchmarks and comparison
  models without publishing the actual scores in the readable page text.
  Any guide citation of Glimmer's benchmark performance should flag that
  this note could not independently verify a single number behind these
  claims.

### Claim 3: Meta states Glimmer was explicitly trained to diagnose and retry after a failed or unexpected tool call, rather than halting

- **Evidence**: Direct capability-list entry from Meta's announcement,
  distinct from the "Reliable Tool Use" and "Multi-Step Reasoning" entries
  that precede it.
- **Confidence**: emerging (a specific, named training target; not
  independently measured or reproduced in this source)
- **Quote**: "Failure Recovery. When a tool call fails or returns an unexpected result, the model is trained to diagnose the error and retry rather than halt."
- **Our assessment**: This is a concrete, harness-relevant training claim —
  it names a specific model behavior (diagnose-and-retry on tool failure)
  as a deliberate training target rather than something a harness must
  prompt or scaffold for separately. It parallels
  `blog-simonwillison-muse-code-spark-12.md` Claim 4 (Meta training Muse
  Spark 1.2 against harness-level trajectories — compaction, subagents,
  goals — via rejection sampling), extending that same "train the model
  itself against harness-shaped behavior" pattern to a second Meta model
  family, this time with a specific named failure-recovery behavior rather
  than a general trajectory-shaping claim.

### Claim 4: Glimmer accepts interleaved text and images through a "dedicated perception encoder," and is explicitly built for compatibility with OpenClaw and other agentic orchestration scaffolds

- **Evidence**: Direct capability-list entries from Meta's announcement.
- **Confidence**: settled (first-party architecture/compatibility
  disclosure)
- **Quote**: "Multimodal Input and Reasoning. Through a dedicated perception encoder, the model accepts interleaved text and images. This enables agents to interpret screenshots, charts, and documents alongside conversation." / "Scaffold Compatibility. Muse Glimmer works across OpenClaw and other agentic orchestration patterns."
- **Our assessment**: The explicit "screenshots, charts, and documents"
  framing targets the same agentic-computer-use use case documented
  elsewhere in the corpus, and the named compatibility with OpenClaw is a
  concrete cross-harness-portability claim — Meta is stating the model was
  validated (or at least designed) against an external orchestration
  framework rather than only its own first-party tooling, unlike the
  co-trained, single-harness pairing documented for Muse Code + Muse Spark
  1.2 in `blog-simonwillison-muse-code-spark-12.md` Claim 1.

### Claim 5: Glimmer's pretraining phase used logit distillation from Muse Spark's own outputs, using a similar data mix to that "teacher" model — Glimmer is a distilled, locally-deployable sibling of Meta's hosted Muse Spark model, not a from-scratch or third-party-base-model release

- **Evidence**: Direct three-phase training methodology description on
  Meta's announcement page, naming Muse Spark specifically as the source of
  the pretraining signal.
- **Confidence**: settled (a specific, named training methodology from the
  model's own creator; not independently verified but directly and
  specifically stated, not inferred)
- **Quote**: "Pre-Training. We trained Muse Glimmer on Muse Spark's outputs using logit distillation, leveraging a similar data mix as the teacher." / "Mid-Training. We trained the model on longer-context, more agent-heavy data with richer reasoning traces, alongside organic data." / "Post-Training. We combined supervised fine-tuning with a mix of on-policy distillation and reinforcement learning across general, reasoning, coding, and agentic domains."
- **Our assessment**: This is the most novel claim in the source for this
  corpus. `blog-simonwillison-muse-spark.md` and
  `blog-simonwillison-muse-code-spark-12.md` document Muse Spark as a
  hosted-only model family (API access via meta.ai, then via Muse Code);
  this source reveals that Meta's open-weights local model is not an
  independent release but a distillation target trained directly on Muse
  Spark's own output distribution. This is architecturally distinct from
  two other open-weights training lineages already in the corpus: Ornith-1.0
  (`blog-simonwillison-ornith.md` Claim 1, built by fine-tuning pretrained
  third-party Gemma 4 + Qwen 3.5 base models) and Inkling
  (`blog-simonwillison-inkling-open-weights.md` Claim 1, trained from
  scratch on 45T tokens). Meta's approach — distill a smaller open-weights
  model directly from a lab's own larger hosted flagship — is a fourth,
  previously undocumented pattern for how an open-weights release relates
  to its training data source.

### Claim 6: Meta quantizes Glimmer's weights from over 55GB at full precision to under 20GB at approximately 4-bit precision, sized to leave headroom for the KV cache, perception encoder, and speculative-decoding drafter within a 24-32GB memory envelope, and states this compression causes "minimal to no degradation on agentic tasks"

- **Evidence**: Direct technical description in the announcement's "Fitting
  the Model on Your Device" section.
- **Confidence**: emerging (a specific, quantified compression ratio, but
  the "minimal to no degradation" claim is a vendor assertion with no
  benchmark numbers given in the fetched text to substantiate it)
- **Quote**: "At full precision, a 30-billion parameter model would require over 55 GB of memory — far more than any consumer GPU offers. We use quantization techniques to compress the model's weights to approximately 4-bit precision, shrinking the language model to under 20 GB. This leaves enough headroom for the model's working memory (its "KV cache"), the perception encoder for image understanding, and the speculative decoding drafter to run simultaneously within a 24 GB or 32 GB envelope. We validated that this compression introduces minimal to no degradation on agentic tasks."
- **Our assessment**: The 24-32GB total envelope (weights + KV cache +
  perception encoder + speculative-decoding drafter, all running together)
  is a more complete accounting than a bare weight-size figure — it's the
  actual practical RAM/VRAM budget a practitioner needs, not just the model
  checkpoint size. This directly extends
  `blog-fowler-boeckeler-local-models-viability.md` Claim 1 (Böckeler's
  15-25GB "comfortable" model-weight RAM budget, with 30GB "stretching it a
  lot," for local agentic coding on Apple Silicon) and Claim 8 (context
  window competing with model weights for the same RAM pool): Meta's own
  30B model, once quantized, lands almost exactly at the edge of Böckeler's
  empirically-derived comfort zone once the KV cache and other runtime
  components are included — independent corroboration, from the vendor's
  own engineering description, of the RAM-budget shape Böckeler found by
  hands-on testing.

### Claim 7: Meta reports that DFlash-based speculative decoding increases Glimmer's decode speed by 3.1x on an RTX 5090, 1.8x on a MacBook M5 Max, and 1.5x on a MacBook M4 Max

- **Evidence**: Direct performance figures in the announcement's "Faster
  Generation Through Speculative Decoding" section and an accompanying bar
  chart's alt text.
- **Confidence**: emerging (specific, quantified vendor-run benchmark
  figures; not independently reproduced by this note or by Willison)
- **Quote**: "Bar chart showing DFlash speculative decoding increasing Muse Glimmer decode speed by 3.1 times on RTX 5090, 1.8 times on M5 Max, and 1.5 times on M4 Max." / "We measure the speed of our K-Quant-17GB model alongside the quantized DFlash drafter on MacBook M4-Max, M5-Max and on a RTX-5090. The model is fast enough for fluid conversation and real-time agent interaction, all running entirely on your device."
- **Our assessment**: The per-device breakdown (largest speedup on
  discrete-GPU RTX 5090, smaller but still substantial gains on
  unified-memory Apple Silicon) is a concrete, checkable data point for
  practitioners choosing hardware for local agentic inference — it
  quantifies that speculative decoding's benefit is hardware-dependent, not
  a flat multiplier, though as a vendor-run measurement it should be
  treated as a starting hypothesis pending independent reproduction (the
  same caution this corpus applies to other vendor-run benchmark claims,
  e.g. `blog-simonwillison-muse-spark.md` Claim 8).

### Claim 8: Willison's own pelican-SVG test, run at LM Studio's 18.16GB quantized version of the model, produced a result where — in his own description — "all the pieces are there but they are pretty jumbled together"

- **Evidence**: Willison's own image caption/alt text for the pelican SVG
  he generated and linked to a gist.
- **Confidence**: anecdotal (a single generation, single practitioner's
  subjective visual judgment, no comparison score)
- **Quote**: "All the pieces are there but they are pretty jumbled together."
- **Our assessment**: This is Willison's characteristically informal
  cross-model creative-output smoke test (see
  `blog-simonwillison-kimi-k3-pelican-benchmark.md`,
  `blog-simonwillison-pelicanmaxxing.md`), applied to Glimmer. It is not in
  tension with Claim 6's "minimal to no degradation on agentic tasks"
  claim — Meta's validation is explicitly scoped to "agentic tasks," and a
  single-shot creative SVG-drawing prompt is exactly the kind of task
  `blog-simonwillison-kimi-k3-pelican-benchmark.md` Claim 6 argues doesn't
  measure "the thing that matters most for today's models: agentic tool
  calling." Treat this as a data point about single-shot creative output
  quality specifically, not as evidence against Meta's narrower agentic-task
  degradation claim.

### Claim 9: Willison ran Glimmer against a real, non-trivial codebase (his own Datasette checkout) via his `llm-coding-agent` plugin and got an accurate, detailed multi-mechanism explanation of the auth system, produced through a fully-logged multi-step tool-calling transcript with notably terse reasoning traces throughout

- **Evidence**: The full published transcript gist, showing the model
  issuing a sequence of `list_files`, `search_files`, and `read_file` tool
  calls before producing its final answer, which correctly distinguishes
  cookie-based auth (itsdangerous-style signed payloads, root-user
  single-use tokens, `/-/auth-token` and `/-/logout` routes), API token auth
  (`dstok_` prefixed signed tokens with optional restrictions), and the
  underlying SQL-based permission-resolution system (`datasette.allowed()`,
  resource > parent > global precedence, deny-beats-allow).
- **Confidence**: anecdotal (single practitioner, single session, single
  codebase, no comparison run against other models on the same task in this
  source)
- **Quote**: "I also tried it out with my llm-coding-agent plugin, running against a fresh checkout of Datasette with the prompt: how does auth work?"
- **Quote (model's reasoning trace, verbatim from the transcript gist, first turn)**: "how does auth work? We need explain auth in datasette. Explore code."
- **Our assessment**: This is exactly the kind of test Willison himself
  argues matters more than the pelican benchmark
  (`blog-simonwillison-kimi-k3-pelican-benchmark.md` Claim 6: "the thing
  that matters most for today's models: agentic tool calling and the
  ability to operate tools reliably as conversations grow in length") — a
  genuine multi-tool-call exploration of an unfamiliar codebase, ending in
  a correct, structurally detailed technical summary. The reasoning traces
  throughout the transcript are strikingly terse ("We need explain auth in
  datasette. Explore code."; "We have enough info to summarize."), which is
  consistent with — though not necessarily caused by the same mechanism as
  — the emergent chain-of-thought compression documented in
  `blog-simonwillison-inkling-open-weights.md` Claim 8 (Thinking Machines
  Lab's Inkling developing telegraphic, grammatically-stripped reasoning
  traces as a side effect of RL token-efficiency pressure). Whether
  Glimmer's terseness comes from a similar RL dynamic, from Muse Spark
  teacher-distillation (Claim 5), or from deliberate design is not stated
  by Meta and cannot be determined from this source alone.

### Claim 10: Willison judges 32GB+ of system RAM as the practical local-deployment comfort point for this size of model, since it leaves room to run other applications simultaneously

- **Evidence**: Willison's own direct statement about his testing machine.
- **Confidence**: anecdotal (a single practitioner's stated preference, not
  a systematic RAM-sizing study)
- **Quote**: "I really like this size of model, because if a machine has 32 GB of RAM or more (mine has 128GB) it leaves plenty of space for running other applications at the same time."
- **Our assessment**: Willison's 32GB comfort threshold aligns closely with
  Meta's own stated "24 GB or 32 GB envelope" for weights + KV cache +
  perception encoder + speculative-decoding drafter combined (Claim 6) —
  an independent practitioner observation landing on the same number the
  vendor engineered toward. It is also consistent with, though somewhat
  more generous than, `blog-fowler-boeckeler-local-models-viability.md`
  Claim 1's finding that 15-25GB models were her "comfortable" range and
  30GB "stretched it a lot" on 48-64GB machines — Glimmer, once quantized,
  sits close to the upper edge of that same practical range.

### Claim 11: Vision testing showed Glimmer producing a detailed, species-level, compositionally-aware description of a photograph of two pelicans on rocks

- **Evidence**: Willison's own `llm` CLI multimodal call against the model,
  with the full response published in a gist.
- **Confidence**: anecdotal (single test, single image, no comparison
  baseline against other models on the same image within this source)
- **Quote**: "The photograph shows a rocky, breakwater-style shoreline on an overcast day with a smooth, gray body of water and a faint dock/pier line in the soft-focused background. In the foreground two large brown pelicans, *Pelecanus occidentalis*, are perched on the jumbled gray-white stones."
- **Our assessment**: This is a thin but concrete positive data point for
  Glimmer's multimodal capability (correct species identification down to
  binomial nomenclature, plumage detail, and compositional description of
  lighting/framing) — consistent with Claim 4's "dedicated perception
  encoder" architecture claim actually functioning as described in at least
  this one case, though a single image with no ground-truth scoring is weak
  evidence on its own.

### Claim 12: Glimmer is distributed directly via Hugging Face, with day-one hosted access through Together AI, Fireworks AI, and OpenRouter, local-runtime support via Ollama, LM Studio, and Unsloth, edge-framework integrations for llama.cpp/MLX/ExecuTorch explicitly described as "landing in the coming days," and scale-serving support via vLLM and SGLang

- **Evidence**: Direct availability/distribution statements in Meta's
  announcement.
- **Confidence**: settled (first-party distribution disclosure, directly
  checkable)
- **Quote**: "Muse Glimmer is built to work with the tools developers already use. Optimized integrations on llama.cpp, MLX, and ExecuTorch will land in the coming days, so you can go from download to working agent in minutes." / "...deploy it with edge frameworks including llama.cpp, ExecuTorch, and MLX, serve it at scale with vLLM and SGLang, or get started quickly through partners like Together AI, Fireworks AI, and OpenRouter. You can even customize it for your use case by leveraging PyTorch's TorchTitan training feature to tune the model further."
- **Our assessment**: The explicit "will land in the coming days" framing
  for the three edge-runtime integrations (llama.cpp, MLX, ExecuTorch) —
  the exact runtimes local practitioners actually use, per
  `blog-fowler-boeckeler-local-models-viability.md`'s LM Studio/GGUF/MLX
  usage and `blog-simonwillison-ornith.md`'s GGUF-via-LM-Studio testing —
  means Glimmer shipped day-one with only partial tooling support for local
  practitioners; anyone evaluating it at launch (as Willison did) was
  necessarily using a pre-optimized or third-party-packaged build (Willison
  used LM Studio's own 18.16GB build directly, per Claim 8) rather than the
  vendor's own optimized edge integration.

## Concrete Artifacts

### Full capability list (verbatim, Meta announcement page)

```
- End-to-end Agentic Task Completion. Muse Glimmer achieves strong success
  rates on full-task benchmarks including DeepSearch QA, MCP-Atlas,
  𝛕-Bench and SWE-Bench, which measure its ability to work within
  scaffolds, write and debug code, and resolve multi-turn requests from
  start to finish.
- Reliable Tool Use. The model handles a wide range of function calls,
  invoking tools with precise schemas throughout extended workflows.
- Multi-Step Reasoning. Muse Glimmer chains reasoning over long horizons,
  sustaining coherent plans across complex, extended workflows.
- Failure Recovery. When a tool call fails or returns an unexpected result,
  the model is trained to diagnose the error and retry rather than halt.
- Multimodal Input and Reasoning. Through a dedicated perception encoder,
  the model accepts interleaved text and images. This enables agents to
  interpret screenshots, charts, and documents alongside conversation.
- Scaffold Compatibility. Muse Glimmer works across OpenClaw and other
  agentic orchestration patterns.
- Controllable Effort. Muse Glimmer supports different reasoning strengths
  to select the right balance between quality and speed.
- Multilingual. Muse Glimmer is trained on data from more than 100
  languages.

Source: research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
```

### Training methodology, three phases (verbatim, Meta announcement page)

```
Pre-Training: trained on Muse Spark's outputs using logit distillation,
  leveraging a similar data mix as the teacher.
Mid-Training: trained on longer-context, more agent-heavy data with richer
  reasoning traces, alongside organic data.
Post-Training: supervised fine-tuning combined with a mix of on-policy
  distillation and reinforcement learning across general, reasoning,
  coding, and agentic domains.

Source: research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
```

### Quantization and speculative decoding (verbatim, Meta announcement page)

```
Full precision:        >55 GB
Quantized (~4-bit):    <20 GB language-model weights
Practical envelope:    24-32 GB (weights + KV cache + perception encoder +
                        speculative-decoding drafter, running together)
Quantized model name:  K-Quant-17GB
Decode speedup via DFlash speculative decoding:
  RTX 5090:   3.1x
  MacBook M5 Max: 1.8x
  MacBook M4 Max: 1.5x

Source: research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
```

### Datasette auth-exploration transcript excerpt (verbatim, Willison's published gist)

```
Model: lmstudio/meta/muse-glimmer (resolved: meta/muse-glimmer)

Prompt: how does auth work?

[First-turn reasoning, verbatim:]
how does auth work?
We need explain auth in datasette. Explore code.

[First tool call: CodingTools_list_files, pattern "**/*auth*" -> returned
tests/test_auth.py, docs/authentication.rst, datasette/actor_auth_cookie.py]

[... 24 further tool-call turns using list_files, search_files, read_file,
alternating with terse reasoning turns such as "We have enough info to
summarize." and "Let's also check tests for auth." ...]

[Final response, excerpt:]
Cookie auth
  Signed with datasette.sign(value, namespace="actor") using
  URLSafeSerializer + DATASETTE_SECRET.
  Payload shape: {"a": <actor dict>, "e": <base62 timestamp>}. Expiry is
  checked on every request.
API token auth
  Default handler: datasette.tokens.SignedTokenHandler.
  Tokens are dstok_<itsdangerous signature> signed with namespace "token".
Permissions
  The central check is datasette.allowed(action, resource?, actor?) ->
  allowed_many() -> check_permissions_for_actions.
  Resolution order: resource > parent > global; deny beats allow at same
  level; no match = deny.

That's it - authentication is "who are you?" via actor_from_request
hooks/cookies/tokens, and authorization is "is this actor allowed to do
this action on this resource?" via the SQL-based permission system with
config/plugin rules.

Source: gist.github.com/simonw/3623676275da1a6078b2500dcc78116f
(linked from simonwillison.net/2026/Aug/10/introducing-muse-glimmer/)
```

### Vision test: pelicans-on-rocks image description (verbatim, Willison's published gist)

```
Command: llm -m lmstudio/meta/muse-glimmer -a
  https://static.inaturalist.org/photos/714731804/large.jpg 'describe image'

Response (excerpt): "The photograph shows a rocky, breakwater-style
shoreline on an overcast day with a smooth, gray body of water and a faint
dock/pier line in the soft-focused background. In the foreground two large
brown pelicans, Pelecanus occidentalis, are perched on the jumbled
gray-white stones. They have the species' characteristic long, down-curved
yellow-orange bills with a large throat pouch, long slender necks and
mottled brown-gray plumage on the back and wings."

Source: gist.github.com/simonw/288ef0dd33a913455d1b1ecc329637e0
(linked from simonwillison.net/2026/Aug/10/introducing-muse-glimmer/)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-ornith.md` (Claim 2 — Willison's identical
    rhetorical pattern applied to Gemma 4's Apache 2.0 license vs. earlier
    "janky" Gemma Terms of Use): the same practitioner-observed pattern of
    major labs moving from restriction-laden custom licenses to plain
    Apache 2.0, now documented for a second lab (Meta) and a second model
    family (Claim 1).
  - `blog-fowler-boeckeler-local-models-viability.md` (Claim 1 — 15-25GB
    "comfortable" local-model RAM budget, 30GB "stretches it a lot"; Claim
    8 — context window competing with model weights for the same RAM
    pool): Meta's own 24-32GB practical envelope for the quantized model
    (Claim 6) and Willison's independently-stated 32GB comfort point (Claim
    10) both land at the upper edge of Böckeler's empirically-derived
    range, corroborating her RAM-budget shape from the vendor engineering
    side and a second practitioner's session, for a larger and more
    capable 30B-class model than she tested.
  - `blog-simonwillison-kimi-k3-pelican-benchmark.md` (Claim 6 — the
    pelican benchmark's biggest limitation is that it doesn't test agentic
    tool calling, "the thing that matters most"): Willison's own Datasette
    auth-exploration test (this note's Claim 9) is a direct, concrete
    instance of the kind of agentic tool-calling test that source argues
    should be prioritized over the pelican benchmark — applied here to the
    same model he also ran the (limited-value) pelican test against.

- **Contradicts**: None identified, and no contradiction issue filed. The
  "jumbled" pelican SVG result (Claim 8) is not in tension with Meta's
  "minimal to no degradation on agentic tasks" quantization claim (Claim
  6) — the two describe different task categories (single-shot creative
  SVG generation vs. Meta's explicitly-scoped "agentic tasks"), a scope
  difference rather than a genuine disagreement, per MINER.md §4a guidance.

- **Extends**:
  - `blog-simonwillison-muse-spark.md` and
    `blog-simonwillison-muse-code-spark-12.md`: both document Meta's Muse
    Spark family as hosted-only (meta.ai chat, then the Muse Code terminal
    agent). This source reveals the previously-undocumented open-weights
    branch of that same lineage — Glimmer is pretrained via logit
    distillation directly from Muse Spark's own outputs (Claim 5), meaning
    Meta's hosted and open-weights model lines are not independent
    products but teacher/student pairs. This also extends
    `blog-simonwillison-muse-code-spark-12.md` Claim 4 (Meta training Muse
    Spark 1.2 against harness-level trajectories via rejection sampling)
    with a second, specifically-named trained-in harness behavior:
    Glimmer's "Failure Recovery" diagnose-and-retry training (this note's
    Claim 3).
  - `blog-simonwillison-inkling-open-weights.md` (Claim 8 — Inkling's
    emergent, RL-induced telegraphic chain-of-thought compression):
    Glimmer's own reasoning traces in the Datasette transcript (Claim 9)
    are similarly terse ("We need explain auth in datasette. Explore
    code."), a second observed instance of minimal-verbosity reasoning in
    an agentic open-weights model, though this source cannot establish
    whether the same RL mechanism, teacher distillation, or a different
    cause produced it.

- **Novel**:
  - **Open-weights model trained via logit distillation from a lab's own
    hosted flagship model's outputs** (Claim 5): a fourth distinct
    open-weights training lineage in the corpus, alongside from-scratch
    training (Inkling), fine-tuning a third-party base model (Ornith-1.0 on
    Gemma 4 + Qwen 3.5), and (documented elsewhere in the broader AI
    industry but not previously in this corpus with this level of detail)
    distillation from a same-lab teacher model.
  - **Quantified per-device speculative-decoding speedups for local
    agentic inference** (Claim 7: 3.1x/1.8x/1.5x across RTX 5090, M5 Max,
    M4 Max) — the first source in the corpus to give hardware-specific
    speculative-decoding multipliers for a local open-weights model, rather
    than a single aggregate throughput number.
  - **"Failure Recovery" as a named, explicit training target** (Claim 3)
    distinct from general tool-use reliability — no existing corpus source
    documents a vendor naming diagnose-and-retry-on-tool-failure as its own
    labeled training objective.

## Guide Impact

- **Chapter on local model deployment / hardware sizing**: Add Meta's
  quantization and memory-envelope figures (Claim 6: 55GB full precision to
  <20GB weights, 24-32GB practical envelope including KV cache and
  perception encoder) and Willison's independently-stated 32GB comfort
  point (Claim 10) as a second, vendor-and-practitioner-corroborated data
  point alongside `blog-fowler-boeckeler-local-models-viability.md`'s
  empirically-derived 15-25GB "comfortable" / 30GB "stretches it" RAM
  budget for local agentic coding — together they suggest 24-32GB is
  becoming the practical ceiling for a single well-optimized 30B-class
  agentic model on consumer hardware in mid/late-2026.
- **Chapter on harness engineering / trained-in agentic behaviors**: Add
  Glimmer's "Failure Recovery" training target (Claim 3) and its logit
  distillation from Muse Spark (Claim 5) alongside the existing
  `blog-simonwillison-muse-code-spark-12.md` material on Meta training
  models against harness-shaped trajectories (compaction, subagents,
  goals) — reinforcing that Meta is applying this "train the model against
  harness behavior" strategy across both its hosted and open-weights model
  lines, not just its flagship.
- **Chapter on model evaluation methodology**: Cite Willison's Datasette
  auth-exploration test (Claim 9) alongside
  `blog-simonwillison-kimi-k3-pelican-benchmark.md` as a second concrete
  example of a practitioner substituting a real multi-tool-call
  codebase-exploration task for the informal pelican benchmark when
  assessing a new agentic model — and note the terse reasoning-trace
  pattern (cross-referenced against Inkling's documented CoT compression)
  as something worth watching across future open-weights releases.
- **Any benchmark/capability table for Glimmer**: Flag per Claim 2 that
  Meta's own announcement provides no numeric scores for any of the four
  named agentic benchmarks (DeepSearch QA, MCP-Atlas, τ-Bench, SWE-Bench)
  in its readable page text — only a link to a separate, unfetched
  methodology report. Any guide citation of Glimmer's benchmark standing
  should be sourced from that report directly, not from this announcement's
  prose.

## Extraction Notes

- **Meta's announcement page required non-standard extraction**: a plain
  browser-UA `curl` of `research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model`
  returns only unrendered Next.js JavaScript loader markup with no visible
  article text. The actual article content was recovered from the page's
  embedded React Server Component payload (`self.__next_f.push([1,"..."])`
  script segments), concatenated and unicode-unescaped. All quotes
  attributed to Meta's announcement in this note were verified against that
  extracted payload text, not against a summarizing fetch tool's paraphrase
  — an initial WebFetch pass on the same URL was cross-checked against this
  raw extraction and found consistent in substance, but the raw-payload
  quotes are what's reproduced here. One decoding artifact from this
  extraction process is noted: the payload's escaped non-breaking space
  before "Glimmer" decoded as a stray "Â" character in intermediate output;
  this is an artifact of the Miner's own extraction script, not of Meta's
  source page, and has been normalized to a plain space in all quotes
  above.
- **Five linked pages followed** (within MINER.md §1's up-to-5 budget):
  Meta's own announcement (the primary source of Claims 2-7, 12), the
  pelican-SVG gist (Claim 8), the Datasette-auth coding-agent transcript
  gist (Claim 9), the vision-description gist (Claim 11), and the LM Studio
  model listing page (`lmstudio.ai/models/muse-glimmer`), which was fetched
  but yielded no extractable prose — it is a client-side-rendered React
  page whose model card content did not appear in the static HTML.
- **Not fetched**: Meta's separate benchmark methodology report at
  `research.meta.ai/static/muse-glimmer-methodology`, linked from the
  announcement's Performance section. This would be a sixth linked page
  beyond MINER.md §1's five-page guidance, and is the only place Glimmer's
  actual numeric benchmark scores might appear (per Claim 2). Flagged as a
  gap and a candidate for a follow-up source if the methodology report is
  ever submitted separately.
- **No contradiction issues filed.** The one candidate tension considered
  (Claim 8's "jumbled" pelican SVG vs. Claim 6's "minimal to no degradation
  on agentic tasks" claim) resolves as a scope difference — creative
  single-shot SVG generation is not an agentic task in Meta's own framing —
  not a genuine disagreement, per MINER.md §4a guidance.
- **Confidence set to `emerging` overall**: Claims 1, 2, 4, 5, and 12 rest
  on directly-quotable, specific first-party disclosures (license terms,
  absence of numbers, architecture description, training methodology,
  distribution channels) and are effectively `settled` as statements of
  what Meta claims, even though several (Claims 2, 6, 7) report
  vendor-run, unverified performance figures. Claims 8-11 are Willison's
  own first-person single-session anecdotal testing. No claim in this note
  is independently, third-party verified — hence `emerging` rather than
  `settled` for the note as a whole, consistent with how
  `blog-simonwillison-muse-code-spark-12.md` and
  `blog-simonwillison-inkling-open-weights.md` rated similar
  vendor-announcement-plus-practitioner-test sources.
