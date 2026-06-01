---
source_url: https://simonwillison.net/2026/May/22/monty-investigation/
source_type: blog-post
title: "pydantic-monty investigation"
author: Simon Willison
date_published: 2026-05-22
date_extracted: 2026-06-01
last_checked: 2026-06-01
status: current
confidence_overall: emerging
issue: "#1015"
---

# pydantic-monty investigation

> Simon Willison's hands-on investigation of `pydantic-monty` 0.0.17 — a Rust-implemented,
> resource-limited Python-subset interpreter designed for sandboxed agent code execution —
> establishes its practical capabilities, firm boundaries, and resource-limit reliability
> through 122 empirical test cases, and provides concrete configuration guidance for
> practitioners embedding it in AI-native workflows.

## Source Context

- **Type**: blog-post (a Simon Willison "beat" post — a few sentences plus a link to
  the research repo at `github.com/simonw/research/tree/main/monty-investigation`. The
  substance lives in the research folder: `README.md`, `_summary.md`, `notes.md`,
  `experiments.py`, and `results.json`. All five artifacts were read in full for this
  note. The README carries an `AI-GENERATED-NOTE` header indicating the research report
  text was LLM-authored under Willison's direction, a pattern consistent with his
  published working style.)
- **Author credibility**: Simon Willison is a well-known Python practitioner (Django
  co-creator), prolific independent LLM tooling commentator, and creator of the `llm`
  CLI. He has no affiliation with Pydantic. His research methodology here — running 122
  empirically constructed test cases against the published package and reporting failures
  honestly — provides more signal than a vendor README. The AI-generated report was
  reviewed by Willison and published under his name; the experiments.py code and
  results.json are first-party artifacts.
- **Scope**: Covers `pydantic-monty` 0.0.17 (commit `2d43c36`, 2026-05-19), tested via
  `uv run --with pydantic-monty`. Characterizes: supported Python subset, unsupported
  features, sandbox isolation behavior, resource limit enforcement, virtual filesystem
  access model, external callback model, snapshot/resume capability, async support,
  and type checking. Does NOT cover: production deployment experience at scale,
  performance benchmarks across hardware, security audits, or comparison with other
  Python sandboxes beyond brief mention of not being "a drop-in Python sandbox."

## Extracted Claims

### Claim 1: pydantic-monty is a Rust-implemented Python-subset interpreter designed for controlled agent code execution, not a drop-in CPython sandbox

- **Evidence**: First-party research report with 122 empirical test cases against the
  published package. The README explicitly distinguishes monty from a general sandbox:
  "It is not a drop-in Python sandbox. It is deliberately much smaller than CPython."
- **Confidence**: settled (empirical investigation by a credible practitioner; the 0.0.17
  package behavior is directly tested)
- **Quote**: "It is not a drop-in Python sandbox. It is deliberately much smaller than
  CPython. The good news is that the boundary is fairly crisp: unsupported imports,
  missing builtins, unmounted filesystem access, path traversal, and absent host
  callbacks generally fail as typed Monty errors rather than escaping into host
  execution."
  *(Source: README.md, simonw/research monty-investigation, "High-Level Findings")*
- **Our assessment**: The distinction matters for guide readers: pydantic-monty is an
  expression interpreter purpose-built for agent-generated data-processing code, not a
  security-hardened VM for arbitrary Python. Its smaller surface area is a feature in
  the agent context — less to reason about, more predictable failure modes.

### Claim 2: pydantic-monty's resource limits (max_duration_secs, max_memory, max_allocations, max_recursion_depth) were reliably enforced in empirical testing, including inside Rust-side builtin loops

- **Evidence**: Direct empirical measurement across 7 resource-limit test cases. Timeout
  tripped in ~50ms for both a Python `while True` loop and `sum(range(10**18))` (a
  Rust-side builtin). Memory, allocation, recursion, and bigint-pow limits all triggered
  immediately with typed exceptions.
- **Confidence**: settled (directly measured; all limits worked as documented)
- **Quote**: "The important detail is that the timeout also worked inside a Rust-side
  builtin loop (`sum(range(10**18))`), not just bytecode-level Python loops."
  *(Source: README.md, simonw/research monty-investigation, "Resource Limits")*
- **Our assessment**: This is the most practically significant finding for agent safety.
  A timeout that only works at the Python bytecode level would be defeatable by code
  that calls into builtins (e.g., sorting or summing large iterables). Willison's test
  confirms the timeout is enforced at the Rust interpreter level, not just the Python
  bytecode level, which closes a meaningful attack surface.

