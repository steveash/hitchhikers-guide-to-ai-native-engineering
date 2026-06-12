---
source_url: https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/
source_type: blog-post
title: "datasette-agent-micropython 0.1a0"
author: Simon Willison
date_published: 2026-06-02
date_extracted: 2026-06-12
last_checked: 2026-06-12
status: current
confidence_overall: emerging
issue: "#1153"
---

# datasette-agent-micropython 0.1a0

> Simon Willison's alpha release of a MicroPython-in-WASM code-execution sandbox
> for Datasette Agent — documents concrete requirements for safe agent code execution,
> the rationale for WebAssembly over alternatives, a thread-based persistent interpreter
> design, and an honest security posture: AI-tested but not production-ready.

## Source Context

- **Type**: blog-post (a "beat" — Simon Willison's short-form release announcement at
  simonwillison.net, June 2, 2026. The post is minimal; substantial technical depth is
  in the companion article "Running Python code in a sandbox with MicroPython and WASM"
  published June 6, 2026, at simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/.
  Both the release post, the companion article, the PyPI pages for `micropython-wasm`
  and `datasette-agent-micropython` were read for this extraction.)
- **Author credibility**: Simon Willison is the creator of Datasette, Django, and the
  `llm` Python CLI. He built both the underlying `micropython-wasm` library and the
  `datasette-agent-micropython` plugin — this is first-party creator documentation.
  He has a track record of shipping working alpha tooling rapidly in the Datasette
  ecosystem and publishing candid assessments of both capabilities and limitations.
  No vendor affiliation. He explicitly acknowledges when AI tools helped him build
  his own AI tools.
- **Scope**: Covers the alpha release of `datasette-agent-micropython` — a Datasette
  Agent plugin that adds sandboxed Python code execution using MicroPython compiled to
  WebAssembly via wasmtime. Includes: security requirements for agent code execution,
  why WebAssembly was chosen over alternatives, the persistent interpreter state
  architecture, AI-assisted development story, security posture, and plugin
  configuration. Does NOT cover: performance benchmarks vs. other sandboxes, production
  deployment experience at scale, security audit by third parties, comparison with
  container-based sandboxing, or formal threat model documentation.

## Extracted Claims

### Claim 1: datasette-agent-micropython enables Datasette Agent to generate and execute Python code safely by running MicroPython inside a WebAssembly sandbox

- **Evidence**: First-party release announcement from the project creator. Two
  published PyPI packages (`micropython-wasm` 0.1a2, `datasette-agent-micropython`
  0.1a0) confirm working implementations. Live demo at agent.datasette.io.
- **Confidence**: settled (first-party; packages published on PyPI; live demo operational)
- **Quote**: "I want Datasette Agent to be able to generate and execute Python code safely. This alpha is looking promising so far. GPT-5.5 has so far failed to break out of the sandbox!"
  *(Source: simonwillison.net/2026/Jun/2/datasette-agent-micropython/)*
- **Our assessment**: This is the fourth plugin for Datasette Agent (after charts,
  image generation, and Fly Sprites). Unlike datasette-agent-sprites (which uses a
  persistent remote Fly Sprites cloud sandbox), this plugin embeds a WASM runtime
  locally in the Python process. The distinction matters architecturally: local WASM
  means no external service dependency, but also means the sandbox runs in the same
  machine as the host application. For practitioners: this is a real working
  implementation at alpha stability, not a design proposal.

### Claim 2: Safe agent code execution requires four distinct security controls: memory limits, CPU limits, file access control, and network access control

- **Evidence**: Author's explicit enumeration in the companion article, framed as
  the requirements that drove his sandbox design. Each requirement maps to a specific
  attack vector (memory exhaustion, CPU-burning loops, data exfiltration via filesystem,
  data exfiltration via network).
- **Confidence**: emerging (author's threat-modeled design framework; not derived from
  a formal security standard, but the four-control structure is well-reasoned and
  consistent with secure sandbox design literature)
- **Quote**: "Executed code must be subject to both memory and CPU limits." and "File access must be strictly controlled. Either no filesystem access at all or I get to define exactly which files can be read and which files can be written to" and "Network access is controlled as well. Sandboxed code should not be able to communicate with anything without going through a layer I fully control"
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: These four controls are a useful minimum specification for
  practitioners evaluating sandbox options for AI agent code execution. "CPU limits"
  is specifically motivated by denial-of-service via string-concatenation loops, not
  just computation-heavy code — the threat model includes malicious/adversarial inputs
  from LLMs. "Network access controlled via a layer I fully control" is a meaningful
  principle: not no-network, but mediated-network, where the host application decides
  what the sandboxed code can reach.

