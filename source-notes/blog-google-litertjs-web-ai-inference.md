---
source_url: https://developers.googleblog.com/litertjs-googles-high-performance-web-ai-inference/
source_type: blog-post
title: "LiteRT.js, Google's high performance Web AI Inference"
author: "Ping Yu, Marko Ristić, Matthew Soulanille, Chintan Parikh (Google)"
date_published: 2026-07-09
date_extracted: 2026-07-12
last_checked: 2026-07-12
status: current
confidence_overall: emerging
issue: "#1786"
---

# LiteRT.js, Google's high performance Web AI Inference

> Google announces LiteRT.js, a JavaScript binding of its native on-device LiteRT runtime that runs `.tflite` models directly in the browser via WebAssembly, claiming up to 3x speedup over prior web ML runtimes and 5-60x GPU/NPU speedup over CPU, with concrete conversion tooling (PyTorch → LiteRT), a simple JS API, and named integrations (Ultralytics YOLO, TensorFlow.js interop) — a vendor-driven alternative to the ONNX-Runtime-Web-based browser inference stack documented elsewhere in this corpus via Simon Willison's vibe-coding experiments.

## Source Context

- **Type**: blog-post (official Google Developers Blog, published July 9, 2026,
  bylined by four named Google engineers/PM — Ping Yu, Marko Ristić, Matthew
  Soulanille [Software Engineers], Chintan Parikh [Product Manager] — a
  first-party product/technology announcement rather than an independent
  technical deep-dive). Two linked sub-pages were fetched directly for
  corroborating technical detail: the LiteRT.js overview/get-started
  documentation (`developers.google.com/edge/litert/web/get_started` and
  `ai.google.dev/edge/litert/web`, which render the same content) covering
  installation, PyTorch conversion, the run-model code path, and TensorFlow.js
  migration guidance.
- **Author credibility**: First-party Google Developers Blog post with four
  named authors (three engineers, one PM), consistent with Google's practice
  for other LiteRT/Gemma-family posts already in this corpus (compare
  `blog-google-gemma-4-12b-developer-guide.md`, six named Google/DeepMind
  authors). This is vendor-authored product announcement copy — performance
  benchmarks are self-reported and should be read as vendor-asserted rather
  than independently verified.
