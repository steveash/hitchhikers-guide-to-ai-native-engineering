---
source_url: https://simonwillison.net/2026/Apr/20/llm-openrouter/
source_type: blog-post
title: "llm-openrouter 0.6"
author: Simon Willison
date_published: 2026-04-20
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: anecdotal
issue: "#442"
---

# llm-openrouter 0.6

> A minimal release announcement for the llm-openrouter plugin, notable for introducing `llm openrouter refresh` — a command that lets practitioners immediately access newly-listed OpenRouter models without waiting for the local cache to expire — motivated by Willison wanting to test Kimi 2.6 the moment it appeared on OpenRouter.

## Source Context

- **Type**: blog-post (Willison link-blog / release-note format; ~150 words of original text; links out to GitHub release page and a Gist transcript of the Kimi 2.6 pelican session)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI + llm-openrouter plugin itself. This is first-party release documentation. His "pelican on a bicycle" prompt is his recurring informal cross-model creative-code benchmark, applied consistently across his posts.
- **Scope**: Covers a single new feature in llm-openrouter 0.6 (`llm openrouter refresh`), the motivating use case (testing Kimi 2.6 on arrival), and the behavioral result of that test (Kimi chose HTML+JavaScript output over plain SVG). Does NOT cover any other OpenRouter models, performance benchmarks, cost comparisons, or API changes.

## Extracted Claims

