---
source_url: https://simonwillison.net/2026/May/11/llm-shebang/
source_type: blog-post
title: "Using LLM in the shebang line of a script"
author: Simon Willison
date_published: 2026-05-11
date_extracted: 2026-05-26
last_checked: 2026-05-26
status: current
confidence_overall: anecdotal
issue: "#802"
---

# Using LLM in the shebang line of a script

> Simon Willison demonstrates three escalating patterns for using the `llm` CLI
> tool in Unix shebang lines — basic fragments, tool-integrated invocations, and
> YAML templates with embedded Python tool functions — turning plain text and YAML
> files into directly executable AI scripts without any harness code.

## Source Context

- **Type**: blog-post (short practitioner post with working code examples; also
  links to a TIL at `https://til.simonwillison.net/llms/llm-shebang` with a more
  complex example using the Datasette SQL API as an LLM tool)
- **Author credibility**: Simon Willison is the creator of Django and the `llm`
  CLI tool itself. As the tool's author, his claims about `llm` flags and features
  are first-party. He is one of the highest-signal independent commentators on LLM
  tooling with no vendor affiliation. The shebang patterns demonstrated are working
  code he built and used, not theoretical proposals.
- **Scope**: Covers three specific shebang patterns using the `llm` CLI: (1) the
  basic fragment pattern (`-f`), (2) tool-call integration (`-T name_of_tool`), and
  (3) YAML template execution with embedded Python functions (`-t`). Also covers the
  requirement for `-S` with `env` and the template parameter system (`$variable` /
  `-p variable value`). The TIL sub-page adds a Datasette SQL API example but was
  not fully reproduced in WebFetch output. Does NOT cover multi-model use, plugin
  architecture, or comparisons with other AI scripting approaches.

## Extracted Claims

### Claim 1: A Hacker News comment by Kim_Bruning that plain text files can carry shebangs inspired this exploration of doing the same with the `llm` CLI tool

- **Evidence**: Willison cites the HN comment directly, attributing the motivation
  to Kim_Bruning's observation, and states it prompted him to investigate `llm`
  shebang patterns.