- **Scope**: Covers LiteRT.js's architecture (native runtime exposed to the
  browser via WebAssembly instead of JS-based kernels), its three hardware
  backends (XNNPACK/CPU, ML Drift/GPU via WebGPU, WebNN/NPU), PyTorch
  conversion and quantization tooling, a minimal JS API example, three
  benchmarked/demoed model integrations (Ultralytics YOLO, Depth Anything,
  Real-ESRGAN), and a TensorFlow.js interop migration path. Does NOT cover:
  independent third-party benchmarking, WebNN production availability
  (explicitly described as "upcoming"/"experimental"), pricing (there is
  none — it's an open npm package), model accuracy/quality evaluation, or
  non-Chromium/non-Apple-Silicon benchmark data (all disclosed benchmarks ran
  on one 2024 MacBook Pro M4).

## Extracted Claims

### Claim 1: LiteRT.js is a JavaScript binding of LiteRT that runs AI models directly in the browser via WebAssembly, positioned as an evolution from TensorFlow.js for `.tflite` model deployment

- **Evidence**: Opening framing statement of the announcement.
- **Confidence**: settled (a factual architecture description of a shipping,
  installable npm package, not a forward-looking claim)
- **Quote**: "We are excited to announce LiteRT.js, a JavaScript binding of LiteRT for running AI directly inside the web browser. By bringing the trusted on-device inference library LiteRT to the web, web developers can now run ML and AI models with maximum performance entirely locally."
- **Our assessment**: The "maximum performance entirely locally" framing is the vendor's own language, but the underlying architectural claim — reusing the same native LiteRT runtime and optimizations already shipped for Android/iOS/desktop, rather than writing new JS-only kernels — is a concrete, checkable design choice, not just marketing. It directly targets developers with existing `.tflite` models who previously had to use TensorFlow.js's JS-kernel execution path.

### Claim 2: LiteRT.js outperforms prior web ML runtimes (e.g., TensorFlow.js's JS-based kernels) by up to 3x across both CPU and GPU inference on classical computer vision and audio processing models

- **Evidence**: Vendor benchmark comparison against "existing web solutions,"
  with an explicit disclosed test environment.
- **Confidence**: anecdotal (vendor-run benchmark; comparison runtimes,
  specific models tested, and methodology are not named or detailed beyond
  "classical computer vision and audio processing models"; single hardware
  configuration)
- **Quote**: "To demonstrate the real-world impact of the unified runtime and hardware-accelerated backends, we evaluated LiteRT.js against existing web solutions. Across classical computer vision and audio processing models, LiteRT.js delivers significant speedups—outperforming other web runtimes by up to 3x across both CPU and GPU inference." / "Note: Performance benchmarks conducted on a 2024 Apple MacBook Pro with M4 Apple Silicon in a controlled browser environment. Individual user performance may vary based on local GPU capabilities, thermal throttling, and browser driver optimization."
- **Our assessment**: This is the headline performance claim and the weakest
  substantiated one: the disclosed footnote is honest about single-machine,
  single-hardware-family testing (Apple Silicon M4 only), but neither the
  specific comparison runtime (TensorFlow.js is implied by context, not named
  in this sentence) nor the specific model set is disclosed. Should be cited
  as a vendor-reported directional figure, not a reproducible benchmark.

### Claim 3: GPU or NPU execution via WebGPU or WebNN delivers 5-60x speedup over CPU-only execution for real-time tasks like object tracking, audio transcription, or image manipulation

- **Evidence**: Second vendor benchmark comparison, same disclosed test
  environment as Claim 2.
- **Confidence**: anecdotal (same limitations as Claim 2 — single hardware
  configuration, unnamed specific models, wide "5-60x" range suggesting high
  variance across workloads rather than a single reproducible number)
- **Quote**: "For demanding real-time applications like object tracking, audio transcription, or image manipulation, leveraging the GPU or NPU via WebGPU or WebNN delivers 5-60x speedup compared to standard CPU execution, ensuring lower latency without compromising performance."
- **Our assessment**: The wide 5-60x range itself is informative — it signals
  that speedup is highly workload-dependent (small ops likely see less gain,
  large parallel ops like image manipulation see more), which is a more
  credible signal than a single cherry-picked number would be, even without
  per-model breakdowns.

### Claim 4: LiteRT.js's hardware acceleration stack maps CPU inference to XNNPACK, GPU inference to ML Drift via WebGPU, and NPU inference to the emerging (experimental) WebNN API

- **Evidence**: Direct architecture description with per-backend detail,
  corroborated by the LiteRT.js documentation page.
- **Confidence**: settled (concrete, named technical stack; WebNN's
  experimental status is explicitly disclosed by the vendor itself, not
  understated)
- **Quote**: "CPU: utilizes XNNPACK, Google's highly optimized library for on-device CPU acceleration, providing robust multi-thread support and a relaxed SIMD build for enhanced performance. GPU: powered by ML Drift, Google's leading solution for on-device GPU acceleration. LiteRT.js leverages WebGPU to enable state-of-the-art GPU acceleration on the web. NPU: harnesses the emerging WebNN API (currently experimental in Chrome and Edge) to target dedicated NPUs for power-efficient, ultra low-latency inference."
- **Our assessment**: This is the most concrete, checkable technical claim in
  the source — each backend names a specific, independently verifiable
  library/API (XNNPACK is a public GitHub project; WebGPU and WebNN are W3C
  specs). The explicit disclosure that WebNN is "currently experimental in
  Chrome and Edge" (i.e., not yet in Firefox or Safari) is an honest
  limitation the vendor did not obscure.

### Claim 5: PyTorch models can be converted to LiteRT in a single step via LiteRT Torch, and further optimized with tailored per-layer quantization via AI Edge Quantizer

- **Evidence**: Feature description with links to a getting-started guide and
  a quantization Colab notebook; corroborated by the LiteRT.js docs page's own
  PyTorch conversion code example (see Concrete Artifacts).
- **Confidence**: settled (specific named tools with linked runnable
  documentation/notebooks; the conversion code shown in the docs page is a
  concrete, minimal, checkable example)
- **Quote**: "With LiteRT Torch, PyTorch models can be converted in a single step, making them instantly ready to leverage advanced browser-based hardware acceleration." / "AI Edge Quantizer allows you to configure tailored quantization schemes across different model layers. This achieves substantial size reductions and performance gains while preserving overall model quality."
- **Our assessment**: "Single step" and "instantly ready" are vendor framing,
  but the actual code path (see Concrete Artifacts) is genuinely a handful of
  lines — `litert_torch.convert(model.eval(), sample_inputs)` followed by
  `.export('model.tflite')` — which is a materially simpler path than the
  PyTorch → ONNX → TensorFlow → TensorFlow.js chain the docs page itself
  describes as the alternative (see Claim 7).

### Claim 6: LiteRT.js shares a unified cross-platform runtime stack with LiteRT on Android, iOS, and desktop, so web apps automatically benefit from optimizations developed for those other platforms

- **Evidence**: Direct architectural claim tying the web binding to the
  broader LiteRT ecosystem already used on mobile/desktop.
- **Confidence**: emerging (architecturally plausible and consistent with
  LiteRT being an established mobile/desktop runtime, but "automatically
  benefit from the latest... upgrades" is a forward-looking maintenance
  claim not independently verifiable from this post alone)
- **Quote**: "As LiteRT.js shares a unified cross-platform stack with LiteRT, your web applications automatically benefit from the latest performance upgrades, quantization improvements, and hardware optimizations developed for Android, iOS, and desktop."
- **Our assessment**: This is the strategic thesis of the whole announcement:
  rather than maintaining a separate JS-only ML runtime (as TensorFlow.js
  effectively was), Google is extending its existing native mobile/desktop
  investment to the browser. Whether "automatically benefit" holds over time
  depends on Google's continued maintenance discipline, which this post
  cannot itself demonstrate — it's a claim about future behavior based on
  present architecture.

### Claim 7: LiteRT.js's PyTorch conversion path is simpler than TensorFlow.js's, because TensorFlow.js requires PyTorch → ONNX → TensorFlow → TensorFlow.js, while LiteRT.js converts PyTorch directly

- **Evidence**: Direct comparison statement from the LiteRT.js documentation
  page's "Integrate into existing TensorFlow.js pipelines" section.
- **Confidence**: settled (a factual claim about the number of conversion
  hops in each toolchain, independently checkable against each framework's
  own public conversion documentation)
- **Quote**: "Easier Model Conversion Path: The LiteRT.js conversion path goes directly from PyTorch to LiteRT. The PyTorch to TensorFlow.js conversion path is significantly more complicated, requiring you to go from PyTorch -> ONNX -> TensorFlow -> TensorFlow.js."
- **Our assessment**: This is Google's own framing of a competitive
  advantage over TensorFlow.js specifically — it does not address ONNX
  Runtime Web (a PyTorch → ONNX, one-hop path that skips TensorFlow.js
  entirely), which is the browser inference runtime Claude recommended and
  used in two independent Willison experiments already in this corpus (see
  Cross-References). The comparison is accurate as stated but incomplete: it
  compares against TensorFlow.js, not against the other major browser ML
  runtime this corpus has direct practitioner experience with.

### Claim 8: The LiteRT.js JS API loads a `.tflite` model, compiles it for a chosen accelerator (webgpu/webnn/wasm), and runs inference with automatic CPU fallback for unsupported ops

- **Evidence**: A minimal, complete code example given in both the
  announcement post and the get-started documentation page.
- **Confidence**: settled (a concrete, runnable code snippet, not a
  paraphrased description)
- **Quote**: "const model = await loadAndCompile('/path/to/model.tflite', {accelerator: 'webgpu', // Can select from 'webnn', 'webgpu', & 'wasm'. // Unsupported ops on webgpu & webnn automatically fallback to CPU.});"
- **Our assessment**: The automatic CPU fallback for unsupported ops on
  WebGPU/WebNN is an operationally important detail not mentioned in the
  announcement post's own prose — it only appears in the docs page's code
  comments. This means a developer targeting `webgpu` doesn't need to
  verify op coverage up front; the runtime silently degrades per-op rather
  than failing outright, which is the kind of practical detail that matters
  for reliability but is easy to miss without reading past the announcement.

### Claim 9: LiteRT.js already has real-world model integrations demoed live: official Ultralytics YOLO export support, a Depth Anything V2 monocular-depth-to-3D-point-cloud demo, and a Real-ESRGAN 4x image upscaler

- **Evidence**: Three named, linked demo integrations with descriptions of
  each demo's mechanism.
- **Confidence**: emerging (concrete, named, linked integrations exist and
  are described with enough technical detail to be checkable — e.g., the
  upscaler's 128x128→512x512 patch-based tiling approach — but no
  independent user has verified these demos run as described; confidence
  is bounded by this being a single vendor's own demo showcase)
- **Quote**: "We are excited to share official LiteRT export support built directly into the Ultralytics Python package." / "Upscale images by 4x in the browser using the Real-ESRGAN model with LiteRT.js, which works by upscaling 128x128 pixel patches to 512x512 which are then reassembled into the final image."
- **Our assessment**: The Ultralytics integration is the strongest signal
  here — Ultralytics is a real, independent, widely-used computer vision
  company/package, and "official LiteRT export support built directly into
  the Ultralytics Python package" is a checkable ecosystem integration
  claim, not just a vendor demo. This is meaningfully different in kind from
  the Depth Anything and Real-ESRGAN demos, which are Google-built
  showcases of open third-party models rather than integrations built by
  the model authors themselves.

### Claim 10: Google's roadmap for LiteRT.js centers on advancing WebNN/NPU integration and adding "highly optimized support for on-device generative AI," with a separate `LiteRT-LM.js` binding already adding browser LLM support

- **Evidence**: "What's next" section, plus a named forthcoming/existing
  sibling project.
- **Confidence**: emerging (WebNN advancement and generative-AI support are
  forward-looking roadmap statements without dates; `LiteRT-LM.js` is stated
  to already exist with a linked JS API reference, making that specific
  sub-claim more concrete than the general roadmap language)
- **Quote**: "We are committed to continually expanding LiteRT.js performance, model coverage, and developer tooling. Looking ahead, our development roadmap centers on advancing WebNN integration for native NPU performance and delivering highly optimized support for on-device generative AI." / "LLM support: LiteRT-LM.js, adds browser support for LLMs via our JavaScript API."
- **Our assessment**: This draws an explicit scope line worth preserving:
  LiteRT.js (this announcement) targets classical ML — vision, audio,
  embeddings, image processing — while LLM-specific browser inference is a
  separate, distinctly-named sibling binding (`LiteRT-LM.js`). This mirrors
  the existing corpus distinction between `litert-lm` (the CLI documented in
  `blog-google-gemma-4-12b-developer-guide.md` for desktop/server LLM
  serving) and this post's LiteRT.js (classical ML in the browser) — LiteRT
  is Google's umbrella runtime brand, but LLM and non-LLM inference are
  shipped as separate bindings per target (CLI vs. browser).

### Claim 11: LiteRT.js installs as a single npm package (`@litertjs/core`) with WebAssembly files that can be served from the package itself or a CDN, requiring no build-toolchain integration beyond copying a `wasm/` folder

- **Evidence**: Installation instructions from the get-started documentation
  page, with both CDN and self-hosted loading code shown.
- **Confidence**: settled (concrete, minimal, checkable installation steps)
- **Quote**: "Install the @litertjs/core package from npm: npm install @litertjs/core / The Wasm files are located in node_modules/@litertjs/core/wasm/. For convenience, copy and serve the entire wasm/ folder."
- **Our assessment**: This is a low-friction installation path relative to
  toolchains that require custom build-step integration (e.g., WASM-specific
  bundler plugins) — a plain npm install plus static file serving from a CDN
  or the package's own directory. Consistent with the "meets developers
  where they are" framing that runs through the rest of the announcement.

## Concrete Artifacts

### LiteRT.js inference code (verbatim from the blog post)

```javascript
import { loadLiteRt, loadAndCompile, Tensor } from '@litertjs/core';

await loadLiteRt('path/to/wasm/directory/');
const model = await loadAndCompile('path/to/your/model.tflite',{ accelerator: webgpu });
const inputTypedArray = new Float32Array(1 * 3 * 244 * 244);
const inputTensor = new Tensor(inputTypedArray, [1, 3, 244, 244]);
const results = await model.run(inputTensor);
// results is a Tensor stored on GPU. To move it to CPU & convert to a typedArray we use
const resultArray = (await results[0].moveTo('wasm')).toTypedArray();
```
*Source: developers.googleblog.com/litertjs-googles-high-performance-web-ai-inference/, "Get started with LiteRT.js" section*

### LiteRT.js install + load (verbatim from the get-started docs page)

```javascript
// npm install @litertjs/core

import { loadLiteRt } from '@litertjs/core'
// Load the LiteRT.js Wasm files from a CDN.
await loadLiteRt('https://cdn.jsdelivr.net/npm/@litertjs/core/wasm/')
// Alternatively, host them from your server.
// They are located in node_modules/@litertjs/core/wasm/
await loadLiteRt(`your/path/to/wasm/`);
```
*Source: developers.google.com/edge/litert/web/get_started, "Installation" section*

### PyTorch → LiteRT conversion (verbatim from the get-started docs page)

```python
import litert_torch

# Load your torch model. We're using resnet for this example.
resnet18 = torchvision.models.resnet18(torchvision.models.ResNet18_Weights.IMAGENET1K_V1)
sample_inputs = (torch.randn(1, 3, 224, 224),)

# Convert the model to LiteRT.
edge_model = litert_torch.convert(resnet18.eval(), sample_inputs)

# Export the model.
edge_model.export('resnet.tflite')
```
*Source: developers.google.com/edge/litert/web/get_started, "Convert a PyTorch Model to LiteRT" section*

### Run the converted model with accelerator selection and CPU fallback (verbatim from the get-started docs page)

```javascript
import { loadAndCompile } from '@litertjs/core';

// Load the model hosted from your server. This makes an http(s) request.
const model = await loadAndCompile('/path/to/model.tflite', {
  accelerator: 'webgpu',
  // Can select from 'webnn', 'webgpu', & 'wasm'.
  // Unsupported ops on webgpu & webnn automatically fallback to CPU.
});

const image = new Float32Array(224 * 224 * 3).fill(0);
const inputTensor = new Tensor(image, /* shape */ [1, 3, 224, 224]);

const outputs = await model.run(inputTensor);
// You can also use `await model.run([inputTensor]);`
// or `await model.run({'input_tensor_name': inputTensor});`

inputTensor.delete();
const output = outputs[0];
const outputData = await output.data();
output.delete();
```
*Source: developers.google.com/edge/litert/web/get_started, "Run the Converted Model" section*

### TensorFlow.js migration steps (verbatim from the get-started docs page)

```
Integrate LiteRT.js into TensorFlow.js pipelines with the following steps:
1. Convert your original TensorFlow, JAX, or PyTorch model to .tflite.
2. Install the @litertjs/core and @litertjs/tfjs-interop NPM packages.
3. Import and use the TensorFlow.js WebGPU backend. This is required for
   LiteRT.js to interoperate with TensorFlow.js.
4. Replace loading the TensorFlow.js model with loading the LiteRT.js model.
5. Substitute the TensorFlow.js model.predict(inputs) or model.execute(inputs)
   with runWithTfjsTensors(liteRtModel, inputs). runWithTfjsTensors takes the
   same input tensors that TensorFlow.js models use and outputs TensorFlow.js
   tensors.
6. Test that the model pipeline outputs the results you expect.

Possible follow-up adjustments: reorder inputs, transpose inputs, rename
inputs — depending on how the converter ordered/laid out the model's
inputs/outputs relative to the existing TensorFlow.js pipeline.
```
*Source: developers.google.com/edge/litert/web/get_started, "Integrate into existing TensorFlow.js pipelines" section*

## Cross-References

- **Corroborates**:
  - `blog-google-gemma-4-12b-developer-guide.md` (Claim 9, `litert-lm serve` —
    a CLI turning Gemma 4 12B into a local OpenAI-compatible API server) and
    `blog-google-gemma-4-12b-laptop-ai-edge.md` (same claim, second
    independent post): both confirm Google's broader LiteRT-branded runtime
    strategy of exposing one native optimization stack across many surfaces
    (Android/iOS/desktop/CLI/browser). This post's Claim 6 (unified
    cross-platform stack) is the browser-specific instance of the same
    strategic pattern already documented for CLI-based LLM serving in those
    two notes.
  - `blog-simonwillison-moebius-browser.md` Claim 12 (Claude recommended ONNX
    Runtime Web on the WebGPU backend — "the layer below Transformers.js" —
    for browser-native custom-model inference) and
    `blog-simonwillison-liteparse-browser.md` (browser-native ML/PDF
    processing via a static-site, in-browser, no-backend architecture):
    both corroborate the general shift toward WebGPU-accelerated,
    lower-level (below-framework) browser inference runtimes as the
    practical state of the art, of which LiteRT.js is a second, vendor-native
    instance alongside ONNX Runtime Web.

- **Contradicts**: None identified. This post's Claim 7 (LiteRT.js's PyTorch
  conversion path is simpler than TensorFlow.js's) does not contradict
  `blog-simonwillison-moebius-browser.md` Claim 12 (Claude chose ONNX Runtime
  Web over Transformers.js) — the two sources compare against different
  baselines (TensorFlow.js vs. Transformers.js/ONNX Runtime Web) and neither
  makes a claim the other directly opposes. No contradiction issue filed.

- **Extends**: `blog-google-gemma-4-12b-developer-guide.md` and
  `blog-google-gemma-4-12b-laptop-ai-edge.md`, both of which document the
  LiteRT-LM CLI for desktop/server LLM serving but do not cover browser-side,
  non-LLM inference at all. This post extends the corpus's coverage of
  Google's LiteRT ecosystem to a third surface (browser, classical ML) and
  clarifies (Claim 10) that LLM inference on the web is a separate,
  distinctly-named sibling binding (`LiteRT-LM.js`), not part of this
  release.

- **Novel**:
  - Browser-native inference via a native, WASM-compiled runtime
    (LiteRT/XNNPACK/ML Drift) rather than JS-authored kernels (the
    TensorFlow.js approach) — no existing corpus source documents this
    specific "native runtime compiled to WASM" architecture for the browser.
  - Vendor-disclosed, hardware-specific performance benchmarks for browser ML
    (3x vs. other web runtimes; 5-60x GPU/NPU vs. CPU) — no existing corpus
    source has quantified browser inference speedups at this level of
    specificity (even with the caveats in Claims 2-3).
  - Official Ultralytics YOLO → LiteRT export support built into the
    Ultralytics Python package itself — a first-party ecosystem integration
    not previously documented in this corpus's browser-ML coverage.
  - The `.tflite` single-format, multi-framework (PyTorch/JAX/TensorFlow)
    conversion story, and the direct TensorFlow.js interop path via
    `runWithTfjsTensors` — both new technical patterns to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The guide's existing browser-native ML
  coverage (implicit via the not-yet-merged Willison ONNX Runtime Web
  experiments) has no mention of LiteRT.js as an alternative runtime choice.
  If/when the guide adds a section on choosing a browser inference runtime
  for agent-built ML features, this source provides a second, vendor-native
  option (native WASM runtime + WebGPU/WebNN hardware acceleration,
  `.tflite` format, `LiteRT Torch` for PyTorch conversion) to weigh against
  ONNX Runtime Web — with the explicit caveat that LiteRT.js's own comparison
  in Claim 7 addresses TensorFlow.js, not ONNX Runtime Web, so it is not
  direct evidence that LiteRT.js beats the runtime Claude has independently
  chosen in this corpus's practitioner reports.
- **No other chapter impact identified**: This source is a technology/runtime
  announcement, not a workflow, harness-configuration, or verification
  practice — it does not map cleanly onto Chapter 01 (Daily Workflows),
  Chapter 03 (Verification), Chapter 04 (Context Engineering), Chapter 05
  (Team Adoption), or Chapter 06 (Security/Threat Model) as those chapters
  are currently scoped (confirmed by reading `guide/*.md` section headers —
  none currently address browser ML runtime selection). Flagging this
  explicitly rather than forcing a fit: the source is real, well-substantiated
  technical material, but its direct actionability for this guide's actual
  scope (agentic coding practice, not ML runtime engineering) is narrow.

## Extraction Notes

- **Raw HTML fetched directly via `curl`, not via the WebFetch summarizer**:
  All quotes were obtained by fetching the raw page HTML with `curl` and
  stripping markup with BeautifulSoup in Python, to get character-for-character
  text rather than a paraphrased WebFetch summary.
- **Sub-pages followed**: the primary announcement post and the LiteRT.js
  get-started documentation page (`developers.google.com/edge/litert/web/get_started`,
  which renders identically to `ai.google.dev/edge/litert/web`) — 2 of the
  "up to 5" sub-pages MINER.md allows. Not followed: the LiteRT Torch
  Colab notebook, the AI Edge Quantizer Colab notebook, the Ultralytics LiteRT
  export docs page, and the LiteRT-LM.js JS API reference — these are
  code-reference/tutorial pages that would mainly duplicate the conversion
  and API detail already extracted verbatim from the primary source and the
  get-started page, rather than surface new substantive claims.
- **Existing overlap checked before writing**: Searched all `source-notes/*.md`
  for "LiteRT", "litert", "tflite", "WebGPU", "WebNN", "XNNPACK", and
  "TensorFlow.js" before drafting. Found overlap only with the two Gemma
  4 12B notes (which cover LiteRT-LM, the LLM-serving CLI — a different
  binding for a different target than this post's browser/classical-ML
  binding) and the two Willison browser-ML notes (which document a
  different runtime, ONNX Runtime Web, for the same class of problem). No
  existing note covers LiteRT.js itself; this is confirmed net-new coverage.
- **Three duplicate Prospector triage comments**: The issue carries three
  near-identical triage assessments (all filed within seconds of each other),
  proposing different and, in two cases, incorrect chapter names (e.g., "Ch03
  Edge Computing & Deployment," "Ch05 Performance & Optimization," "Ch03
  Agent Patterns" — none of which match this guide's actual chapter
  structure: 00-principles, 01-daily-workflows, 02-harness-engineering,
  03-verification, 04-context-engineering, 05-team-adoption,
  06-security-threat-model, confirmed by listing `guide/*.md`). This note's
  Guide Impact section maps to the actual chapter structure rather than the
  triage comments' invented chapter names.
- **Confidence rationale**: Set to `emerging` rather than `settled` because,
  while the architecture and API claims (Claims 1, 4, 5, 7, 8, 11) are
  concrete and independently checkable against the linked documentation, the
  headline performance claims (Claims 2, 3) are vendor-reported, single-machine
  benchmarks without named comparison runtimes or disclosed model sets. Not
  `anecdotal` overall, because the API, conversion tooling, and hardware
  backend mapping are verifiable, reproducible technical facts rather than a
  one-off practitioner anecdote.
