---
source_url: https://simonwillison.net/2026/May/11/llm-shebang/
source_type: blog-post
title: "Using LLM in the shebang line of a script"
author: Simon Willison
date_published: 2026-05-11
date_extracted: 2026-05-19
last_checked: 2026-05-19
status: current
confidence_overall: emerging
issue: "#802"
---

# Using LLM in the shebang line of a script

> Simon Willison demonstrates three levels of sophistication for using the `llm`
> CLI tool in Unix shebang lines — plain fragments, external tool integration via
> `-T`, and YAML-embedded Python function tools via `-t` — extending the
> executable-text-file pattern to a multi-model CLI that supports GPT and Claude
> alongside a path to database-backed contextual agents.

## Source Context

- **Type**: blog-post (Willison's TIL / link-blog format; short post with code
  examples; links to the full TIL at `til.simonwillison.net/llms/llm-shebang`
  for a Datasette SQL example. The blog post was read in full; the linked TIL
  was followed as a sub-page per MINER.md §1.)
- **Author credibility**: Simon Willison is the creator of Django, the author
  and maintainer of the `llm` CLI tool, and one of the most-cited independent
  practitioners in the AI tooling space. He has direct first-party authority
  on how the `llm` CLI works. This is not speculation; it describes patterns
  he implemented and uses himself.
- **Scope**: Covers three shebang patterns for the `llm` CLI: (1) plain-text
  fragment files using `-f`; (2) tool-augmented prompts using `-T`; (3) YAML
  templates with embedded Python function tools using `-t`. The TIL sub-page
  extends to template parameters, the `-x` flag for code-block extraction, and
  a Datasette SQL API example for contextual blog search. Does NOT cover: Claude
  Code integration, multi-agent orchestration, batch processing, or the full
  `llm` plugin ecosystem.

## Extracted Claims

### Claim 1: A HN community observation that "you can put a shebang on an english text file now" directly inspired this exploration of llm CLI shebang patterns

- **Evidence**: Willison's opening sentence of the blog post, citing the HN
  comment as the trigger. The HN thread is at
  `https://news.ycombinator.com/item?id=48073246#48090590`, commenter Kim_Bruning.
- **Confidence**: settled (first-person attribution in the post)
- **Quote**: "This comment on Hacker News inspired me to investigate patterns for
  using my LLM CLI tool in a shebang line"
- **Our assessment**: This is notable for the guide because it confirms the
  shebang-as-LLM-interface pattern is emergent practitioner insight arriving
  from the community, not a vendor-designed workflow. Both the airun/claude-run
  pattern (`discussion-hn-airun-executable-markdown.md` Claim 1) and this llm
  CLI pattern developed independently from community experimentation rather than
  top-down design. The Kim_Bruning comment confirms the community recognized
  that `env -S` changes the shebang game for multi-argument interpreters —
  including LLM tools.

### Claim 2: The `#!/usr/bin/env -S llm -f` shebang makes any plain text file a directly executable LLM prompt via the llm CLI's fragment mechanism

- **Evidence**: Working code example in the blog post. The pattern is
  mechanically simple: add the shebang to any text file, `chmod +x`, run it.
  The file content becomes the prompt.
- **Confidence**: settled (working example from the tool's author; the `llm`
  CLI is publicly available and the behavior is deterministic at invocation)
- **Quote**: "Here's the simplest, which takes advantage of LLM fragments:"
- **Our assessment**: This is the core claim and it is mechanically sound. The
  `llm` CLI's `-f` flag works by treating the file as a fragment and appending
  its content to the prompt; the shebang causes the file to be passed as an
  argument to `llm`. The result: a text file becomes a first-class Unix
  executable. The pattern is lighter-weight than the airun/claude-run approach
  (`discussion-hn-airun-executable-markdown.md`) because it does not require a
  separate wrapper tool — the `llm` CLI itself handles both the invocation and
  the model call.

### Claim 3: The `-S` (split) option to `env` is required in shebang lines that pass multiple arguments to the interpreter — without it, `env` treats the entire remainder as a single command name

- **Evidence**: Explanation in the TIL sub-page with a direct statement of the
  failure mode.
- **Confidence**: settled (Unix `env` behavior is OS-level documented behavior;
  the `-S` flag is standard; the failure without it is deterministic)
- **Quote**: "The `-S` (for split) option to `env` is required because, without
  it, the `env` command will treat the rest of the line as the full name of the
  command"