### Claim 3: pydantic-monty's security model depends entirely on the scope of explicitly exported host callbacks — any callback you expose gives Monty code access to the capability that callback has

- **Evidence**: Empirical demonstration: a host callback named `host_read_len` that read
  `/etc/hosts` from the host and returned its length was accessible to Monty code.
  The README states this explicitly as the security model.
- **Confidence**: settled (demonstrated empirically; explicitly documented as the intended
  design)
- **Quote**: "The key security model is: Monty code cannot directly touch most host
  resources, but any external function or OS callback you expose is fully trusted.
  If you expose a callback that reads host files, Monty code can read host files
  through that callback."
  *(Source: README.md, simonw/research monty-investigation, "High-Level Findings")*
- **Our assessment**: This is the critical practitioner guidance. Pydantic-monty's
  sandbox is a capability boundary, not an access-control system. Practitioners must
  treat every exposed callback as a capability grant. The guide should surface this
  as a design principle: narrow, typed callbacks are the safety mechanism.

### Claim 4: pydantic-monty handles a wider Python subset than its README headline suggests, including most control flow, common builtins, and key stdlib modules

- **Evidence**: 76 of 122 empirical test cases succeeded. Passing cases include
  arithmetic, bools, comparisons, ternary, walrus, f-strings, slicing, data structures
  (list/dict/set/tuple/bytes literals, big ints), functions with default/keyword/varargs,
  lambdas, comprehensions, generator expressions, and stdlib (`sys`, `math`, `re`,
  `json`, basic `datetime` constructors).
- **Confidence**: settled for 0.0.17 (empirically measured)
- **Quote**: "The package handled a larger subset of everyday Python than the README
  headline suggests"
  *(Source: README.md, simonw/research monty-investigation, "Python That Worked")*
- **Our assessment**: The headline capabilities (data transformation, loops, branching)
  are sufficient for the agent data-processing use case. The gap is at the
  introspection/library boundary, not at the computation boundary.

### Claim 5: pydantic-monty deliberately omits class definitions, context managers, generators, dynamic introspection (eval/exec/globals/dir/locals), and most third-party or advanced stdlib imports

- **Evidence**: Empirical failures: class definitions, `match`, `with`, `yield`,
  matrix multiplication, `eval`, `exec`, `globals`, `dir`, `locals`, `callable`,
  `open`, `object`. Imports failed for `statistics`, `random`, `socket`, `subprocess`,
  third-party `pydantic`. Also: `getattr('abc', 'upper')()` raised `AttributeError`
  despite string methods like `.strip()` working directly.
- **Confidence**: settled for 0.0.17 (empirically tested)
- **Quote**: "Syntax/features: class definitions, `match`, `with`, `yield`, complex
  constants, matrix multiplication."
  *(Source: README.md, simonw/research monty-investigation, "Python That Failed Or Was Limited")*
- **Our assessment**: The absence of classes is the single largest constraint for
  agent-generated code. LLM-generated Python frequently uses classes for data
  representation. Agents targeting pydantic-monty need prompting or output validation
  to stay within the supported subset.

### Claim 6: pydantic-monty's virtual filesystem (OSAccess and MountDir) provides controlled file access with three modes — read-only, overlay (writes visible to Monty but not host), and read-write (changes host files)

- **Evidence**: Empirical verification of all three modes. Read-only blocked writes.
  Overlay writes did not change host files. Read-write mode changed the host directory.
  Path traversal through a mount was blocked with `PermissionError`. Access to unmounted
  paths was blocked.
- **Confidence**: settled for 0.0.17 (directly tested with temp directories)
- **Quote**: "`MountDir('/mnt', ..., mode='read-only')` allowed reads and blocked writes.
  `MountDir(..., mode='overlay')` allowed writes visible to Monty without changing host
  files. `MountDir(..., mode='read-write')` changed the host directory."
  *(Source: README.md, simonw/research monty-investigation, "Sandbox Findings")*
- **Our assessment**: The overlay mode is the most useful for agent workflows: give the
  agent a scratch filesystem that it can read and write freely without touching host
  state. The read-write mode should be used only when host persistence is intentional.

### Claim 7: Snapshot/resume support allows Monty execution to pause at an external call, serialize state to ~366 bytes, and resume with an injected return value — enabling async agent workflows

