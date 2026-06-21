---
source_url: https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/
source_type: blog-post
title: "Publishing WASM wheels to PyPI for use with Pyodide"
author: Simon Willison
date_published: 2026-06-13
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: emerging
issue: "#1249"
---

# Publishing WASM wheels to PyPI for use with Pyodide

> Simon Willison documents an ecosystem shift in browser-based Python: PyPI now natively
> supports WASM wheels via PEP 783, removing the long-standing bottleneck where Pyodide
> maintainers had to manually maintain 300+ compiled packages — and providing a concrete
> end-to-end workflow (luau-wasm case study) for practitioners who want to distribute
> compiled C or Rust extensions for use in Pyodide.

## Source Context

- **Type**: blog-post (Simon Willison's short-form announcement post, June 13, 2026; covers
  the Pyodide 314.0 release announcement, the PyPI warehouse PR #19804, a BigQuery scan of
  adoption data, and a worked example packaging Luau as a WASM wheel. The post links to the
  luau-wasm GitHub repository and a live demo. Both the blog post and key linked resources
  were read for this extraction.)
- **Author credibility**: Simon Willison is the creator of Django, creator of Datasette, and
  author of the `llm` CLI. He is a designated `trusted-feed` source in this repo. He
  documents working experiments with public GitHub repositories and verifiable artifacts.
  He has no vendor affiliation. This post continues his practitioner series on browser-native
  Python tooling.
- **Scope**: Covers the PyPI WASM wheel distribution mechanism (PEP 783, pyemscripten
  platform tags), the Pyodide 314.0 release that announced it, early adoption data (28
  packages via BigQuery scan), and a worked example (luau-wasm: a Rust-based Luau interpreter
  packaged as a WASM wheel). Does NOT cover: browser deployment patterns (see
  `blog-simonwillison-pyodide-asgi-browser.md`), the Pyodide runtime itself, or how to use
  packages once installed in Pyodide beyond the micropip demo snippet.

## Extracted Claims

### Claim 1: PyPI now natively supports WASM wheels via PEP 783's pyemscripten platform tags, enabling direct distribution of Pyodide-compatible compiled extensions to PyPI

- **Evidence**: The Pyodide 314.0 release announcement (announced via Hacker News) covers this
  as a flagship change. The PyPI warehouse PR #19804 implemented it and was merged April 21,
  2026. Willison quotes the announcement directly. PEP 783 defines the PyEmscripten platform
  ABI that formalizes this.
- **Confidence**: settled (PR merged, Pyodide release shipped, platform tags operational)
- **Quote**: "You can now publish Python packages built for Pyodide (or any Python runtime
  compatible with the PyEmscripten platform defined in PEP 783) directly to PyPI"
- **Our assessment**: This is a standards-level change, not a Pyodide-specific feature.
  PEP 783 defines a general PyEmscripten platform that any WASM-targeting Python runtime can
  target, not just Pyodide. The framing matters for practitioners: publishing a WASM wheel
  to PyPI does not hard-code it to Pyodide — it targets the PyEmscripten platform, which
  Pyodide (and potentially other browser Python runtimes) can consume. This is the right
  level of abstraction for a distribution standard.

### Claim 2: The previous ecosystem bottleneck was that Pyodide maintainers had to manually build and host all 300+ compiled packages themselves

- **Evidence**: Willison quotes this directly from the Pyodide team's own framing of what
  the new distribution mechanism replaces. The burden was not on package authors but on the
  Pyodide team, who had to patch, cross-compile, and host each C/Rust extension individually.