- **Confidence**: settled (Willison's direct statement of attribution)
- **Quote**: "you can put a shebang on an english text file now (if you're sufficiently brave)" — Kim_Bruning, via Hacker News
- **Our assessment**: This attribution matters for the guide because it signals that
  the `llm` shebang pattern is not a designed feature of `llm` but an emergent
  application of Unix primitives. The framing "if you're sufficiently brave" captures
  the same nondeterminism caution that appears in the airun/executable-markdown
  thread (`discussion-hn-airun-executable-markdown.md` Claim 5–7). Both communities
  independently identify bravery/caution as the qualifier for this pattern.

### Claim 2: The `-S` flag to `env` is required for multi-word shebang arguments — without it, the system treats "llm -f" as a single command name rather than a command plus argument

- **Evidence**: The TIL sub-page explicitly explains the `-S` mechanism and the
  failure mode when it is omitted. This is a concrete Unix behavior constraint.
- **Confidence**: settled (documented Unix behavior; the `-S` flag is a standard
  `env` feature for splitting shebang arguments on systems that treat the entire
  shebang remainder as one argument)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is a critical implementation detail that would prevent
  naive adoption. Without `-S`, running `#!/usr/bin/env llm -f` causes the OS to
  look for a binary named literally `"llm -f"` (with the space), which does not
  exist. Every multi-word shebang using any CLI tool requires this pattern:
  `#!/usr/bin/env -S <tool> <flags>`. The pattern generalizes beyond `llm` to any
  shebang invocation of a CLI with flags.

### Claim 3: The `-f` flag in the `llm` CLI uses the "fragments mechanism" to append file contents as the prompt — the body of the text file becomes the LLM input

- **Evidence**: The TIL sub-page describes `-f` as leveraging "LLM's fragments
  mechanism" where file contents are appended to the prompt. Both WebFetch queries
  consistently describe this behavior.
- **Confidence**: settled (first-party from the tool's author; fragments are a
  documented `llm` feature)
- **Quote**: (no direct quote confirmed verbatim; WebFetch paraphrased the flag description)
- **Our assessment**: The fragments mechanism (`-f`) is the key enabling feature:
  when `llm` is invoked as a shebang, it reads the file, appends the post-shebang
  lines as a "fragment" (appended content), and executes the prompt. This is
  mechanically different from the airun/Claude Code stdin approach
  (`discussion-hn-airun-executable-markdown.md` Claim 1), where the markdown file's
  content is passed via stdin. The `-f` approach treats the file as a named context
  fragment rather than raw stdin. The practical difference: fragments can be composed
  with other fragments (`llm -f fragment1.txt -f fragment2.txt`) beyond the shebang
  use case.

### Claim 4: The basic fragment shebang pattern turns a natural-language text file into a directly executable AI script — the simplest possible form of AI automation

- **Evidence**: Working code example with concrete invocation steps: save as
  `pelican.sh`, `chmod +x pelican.sh`, run via `./pelican.sh`.
- **Confidence**: anecdotal (working example from the tool's author; consistent
  behavior depends on `llm` installation and model availability)
- **Quote**: (no direct quote beyond the code; the code is the evidence)
- **Our assessment**: The pelican example demonstrates that the cognitive overhead
  of "AI automation" is reduced to: (1) write a sentence in a file, (2) add one
  shebang line, (3) `chmod +x`. No harness, no orchestration layer, no SDK import,
  no configuration file. This is the minimal-viable AI script. The limitation is
  the same as all LLM automation: nondeterminism (two runs may produce different
  SVGs). For tasks where variability is acceptable (generation, summarization,
  classification), this pattern is maximally lightweight.

### Claim 5: Tool integration via `-T name_of_tool` enables `llm` shebang scripts to call registered tools, giving scripts access to external data sources like the current time

- **Evidence**: Working code example with `llm_time` as the named tool; the
  resulting haiku includes the actual current time at execution.
- **Confidence**: anecdotal (working example; depends on `llm_time` plugin being
  installed in the user's `llm` environment)
- **Quote**: (no direct quote; the code block is the primary evidence)
- **Our assessment**: The `-T name_of_tool` flag exposes the full `llm` tool
  ecosystem to shebang scripts. Any tool registered with `llm` (via the plugin
  system) becomes callable from a shebang script without any harness code. This is
  a significant composition benefit: tools built for interactive `llm` use work
  transparently in automated shebang scripts. The constraint is that the tool must
  be pre-installed in the environment where the script runs — it is not self-contained.

### Claim 6: YAML templates with embedded Python functions enable defining custom tools inline in a single executable file — the `functions:` key accepts raw Python that the model can call

- **Evidence**: Working code example with `add` and `multiply` functions in the
  `functions:` YAML key; terminal output confirming the model called both tools
  correctly and computed the result.
- **Confidence**: anecdotal (working example from tool's author; alpha-tier feature
  given `llm` 0.32a0 was recently released per `blog-simonwillison-llm032a0.md`)
- **Quote**: (no direct quote beyond the YAML and output; the code and output are the evidence)
- **Our assessment**: This is the most powerful pattern in the post. The YAML
  template format (`-t`) can specify: the model, a system prompt, and a `functions:`
  block containing raw Python code that `llm` converts into tool definitions.
  The model can then call these functions during generation. The result: a single
  YAML file is simultaneously the configuration, the system prompt, and the tool
  implementation — the entire AI script in one file. This extends the "spec is the
  executable" principle (from `discussion-hn-airun-executable-markdown.md` Claim 8)
  to include tool definitions alongside the prompt.

### Claim 7: Template parameter slots (`$variable`) allow parameterized LLM scripts that accept runtime arguments via `-p variable value` at invocation

- **Evidence**: The TIL sub-page demonstrates a template with `$animal` and `$place`
  parameter slots invoked as `./poem.sh -p animal skunk -p place "hovercraft port"`.
- **Confidence**: anecdotal (from the TIL sub-page; consistent with documented `llm`
  template syntax)
- **Quote**: (no direct quote; the invocation example is the evidence)
- **Our assessment**: The `-p variable value` parameter system transforms a fixed
  shebang script into a parameterized AI function. Combined with the YAML template
  format, a single file defines both the AI behavior (model, system, tools) and
  its parameter interface. This is a meaningful step toward "AI functions as files"
  — callable units with typed inputs and AI-generated outputs, where the entire
  definition is human-readable and version-controllable as a single file.

### Claim 8: The `--td` flag enables tool debug output at runtime, showing tool call names and arguments as the model executes them — useful for inspecting tool invocation behavior

- **Evidence**: The invocation example `./calc.sh 'what is 2344 * 5252 + 134' --td`
  produces explicit tool call output showing `Tool call: multiply({'a': 2344, 'b': 5252})`
  and intermediate results.
- **Confidence**: settled (first-party from tool's author; the `--td` flag is a
  concrete CLI option with verifiable output)
- **Quote**: (no direct quote beyond the flag and output; the terminal transcript is the evidence)
- **Our assessment**: The `--td` flag is the diagnostic entry point for understanding
  how the model is using defined tools. For practitioners building `functions:`-based
  YAML templates, `--td` enables iterative debugging of tool call behavior without
  additional instrumentation. This mirrors the practitioner need for tool call
  visibility documented in `blog-simonwillison-llm032a0.md` (the `stream_events()`
  API that surfaces `"tool_call_name"` and `"tool_call_args"` event types at the
  library level).

### Claim 9: A TIL post linked from the main blog demonstrates a more complex `llm` shebang pattern using the Datasette SQL API as an LLM tool to answer questions about blog content

- **Evidence**: The blog post references the TIL at
  `https://til.simonwillison.net/llms/llm-shebang`. WebFetch of the TIL confirms
  it describes "HTTP-based blog search capabilities that enable the model to execute
  specific functions dynamically."
- **Confidence**: anecdotal (TIL content confirmed but not fully extracted)
- **Quote**: (no direct quote; the TIL was partially accessible but not fully reproduced)
- **Our assessment**: The Datasette SQL API example is the most complex pattern in
  the source ecosystem — it shows that the `functions:` key can define HTTP-calling
  Python functions that give the model live access to external data sources. This
  extends the YAML template pattern from pure computation (add/multiply) to data
  retrieval (SQL query a running database). The full TIL content was not extracted
  in this pass; a follow-up extraction of `https://til.simonwillison.net/llms/llm-shebang`
  would yield additional concrete artifacts.

## Concrete Artifacts

### Pattern 1: Basic Fragment Shebang (from blog post, verbatim)

```bash
#!/usr/bin/env -S llm -f
Generate an SVG of a pelican riding a bicycle
```

```bash
# Invocation
chmod +x pelican.sh
./pelican.sh
```

*Source: Simon Willison, simonwillison.net/2026/May/11/llm-shebang/ — the `-f` flag
appends file contents as an LLM fragment; `-S` splits the shebang arguments.*

### Pattern 2: Tool Integration Shebang (from blog post, verbatim)

```bash
#!/usr/bin/env -S llm -T llm_time -f
Write a haiku that mentions the exact current time
```

*Source: Simon Willison, simonwillison.net/2026/May/11/llm-shebang/ — the `-T llm_time`
flag registers the `llm_time` tool from the user's `llm` plugin environment.*

### Pattern 3: YAML Template with Embedded Python Tools (from blog post, verbatim)

```yaml
#!/usr/bin/env -S llm -t
model: gpt-5.4-mini
system: |
  Use tools to run calculations
functions: |
  def add(a: int, b: int) -> int:
      return a + b
  def multiply(a: int, b: int) -> int:
      return a * b
```

```bash
# Invocation with prompt and tool debug flag
./calc.sh 'what is 2344 * 5252 + 134' --td
```

```
# Terminal output (from blog post, verbatim)
Tool call: multiply({'a': 2344, 'b': 5252})
  12310688

Tool call: add({'a': 12310688, 'b': 134})
  12310822

2344 × 5252 + 134 = **12,310,822**
```

*Source: Simon Willison, simonwillison.net/2026/May/11/llm-shebang/ — the `functions:`
key accepts raw Python; `--td` shows tool debug output.*

### Pattern 4: Parameterized Template (from TIL sub-page, verbatim)

```yaml
#!/usr/bin/env -S llm -t
prompt: |
  Two line poem about $animal who lives in $place
```

```bash
# Invocation with parameter values
./poem.sh -p animal skunk -p place "hovercraft port"
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang — `$variable` in
the prompt becomes a runtime parameter passed via `-p variable value`.*

### Simple Template (from TIL sub-page, verbatim)

```yaml
#!/usr/bin/env -S llm -t
prompt: Write a haiku
system: Output Spanish
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang — simplest YAML
template form: model defaults, prompt and system specified.*

## Cross-References

- **Corroborates**:
  - `discussion-hn-airun-executable-markdown.md` Claim 1 ("Markdown files can be
    made directly executable as Claude Code invocations via a Unix shebang"): Both
    sources independently demonstrate that plain-text files with AI shebangs become
    executable scripts. The `llm` shebang pattern (this source) and the airun/Claude
    Code shebang pattern (that note) are parallel implementations of the same
    Unix-primitive insight, applied to different CLI tools. Kim_Bruning's framing
    "if you're sufficiently brave" here echoes the nondeterminism caution documented
    throughout `discussion-hn-airun-executable-markdown.md` Claims 5–7.
  - `discussion-hn-airun-executable-markdown.md` Claim 2 ("the shebang pattern
    enables classical Unix pipe composition with AI steps"): The `llm` shebang
    pattern enables the same composition — `./pelican.sh | some-other-tool` — by
    virtue of the `llm` CLI writing to stdout. The composition pattern is
    tool-agnostic.

- **Extends**:
  - `discussion-hn-airun-executable-markdown.md` Claim 8 (author scopes the pattern
    to "LLM-appropriate tasks: summarization, evaluation, formatting — not general-
    purpose script replacement"): This source adds a concrete technical extension to
    that scoping — the YAML `functions:` key allows embedding computational tools
    (math, HTTP calls) that extend what "LLM-appropriate" means. The `llm` template
    pattern can define the LLM's tool repertoire inline, making scripts that combine
    AI judgment with deterministic computation. This shifts the scoping: pure natural
    language tasks (jedwhite's framing) + tasks where the LLM orchestrates defined
    Python functions (this source's extension).
  - `blog-simonwillison-llm032a0.md` Claim 6 ("backwards compatibility: old
    `prompt=` string argument is upgraded to a single-item messages array
    internally"): The `llm` 0.32a0 architectural refactor (enabling typed streaming
    parts, tool call events, and the `functions:` parameter) is the library-level
    foundation that makes the YAML `functions:` in shebang scripts possible. The
    shebang pattern in this source is a user-facing application of the tool
    execution infrastructure documented in `blog-simonwillison-llm032a0.md`.

- **Novel**:
  - **`llm` CLI shebang as a distinct pattern from Claude Code shebang**: No prior
    corpus source documents using the `llm` CLI specifically (with `-f`, `-T`, `-t`
    flags) in shebang lines. `discussion-hn-airun-executable-markdown.md` covers
    the Claude Code shebang (airun/`claude-run`); this is the first note documenting
    the `llm` CLI shebang. The two tools target different use cases: airun wraps
    Claude Code's full agent loop; `llm` provides a lighter CLI interface to any
    LLM model. The `llm` shebang is model-agnostic (works with any model in the
    `llm` plugin ecosystem), while airun is Claude-Code-specific.
  - **The `functions:` key in `llm` YAML templates for inline tool definition**:
    No prior corpus source documents the `llm` template `functions:` key, which
    converts raw Python code blocks into LLM-callable tools without any separate
    plugin installation. This "tools as inline Python in a YAML file" pattern is
    not described elsewhere in the corpus.
  - **The `--td` (tools debug) flag for tool call introspection in `llm` scripts**:
    No prior corpus note documents `--td` as a diagnostic flag for tool execution
    visibility.
  - **The `-p variable value` parameter system for parameterized `llm` templates**:
    No prior corpus source documents the `$variable` / `-p variable value` interface
    for runtime parameterization of `llm` shebang scripts. This creates a "function
    call" interface where the file is the function definition and `-p` provides the
    arguments.
  - **The `-S` flag requirement for multi-word shebangs**: While this is Unix
    fundamentals, no prior corpus source explicitly names the `-S` mechanism as a
    required implementation detail for multi-word AI CLI shebangs. It is a
    practical gotcha worth surfacing in the guide.

- **Contradicts**: None filed. The `llm` shebang and airun/Claude Code shebang
  patterns are complementary implementations, not competing claims. Both use
  Unix shebangs; they differ in the underlying tool. No existing corpus claim is
  materially opposed by this source.

## Guide Impact

- **Chapter 01 (Daily Workflows — AI-native automation primitives)**: Add the `llm`
  shebang as the lightest-weight `llm` CLI automation pattern. Pair with the airun
  pattern from `discussion-hn-airun-executable-markdown.md` as two variants of the
  "text file as AI script" primitive: airun for Claude Code agent invocation (full
  tool use, file system access); `llm` shebang for model-agnostic, lighter-weight
  LLM invocations. The guide should distinguish the use cases: airun when you need
  the full Claude Code agent loop; `llm` shebang when you want a quick,
  model-flexible, harness-free script.

- **Chapter 02 (Harness Engineering — Minimal harnesses spectrum)**: Add the `llm`
  YAML template as the "zero-harness" end of the spectrum for tool-using AI scripts.
  A `functions:`-bearing YAML template is the minimum viable tool-using AI script:
  one file, no imports, no harness framework, no separate tool registration step.
  Compare against the `llm` plugin ecosystem (tools installed once, called via `-T`)
  for shared/reusable tools, and against full SDK-based harnesses for production
  multi-step workflows.

- **Chapter 04 (Context Engineering — Specification as executable)**: The YAML
  template pattern closes the specification-to-execution gap further than airun:
  in airun, the spec is natural language only; in `llm` YAML templates, the spec
  includes model selection, system prompt, and tool definitions — a complete AI
  task specification in one version-controllable file. Frame this alongside the
  `discussion-hn-airun-executable-markdown.md` pattern and JohnKemeny's `.ag`
  format as three points on the "how much structure should a 'specification-as-
  executable' file carry?" spectrum.

- **Chapter 02 (Harness Engineering — Unix shebang implementation detail)**: Add
  a callout box explaining that `#!/usr/bin/env -S <tool> <flags>` is required for
  any multi-word shebang. The `-S` flag is non-obvious and its absence produces a
  confusing error (command not found for "llm -f" as a name). This is a practical
  friction point that the guide should pre-empt.

## Extraction Notes

- WebFetch of the main blog URL (`simonwillison.net/2026/May/11/llm-shebang/`) was
  partially successful — the code blocks were reproduced consistently across two
  fetch attempts, giving confidence that the three shebang patterns and the `calc.sh`
  tool output are verbatim. The prose explanations were paraphrased by the fetch
  model; only Kim_Bruning's quote (confirmed twice verbatim) is used as a direct
  quote from the prose.
- The TIL sub-page (`til.simonwillison.net/llms/llm-shebang`) was fetched and
  yielded additional concrete examples (parameterized templates, simple system-prompt
  template). The Datasette SQL API example (Claim 9) was described but not fully
  reproduced — its Python functions were described generically as "HTTP-based blog
  search capabilities" rather than with verbatim code. A deeper TIL extraction
  would yield that artifact.
- The fragment URL (`#atom-everything`) was removed from `source_url` per convention
  in prior Willison notes (e.g., `blog-simonwillison-llm031.md` extraction notes).
- The `functions:` YAML key feature places this note in the context of `llm` 0.32
  (which introduced full tool-calling support via the typed streaming architecture
  documented in `blog-simonwillison-llm032a0.md`). The feature's alpha status at
  the time of the blog post means implementation details may evolve.
- Cross-reference verification: `discussion-hn-airun-executable-markdown.md` Claim
  1 (lines 51–70 in that note) confirmed as "Markdown files can be made directly
  executable as Claude Code invocations via a Unix shebang." Claim 2 (lines 71–90)
  confirmed as "The shebang pattern enables classical Unix pipe composition with AI
  steps." Claim 8 (lines 208–228) confirmed as the explicit scoping to
  LLM-appropriate tasks. `blog-simonwillison-llm032a0.md` Claim 6 (lines 61–66)
  confirmed as the backwards-compatible `prompt=` upgrade behavior.