- **Our assessment**: This is a practical implementation prerequisite that
  practitioners need to know and that no prior corpus source explains. Any
  shebang that passes multiple flags to an interpreter (`llm -T tool -f`,
  `node --experimental-vm-modules`, etc.) requires `-S` on systems that support
  it. The claim generalizes beyond the `llm` use case: any AI CLI tool used in a
  shebang with multiple flags needs `env -S`. This is the key technical detail
  that separates "I know shebangs" from "I can use multi-flag shebangs."

### Claim 4: The `-f` flag causes the file's own content to be appended to the LLM prompt as a fragment — the script is both the executable and the prompt text

- **Evidence**: TIL sub-page direct explanation of `-f` behavior in shebang
  context.
- **Confidence**: settled (first-party; author is the tool maintainer)
- **Quote**: "The argument to `-f` is the path to a file, and the contents of
  that file will then be appended to the prompt."
- **Our assessment**: This is architecturally interesting: the `-f` flag in
  shebang context creates a self-referential file where the file IS the script
  AND the content IS the prompt. Compare with the airun pattern
  (`discussion-hn-airun-executable-markdown.md` Claim 1) where the markdown
  content becomes the prompt through a separate wrapper. Here, `llm` handles
  the fragment inclusion natively — no wrapper needed. The shebang line is
  metadata/invocation; everything below it is the prompt. Constraint: `-f`
  must come last in the shebang because the file path is appended there.

### Claim 5: External tools can be incorporated into shebang scripts via the `-T tool_name` flag, enabling capabilities like time awareness without any in-file Python code

- **Evidence**: Working code example: `#!/usr/bin/env -S llm -T llm_time -f`
  with the prompt "Write a haiku that mentions the exact current time"
- **Confidence**: settled (working example; `-T` is a documented `llm` CLI
  flag for tool inclusion; `llm_time` is a real `llm` plugin)
- **Quote**: "But you can also incorporate tool calls using the `-T name_of_tool`
  option:"
- **Our assessment**: The `-T` flag is the bridge between the simple fragment
  shebang and the full YAML template approach. It allows adding tool capabilities
  to a plain-text script without converting it to YAML — the file stays readable
  prose and the tool is specified in the shebang line. For practitioners, this
  means a "time-aware haiku generator" is a two-line file: the shebang with the
  tool flag and the English instruction. The tool plugin model (llm_time,
  llm_browser, etc.) means capability expansion happens at the shebang level
  without changing the prompt content.

### Claim 6: The `-x` flag can be added to the shebang to extract only code blocks from the LLM response, enabling clean output for generated executable files

- **Evidence**: Code example in the TIL:
  `#!/usr/bin/env -S llm -x -f` followed by `Generate an SVG of a pelican riding a bicycle`
- **Confidence**: settled (working example; `-x` is a documented `llm` CLI flag)
- **Quote**: (no direct quote; behavior shown via code example in the TIL)
- **Our assessment**: The `-x` flag is a useful composition primitive for the
  shebang pattern. A script that generates SVG, shell scripts, or code can use
  `-x` to strip the LLM's prose framing and return only the code block — making
  the output directly usable by downstream tools. This is the shebang equivalent
  of the `-x` extract pattern practitioners use in interactive llm sessions.

### Claim 7: YAML templates can be embedded directly in shebang scripts via `#!/usr/bin/env -S llm -t`, defining model, system prompt, and Python tool functions in a single file

- **Evidence**: Working code example with a calculator template defining
  `add()` and `multiply()` Python functions, invoked with
  `./calc.sh 'what is 2344 * 5252 + 134' --td`
- **Confidence**: settled (working example from tool author; the `llm` `-t`
  template flag is documented)
- **Quote**: "Or even execute YAML templates directly that define extra tools as
  Python functions"
- **Our assessment**: This is the most architecturally novel level of the
  pattern. The `#!/usr/bin/env -S llm -t` shebang invokes the `llm` template
  engine on the file rather than the fragment engine. The YAML below the shebang
  specifies model, system prompt, and inline Python functions as tools. The
  result is a self-contained agentic script where the model, system context,
  tool definitions, AND the invocation mechanism are all in one file. Compare
  with the JohnKemeny `.ag` format in `discussion-hn-airun-executable-markdown.md`
  Claim 11 — that format aimed for formal contract-style invocation
  (Require/Invariant/Ensure/Rescue); this template approach aims for
  pragmatic tool embedding. Both are "structured" shebang patterns but on
  different axes: JohnKemeny's is about constraint specification; Willison's
  is about capability definition.

### Claim 8: LLM templates support parameterization via `$variable` syntax, making the same script reusable across different inputs

- **Evidence**: TIL code example showing:
  ```
  #!/usr/bin/env -S llm -t
  prompt: |
    Two line poem about $animal who lives in $place
  ```