- **Evidence**: Empirical test: `Monty.start()` paused at `fetch(url)` as a
  `FunctionSnapshot`, serialized to 366 bytes, was restored with `load_snapshot()`,
  and completed with output `6` after injecting `{'return_value': 'abcdef'}`.
  Compiled `Monty` instances also serialized/loaded via `dump()`/`Monty.load()`.
- **Confidence**: settled for 0.0.17 (directly verified)
- **Quote**: "The snapshot serialized to 366 bytes."
  *(Source: README.md, simonw/research monty-investigation, "External Calls And Snapshots")*
- **Our assessment**: Snapshot/resume makes pydantic-monty suitable for agent-in-the-loop
  patterns where the agent calls a tool, waits for an external result, and continues.
  The compact serialization (366 bytes for a function call state) means snapshots can
  be stored cheaply in agent memory or passed across message queues.

### Claim 8: pydantic-monty's type checker catches type errors at construction time — bad operators, invalid return types, undefined names, and stub mismatches — before the code runs

- **Evidence**: Four type-checking cases verified empirically: `"hello" + 1` (bad operator),
  `def f() -> int: return 'x'` (bad return type), `missing_name + 1` (undefined name),
  and calling `external('bad')` against a stub `def external(x: int) -> str: ...`
  (stub mismatch).
- **Confidence**: settled for 0.0.17 (directly tested)
- **Quote**: "Monty's type checker caught: Unsupported operator: `\"hello\" + 1`. Invalid
  return type: `def f() -> int: return 'x'`. Undefined names. Stub mismatch: calling a
  stubbed `external(x: int)` with a string."
  *(Source: README.md, simonw/research monty-investigation, "Type Checking")*
- **Our assessment**: Pre-execution type checking is a significant safety mechanism for
  agent-generated code: rather than running code that fails mid-execution with a runtime
  error, practitioners can validate it up front. The stub mechanism lets practitioners
  declare the type contracts for exposed host callbacks and catch agent-generated
  mismatches before execution.

### Claim 9: pydantic-monty's REPL (MontyRepl) persists state across snippet evaluations and survives runtime errors without resetting state

- **Evidence**: Empirical test across 6 REPL steps: defined `x = 10`, used it, defined
  a function, called it, triggered `1 / 0`, and confirmed `x` was still accessible
  after the error.
- **Confidence**: settled for 0.0.17 (directly tested)
- **Quote**: "REPL state persisted across snippets and survived a runtime error in the
  tested scenario."
  *(Source: README.md, simonw/research monty-investigation, "Python That Worked")*
- **Our assessment**: The REPL mode supports multi-turn agent interaction where each
  agent turn appends code to a running session. State persistence across runtime errors
  is important: an agent that occasionally produces bad code shouldn't reset the entire
  execution context.

### Claim 10: Version-sensitive behavior in pydantic-monty 0.0.17 silently omits f-string formatting flags (grouping, alternate-form), diverging from source-level tests that expect strict rejection

- **Evidence**: Empirical finding: `f'{1000:,d}'`, `f'{1000:_d}'`, and `f'{255:#x}'`
  all succeeded but silently omitted the formatting behavior, returning `'1000'`,
  `'1000'`, `'ff'`. The cloned source at commit `2d43c36` has Rust parser tests
  expecting these to be rejected with syntax errors.
- **Confidence**: emerging (tested against 0.0.17; newer versions may be stricter)
- **Quote**: "The cloned source already has parser tests expecting these flags to be
  rejected, so newer source may be stricter than the published wheel."
  *(Source: README.md, simonw/research monty-investigation, "Python That Failed Or Was Limited")*
- **Our assessment**: This is the most actionable version-sensitivity finding. Agents
  relying on f-string formatting for output formatting (e.g., currency display, hex
  output) may silently produce incorrect results in 0.0.17. Practitioners upgrading
  pydantic-monty should run the f-string format-spec cases as regression tests.

### Claim 11: Willison recommends always setting all four resource limits, preferring overlay mode for scratch file access, and keeping external callbacks narrow and typed

- **Evidence**: Practical guidance section in README.md, distilled from the empirical
  investigation. Presented as "Recommended defaults for agent code."