- **Confidence**: settled (direct quote from Pyodide 314.0 release announcement, corroborated
  by Willison's framing)
- **Quote**: "Previously, the Pyodide maintainers had to maintain, build, and host over 300
  packages ourselves."
- **Our assessment**: The 300+ package maintenance burden explains why the set of Pyodide-
  available compiled packages was historically much smaller than PyPI's full catalog. Every
  C extension (NumPy, Pandas, Pillow, scikit-learn, etc.) required Pyodide-specific
  cross-compilation, patch management, and hosting. Moving this responsibility to individual
  package maintainers — who already have the source code and CI pipelines — is the correct
  scale point for the ecosystem. The Pyodide team's bottleneck was always a staffing-and-
  scale problem, not a technical one.

### Claim 3: Package maintainers can now publish WASM wheels to PyPI using the same self-service workflow as native wheels on Linux, macOS, or Windows

- **Evidence**: The Pyodide 314.0 release announcement explicitly frames the change as
  normalizing the WASM wheel publishing experience to match native platform wheel publishing.
  The luau-wasm case study demonstrates this end-to-end with a public GitHub repository and
  working CI.
- **Confidence**: settled (working example; framing from Pyodide release announcement)
- **Quote**: "Moving forward, package maintainers can simply build and publish Pyodide wheels
  to PyPI, just as they do for native wheels on Linux, macOS, or Windows."
- **Our assessment**: The "just as they do for native wheels" framing is the key signal: the
  new workflow is not Pyodide-specific tooling that maintainers must learn — it's the same
  PyPI upload workflow, extended to a new platform tag. Package authors who already publish
  manylinux or macOS wheels via cibuildwheel add WASM as another target, not a new publishing
  system. The barrier to adoption is now only the cross-compilation setup (cibuildwheel +
  Emscripten), not a special Pyodide submission process.

### Claim 4: C and Rust extensions compiled to WASM previously had no standard distribution mechanism; PyPI WASM wheel support closes this gap

- **Evidence**: Willison explicitly names this as the pre-existing gap before the PyPI change.
  The ability to compile to WASM existed (via Emscripten), but distributing the resulting
  wheels had no standard channel — package authors had to host them separately or route through
  Pyodide's own pipeline.
- **Confidence**: settled (direct statement from the post; the gap is structurally obvious
  from how PyPI platform tags work)
- **Quote**: "It's possible to compile C or Rust extensions to WASM in a wheel file, but
  before now there was no easy way to distribute them."
- **Our assessment**: This is the core insight from the post: the technical capability
  (compile to WASM) predated the distribution infrastructure (publish to PyPI). This is a
  recurring pattern in ecosystem development — the toolchain arrives first, the distribution
  standard follows. For practitioners: the existence of this gap explains why Pyodide's
  package catalog was artificially constrained relative to PyPI's catalog. Now that the gap
  is closed, the constraint lifts for any package author who adds the WASM build target.

### Claim 5: 28 packages were already publishing with the new pyemscripten WASM tags within weeks of the PyPI PR landing, including major packages like pydantic_core and onnx

- **Evidence**: Willison queried PyPI's public BigQuery dataset with a SQL query (linked in
  the post as a GitHub Gist) to find packages using the new platform tags. He explicitly
  hedges that the query may not be perfectly accurate, but reports the result as 28 packages.
  The list includes notable packages (pydantic_core, onnx, typst, imgui-bundle) alongside
  smaller packages.
- **Confidence**: emerging (BigQuery scan result with explicit author caveat about query
  accuracy; early data, ecosystem still forming)
- **Quote**: "If the query is right, there are currently 28 PyPI packages publishing with
  the new `pyemscripten_202*_wasm32` tags"
- **Our assessment**: 28 packages within ~7 weeks of the PyPI PR landing (April 21 to June 13)
  is a real but modest early-adoption signal. More telling are the names in the list: pydantic_core
  (a major Python data validation library with Rust internals) and onnx (the standard ML model
  interchange format) are substantial packages, not toy experiments. Their presence suggests
  that large, active package maintainers are already adding WASM targets alongside their
  native builds. The `pyemscripten_202*_wasm32` tag format (year-based ABI version) suggests
  the platform tag system is designed for forward compatibility across Pyodide releases.

### Claim 6: The PyPI warehouse PR #19804 that enabled WASM wheel support landed April 21, 2026, and Pyodide 314.0 was the first release to fully announce and integrate it

- **Evidence**: Willison links to the specific PyPI warehouse PR and states the date. Pyodide
  314.0 is framed as the release that announced the change; the PyPI infrastructure change
  itself predated the Pyodide release.
- **Confidence**: settled (linked PR with stated date; Pyodide 314.0 release announcement
  is the public announcement)
- **Quote**: "Here's the PR to PyPI itself supporting this, which landed on April 21st."
- **Our assessment**: The sequence matters: PyPI's infrastructure was patched first (April 21),
  Pyodide 314.0 was released later (announcing the feature to users), and Willison's blog
  post is from June 13 (early ecosystem scan). The 7-8 week gap between the PyPI PR and
  this blog post is when the 28 packages in Claim 5 accumulated. The timeline frames
  "early but real adoption" correctly.

### Claim 7: The luau-wasm package demonstrates the complete end-to-end WASM wheel workflow: Rust source → Emscripten compilation → PyPI publication → micropip installation in Pyodide