### Claim 1: The `llm openrouter refresh` command refreshes the plugin's model list without waiting for the local cache to expire
- **Evidence**: Verbatim release note text from both the blog post and the GitHub release page (https://github.com/simonw/llm-openrouter/releases/tag/0.6). The feature is the sole change in 0.6.
- **Confidence**: settled (first-party release documentation from the plugin's author)
- **Quote**: "`llm openrouter refresh` command for refreshing the list of available models without waiting for the cache to expire."
- **Our assessment**: The command addresses a real operational friction: when a new model appears on OpenRouter, it is not immediately visible via `llm models` because the plugin caches its model list. Before 0.6, practitioners had to wait for the cache TTL to expire or manually delete the cache. The `refresh` subcommand makes this explicit and imperative — a one-command fix for the "model isn't showing up yet" problem. This is a small but practitioner-facing improvement to the daily-workflow loop of evaluating newly-released models via the CLI.

### Claim 2: Willison created the `llm openrouter refresh` command specifically so he could test Kimi 2.6 immediately on its OpenRouter listing
- **Evidence**: Willison's direct statement in the post, provided as the motivating context for the release.
- **Confidence**: settled (first-party; author explaining his own motivation)
- **Quote**: "I added this feature so I could try Kimi 2.6 on OpenRouter as soon as it became available there."
- **Our assessment**: The motivation matters for harness engineering: a practitioner noticed model-evaluation latency as a friction point and built the fix into the tool itself. This is the pattern of iterative harness improvement — identifying workflow friction, solving it with a targeted command, and releasing the fix quickly. The fact that `llm openrouter refresh` ships the same day Willison is testing Kimi 2.6 (April 20, 2026) is evidence of tight feedback between model availability and tooling response.

### Claim 3: Kimi 2.6, when given the standard pelican-on-a-bicycle prompt via `llm` CLI + OpenRouter, chose to produce an HTML page with a JavaScript-driven interactive animation UI rather than a plain SVG
- **Evidence**: Willison's direct observation in the post, consistent with the linked Gist transcript (https://gist.github.com/simonw/ecaad98efe0f747e27bc0e0ebc669e94) which shows an HTML page with playback controls.
- **Confidence**: anecdotal (single observation, one model, one prompt)
- **Quote**: "Here's its pelican - this time as an HTML page because Kimi chose to include an HTML and JavaScript UI to control the animation."
- **Our assessment**: The "Kimi chose to include" framing is significant: Willison's prompt was for a pelican animation, not for an interactive UI. Kimi added the interactive layer (play/pause, speed slider, wing-flap intensity slider) unprompted. This is a variant of the same "scope creep" behavior documented for GLM-5.1 (which spontaneously added CSS animations alongside an SVG — `blog-simonwillison-glm51.md` Claim 2). Both models exceeded the literal task specification in the same creative direction. The difference: Kimi's output is interactive at runtime (the user can control the animation), whereas GLM-5.1's CSS animations ran automatically. For harness engineers: large frontier models may interpret a creative-code prompt as an invitation to add usability affordances. If you want exactly a plain SVG, you need a more constraining prompt.

### Claim 4: Kimi 2.6's JavaScript-based animation uses `requestAnimationFrame` for motion control, inverse kinematics for leg articulation, and deliberately avoids CSS animations for SVG elements
- **Evidence**: Gist transcript (the HTML source for the pelican animation). The Gist shows interactive controls including a speed slider (range 0–20) and wing-flap intensity slider (range 0–10). The technical implementation details (requestAnimationFrame, inverse kinematics, CSS-animation avoidance) come from the Gist transcript.
- **Confidence**: anecdotal (single session, creative task only; technical choices reflect Kimi's internal code-generation policy, not a user constraint)
- **Quote**: (no direct quote from the main post; implementation details are in the Gist transcript, not reproduced verbatim here — see Extraction Notes)
- **Our assessment**: The avoidance of CSS animations is architecturally correct for this use case: CSS `transform` animations on SVG elements can conflict with inline SVG `transform` attributes (exactly the bug GLM-5.1 encountered in `blog-simonwillison-glm51.md` Claim 3). Kimi's choice of pure JavaScript for animation control sidesteps the CSS/SVG transform interaction problem entirely. Whether this was intentional model knowledge or coincidental design is unknowable from the transcript alone, but the output is technically sound. The interactive controls (speed and wing-flap intensity sliders) go substantially beyond a minimal pelican animation — the model added usability features for a demo context without being asked.

### Claim 5: llm-openrouter has evolved from a basic model-access wrapper in 2023 to a full-capability plugin by 2026, accumulating tool calling, reasoning options, web search grounding, schema support, image attachments, and async access across seven releases
- **Evidence**: Complete version history from GitHub releases (https://github.com/simonw/llm-openrouter/releases). Each release's notes are verbatim from the GitHub API.
- **Confidence**: settled (GitHub release history is authoritative; feature claims are verifiable against the released code)
- **Quote**: "Support for tool calling" and "Support for reasoning options, for example `llm -m openrouter/openai/gpt-5 'prove dogs exist' -o reasoning_effort medium`" (from the 0.5 release notes)
- **Our assessment**: The version progression shows llm-openrouter tracking the `llm` library's capability surface closely: as the base `llm` CLI added schemas, tools, reasoning, and async (across 0.28–0.31), llm-openrouter added the corresponding OpenRouter-facing support. By 0.5 (September 2025), the plugin supports the full `-o reasoning_effort` option documented for other models in `blog-simonwillison-llm031.md`. By 0.6, the plugin adds operational lifecycle management (`refresh`). The trajectory suggests llm-openrouter is a maintained, production-adjacent tool — not a proof-of-concept.

## Concrete Artifacts

### llm-openrouter version history (from GitHub releases, verbatim)

```
Version  Published     Release notes (verbatim from GitHub)
-------  -----------   --------------------------------------------------
0.1      2023-08-21    Initial release. Adds support for models hosted by openrouter.ai
0.2      2024-05-03    Added missing httpx dependency; respects OPENROUTER_KEY env var;
                       fixed error if urllib3 not installed
0.3      2024-12-08    Enable image attachments for models that support images;
                       provide async model access; fix docs for OPENROUTER_KEY env var
0.4      2025-03-10    Schema support for OpenRouter models that support structured output;
                       llm openrouter key command; -o online 1 for web search grounding;
                       llm openrouter models command (--json, --free options);
                       -o provider '{JSON}' for custom provider routing
0.4.1    2025-04-23    Fixed a bug with llm openrouter models
0.5      2025-09-20    Support for tool calling; support for reasoning options
                       (e.g. -o reasoning_effort medium)
0.6      2026-04-20    llm openrouter refresh command for refreshing the list of
                       available models without waiting for the cache to expire

Source: github.com/simonw/llm-openrouter/releases (GitHub API, verified 2026-05-25)
```

### CLI commands added across the release lifecycle

```bash
# 0.1+ — basic model access pattern (unchanged core)
llm install llm-openrouter
llm -m openrouter/<provider>/<model> 'Your prompt here'

# 0.3+ — image attachments
llm -m openrouter/<provider>/<model> 'Describe this image' -a image.png

# 0.4+ — web search grounding (Exa-powered)
llm -m openrouter/<provider>/<model> -o online 1 'What happened today?'

# 0.4+ — list available models
llm openrouter models           # full list
llm openrouter models --free    # free-tier models only
llm openrouter models --json    # JSON output

# 0.5+ — tool calling and reasoning options
llm -m openrouter/openai/gpt-5 'prove dogs exist' -o reasoning_effort medium

# 0.6 — refresh model list immediately
llm openrouter refresh
```

*Source: Simon Willison, github.com/simonw/llm-openrouter/releases, 2023–2026*

### Kimi 2.6 pelican session CLI invocation (inferred from post + Gist)

```bash
# Install/update plugin and refresh model list
llm install llm-openrouter
llm openrouter refresh

# Run the pelican benchmark against Kimi K2.6 via OpenRouter
llm -m openrouter/moonshotai/kimi-k2.6 'Generate an SVG of a pelican on a bicycle'
```

*Source: Simon Willison, simonwillison.net/2026/Apr/20/llm-openrouter/ — commands inferred from post context; Kimi K2.6 OpenRouter slug from openrouter.ai/moonshotai/kimi-k2.6*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-glm51.md` Claim 6 (lines 56–61): The `llm` CLI + OpenRouter plugin providing a consistent interface for testing frontier-scale models is the exact same workflow demonstrated here with Kimi 2.6. The 0.6 `refresh` command extends that workflow's operability — no new paradigm, just reduced friction.
  - `blog-simonwillison-glm51.md` Claim 2 (lines 32–36): GLM-5.1's spontaneous HTML+CSS output is the closest prior example of a model exceeding the literal pelican prompt with an unprompted UI layer. This source's Claim 3 (Kimi 2.6's HTML+JavaScript interactive controls) is a second instance of the same "scope creep" behavior pattern, now in a different model and with an interactive output rather than auto-animated CSS.
  - `blog-simonwillison-deepseek-v4.md` Claim 9 (lines 82–88): Willison used the same `llm` CLI + llm-openrouter workflow to test DeepSeek V4, establishing the consistency of this toolchain as his cross-model test harness.

- **Contradicts**: None identified. Kimi 2.6's choice of JavaScript over CSS (Claim 4) does not contradict the GLM-5.1 CSS approach — both are valid for pelican animations; the technical choice (avoid CSS animations for SVG) is sound for different reasons in each case.

- **Extends**:
  - `blog-simonwillison-glm51.md` Claim 6: The `refresh` command is an explicit operational improvement to the `llm` + OpenRouter harness pattern — adding lifecycle management (model list currency) to the existing model-access workflow.
  - `blog-simonwillison-llm031.md`: llm 0.31 was published four days after this post (April 24, 2026) and added native GPT-5.5 access to the base `llm` CLI. The same week saw both the llm-openrouter plugin gain model-refresh capability (April 20) and the base `llm` CLI gain GPT-5.5 native support (April 24) — consistent with a pattern of rapid, coordinated tooling improvements across the `llm` ecosystem.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 6: The Batch Issue 351 (May 1, 2026) documents Kimi K2.6's architecture (1T parameters, 32B active, 300 parallel subagents). This post is the first in-corpus demonstration of Kimi K2.6 via the `llm` CLI — the access path that practitioners would use to evaluate the model documented in The Batch.

- **Novel**:
  - **`llm openrouter refresh` as an explicit model-list lifecycle command**: No prior note in the corpus discusses the model-cache latency problem in the `llm` CLI ecosystem or the refresh pattern as a solution. This is the first in-corpus documentation of this operational primitive.
  - **Second in-corpus instance of a model spontaneously producing interactive JavaScript controls (beyond the literal SVG prompt)**: The GLM-5.1 case (CSS animations) was the first; Kimi 2.6 (JavaScript UI with sliders) is the second. Two instances strengthen the claim that frontier models interpret creative-code prompts as invitations to add usability affordances.
  - **First in-corpus observation of Kimi K2.6 via the `llm` CLI**: Prior notes mention Kimi K2.6 as a model (from The Batch's benchmarking) but do not document the CLI access path for testing it.

## Guide Impact

- **Chapter 01 (Daily Workflows — `llm` CLI Tooling)**: If the guide documents the `llm install llm-openrouter` + `llm -m openrouter/...` workflow (as recommended in `blog-simonwillison-glm51.md` Guide Impact), add `llm openrouter refresh` as the operational command for when a newly-announced model does not appear in `llm models`. This closes the loop on the "model just announced, how do I test it now?" question. The concrete sequence: `llm openrouter refresh && llm -m openrouter/<slug> '...'`.
- **Chapter 02 (Harness Engineering — Model Selection Interface)**: The `llm openrouter models --free` and `llm openrouter models --json` subcommands (added in 0.4, April 2025) provide programmatic access to OpenRouter's model catalogue. If the guide covers model selection tooling, these commands are worth noting as a CLI-native way to enumerate and filter OpenRouter's full model list without a separate API call.
- **Chapter 01 or 04 (Prompt Design / Model Behavior)**: Claim 3 (Kimi 2.6 adding interactive JS controls unprompted) and the corroborating GLM-5.1 case provide evidence for a guide principle: if you prompt a large model with a creative-code task and want literal output (just the SVG), you should constrain the output format explicitly. "Generate an SVG of a pelican on a bicycle" will sometimes yield an HTML page with an interactive UI. Document this as a "prompt scope" consideration — models at frontier scale often interpret ambiguous creative tasks as invitations for richer output.

## Extraction Notes

- **Thin source, as expected**: The post is ~150 words of original text (title, one feature bullet, two explanatory sentences, one pelican image, one transcript link). The Gist transcript is the richest adjacent artifact, but it is the output of the model session rather than editorial content from Willison. WebFetch of the Gist returned a structured summary, not verbatim text; all Gist-sourced claims (Claim 4) are marked accordingly and no verbatim Gist text is quoted.
- **No sub-pages followed beyond GitHub releases and PyPI**: The Kimi K2.6 blog post (kimi.com/blog/kimi-k2-6) and OpenRouter listing (openrouter.ai/moonshotai/kimi-k2.6) are linked from the post but are out-of-scope secondary sources. The Gist animation HTML was not followed in detail for the same reason.
- **Version table dates verified against PyPI and GitHub releases**: All dates in the Concrete Artifacts version table are sourced directly from GitHub Releases API and confirmed against PyPI history. The correct dates are: 0.1 → 2023-08-21, 0.2 → 2024-05-03, 0.3 → 2024-12-08, 0.4 → 2025-03-10, 0.4.1 → 2025-04-23, 0.5 → 2025-09-20, 0.6 → 2026-04-20. Version 0.4.1 is included. (Note: a prior mining attempt on this source — PR #663, closed 2026-05-24 — contained incorrect years for 0.1–0.4 in the version table; this note uses the correct PyPI/GitHub dates.)
- **Cross-reference verification performed**:
  - `blog-simonwillison-glm51.md` Claim 6 confirmed at lines 56–61 (the `llm` CLI + OpenRouter unified interface; `-c` continuation flag).
  - `blog-simonwillison-glm51.md` Claim 2 confirmed at lines 32–36 (spontaneous HTML+CSS output unprompted).
  - `blog-simonwillison-deepseek-v4.md` Claim 9 confirmed at lines 82–88 (OpenRouter pelican test via `llm` CLI; no direct quote on test method).
  - `blog-simonwillison-llm031.md` date_published 2026-04-24 confirmed at frontmatter line 6 — same-week characterization verified.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 6 confirmed at lines 61–66 (Kimi K2.6 parallel subagent architecture).