- **Confidence**: emerging (practitioner guidance, not a universal benchmark)
- **Quote**: "Always set `max_duration_secs`, `max_memory`, `max_allocations`, and
  `max_recursion_depth`. Prefer `OSAccess` memory files or `MountDir(..., mode='overlay')`
  for scratch file access. Keep external functions narrow and typed."
  *(Source: README.md, simonw/research monty-investigation, "Practical Usage Guidance")*
- **Our assessment**: Solid defaults. The reasoning behind "narrow and typed" is made
  explicit by the security model in Claim 3: wide callbacks are capability grants.
  Narrow, typed callbacks with stubs also enable pre-execution type checking (Claim 8).

## Concrete Artifacts

### Resource limit test cases (from experiments.py)

```python
# Source: github.com/simonw/research/blob/main/monty-investigation/experiments.py
# "resource_limit_cases" function

run_case(
    "timeout_infinite_loop",
    "while True:\n    pass",
    limits={"max_duration_secs": 0.05},
)
run_case(
    "timeout_builtin_sum_huge_range",
    "sum(range(10**18))",
    limits={"max_duration_secs": 0.05},
)
run_case(
    "memory_limit_list_growth",
    "xs = []\nfor i in range(1000):\n    xs.append('x' * 100)\nlen(xs)",
    limits={"max_memory": 100},
)
run_case(
    "allocation_limit_many_lists",
    "xs = []\nfor i in range(1000):\n    xs.append([i])\nlen(xs)",
    limits={"max_allocations": 10},
)
run_case(
    "recursion_limit",
    "def recurse(n):\n    if n <= 0:\n        return 0\n    return 1 + recurse(n - 1)\nrecurse(20)",
    limits={"max_recursion_depth": 5},
)
run_case(
    "bigint_pow_memory_limit",
    "2 ** 10000000",
    limits={"max_memory": 1_000_000},
)
run_case(
    "normal_work_with_limits",
    "sum(range(1000))",
    limits={"max_duration_secs": 1.0, "max_memory": 1_000_000, "max_allocations": 100_000},
)
```

### Resource limit results table (from README.md)

```
# Source: README.md, simonw/research monty-investigation, "Resource Limits"

| Case                        | Limit                     | Result                     |
| ---                         | ---                       | ---                        |
| `while True: pass`          | `max_duration_secs=0.05`  | `TimeoutError` in ~50ms    |
| `sum(range(10**18))`        | `max_duration_secs=0.05`  | `TimeoutError` in ~50ms    |
| Growing list of strings     | `max_memory=100`          | `MemoryError` immediately  |
| Many list allocations       | `max_allocations=10`      | `MemoryError` immediately  |
| Recursive function          | `max_recursion_depth=5`   | `RecursionError` immediately |
| `2 ** 10000000`             | `max_memory=1_000_000`    | `MemoryError` immediately  |
| `sum(range(1000))`          | combined normal limits    | succeeded                  |
```

### Filesystem sandbox test cases (from experiments.py)

```python
# Source: github.com/simonw/research/blob/main/monty-investigation/experiments.py
# "filesystem_sandbox_cases" function

# OSAccess: in-memory files + controlled env vars
fs = pydantic_monty.OSAccess(
    [pydantic_monty.MemoryFile("/data/input.txt", content="alpha\nbeta\n")],
    environ={"SECRET": "mounted-env"},
)
# Reads and writes to memory files succeed; socket not importable even with OSAccess

# MountDir modes
ro = pydantic_monty.MountDir("/mnt", root, mode="read-only")
# → reads succeed, writes blocked, path traversal blocked, unmounted paths blocked

overlay = pydantic_monty.MountDir("/mnt", root, mode="overlay")
# → writes visible inside Monty, host directory unchanged

rw = pydantic_monty.MountDir("/mnt", root, mode="read-write")
# → writes persist to host directory
```

### Snapshot/resume example (from experiments.py)

```python
# Source: github.com/simonw/research/blob/main/monty-investigation/experiments.py
# "external_and_snapshot_cases" function

monty = pydantic_monty.Monty("data = fetch(url)\nlen(data)", inputs=["url"])
snap = monty.start(inputs={"url": "https://example.test/data"})
# snap is FunctionSnapshot; snap.function_name == "fetch"
dumped = snap.dump()
# len(dumped) == 366 bytes
restored = pydantic_monty.load_snapshot(dumped)
done = restored.resume({"return_value": "abcdef"})
# done.output == 6
```

### Type checking with stubs (from experiments.py)