- **Confidence**: settled (working example; `$variable` interpolation is a
  documented `llm` template feature)
- **Quote**: (no direct quote; shown via code example in the TIL)
- **Our assessment**: Template parameterization turns a shebang script into a
  reusable prompt function. The invocation `./poem.sh --param animal=cat --param
  place="the moon"` would substitute the variables. For practitioners, this
  is the first step toward a library of parameterized LLM scripts that can be
  called from other scripts or CI pipelines — each script is a typed prompt
  function with a defined interface.

### Claim 9: The pattern scales to complex real-world tasks: a YAML template can embed a Python function that calls the Datasette SQL API to provide contextual answers about blog content

- **Evidence**: TIL sub-page Datasette example with `model: gpt-5.5`, system
  prompt "You answer questions from Simon Willison's blog", and a Python
  function using `httpx` to query `datasette.simonwillison.net/simonwillisonblog.json`.
  Example invocation: `./blog.sh "Has Simon implemented GraphQL?"`
- **Confidence**: emerging (working example by the tool author; Datasette is
  Willison's own project so this is a first-party integration; the pattern
  generalizes to any API-queryable data source)
- **Quote**: "Read the full TIL for a more complex example that uses the
  Datasette SQL API to answer questions about content on my blog."
- **Our assessment**: This is the most significant claim for the guide. The
  Datasette example shows that the llm shebang template pattern is not a toy —
  it can implement a retrieval-augmented generation (RAG) pipeline in a single
  YAML file. The Python function in `functions:` is effectively a tool that
  performs SQL-based retrieval; the LLM uses it to answer questions grounded in
  database content. For practitioners, this means the full RAG stack
  (retrieval function + LLM call + answer) can live in a single executable file
  with no orchestration framework. The invocation `./blog.sh "Has Simon implemented
  GraphQL?"` is indistinguishable from any other shell command.

### Claim 10: Runtime arguments passed after the script name are forwarded to `llm`, enabling model selection and other flags at invocation time without changing the script file

- **Evidence**: TIL direct statement with example.
- **Confidence**: settled (first-party; standard argument-forwarding behavior)
- **Quote**: "Other arguments will be passed through to LLM, so if you want to
  use a different model: ./pelican.sh -m gpt-5.4-nano"
- **Our assessment**: This is a significant design property. A shebang script
  is NOT locked to one model — the user can override at invocation time with
  `-m model_name`. Combined with the template's `model:` field (which sets the
  default), this creates a two-level model selection system: the file specifies
  the preferred model; the caller overrides if needed. For CI pipelines, this
  means the same script can use a fast/cheap model in development and a more
  capable model in production, just by changing the invocation argument.

## Concrete Artifacts

### Level 1 — Plain Fragment Shebang (from TIL, verbatim)

```
#!/usr/bin/env -S llm -f
Generate an SVG of a pelican riding a bicycle
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang*

```
#!/usr/bin/env -S llm -x -f
Generate an SVG of a pelican riding a bicycle
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang — `-x` extracts
only the code block from the response*

### Level 2 — Tool Integration Shebang (from TIL, verbatim)

```
#!/usr/bin/env -S llm -T llm_time -f
Write a haiku that mentions the exact current time
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang — `llm_time` is
an `llm` plugin that provides the current time as a tool*

### Level 2b — YAML Template with System Prompt (from TIL, verbatim)

```
#!/usr/bin/env -S llm -t
prompt: Write a haiku
system: Output Spanish
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang*

### Level 2c — Parameterized Template (from TIL, verbatim)

```
#!/usr/bin/env -S llm -t
prompt: |
  Two line poem about $animal who lives in $place
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang — parameters
passed at invocation with `--param animal=cat --param place="the moon"`*

### Level 3 — YAML Template with Embedded Python Tools (from TIL, verbatim)

```
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

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang — invoked with
`./calc.sh 'what is 2344 * 5252 + 134' --td`*

### Calculated Output from Level 3 Example (from TIL)

```
2344 × 5252 + 134 = **12,310,822**
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang — output from
running `./calc.sh 'what is 2344 * 5252 + 134' --td`*

### Level 4 — YAML Template with Datasette SQL Tool (from TIL, partial — full function body exceeds quote scope)

```
#!/usr/bin/env -S llm -t
model: gpt-5.5
system: |
  You answer questions from Simon Willison's blog
functions: |
  import httpx
  url = "https://datasette.simonwillison.net/simonwillisonblog.json"
  [... SQL-based retrieval function using httpx ...]