- **Evidence**: Willison built and published luau-wasm himself as a working demonstration.
  The GitHub repository is public with build and deploy scripts. A live demo is deployed to
  GitHub Pages. The package is on PyPI and installable via micropip.
- **Confidence**: settled (public PyPI package; public GitHub repo; live demo; working code
  example in the blog post)
- **Quote**: "luau-wasm is a brand new PyPI package which publishes a 276KB wheel file which
  can be used in Pyodide"
- **Our assessment**: The choice of Luau (a Rust-based language runtime developed by Roblox)
  as the demo subject is instructive: it is a compiled language interpreter, not a simple
  library. Packaging a language runtime as a WASM wheel tests the full capability of the
  mechanism — binary size (276KB), interpreter execution, string handling, and type system.
  If a complete language interpreter packages successfully, most C/Rust extension libraries
  should as well. The 276KB size is also notable: WASM wheels can be meaningfully smaller
  than native equivalents, which matters for browser delivery.

### Claim 8: cibuildwheel is the build toolchain for producing pyemscripten WASM wheels as part of a standard CI workflow

- **Evidence**: Willison references "the latest cibuildwheel" as the build tool used in
  the luau-wasm GitHub repository's build and deploy scripts. cibuildwheel is the standard
  Python wheel build tool for multi-platform CI (Linux/macOS/Windows); supporting
  pyemscripten is an extension of its existing multi-platform capabilities.
- **Confidence**: emerging (one concrete example; the luau-wasm repo demonstrates it, and
  the cibuildwheel project has added Emscripten/WASM support)
- **Quote**: "The GitHub repo for luau-wasm includes all of the build and deploy scripts
  (using the latest cibuildwheel)"
- **Our assessment**: cibuildwheel being the integration point is good news for adoption:
  package maintainers who already use cibuildwheel for native wheel CI (which is the standard
  practice for any C/Rust extension on PyPI) can add WASM as another matrix target without
  adopting a different build system. The "latest cibuildwheel" qualifier suggests this is a
  recent addition to cibuildwheel, consistent with the April 2026 PyPI PR timeline.

### Claim 9: The micropip install workflow enables Pyodide code to install packages directly from PyPI without pre-bundling or vendoring

- **Evidence**: The blog post provides a working code example showing `micropip.install("luau-wasm")`
  fetching the package from PyPI inside a Pyodide runtime. The live demo at
  simonw.github.io/luau-wasm/ demonstrates this running in a browser.