```python
# Source: github.com/simonw/research/blob/main/monty-investigation/experiments.py
# "type_check_cases" function

# Stub declares external callback type contract
type_check_case(
    "type_check_with_stub",
    "result = external(1)",
    stubs="def external(x: int) -> str: ..."
)
# → ok

type_check_case(
    "type_check_stub_mismatch",
    "result = external('bad')",
    stubs="def external(x: int) -> str: ..."
)
# → error: type mismatch caught before execution
```

### Practical configuration defaults (from README.md)

```
# Source: README.md, simonw/research monty-investigation, "Practical Usage Guidance"
# "Recommended defaults for agent code"

- Always set max_duration_secs, max_memory, max_allocations, and max_recursion_depth.
- Prefer OSAccess memory files or MountDir(..., mode='overlay') for scratch file access.
- Keep external functions narrow and typed.
- Use type-check stubs for exposed callbacks.
- Treat results.json style probes as regression tests when upgrading pydantic-monty.
```

## Cross-References

- **Corroborates**: No existing source note directly covers pydantic-monty. The
  sandboxed-execution-for-agents pattern is adjacent to `docs-ghaw-sandbox-reference.md`
  (Claim 4's three-tier filesystem model), but AWF operates at the agent-job level
  (network egress, Docker socket hiding) while pydantic-monty operates at the code
  expression level inside a tool call. These are complementary layers, not competing
  ones.
- **Contradicts**: None identified. No existing source note makes claims about
  pydantic-monty or Python-subset interpreters for agent sandboxing.
- **Extends**: `docs-ghaw-sandbox-reference.md` establishes the principle that sandbox
  configuration must be explicit (Claim 1's "zero capability by default"). Pydantic-monty
  applies the same principle at a finer granularity: every exposed callback is an
  explicit capability grant (Claim 3 of this note).
- **Novel**: The specific Python subset characterization (76/122 cases passing in 0.0.17),
  the empirical resource limit measurements (all four limit types verified at Rust level),
  the f-string silent-omission version-sensitivity finding, the snapshot byte size (366
  bytes), and the type-checking-with-stubs pattern are all new to the corpus.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: The corpus lacks concrete, empirically tested
  guidance on sandboxing agent-generated Python execution. This source fills that gap
  directly. Specific additions warranted:
  - Add pydantic-monty as a named option for sandboxed agent code execution, citing
    Claims 1, 2, and 3 for its capabilities and security model.
  - Add the resource-limit enforcement finding (Claim 2, including timeout-in-builtins)
    as a differentiator from application-level timeouts that can be bypassed by calling
    into C extensions or builtins.
  - Add the capability-as-callback security model (Claim 3) as a design principle for
    any tool-call sandbox: the security boundary is the set of exposed callbacks, not
    the interpreter itself.
- **Chapter 02 (Harness Engineering)**: The tool ecosystem section should note
  pydantic-monty as a component for harnesses that execute agent-generated data
  transformation code. The REPL state-persistence finding (Claim 9) and snapshot/resume
  (Claim 7) are relevant for harness designers who need multi-turn or async execution
  semantics.
- **Chapter 07 (Safety and Control)** (if it exists): The type-check-before-run
  pattern (Claim 8) is a concrete pre-execution validation mechanism that can be
  added to a safety checklist for agent-generated code.

## Extraction Notes

The blog post itself is a short "beat" entry (a few sentences plus a research repo link).
All substantive content was extracted from the linked research folder in
`github.com/simonw/research/tree/main/monty-investigation`, specifically:
- `README.md` (8,612 bytes) — the main research report
- `_summary.md` (1,763 bytes) — executive summary
- `notes.md` (5,107 bytes) — investigator's working notes
- `experiments.py` (20,881 bytes) — the test harness (read selectively for
  artifacts; full file reviewed for coverage)
- `results.json` (44,762 bytes) — raw test output (not read directly; results
  are summarized in README.md)

The README carries an `AI-GENERATED-NOTE` header indicating the report was LLM-authored
under Willison's direction. This is consistent with his published research workflow. The
claims are backed by the empirical `experiments.py` test harness and `results.json`
results, which are first-party artifacts regardless of who drafted the prose summary.

The previous Monty article (simonwillison.net/2026/Feb/6/pydantic-monty/) was read for
context. It covered compiling Monty to WebAssembly for browser use — a different focus
than this investigation. Cross-referencing between the two articles did not surface any
internal contradictions.