```

*Source: Simon Willison, til.simonwillison.net/llms/llm-shebang#templates-with-tools
— invoked with `./blog.sh "Has Simon implemented GraphQL?"`. Full Python function
body at the TIL URL; quoted partially here to stay within fair use.*

### Three-Level Pattern Summary (Miner synthesis)

```
Level 1: Fragment   #!/usr/bin/env -S llm -f
                    Plain English below the shebang IS the prompt.
                    File content → LLM → stdout

Level 2: Tools      #!/usr/bin/env -S llm -T llm_time -f
                    Same as Level 1, but named tools add capabilities.
                    Plugin tools (llm_time, llm_browser...) invocable from prompt.

Level 3: Template   #!/usr/bin/env -S llm -t
                    YAML below the shebang: model + system + functions + prompt.
                    Python functions defined inline as callable tools.
                    Parameterizable via $variable syntax.
                    Model overridable at invocation: ./script.sh -m gpt-5.4-nano
```

## Cross-References

- **Corroborates**:
  - `discussion-hn-airun-executable-markdown.md` (Claims 1, 2): That note
    establishes the shebang-based executable AI script pattern using airun/
    claude-run. This source independently arrives at the same design philosophy:
    text files as executable LLM invocations via Unix shebangs. The convergence
    from two separate tools (airun and llm) on the same shebang mechanism is
    additional confirmation that the pattern is a natural fit for Unix-native AI
    automation — not a tool-specific quirk. The "AI-as-Unix-tool" design principle
    now has two independent practitioner implementations in the corpus.
  - `discussion-hn-airun-executable-markdown.md` (Claim 8): jedwhite explicitly
    scopes executable AI scripts to "summarization, evaluation, formatting" tasks.
    The llm shebang fragments pattern (Claim 2 here) is consistent with that scope:
    simple prompts for one-shot tasks. The Datasette SQL example (Claim 9 here)
    extends beyond that scope into retrieval-augmented tasks, suggesting the
    template-with-tools pattern covers a wider domain than the plain fragment
    pattern.
  - `blog-simonwillison-llm031.md` (Claim 1) and `blog-simonwillison-llm032a0.md`
    (Claims 1–4): Those notes document the `llm` CLI tool's architecture and
    evolution. This source shows the `llm` tool's real-world deployment in a
    workflow primitive. The fragment system (`-f`) and template system (`-t`)
    documented here are features of the `llm` CLI covered in those notes; this
    source shows them applied to the shebang use case, which neither prior note
    covers.

- **Extends**:
  - `discussion-hn-airun-executable-markdown.md` (Claim 1): That note documented
    the shebang executable-script pattern for Claude Code (airun/claude-run).
    This source extends the pattern to the `llm` CLI, which supports Claude,
    GPT-5.x, and other models. The two sources together establish that the
    shebang-as-AI-invocation pattern is model-agnostic and tool-agnostic — it
    is a Unix-level pattern that any CLI-wrapped LLM can support.
  - `discussion-hn-airun-executable-markdown.md` (Claim 11 — JohnKemeny's `.ag`
    format): The `.ag` format aimed for formal contract structure
    (Require/Invariant/Ensure/Rescue). Willison's YAML template approach aims for
    practical tool embedding (model + system + functions). Together they represent
    two distinct philosophies for structured AI shebang files: constraint-first
    (`.ag`) vs capability-first (llm templates). The guide should present both.
  - `blog-simonwillison-llm032a0.md` (Claim 10 — stream events API): The
    llm-shebang pattern uses the `llm` CLI at the invocation level; the 0.32a0
    refactor extends the Python API layer. Together, the two sources document
    complementary surfaces of the `llm` tool: CLI composition (this source) vs
    programmatic streaming (0.32a0).

- **Contradicts**: None identified. The llm shebang pattern does not conflict with
  any existing corpus note. The airun note claimed the shebang pattern as novel
  for its tool; this source extends novelty to the `llm` tool, which is a distinct
  implementation of the same pattern — not a contradiction.

- **Novel**:
  - **`#!/usr/bin/env -S llm -f` as a text-file-to-LLM pipeline primitive**: No
    prior corpus source documents using the `llm` CLI directly in a Unix shebang.
    The airun note covers the claude-run shebang; this is the first note documenting
    the `llm` shebang pattern.
  - **YAML-embedded Python tool definitions in shebang scripts**: No prior corpus
    source documents inline Python function tools defined in a YAML template inside
    an executable file. The template-with-functions pattern (`#!/usr/bin/env -S llm
    -t` + YAML `functions:` block) is entirely new to the corpus.
  - **Single-file RAG via YAML + httpx tool**: The Datasette SQL example (Claim 9)
    is the first corpus evidence of a retrieval-augmented generation pipeline
    fitting in a single executable file with no orchestration framework. Prior
    RAG coverage in the corpus focuses on multi-component architectures.
  - **`env -S` technical prerequisite for multi-flag shebangs**: No prior corpus
    source explains why `env -S` is required for shebangs with multiple flags.
    This is a practical implementation detail applicable to any multi-flag shebang
    pattern, including future AI CLI tools.
  - **Two-level model selection (YAML default + invocation override)**: The ability
    to specify a default model in the YAML template AND override at invocation
    (`./script.sh -m model_name`) is a new configuration pattern not documented
    in any prior corpus note. It creates a clean interface between script-author
    intent (default model) and caller context (override model).