### Claim 3: WebAssembly was chosen over JavaScript embedding and other alternatives because it was designed from the start to support isolation, with a decade of browser testing

- **Evidence**: Author's explicit design decision with reasoning in companion article.
  He also identified a specific Python library (`wasmtime`) that is "actively maintained,
  and has binary wheels" — operational criteria alongside security criteria.
- **Confidence**: emerging (author's design decision; the WASM isolation argument is
  well-established in the literature, but the "better than JavaScript" comparison is
  the author's assessment)
- **Quote**: "WebAssembly is a much better candidate. It was designed from the start to support all of the characteristics I care about and has been tested in browsers for nearly a decade."
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: The JavaScript engine rejection ("extremely complicated, and are
  not designed for easy embedding") and the Pyodide rejection (browser/Node.js only;
  see Claim 4) left WebAssembly as the clear choice. The "tested in browsers for nearly
  a decade" argument is important: WASM's security model has been stress-tested by
  browser vendors with significant security incentives. Using wasmtime (a standalone
  WASM runtime) brings that security model to server-side Python without requiring
  Node.js.

### Claim 4: Pyodide (the browser-based Python-in-WASM runtime) was explicitly rejected as a sandboxing option because it can only run in a browser or Node.js context

- **Evidence**: Author's statement in companion article, citing October 2024 guidance
  from the Pyodide project itself.
- **Confidence**: settled (factual constraint about Pyodide's build toolchain
  dependencies; confirmed by the Pyodide project's own documentation)
- **Quote**: "Pyodide is built by the Emscripten toolchain and can only run in a browser or Node.js"
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: This is a direct constraint that eliminates Pyodide for
  server-side Python sandboxing. The `blog-simonwillison-pyodide-asgi-browser.md`
  note documents a working use of Pyodide in a browser context — which is exactly
  the runtime context Pyodide supports. The two approaches (Pyodide in browser vs.
  MicroPython WASM server-side) are complementary rather than competing: they target
  different deployment contexts. Practitioners building server-side agent code
  execution should not assume Pyodide is an option.

### Claim 5: Persistent interpreter state — enabling variables and imports to survive across multiple tool calls in the same session — was the hardest technical problem, solved via a Python thread + host function architecture

- **Evidence**: Author's direct characterization in companion article, with full
  architecture description and a code example demonstrating cross-call state
  persistence. Published code on GitHub provides independent verification.
- **Confidence**: settled (code published at GitHub; architecture described; working
  example provided)
- **Quote**: "The trickiest piece to solve was persistent interpreter state." and "Inside WASM the MicroPython interpreter blocks waiting for a `__session_next__()` host function to return the next line of code."
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: The architecture is non-obvious: a Python thread on the host
  side manages a request/reply queue; inside WASM, MicroPython calls back to the host
  via `__session_next__()` (blocking) to receive the next code fragment; results are
  returned via `__session_result__()`. This bidirectional host-function design is what
  enables persistent state. Without it, each `run()` call would require a fresh WASM
  interpreter startup and all state would be lost. For practitioners: the thread-based
  persistent session pattern is reusable for any WASM interpreter that supports host
  function callbacks.

### Claim 6: The host function interface was implemented in 78 lines of C, compiled into a 362KB WebAssembly binary distributed as a PyPI wheel

- **Evidence**: Author's direct measurements in companion article, with a GitHub link
  to the specific C source file. PyPI distribution means no end-user compilation.
- **Confidence**: settled (specific measurements, public GitHub source, published PyPI
  package)
- **Quote**: "78 lines of C, which ends up compiled into the 362KB WebAssembly blob."
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: The 362KB WASM binary packaged as a PyPI wheel is architecturally
  significant: no end-user compilation of C or MicroPython is required — `pip install
  micropython-wasm` is sufficient. This is the "actively maintained, and has binary
  wheels" requirement for wasmtime applied to the output artifact. The 78-line C module
  is small enough for a practitioner to audit directly — Willison explicitly read and
  verified it with multiple AI models to check for flaws.

### Claim 7: CPU limits are implemented via wasmtime's "fuel" mechanism, but the author acknowledges uncertainty about the right fuel budget

- **Evidence**: Author's explicit admission in companion article. Plugin defaults
  (10 million fuel units in datasette-agent-micropython PyPI description) differ from
  the 20 million mentioned in the companion article — the setting was changed between
  versions.
- **Confidence**: anecdotal (author's own admitted uncertainty about calibration)
- **Quote**: "I'm not confident that it's the most appropriate value"
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: The fuel mechanism is real (wasmtime's built-in CPU budget
  concept), but its calibration is an open problem. Willison tested it with a
  `while True: s += "longer"` infinite loop and confirmed it halts with exit code 1
  and the message "micropython-wasm: guest exited with code 1". The admission that
  "the units are hard to reason about" is important for practitioners: fuel-based CPU
  limits require empirical calibration for the target workload, not just a default.

### Claim 8: GPT-5.5 Pro and Codex Desktop were used to build the sandbox, with AI tools enabling rapid prototyping from initial research to working C implementation

- **Evidence**: Author's direct description in companion article — GPT-5.5 Pro for
  identifying relevant prior work (MicroPython WASI PR), Codex for implementing the
  initial prototype.
- **Confidence**: anecdotal (single practitioner account)
- **Quote**: "I had GPT-5.5 Pro do some research for me...Codex ended up solving this with 78 lines of C."
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: This is a concrete example of AI-assisted development of AI
  infrastructure — the tool being built (an agent code execution sandbox) was built
  with AI agents. GPT-5.5 Pro identified the key upstream MicroPython PR (WASI
  support by Yamamoto Takahashi) that Willison might not have found manually. Codex
  implemented the C host function module. Willison's role shifted toward direction,
  validation, and auditing ("I read the C and had two different models explain it to
  me") rather than authorship.

### Claim 9: GPT-5.5 tested against the sandbox in adversarial attempts has so far failed to break out

- **Evidence**: Author's statement in the release post. The companion article
  provides slightly more detail but the core claim is identical.
- **Confidence**: anecdotal (limited informal testing by a single evaluator using a
  single model; not a formal security audit; "so far" is explicitly non-definitive)
- **Quote**: "GPT-5.5 has so far failed to break out of the sandbox!"
  *(Source: simonwillison.net/2026/Jun/2/datasette-agent-micropython/)*
- **Our assessment**: "So far" and an exclamation mark together signal cautious
  optimism, not security confidence. One model failing to escape in informal testing
  is weak evidence of sandbox security — it establishes that the obvious attacks
  don't work, not that the sandbox is sound. For practitioners: treat this as
  "passed initial smoke testing" rather than "security hardened." The author's own
  security disclaimer (Claim 10) is the authoritative risk assessment.

### Claim 10: The author explicitly marks the sandbox as alpha software not ready for production deployment, and acknowledges the irony of building a new sandboxing library after criticizing immature sandboxing libraries

- **Evidence**: Author's direct security disclaimer in companion article.
- **Confidence**: settled (unambiguous first-party disclaimer)
- **Quote**: "I've put it through enough testing that I'm OK using it myself...I'm not ready to recommend it to anyone who isn't willing to take a significant risk."
  *(Source: simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)*
- **Our assessment**: This is the most operationally important claim for practitioners.
  The author is not underselling: "significant risk" means this is not a production
  sandbox. The PyPI page for `micropython-wasm` notes it's built from "MicroPython
  PR #13676" and "MicroPython's WASI Unix variant is still experimental upstream, so
  this package should also be treated as experimental." Two layers of experimental
  upstream status (MicroPython WASI + the wrapper package) are compounded. The guide
  should not recommend this as a production sandboxing pattern until the upstream
  stabilizes.

### Claim 11: The datasette-agent-micropython plugin maintains per-conversation interpreter state, with configurable limits for concurrent sessions, wall-clock timeout, WASM memory, fuel budget, and maximum output length

- **Evidence**: PyPI package description for `datasette-agent-micropython`, first-party
  documentation.
- **Confidence**: settled (first-party PyPI description)
- **Quote**: (no single prose quote; see Concrete Artifacts for the full configuration
  parameter list)
- **Our assessment**: The five configurable limits (sessions: 16, timeout: 5s, memory:
  16MB, fuel: 10M, output: 10K chars) are the operational interface between the plugin
  administrator and the sandbox security model. Administrators who deploy this plugin
  must make active decisions about these values. The defaults are reasonable starting
  points but the fuel default changed between the companion article (20M) and the PyPI
  release (10M), suggesting ongoing calibration. The per-conversation session model
  means each conversation's Python state is isolated — two simultaneous users cannot
  share or corrupt each other's interpreter state.

### Claim 12: The plugin exposes a `read_only_sql_query()` host function giving sandboxed MicroPython code access to Datasette databases while enforcing the requesting user's permission level

- **Evidence**: PyPI package description for `datasette-agent-micropython`.
- **Confidence**: settled (first-party PyPI documentation)
- **Quote**: "Database Integration: Includes a `read_only_sql_query()` helper function for querying Datasette databases with SQL, supporting parameterized queries and respecting user permissions."
  *(Source: PyPI, pypi.org/project/datasette-agent-micropython/)*
- **Our assessment**: The controlled host function exposure pattern is significant:
  sandboxed code cannot make arbitrary network calls or file reads, but it can call
  `read_only_sql_query()` which goes through the Datasette permission layer. This
  implements the "network access controlled via a layer I fully control" principle
  from Claim 2 in a specific, useful way. LLM-generated Python code inside the
  sandbox gets SQL access to the database but cannot exfiltrate that data to
  arbitrary endpoints.

## Concrete Artifacts

### Persistent Session API (verbatim from simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)

```python
with MicroPythonSession() as session:
    print(session.run("x = 10\nprint(x)").stdout)
    print(session.run("x += 5\nprint(x)").stdout)
```

*Demonstrates cross-call state persistence: `x` retains its value between the two
`session.run()` calls. The `MicroPythonSession` context manager manages the background
thread hosting the persistent MicroPython interpreter inside WASM.*

### CLI Invocation (verbatim from PyPI, pypi.org/project/micropython-wasm/)

```bash
uvx micropython-wasm -c 'print("Hello world")'
```

### CPU Limit Exhaustion Response (verbatim from simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/)

```
micropython-wasm: guest exited with code 1
```

*Error produced when wasmtime fuel budget is exhausted, e.g., by `while True: s += "longer"`.*

### datasette-agent-micropython Plugin Configuration (from PyPI, pypi.org/project/datasette-agent-micropython/)

```
Configurable limits (via Datasette plugin settings):
  - Maximum concurrent sessions: default 16
  - Wall clock timeout:          default 5.0 seconds
  - WebAssembly memory:          default 16MB
  - Execution fuel budget:       default 10,000,000
  - Maximum output characters:   default 10,000
```

### Plugin Tool Parameters (from PyPI, pypi.org/project/datasette-agent-micropython/)

```
Tool: execute_micropython
Parameters:
  python         — Python code to execute
  reset_context  — clear interpreter state (boolean)
  show_result    — display code and output inline (boolean)
```

*The `reset_context` parameter allows the agent to explicitly discard interpreter
state mid-conversation, supporting stateless one-shot execution within a stateful session.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-agent.md` Claim 5: "My favorite feature of Datasette
    Agent is that, like the rest of Datasette, it's extensible using plugins." This
    source adds the fourth plugin to the ecosystem, confirming the plugin extension
    model continues to scale beyond the three launch plugins. The extensibility claim
    is further corroborated by a plugin adding a non-trivial capability (WASM sandboxing)
    without modifying core agent code.
  - `blog-simonwillison-datasette-agent-charts.md` Claim 7: Both plugins install as
    standard Datasette packages alongside datasette-agent. The composable plugin
    pattern (separate installable packages for separate capabilities) is confirmed
    again with this release.

- **Extends**:
  - `blog-simonwillison-datasette-agent.md` Claim 6: That note documents
    `datasette-agent-sprites` ("provides tools for executing code in a Fly Sprites
    persistent sandbox") as one of three launch plugins. This source introduces a
    **second** code-execution plugin with a different architecture: local WASM vs.
    remote Fly Sprites cloud sandbox. Together they represent two distinct sandboxing
    strategies available to Datasette Agent deployments — embedded (no external
    dependency, bounded by host machine resources) vs. remote (network-dependent,
    potentially more isolated from the host).
  - `blog-simonwillison-pyodide-asgi-browser.md` overall: That note documents Pyodide
    running Python ASGI apps in a browser via service workers. The companion article for
    this source explicitly rejects Pyodide for server-side sandboxing because
    "Pyodide is built by the Emscripten toolchain and can only run in a browser or
    Node.js." The two notes are complementary: Pyodide owns the browser deployment
    context; MicroPython WASM via wasmtime owns the server-side Python deployment
    context. Neither is a drop-in replacement for the other.

- **Novel**:
  - **First corpus documentation of MicroPython WASM as a server-side agent code
    execution sandbox**: No existing corpus note describes a pattern where MicroPython
    is compiled to WASM and embedded in a Python process via wasmtime as an agent
    code execution capability.
  - **First corpus documentation of the four-control security requirement framework
    for agent code execution**: Memory + CPU + file + network as a structured
    requirement set for evaluating and building agent code sandboxes.
  - **First corpus documentation of AI-built AI infrastructure via the adversarial
    sandbox testing pattern**: GPT-5.5 helping build and then being used to probe
    its own execution sandbox is a novel loop in the corpus.
  - **Host function exposure as a controlled capability pattern**: `read_only_sql_query()`
    as a mediated host function giving sandboxed code SQL access without arbitrary
    network access is a concrete implementation of least-privilege capability exposure
    that is new to the corpus.
  - **Thread-based persistent WASM interpreter state architecture**: The
    `__session_next__()` host function blocking approach for persistent WASM interpreter
    state is a specific, reusable pattern not documented elsewhere in the corpus.

- **Contradicts**: None identified. The micropython-wasm and datasette-agent-sprites
  approaches to code execution sandboxing differ in architecture (local WASM vs. remote
  cloud) but target different deployment contexts — this is a conditioning variable,
  not a contradiction. No contradiction issue required.

## Guide Impact

- **Chapter 02 / Chapter on Agent Tool Design (safe code execution as an agent tool)**:
  Add datasette-agent-micropython as a concrete worked example of safe code execution
  as an agent capability. Key design decisions to highlight: (1) the four-control
  security requirement framework (Claim 2) as a checklist for sandbox evaluation, (2)
  the local WASM vs. remote sandbox tradeoff (this source vs. datasette-agent-sprites
  from `blog-simonwillison-datasette-agent.md` Claim 6), (3) the host function exposure
  pattern for giving sandboxed code controlled access to host capabilities (Claim 12).

- **Chapter 03 / Chapter on Safety in Agentic Systems (sandboxing patterns)**:
  Add the WebAssembly sandboxing rationale (Claim 3) alongside the explicit Pyodide
  rejection (Claim 4) as a decision framework. Practitioners evaluating sandbox
  options should know: Pyodide requires browser/Node.js, wasmtime-based WASM works
  server-side, JavaScript embedding is complex. The guide should note Claim 10's
  explicit alpha/experimental status — this pattern is promising but not yet
  production-safe. Pair with the fuel calibration uncertainty (Claim 7) as a
  practical caveat.

- **Chapter 04 or Security chapter (security testing of AI agents against their
  own sandboxes)**: Add Claim 9 (GPT-5.5 tested against the sandbox) as an example
  of adversarial sandbox testing, with the caveat that one model failing informally
  is weak evidence. The guide should recommend formal security auditing before
  production deployment of any AI-generated or AI-assisted sandbox implementation.

- **Chapter on AI-assisted development (meta-pattern: AI builds AI tools)**:
  Add Claims 8 and 10 together. GPT-5.5 Pro + Codex accelerated the sandbox from
  idea to working prototype; the author's explicit irony acknowledgment ("Having
  complained about immature, loosely-maintained sandboxing libraries, it's deeply
  ironic that I've now built my own!") is a signal that AI tooling lowers the barrier
  to building infrastructure that was previously too costly to build, including
  security-sensitive infrastructure that requires the same rigor it would have required
  before.

## Extraction Notes

- **Two primary sources fetched**: The June 2 release post is the canonical source
  URL (as listed in the issue). The June 6 companion article
  (simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/) provides all substantive
  technical detail. Both were read; the companion article is the source for the
  majority of technical claims here.
- **PyPI pages also consulted**: Both `micropython-wasm` (0.1a2) and
  `datasette-agent-micropython` (0.1a0) PyPI pages were fetched and provide
  first-party documentation of the packages.
- **Verbatim quotes**: The WebFetch model provided verbatim text for the brief
  release post but declined full verbatim reproduction of the companion article
  on copyright grounds. Key quotes were obtained via targeted extraction prompts.
  All quotes in this note were verified as character-for-character matches against
  the source text excerpts returned by WebFetch.
- **Fuel default discrepancy**: The companion article (Jun 6) mentions 20 million
  fuel units as the default; the PyPI page for datasette-agent-micropython lists
  10 million. This likely reflects a configuration change between the article and
  the 0.1a0 release. Claim 7 notes both values.
- **Cross-references verified**: `blog-simonwillison-datasette-agent.md` Claim 5
  confirmed at lines 118–129 of that note; Claim 6 confirmed at lines 131–149.
  `blog-simonwillison-datasette-agent-charts.md` Claim 7 confirmed at lines 141–153.
  `blog-simonwillison-pyodide-asgi-browser.md` Claim 1 confirmed at lines 47–60.
- **No contradictions filed**: The micropython approach and Fly Sprites approach
  are different designs for different deployment contexts (embedded vs. remote).
  No existing corpus claim materially opposes the claims in this source.