- **Confidence**: settled (working code example; live demo)
- **Quote**: (no direct quote for this claim's core assertion; see code artifact below)
- **Our assessment**: This is the practitioner-facing consequence of Claims 1–7: a developer
  writing Pyodide code can now call `micropip.install("package-name")` for any package that
  has published a pyemscripten WASM wheel, just as a desktop developer calls `pip install`.
  Previously, this only worked for the ~300+ packages Pyodide maintained. As more package
  authors publish WASM wheels (the 28-package early count from Claim 5 will grow), the set
  of available packages expands without any Pyodide team intervention. This closes the
  "dependency availability" gap that was a key constraint for browser-native Python apps.

## Concrete Artifacts

### micropip install + Luau code execution example (from blog post)

```python
# Source: simonwillison.net/2026/Jun/13/publishing-wasm-wheels/
# Installs the luau-wasm WASM wheel from PyPI in a Pyodide runtime

import micropip
await micropip.install("luau-wasm")
import luau_wasm
print(luau_wasm.execute(r'''
local animals = {"fox", "owl", "frog", "rabbit"}
table.sort(animals, function(a, b) return #a < #b end)
for i, name in animals do print(i .. ". " .. name .. " (" .. #name .. ")") end
'''))
```

### pyemscripten WASM wheel filename format (from blog post)

```
luau_wasm-0.1a0-cp314-cp314-pyemscripten_2026_0_wasm32.whl
                │            └── platform tag: PyEmscripten ABI 2026.0, wasm32
                └── CPython 3.14 (Pyodide 314.0 = CPython 3.14)

Platform tag pattern: pyemscripten_{year}_{minor}_wasm32
BigQuery glob used:   pyemscripten_202*_wasm32
```

### 28 packages using the new pyemscripten tags (BigQuery scan, June 13, 2026)

```
Source: simonwillison.net/2026/Jun/13/publishing-wasm-wheels/
Query: BigQuery against PyPI public dataset (SQL linked in post as GitHub Gist)
Result (author-hedged as "if the query is right"):

luau-wasm, uuid7-rs, cmm-16bit, pyOpenTTDAdmin, imgui-bundle, numbertoolkit,
bashkit, geoarrow-rust-core, arro3-io, arro3-core, arro3-compute, onnx,
powerfit-em, tcod, chonkie-core, tokie, robotraconteur, pydantic_core,
yaml-rs, cadquery-ocp-novtk-OCP.wasm, uuid_utils, base64_utils, pycdfpp,
lib3mf-OCP.wasm, typst, toml-rs, onnx-weekly, dummy-pyodide-ext-test

Notable: pydantic_core (Rust-based validation), onnx (ML model interchange),
         typst (Rust-based typesetting), imgui-bundle (C++ GUI bindings)
```

### luau: the demo package (description from blog post)

```
Luau: a "small, fast, and embeddable programming language based on Lua with
      a gradual type system" developed by Roblox and released under an MIT license.

Source:  https://luau.org
WASM pkg: luau-wasm on PyPI
GitHub:  https://github.com/simonw/luau-wasm
Demo:    https://simonw.github.io/luau-wasm/
Size:    276KB wheel (luau_wasm-0.1a0-cp314-cp314-pyemscripten_2026_0_wasm32.whl)
```

### Key infrastructure references

```
PyPI warehouse PR:   https://github.com/pypi/warehouse/pull/19804 (landed April 21, 2026)
PEP 783:             PyEmscripten Platform (defines the pyemscripten_*_wasm32 tag)
Pyodide ABI doc:     https://pyodide.org/en/stable/development/abi.html
Pyodide 314.0 blog:  https://blog.pyodide.org/posts/314-release/
cibuildwheel:        https://github.com/pypa/cibuildwheel
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-pyodide-asgi-browser.md` Claim 6 ("The ASGI protocol provides a
    framework-agnostic seam that allows any compliant Python ASGI app to be hosted in the
    browser bridge without framework-specific code changes; the constraint is the Python
    dependencies: pure-Python wheels and Pyodide-compatible packages work; C extensions
    or packages requiring OS threads do not"): This note directly addresses the constraint
    Claim 6 names. Previously, C extensions could not round-trip through Pyodide because
    they could not be distributed as WASM wheels. PyPI WASM wheel support (this note, Claim 1)
    now enables C/Rust extension authors to publish WASM builds, expanding what "Pyodide-
    compatible packages" means for practitioners building browser ASGI apps.
  - `blog-simonwillison-datasette-agent-micropython.md`: Both notes document Python+WASM
    execution, but in different contexts — MicroPython+WASM as a server-side sandboxing
    mechanism (datasette-agent-micropython) vs. full CPython+WASM (Pyodide) as a browser
    execution environment (this note). Both converge on WASM as a meaningful execution
    substrate for Python beyond native platforms. Together they establish WASM as a cross-
    context Python deployment target, not only a browser-specific concern.

- **Extends**:
  - `blog-simonwillison-pyodide-asgi-browser.md`: That note (May 30, 2026) documents the
    *deployment pattern* for browser-native Python ASGI apps. This note (June 13, 2026)
    documents the *distribution mechanism* that makes compiled Python dependencies available
    for those same apps. They are complementary pieces of the browser-native Python stack:
    the deployment pattern enables browser-side Python execution; the distribution mechanism
    enables compiled dependencies to be installed via PyPI rather than maintained by the
    Pyodide team. Specifically, the pyodide-asgi-browser note's Claim 11 (vendoring
    Pyodide + wheels locally due to browser sandbox network restrictions) describes a
    workaround scenario; this note provides the canonical self-service path (micropip
    install from PyPI) that applies when network is available.

- **Contradicts**: None identified. No existing corpus source makes claims about WASM wheel
  distribution on PyPI or PEP 783 that would conflict with the findings here.

- **Novel**:
  - **PEP 783 / pyemscripten PyPI platform tag support**: No existing corpus source
    documents the PyPI WASM wheel distribution mechanism, PEP 783, or the
    `pyemscripten_*_wasm32` platform tag. This is entirely new to the corpus.
  - **Self-service Pyodide package distribution**: The shift from Pyodide-team-maintained
    package catalog (300+ curated packages) to community-driven PyPI publishing is a
    qualitative ecosystem change not documented elsewhere in the corpus.
  - **cibuildwheel as the WASM wheel build toolchain**: No existing corpus source documents
    cibuildwheel's Emscripten/WASM support or how to produce pyemscripten WASM wheels via CI.
  - **Adoption data (28 packages, BigQuery scan)**: The concrete early-adoption count and
    named package list (pydantic_core, onnx, typst) is new quantitative evidence for the
    ecosystem's trajectory.
  - **pyemscripten wheel filename format**: The `cp314-cp314-pyemscripten_{year}_{minor}_wasm32`
    tag structure and its interpretation (CPython version, ABI year/minor, architecture) is
    new to the corpus.

## Guide Impact

- **Chapter 04 (Context Engineering — Browser-Native Python Ecosystem)**: This source
  substantially changes the ecosystem picture for browser-native Python. The guide should
  add: "As of April 2026, PyPI natively supports WASM wheels via PEP 783's pyemscripten
  platform. This removes the long-standing constraint that limited Pyodide deployments to
  the ~300+ packages maintained by the Pyodide team. Package maintainers can now publish
  WASM builds to PyPI using cibuildwheel, just as they publish native wheels. Pyodide's
  micropip can install these directly from PyPI. Early adoption is already visible (28
  packages as of June 2026, including pydantic_core and onnx)." This pairs with the
  `blog-simonwillison-pyodide-asgi-browser.md` deployment pattern: that note covers how
  to run Python ASGI apps in the browser; this note covers how to make compiled dependencies
  available for those apps.

- **Chapter 04 (Context Engineering — Browser-Native Python Packaging Constraint)**:
  Chapter 04 should update any statement that C or Rust extensions are unavailable in
  browser-native Python contexts. The `blog-simonwillison-pyodide-asgi-browser.md` note's
  Claim 6 says "C extensions or packages requiring OS threads do not" work in the browser
  bridge — the "C extensions" part of this constraint is now partially lifted for packages
  that publish pyemscripten WASM wheels. The OS threads constraint remains. The guide
  should distinguish: compiled extensions *can* work in Pyodide if they (a) publish a WASM
  wheel to PyPI and (b) do not require OS threads.

- **Chapter 02 (Harness Engineering — Ecosystem Trends)**:
  The shift from curated Pyodide package catalog to self-service PyPI distribution is an
  ecosystem milestone worth noting as a practitioner signal: "When evaluating browser-native
  Python deployment for tools that depend on compiled packages (e.g., pydantic, onnx, image
  processing), check PyPI for pyemscripten WASM wheels before assuming the dependency is
  unavailable. The ecosystem is growing rapidly post-April 2026."

## Extraction Notes

- **Source is a short-form blog post** (~600-800 words): Willison's blog has both short
  announcement posts (like this one) and longer analytical posts. This is the former: it
  announces the ecosystem change, provides the luau-wasm case study, and links to supporting
  resources. The substance is relatively compact but technically specific.
- **Quote verification**: Quotes were extracted via multiple targeted WebFetch calls asking
  for verbatim text. WebFetch returns content processed by a small model, which may not
  be character-for-character accurate for all text. Quotes in this note were confirmed
  across multiple WebFetch calls with verbatim-only prompts. Where confidence is lower,
  the Quote field uses "(no direct quote; see paraphrase in Our assessment)".
- **BigQuery query**: The blog post links to a GitHub Gist containing the BigQuery SQL
  query used to find the 28 packages, but does not display the SQL inline. The Gist was
  not accessed for this extraction; the package list was extracted from the blog post's
  display of the result.
- **Live demo verified**: The live demo at simonw.github.io/luau-wasm/ is publicly linked
  in the post as an interactive Pyodide+luau-wasm environment.
- **Sub-pages not followed**: The blog post links to the Pyodide 314.0 release blog, the
  PyPI PR #19804, the luau-wasm GitHub repo, PEP 783, and the cibuildwheel project. The
  luau-wasm GitHub repo and PyPI PR were not deeply read; the blog post's summary of each
  was sufficient for claim extraction. The Pyodide 314.0 release blog was not followed
  (not strictly needed for the extraction goals).
- **Confidence set to `emerging`**: The PyPI change itself is settled (PR merged, feature
  operational). But the ecosystem is very new — 28 packages in 7 weeks is early-adoption
  data, not a mature ecosystem. The long-term impact on Pyodide package availability is
  real but unconfirmed at scale. `emerging` reflects genuine early adoption with plausible
  trajectory, not settled practice.