## Guide Impact

- **Chapter 01 (Daily Workflows — Unix-native AI integration)**: Add the three
  levels of llm shebang pattern as a "minimal harness" primitive for one-shot
  LLM tasks. The pattern fits the same use case as the airun note
  (`discussion-hn-airun-executable-markdown.md`) but uses a different tool. The
  guide should present both patterns and distinguish: airun wraps Claude Code for
  full agentic behavior; llm shebang invokes `llm` for lighter-weight, multi-model
  prompt execution. Together they define the "no-framework AI script" spectrum.

- **Chapter 02 (Harness Engineering — Template patterns)**: Add the YAML-with-tools
  template (Level 3 above) as the minimal harness for LLM scripts that need
  tool access. The pattern demonstrates that model selection, system context, and
  tool functions can be co-located in a single executable file — a "self-contained
  agent" design pattern that contrasts with the more common pattern of keeping
  tool definitions in a separate harness.

- **Chapter 02 (Harness Engineering — env -S prerequisite)**: Add a callout that
  multi-argument shebangs require `env -S` (the split flag). Any guide section
  covering shebang-based AI invocation should include this as a prerequisites note
  to prevent the silent failure mode where `env` treats the entire argument string
  as a single command name.

- **Chapter 04 (Context Engineering — Single-file RAG)**: The Datasette SQL
  example (Claim 9) is a concrete instance of context engineering at the
  script level: the system prompt and the retrieval function together define the
  context available to the model. The guide could use this as a worked example
  of context engineering in a constrained environment (single file, no framework)
  to illustrate the core principle before introducing multi-component RAG
  architectures.

## Extraction Notes

- The source at `simonwillison.net/2026/May/11/llm-shebang/` is a short blog
  post that introduces the pattern and links to the full TIL at
  `til.simonwillison.net/llms/llm-shebang`. Both were read in full; the TIL
  sub-page was followed as permitted by MINER.md §1 (up to 5 linked pages).
  The TIL returned HTTP 404 on first attempt but was accessible on retry.
  Quotes and code examples are attributed to the source they appeared in.
- The Datasette SQL example's full Python function body (the `search_blog`
  function with its httpx call and SQL query) was not reproduced verbatim due
  to length; it is described and attributed at `til.simonwillison.net/llms/
  llm-shebang#templates-with-tools`. The partial reproduction of the YAML header
  is verbatim; the `[...]` notation marks where the function body was omitted.
- The HN thread at `news.ycombinator.com/item?id=48073246#48090590` returned
  HTTP 429 (rate limited) during extraction. The commenter (Kim_Bruning) and
  the quoted text ("you can put a shebang on an english text file now") are
  from the blog post itself, which attributes the comment.
- The YAML `functions:` block in the calc example uses a backslash before `*`
  in the WebFetch output (`a \* b`), which is markdown escaping; the actual
  source has `a * b`. The artifact above uses the unescaped form.
- No contradiction issues were filed: the shebang pattern in this source
  extends rather than contradicts the airun shebang pattern documented in
  `discussion-hn-airun-executable-markdown.md`. They are distinct tools with
  complementary strengths.
- Cross-reference verification performed:
  - `discussion-hn-airun-executable-markdown.md` Claim 1 confirmed (lines 51–70):
    markdown files as Claude Code shebang executables.
  - `discussion-hn-airun-executable-markdown.md` Claim 8 confirmed (lines 211–228):
    jedwhite's scoping to summarization/formatting tasks.
  - `discussion-hn-airun-executable-markdown.md` Claim 11 confirmed (lines 274–294):
    JohnKemeny's `.ag` format with Require/Invariant/Ensure/Rescue sections.
  - `blog-simonwillison-llm031.md` Claim 1 confirmed (lines 27–31): native GPT-5.5
    access via `llm -m gpt-5.5`.
  - `blog-simonwillison-llm032a0.md` Claim 10 confirmed (lines 89–94): typed
    streaming parts `stream_events()` / `astream_events()` API.
