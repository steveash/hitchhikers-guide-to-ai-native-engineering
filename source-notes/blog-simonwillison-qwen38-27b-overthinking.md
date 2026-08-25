---
source_url: https://simonwillison.net/2026/Aug/16/qwen-38-27b/
source_type: blog-post
title: "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things"
author: Simon Willison
date_published: 2026-08-16
date_extracted: 2026-08-25
last_checked: 2026-08-25
status: current
confidence_overall: anecdotal
issue: "#2929"
---

# Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things

> Simon Willison's hands-on evaluation of Qwen 3.8 27B (Alibaba's Apache-2
> vision-capable local model, released 2026-08-15) on an M5 Max MacBook Pro
> and an NVIDIA DGX Spark: the model's default `xhigh` reasoning_effort
> produces spectacular over-thinking (21 minutes / 22,276 reasoning tokens
> for a trivial SVG request), vision/bounding-box and coding-agent-loop
> capability both check out, raw throughput (15-30 tok/s locally) trails
> hosted APIs by roughly 3-10x, and Multi-Token Prediction serving gave a
> measured ~72% speed boost over the default GGUF path.

## Source Context

- **Type**: blog-post (simonwillison.net, personal technical blog; part of
  Willison's ongoing "LLMs on personal devices" series, entry 22)
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this corpus (creator of Django, Datasette, and the `llm` CLI
  tool). This is first-person, hands-on practitioner testing — his own two
  machines (M5 Max MacBook Pro, NVIDIA DGX Spark), his own prompts, his own
  recurring "pelican riding a bicycle" benchmark — not a vendor announcement
  or a controlled study. He explicitly frames some findings as amusement
  ("I've been finding the results extremely entertaining") rather than
  rigorous measurement, and flags his own uncertainty where relevant (e.g.
  no stated hardware for the bounding-box latency).
- **Scope**: Covers Qwen 3.8 27B specifically (the 27B open-weight sibling
  of Alibaba's Qwen3.8-Max flagship): the `reasoning_effort` default and its
  practical cost, vision/bounding-box capability, a first attempt at driving
  a coding agent loop (Pi) against a real codebase (Datasette), raw
  token-per-second throughput compared to hosted APIs, and one community
  serving optimization (Multi-Token Prediction via `llama-server`). Does
  NOT cover: Qwen 3.8 27B's benchmark scores against other models,
  quantization levels other than the 17GB Q4_K_M GGUF, non-Apple/non-NVIDIA
  hardware, multi-session/longitudinal use (this is Willison's first two
  days with the model, released 2026-08-15), or independent verification of
  Qwen's self-reported benchmarks (explicitly flagged by Willison himself as
  unverified: "It will be interesting to hear what independent benchmarks
  have to say about the model.").

## Extracted Claims

### Claim 1: Qwen 3.8 27B defaults to `xhigh` reasoning_effort out of the box, and Qwen's own documentation frames this as the intended default for "complex tasks demanding thorough analysis"
- **Evidence**: Direct quote of Qwen's documentation, reproduced by Willison, plus his own confirmation that the LM Studio GGUF build he tested preserves that default.
- **Confidence**: settled (directly quoted vendor documentation, corroborated by the author's own observed runtime behavior)
- **Quote**: "Qwen3.8 comes with official support for `reasoning_effort`, which can be used to adjust reasoning depth and control cost:" followed by the three bulleted levels: "`xhigh` (default): for complex tasks demanding thorough analysis", "`medium`: balancing accuracy and speed", "`low`: efficient reasoning optimizing for speed and cost" (reproduced in full in Concrete Artifacts below)
- **Our assessment**: This directly extends `blog-ronacher-what-is-reasoning.md` Claim 5 (reasoning effort is implemented as system-prompt-baked behavior, not a sampling parameter, illustrated there with GPT-OSS's terse `Reasoning: low` directive and DeepSeek DwarfStar's elaborate multi-sentence directive) with a third concrete provider example: Qwen's three-level `xhigh`/`medium`/`low` naming scheme, defaulting to the highest-effort tier. The naming scheme itself is not new to this corpus — `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 4 already recorded Qwen exposing "low / medium / xhigh reasoning-effort modes", though for the Qwen3.8-**Max** flagship and sourced only to a third-party summary tweet (`@ZhihuFrontier`), with no indication of which mode is the default. What this claim adds is (a) confirmation that the same three-tier scheme carries down to the open-weight 27B variant, (b) vendor documentation that `xhigh` is the *default*, and (c) via Claims 2-4, the measured practical cost of that default. Qwen remains the most aggressive default (`xhigh`) of any provider documented so far in this corpus.

### Claim 2: The `xhigh` default produces spectacular over-thinking on trivial creative prompts — a pelican-riding-a-bicycle SVG took 21 minutes and 22,276 reasoning tokens to produce 3,223 tokens of visible output
- **Evidence**: Direct first-person timing and token-count measurement from Willison's own test run, with a linked reasoning trace for inspection.
- **Confidence**: anecdotal (single run, single prompt, author's own hardware and session — not a controlled or repeated measurement)
- **Quote**: "It took **21 minutes** to generate, using 22,276 reasoning tokens to produce 3,223 tokens of output."
- **Our assessment**: This is the single most citable, concrete cost figure in the source: a roughly 7:1 ratio of reasoning tokens to output tokens on a task with no inherent difficulty (drawing a recognizable SVG). Willison's own verdict — "Was that worth waiting 21 minutes for? Absolutely not." (quoted verbatim in the following paragraph of the source) — makes explicit that this is a practical usability failure, not just a curiosity. This is new, quantified evidence for the general "reasoning-effort defaults can be miscalibrated for local models" pattern; the corpus previously had `blog-fowler-boeckeler-local-models-viability.md` Claim 3 documenting unproductive reasoning loops on small local models qualitatively ("Wait, ...", "Actually, ...") but without a comparably precise token/time cost figure.

### Claim 3: Running the identical SVG prompt with reasoning turned off took just over two minutes (137s, 3,715 tokens) but produced a visibly lower-quality result — a "bad shape" bicycle frame and a less obvious pelican pouch
- **Evidence**: Direct first-person timing/token comparison plus a qualitative before/after visual description, with a linked transcript.
- **Confidence**: anecdotal (single run, single prompt, subjective quality judgment by the author)
- **Quote**: "This one produced **3,715 tokens** and took 137s—just over two minutes." (immediately following, in the source, Willison's mention of running "that same prompt run with reasoning turned off")
- **Our assessment**: This is a real speed/quality tradeoff, not a free lunch: reasoning-off was roughly 9x faster (137s vs 21 minutes) but produced a subjectively worse result on the same creative task. This nuances Claim 2 — the guide-relevant takeaway is not simply "disable reasoning," but "the default level is miscalibrated in the direction of far too much cost for the marginal quality gained," which is a narrower and more defensible claim than "reasoning is unnecessary."

### Claim 4: Even a maximally simple prompt ("draw an svg of a circle") triggered extended over-thinking under the `xhigh` default, and the resulting output was an elaborate, unrequested design rather than what was asked for
- **Evidence**: Direct first-person test with a deliberately trivial prompt, plus a verbatim excerpt of the model's reasoning trace showing it deciding to add scope beyond the request.
- **Confidence**: anecdotal (single run, single prompt)
- **Quote**: "Several minutes later it produced this _absolutely beautiful_ animated circle, which was entirely not what I had asked for!"
- **Our assessment**: This is the sharpest illustration in the source of over-thinking as a scope-creep problem, not just a latency problem: the model's own reasoning trace shows it explicitly deciding to exceed the request ("Simple request — but I want it to be a carefully crafted piece... I can add craft: concentric guide circles... restrained ambient motion"). For an agentic coding context, this is a more concerning failure mode than slowness alone — a model reasoning itself into scope expansion on a simple, well-specified task is a correctness risk (doing the wrong thing carefully) as well as a cost risk.

### Claim 5: Willison's explicit recommendation is to ignore Qwen 3.8 27B's default and run it at low or no reasoning first
- **Evidence**: Direct first-person recommendation, stated as a summary conclusion after the SVG and circle tests.
- **Confidence**: anecdotal (single practitioner's judgment call after a small number of test prompts, not a systematic sweep across reasoning levels)
- **Quote**: "My strong recommendation: ignore that default. Run Qwen 3.8 27B on low or even no reasoning levels at first. It’s a great model, but wow that default setting is a bad place to start."
- **Our assessment**: This directly corroborates `blog-fowler-boeckeler-local-models-viability.md` Claim 3 (disabling reasoning on small local models was "not only faster... but also performed the same to slightly better" in Böckeler's automated eval) from an independent practitioner, independent model generation (Qwen 3.8 27B vs. Qwen3.6 35B MoE), and independent task set (creative SVG generation vs. functional web-frontend tasks). Both sources converge on the same practical guidance — start local models at a low reasoning setting rather than trusting the vendor default — even though they used different models and different evaluation methods. Not filed as a contradiction against Claim 6 below (the bounding-box case where reasoning-off produced a bug): the two findings are reconciled by the source itself as task-dependent, not opposed.

### Claim 6: Qwen 3.8 27B is very good at generating bounding boxes for object detection on a 0-1000 normalized scale, producing an exact match against a real photograph in one shot
- **Evidence**: Direct first-person test using the `llm` CLI tool against a real photograph, with the model's raw JSON output and a rendered visual overlay for verification.
- **Confidence**: anecdotal (single image, single prompt, author's own subjective "such a good match" judgment, though the coordinates and rendered overlay are independently checkable)
- **Quote**: "This is _such a good match_."
- **Our assessment**: This is a concrete, positive vision-capability data point for a 27B local model, using a specific, reproducible method (0-1000 scale bounding box prompting) that Willison notes he has found effective with prior Qwen models too. It corroborates the general finding in this corpus that recent Qwen-family models have strong vision/object-detection capability at relatively small parameter counts, though this is a single-image test, not a benchmark.

### Claim 7: Without reasoning, the same bounding-box task produced boxes in the wrong place inside a self-built HTML labeling tool, whereas with reasoning enabled the tool worked correctly (though massively over-engineered) — leading Willison to reconsider whether the over-thinking is entirely wasted
- **Evidence**: Direct first-person before/after comparison: a tool built by the model with reasoning on (correct box placement, but "massively over-engineered" with an unrequested demo scene) versus the same tool built with reasoning off (boxes rendered in the wrong position).
- **Confidence**: anecdotal (single build, single task, no repeated trials to establish a failure rate)
- **Quote**: "Is all that over-thinking necessary? Maybe it is, at least a bit. I tried with reasoning turned off and got this version, (transcript here), which nearly works but shows the boxes in the wrong place:"
- **Quote (following paragraph, after an intervening screenshot)**: "So without reasoning it didn’t quite one-shot a working tool. I’m sure it could get there with some follow-up prompts, but this is a good example of how reasoning can make a difference."
- **Our assessment**: This is the source's own internal nuance to Claim 5's blanket "run at low/no reasoning" recommendation — for a task involving precise coordinate-scaling math (converting 0-1000 normalized bbox coordinates to actual pixel positions), disabling reasoning produced a functional bug, not just a stylistic difference. Read together with Claims 2-5, the source's overall position is not "reasoning is useless for this model" but "the default effort level is miscalibrated toward far too much cost for open-ended/creative tasks, while some coordinate-math/precision tasks may genuinely benefit from reasoning" — a task-dependent finding, not a blanket rule. This is consistent with (not contradicting) `blog-fowler-boeckeler-local-models-viability.md` Claim 9's separate finding that task characteristics are "one of the biggest factors" determining small local model viability.

### Claim 8: Qwen 3.8 27B can drive a coding agent loop via the Pi harness against a real codebase, producing a correct multi-file answer to an open-ended question and later writing and testing a working Python conversion script from a follow-up prompt
- **Evidence**: Direct first-person session account: Willison configured Pi to route to Qwen 3.8 27B running in LM Studio on the DGX Spark (shared via `tailscale serve`), then ran two real tasks against his own Datasette codebase — an open-ended "how does auth work?" question and a script-writing request — with linked transcripts for both.
- **Confidence**: anecdotal (two tasks, one session, one codebase, one practitioner)
- **Quote**: "After a sequence of reasoning and tool calls that accessed a bunch of different files it produced this reply, which is very solid."
- **Quote (second task)**: "And it built and tested this pi_jsonl_to_md.py, which did exactly what I needed."
- **Our assessment**: This directly extends the corpus's existing Qwen-family coding-agent-viability thread (`blog-simonwillison-georgi-gerganov.md` Claim 1, Gerganov's daily use of the predecessor Qwen3.6-27B for "mundane" maintainer tasks via a stripped Pi harness) with a first, positive practitioner data point for the newer Qwen 3.8 27B specifically: long context, reliable multi-file tool-calling, and a self-contained "build and test a script" task all succeeded in Willison's first session. Also parallels `blog-simonwillison-ornith.md` Claim 8 (a 35B local model "handled with ease" via LM Studio + Pi against the same Datasette codebase) — this is now the corpus's third local-model-plus-Pi-plus-Datasette data point, giving a consistent recurring benchmark task across different local models over time. Willison chose Pi specifically for its short system prompt ("a better fit for trying out smaller models"), the same rationale documented in the Gerganov and Ornith notes.

### Claim 9: Local inference throughput for Qwen 3.8 27B (15-30 tokens/second via LM Studio) trails hosted frontier API models by roughly 3-10x, and this speed gap — not reasoning-effort tuning — is the main practical barrier to daily local use
- **Evidence**: Direct first-person throughput measurement from LM Studio sessions, compared against third-party tracked hosted-API speeds (Artificial Analysis).
- **Confidence**: settled for the local throughput figure (author's own direct, repeated observation: "I’ve been getting around 15-30 tokens a second from LM Studio") / emerging for the hosted comparison (sourced to a named third-party tracker, Artificial Analysis, not independently re-verified by this Miner)
- **Quote**: "I’ve been getting around 15-30 tokens a second from LM Studio. That’s not terrible, but it’s slow enough that it’s going to be hard to win me away from hosted API models, which can return results a whole lot faster. Artificial Analysis track token speed and show OpenAI 5.6 Sol at 74 tokens/second and 5.6 Luna at an impressive 184/second."
- **Our assessment**: This is a concrete, dated (2026-08) throughput data point that quantifies the local-vs-hosted speed gap for a 27B dense model on high-end consumer/prosumer hardware (M5 Max MacBook Pro, NVIDIA DGX Spark). It's directly comparable to `blog-simonwillison-ornith.md` Claim 10 (a 35B MoE model producing SVG output at 103 tokens/second, also via LM Studio) — the roughly 3-7x throughput difference between Qwen 3.8 27B (15-30 tok/s, dense) and Ornith-1.0's 35B MoE variant (103 tok/s) is consistent with Willison's own architectural explanation in Claim 10 below (dense models are memory-bandwidth-bound in a way MoE models are not). Practitioners should read local-model throughput figures as architecture-dependent (dense vs. MoE), not simply parameter-count-dependent.

### Claim 10: Community-driven Multi-Token Prediction (MTP) serving via `llama-server` gave a measured ~72% speed improvement over LM Studio's default GGUF serving path, per a comparative benchmark Willison ran using GPT-5.6 in Codex
- **Evidence**: Direct first-person report of a specific `llama-server` invocation with MTP flags, plus a linked comparative benchmark result attributed to a run by "GPT-5.6 in Codex."
- **Confidence**: emerging (a single comparative benchmark run, on the author's own DGX Spark hardware, using an LLM-run benchmarking process rather than a hand-verified methodology — the exact benchmark script/methodology is not reproduced in the post itself, only linked)
- **Quote**: "I had GPT-5.6 in Codex run a comparative benchmark on the Spark and the `--spec-type draft-mtp` server outperformed the LM Studio default GGUF by around 72%."
- **Our assessment**: This is a specific, actionable optimization lead for practitioners running Qwen 3.8 27B (or other MTP-supporting models) locally: switching from LM Studio's default GGUF serving to `llama-server` with `--spec-default --spec-type draft-mtp --reasoning-preserve` is reported to nearly double effective throughput. It directly extends the corpus's existing MTP thread (`blog-latentspace-ainews-harness-drift-quantization.md` Claim 5, documenting Tencent's Hy3 shipping 1-bit/4-bit quantized weights "servable on a single GPU via llama.cpp with MTP enabled") with a second, independent MTP data point — this time a measured throughput percentage for a different model family (Qwen vs. Hy3), attributed to a specific `llama.cpp` invocation (credited by Willison to a tweet from Georgi Gerganov, llama.cpp's creator, who is separately documented in this corpus at `blog-simonwillison-georgi-gerganov.md` as a Qwen local-model practitioner himself).

### Claim 11: Qwen 3.8 27B is a dense (non-Mixture-of-Experts) model, and Willison attributes its comparatively slow performance on both his test machines to dense models' higher memory-bandwidth requirements relative to MoE architectures
- **Evidence**: Direct first-person architectural explanation offered as Willison's own closing analysis.
- **Confidence**: emerging (a plausible, standard architectural explanation, but presented as the author's own inference rather than a benchmarked or vendor-confirmed claim)
- **Quote**: "That’s the catch with these dense (non-Mixture-of-Experts) models—they require a whole lot of memory bandwidth to perform well, and neither of the machines I have access to are top performers in that regard."
- **Our assessment**: This gives practitioners a concrete architectural reason to expect the throughput gap in Claim 9: dense models are memory-bandwidth-bound in a way sparse MoE models (like the corpus's other local-model data points — Ornith-1.0's 35B MoE at 103 tok/s, `blog-simonwillison-ornith.md` Claim 10; DeepSeek V4 Flash's MoE architecture referenced elsewhere in the corpus) are not to the same degree. This is a useful selection heuristic: when local-hardware memory bandwidth (not just RAM capacity) is the constraint, an MoE model of similar or larger total parameter count may outperform a smaller dense model on raw throughput.

## Concrete Artifacts

### Qwen's own reasoning_effort documentation (verbatim, as quoted by Willison)
```
Qwen3.8 comes with official support for reasoning_effort, which can be used
to adjust reasoning depth and control cost:

  * xhigh (default): for complex tasks demanding thorough analysis
  * medium: balancing accuracy and speed
  * low: efficient reasoning optimizing for speed and cost

Source: simonwillison.net/2026/Aug/16/qwen-38-27b/, quoting Qwen's own
model documentation (huggingface.co/Qwen/Qwen3.8-27B)
```

### Bounding-box detection prompt and output (verbatim)
```
Command:
  llm -a https://static.inaturalist.org/photos/714731804/large.jpg \
    -m lmstudio/qwen/qwen3.8-27b \
    'Return JSON bounding boxes for the pelicans in this photo, 0-1000 scale for each dimension'

Output:
  [
    {"bbox_2d": [195, 290, 370, 780], "label": "pelicans"},
    {"bbox_2d": [445, 320, 675, 850], "label": "pelicans"}
  ]

Source: simonwillison.net/2026/Aug/16/qwen-38-27b/ (2026-08-16)
```

### Pi agent configuration for Qwen 3.8 27B via LM Studio + Tailscale (verbatim, `~/.pi/agent/models.json`)
```json
{
  "providers": {
    "spark": {
      "baseUrl": "https://spark-18b3.tail68a31.ts.net/v1",
      "api": "openai-responses",
      "apiKey": "dummy",
      "models": [
        {
          "id": "qwen3.8-27b",
          "reasoning": true
        }
      ]
    }
  }
}

Invocation: pi --provider spark --model qwen3.8-27b
Source: simonwillison.net/2026/Aug/16/qwen-38-27b/ (2026-08-16)
```

### `llama-server` invocation for Multi-Token Prediction (MTP) serving (verbatim)
```
llama serve \
 -hf  ggml-org/Qwen3.8-27B-GGUF:Q4_K_M \
 -hfd ggml-org/Qwen3.8-27B-GGUF:Q4_0 \
 --spec-default \
 --spec-type draft-mtp \
 --reasoning-preserve

Result: ~72% throughput improvement over LM Studio's default GGUF serving,
per a comparative benchmark run by "GPT-5.6 in Codex" on the author's NVIDIA
DGX Spark.

Source: simonwillison.net/2026/Aug/16/qwen-38-27b/ (2026-08-16), crediting
a tweet from Georgi Gerganov (llama.cpp creator)
```

## Cross-References

### Cross-reference verification notes
`blog-ronacher-what-is-reasoning.md`, `blog-fowler-boeckeler-local-models-viability.md`,
`blog-simonwillison-georgi-gerganov.md`, `blog-simonwillison-ornith.md`,
`blog-latentspace-ainews-harness-drift-quantization.md`,
`blog-latentspace-ainews-qwen38-max-27b-launch.md`, and
`blog-simonwillison-cors-chat.md` were each re-read
directly and the specific claim numbers cited above were confirmed against
each note's numbered `### Claim N:` headings in document order before
writing this section, per MINER.md §4b. The corpus was additionally
keyword-searched for "Qwen 3.8" and "DGX Spark" across `source-notes/*.md`
to catch same-model and same-hardware notes that a topic-only scan would
miss.

- **Corroborates**:
  - `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 4 (Qwen3.8-Max
    "API exposes low / medium / xhigh reasoning-effort modes," per a
    third-party summary tweet attributed to `@ZhihuFrontier`): Claim 1 here
    confirms that same three-tier scheme in the open-weight 27B variant,
    upgrading the evidence from a third-party summary to Qwen's own quoted
    model documentation, and adds the piece the launch note did not have —
    which tier is the default (`xhigh`, the highest). The launch note is
    this corpus's record of the model family at announcement time
    (2026-08-04); this note is the hands-on follow-up on the 27B
    open-weight release (2026-08-16).
  - `blog-simonwillison-cors-chat.md` Claim 1 (Willison built the CORS Chat
    browser client in a single day "to help test Qwen 3.8 27B running in LM
    Studio on both my M5 MacBook Pro and an NVIDIA DGX Spark"): the closest
    cross-reference in the corpus — same author, same model, same two test
    machines (this post specifies the Mac as a "128GB M5 Max MacBook Pro"),
    same LM Studio runtime, published one day apart (2026-08-15 and
    2026-08-16). That note is the *tooling* Willison built to run the
    evaluation; this note is the *findings* from it. The cors-chat note's
    own Cross-References section anticipates this one, recording that
    benchmark results for Qwen 3.8 27B "appear in Willison's separate
    next-day post" and were "not yet present in this corpus as of this
    extraction" — this note closes that gap, and the link should be read as
    reciprocal. Practical note for the Smith: the two are best cited
    together, since cors-chat documents the reasoning-effort control
    surface (its Claim 7 — reasoning effort "none through max" exposed in
    the UI) that makes the override recommended in Claim 5 here
    operationally easy.
  - `blog-fowler-boeckeler-local-models-viability.md` Claim 3 (disabling
    reasoning on small local models was faster and same-to-slightly-better
    quality in an automated eval): Claim 5 here (Willison's "run at low or
    no reasoning" recommendation) reaches the same practical conclusion
    from an independent practitioner, model, and task set.
  - `blog-simonwillison-georgi-gerganov.md` Claim 1 (Gerganov's daily,
    productive use of the predecessor Qwen3.6-27B for coding tasks via a
    stripped Pi harness): Claim 8 here extends the same "Qwen 27B-class
    model + Pi harness" pattern to the newer Qwen 3.8 27B generation, with
    a first positive data point (though only a single session, not
    Gerganov's 1.5 months of use).
  - `blog-simonwillison-ornith.md` Claim 8 (a 35B local model "handled with
    ease" via LM Studio + Pi against the same Datasette codebase) and
    Claim 10 (103 tokens/second SVG generation via the same tooling
    combination): both are direct methodological corroboration — this
    source uses the identical LM Studio + Pi + Datasette combination as its
    coding-agent test, and Claim 9 here supplies a comparable throughput
    figure (15-30 tok/s) for a differently-architected (dense vs. MoE)
    model of similar parameter count.
  - `blog-latentspace-ainews-harness-drift-quantization.md` Claim 5
    (Tencent Hy3 shipping 1-bit/4-bit quantized weights "servable on a
    single GPU via llama.cpp with MTP enabled"): Claim 10 here gives a
    second, independent MTP data point — this time a measured ~72%
    throughput improvement for a different model family (Qwen), rather
    than only a qualitative "servable on a single GPU" deployment claim.

- **Contradicts**: None filed. One candidate tension was considered and
  ruled out per MINER.md §4a: Claim 5 (Willison's blanket-sounding
  recommendation to run at low/no reasoning) initially appears to sit
  against Claim 7 (disabling reasoning produced a functional bug in the
  bounding-box tool). This is not filed as a contradiction because the
  source itself explicitly reconciles the two findings as task-dependent
  ("Is all that over-thinking necessary? Maybe it is, at least a bit") —
  Willison's own final position is nuanced (low/no reasoning as a
  starting point for open-ended/creative tasks; reasoning may matter more
  for tasks with a precise coordinate-math correctness dimension), not two
  claims that materially oppose each other on the same question. This is
  recorded in Claim 7's "Our assessment" rather than as a filed
  contradiction, consistent with how this corpus treats other
  task-dependent local-model findings (e.g.
  `blog-fowler-boeckeler-local-models-viability.md` Claim 9's "task choice
  is the biggest factor" framing).

- **Extends**:
  - `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 11
    (TeortaxesTex's speculation that Qwen 3.8 Max may be
    "distillable/OPD-able into Qwen 3.8 27B for task-specific parity,
    implying a route from flagship capability to laptop-deployable
    specializations"): Claims
    8-9 here are the corpus's first real-world test of that launch-time
    speculation. The "laptop-deployable" framing partly holds and partly
    does not — the 27B does drive a real agentic coding loop against a real
    codebase successfully (Claim 8), supporting the capability half of the
    speculation, but Claim 9's measured 15-30 tok/s on a 128GB M5 Max
    MacBook Pro and a DGX Spark shows that *deployability* is bounded by
    throughput rather than capability, with Claim 11 here supplying the
    architectural reason (dense models are memory-bandwidth-bound). Read
    together, the launch note's speculative "route to laptop deployment"
    gains a concrete qualifier: on 2026-08 prosumer hardware the route
    exists but runs 3-10x slower than hosted APIs. This also sharpens
    launch-note Claim 8's separate infrastructure-cost argument (the 2.4T
    flagship is impractical to self-host) — the 27B is practical to
    self-host, just slow.
  - `blog-ronacher-what-is-reasoning.md` Claim 5 (reasoning effort as
    system-prompt-baked behavior, illustrated with GPT-OSS's `Reasoning:
    low` and DeepSeek DwarfStar's elaborate directive): Claim 1 here adds a
    third concrete provider naming scheme (Qwen's `xhigh`/`medium`/`low`),
    notable for defaulting to the single highest-effort tier of any
    provider documented so far in this corpus.
  - `blog-simonwillison-georgi-gerganov.md` and `blog-simonwillison-ornith.md`
    (the corpus's existing Qwen/Pi-family local-coding-agent evidence):
    Claim 8 here is the corpus's first data point specifically for Qwen
    3.8 27B (as distinct from Qwen3.6-27B or the unrelated Ornith-1.0
    model family) driving an agentic coding loop.

- **Novel**:
  - **The measured cost of the `xhigh` default** (Claims 2-4): the corpus's
    first quantified reasoning-effort-default cost figures (21 minutes /
    22,276 reasoning tokens vs. 137s / 3,715 tokens for an identical
    prompt) for any local model. Scoped deliberately: the
    `xhigh`/`medium`/`low` *naming scheme* of Claim 1 is **not** novel to
    this corpus — `blog-latentspace-ainews-qwen38-max-27b-launch.md`
    Claim 4 already documented those three modes for Qwen3.8-Max at launch.
    What is new here is that `xhigh` is the shipped default, that the
    scheme carries down to the open-weight 27B, and above all the measured
    price of leaving that default alone.
  - **The over-thinking-as-scope-creep failure mode** (Claim 4 — the model
    reasoning itself into an unrequested elaborate design rather than the
    simple circle asked for): new to the corpus; prior local-model
    over-thinking documentation (Böckeler) covers unproductive reasoning
    loops but not scope expansion specifically.
  - **The task-dependent reasoning-effort nuance** (Claim 7 — reasoning
    off caused a functional coordinate-placement bug in a self-built tool):
    a new counterpoint to the general "disable reasoning for local models"
    guidance, grounded in a specific precision-dependent task type.
  - **Local-vs-hosted throughput comparison figures** (Claim 9 — 15-30
    tok/s local vs. 74-184 tok/s hosted, per Artificial Analysis): new,
    dated (2026-08) quantified data point.
  - **The measured MTP speed improvement** (Claim 10 — ~72% via
    `llama-server --spec-type draft-mtp`) and **the dense-vs-MoE
    memory-bandwidth explanation for local throughput** (Claim 11): both
    new to the corpus at this level of specificity.

## Guide Impact

- **Chapter 02 (Harness Engineering) — reasoning-effort defaults for local
  models**: Add Qwen 3.8 27B's `xhigh` default and its measured cost
  (Claim 2: 21 minutes / 22,276 reasoning tokens for a trivial SVG prompt)
  as a concrete, citable example of a vendor reasoning-effort default that
  is badly miscalibrated for practical local use. Recommend practitioners
  check and override the default reasoning_effort level immediately when
  adopting a new local model, rather than assuming a sensible default —
  extending the corpus's existing reasoning-effort guidance
  (`blog-ronacher-what-is-reasoning.md`, `docs-github-copilot-cca-reasoning-level.md`)
  with a specific worst-case cost figure.

- **Chapter 02/03 (Harness Engineering / Verification) — task-dependent
  reasoning tradeoffs**: Add Claim 7 (reasoning-off produced a functional
  bug in a coordinate-math tool, while reasoning-on succeeded but was
  over-engineered) as a caution against a blanket "always disable
  reasoning for local models" rule. Recommend framing reasoning-effort
  selection as task-dependent — likely lower for open-ended/creative
  generation, likely higher for tasks requiring precise numeric/coordinate
  correctness — pending more systematic evidence.

- **Chapter 04 (Model Selection & Cost) — local throughput expectations**:
  Add Claim 9's concrete throughput comparison (15-30 tok/s local for a
  dense 27B model vs. 74-184 tok/s for hosted frontier APIs) as a current,
  dated data point for teams weighing local-model deployment against
  hosted APIs on pure latency/throughput grounds — pairing with Claim 11's
  architectural explanation (dense models are memory-bandwidth-bound) so
  practitioners know to weight MoE architecture favorably when raw local
  throughput matters more than parameter count.

- **Chapter 04 (Model Selection & Cost) — MTP as a serving optimization**:
  Add Claim 10 (the `llama-server --spec-type draft-mtp` ~72% throughput
  gain) as a concrete, actionable optimization for teams already committed
  to self-hosting an MTP-capable open-weight model, extending the corpus's
  existing MTP thread with a second measured data point from a different
  model family.

## Extraction Notes

- **Fetch method**: fetched the raw page HTML directly via `curl` with a
  browser user-agent (HTTP 200), then converted to markdown with
  `html2text` (link-preserving, no line-wrapping) before extracting any
  quotes. All `Quote` fields in this note are copied character-for-character
  from that locally-parsed text, not from a WebFetch summarizer paraphrase.
- **No sub-pages followed as substantive additional sources**: the post
  links to several gists/transcripts (reasoning traces, session transcripts,
  a built HTML tool) that serve as supporting evidence for claims already
  extracted from the main post text; these were referenced but not
  separately fetched and mined as independent sources, consistent with
  MINER.md's up-to-5-page budget being reserved for substantive linked
  *pages* (e.g., documentation, related articles) rather than raw
  transcript/log artifacts that only corroborate what the post itself
  already states in prose. The linked Qwen HuggingFace model card
  (huggingface.co/Qwen/Qwen3.8-27B) and benchmark page were not
  independently fetched; Claim 1's Qwen documentation quote is taken as
  relayed by Willison, not independently re-verified against Qwen's own
  page by this Miner.
- **No contradiction issue filed** — see Cross-References → Contradicts
  above for the one candidate tension considered and ruled out as a
  task-dependent nuance rather than a genuine contradiction.
- **Quote verification**: every `Quote` field in this note was checked
  programmatically as a character-for-character substring of the raw
  fetched source text (after stripping Markdown link syntax `[text](url)`
  down to its rendered anchor text, since the source contains several
  in-line links mid-sentence). Two quotes spanning a paragraph break with
  an intervening image (Claim 7) were kept as two separate labeled `Quote`
  fields rather than spliced into one, per MINER.md §2a point 3.
- **Confidence rated `anecdotal` overall**: every claim originates from a
  single practitioner's first two days of hands-on testing (one model,
  two machines, a handful of prompts, no repeated trials or statistical
  sampling). Several individual claims are rated `settled` where they
  reproduce directly quotable, independently checkable artifacts (Qwen's
  own documentation text, the author's own repeatedly-observed local
  throughput range, the `llama-server`/Pi configuration snippets); the
  rest are rated `anecdotal` or `emerging` to reflect single-run
  measurements, subjective quality judgments, or the author's own hedged
  architectural inferences. The note-level rating reflects the overall
  character of the source: a credible, well-instrumented practitioner
  first-look, not a controlled or replicated study.
