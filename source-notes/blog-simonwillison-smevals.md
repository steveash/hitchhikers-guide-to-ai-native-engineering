---
source_url: https://simonwillison.net/2026/Jul/31/smevals/
source_type: blog-post
title: "smevals - a small eval suite for evaluating models, prompts, and harnesses"
author: Simon Willison
date_published: 2026-07-31
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: emerging
issue: "#2517"
---

# smevals - a small eval suite for evaluating models, prompts, and harnesses

> Willison's link-blog announcement of `smevals`, a YAML-driven Python CLI
> eval framework he co-built with Jesse Vincent's Prime Radiant lab, quoting
> a settled vocabulary (eval / task / config / run / runner / grader / grade
> / check / checker) and demonstrating the run-then-grade separation of
> concerns via a worked haiku-writing example.

## Source Context

- **Type**: blog-post (Willison's link-blog format — a short framing post
  that links out to the primary announcement). Per MINER.md §1, this note
  follows both substantive links in Willison's post: the full announcement
  at `primeradiant.com/blog/2026/smevals.html` and the tool's own README at
  `github.com/prime-radiant-inc/smevals/blob/main/README.md` (fetched as raw
  HTML/Markdown, not via a summarizing pass, so quotes could be verified
  character-for-character). Nearly all of the technical vocabulary and
  concrete artifacts below come from those two linked pages; Willison's own
  post contributes the framing, the "third iteration" personal history, and
  the pointer to a live worked example.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo (creator of Django, Datasette, `sqlite-utils`, and the
  `llm` CLI — the latter is itself used as the example Runner in `smevals`'
  own README). Notably, the linked Prime Radiant announcement page is *also*
  byline-attributed to "Simon Willison, Researcher" — he is not merely
  amplifying someone else's tool here; he co-built it and wrote both the
  announcement and the link-blog post about it. This is first-party,
  first-hand documentation of a tool the author built and is actively using,
  not commentary on someone else's work.
- **Scope**: Covers the design vocabulary, on-disk file layout, CLI command
  surface, Runner/Checker process contracts (environment variables, exit
  codes, stdout schema), and a single worked example (a haiku-writing eval
  graded first by a naive line-count check, then by an LLM-judge check) of
  `smevals`, a tool released the same day as this post. Does NOT cover
  independent third-party validation of the tool, comparative benchmarking
  against other eval frameworks (pytest-based, DeepEval, ragas, etc. — see
  `blog-thoughtworks-anand-agent-evaluation-framework.md`), or results from
  using `smevals` at scale across multiple projects (Willison states this is
  future work).

## Extracted Claims

### Claim 1: smevals settles on a seven-term vocabulary — eval, task, config, run, runner, grader, grade, and check/checker — to describe every stage of building and running an eval suite
- **Evidence**: Identical bulleted definition list appears verbatim on both
  Willison's own blog and the linked Prime Radiant announcement page (which
  Willison's post explicitly calls "the announcement" he is quoting from).
  Willison states this vocabulary took the most design effort of the whole
  project.
- **Confidence**: emerging (a practitioner-coined vocabulary released the
  same day as this post; internally consistent and cross-verified against
  the tool's own README, but not yet a term-of-art with independent adoption)
- **Quote**: "An eval is a collection of challenges designed to answer a
  question about a model, for example, how good is that model at generating
  SVGs? Each eval is a collection of tasks. A task is a specific challenge,
  for example \"Generate an SVG of a pelican riding a bicycle\". When you run
  the eval you do so against one or more configs. Each config specifies a
  model to be evaluated, but may also include other parameters to test, such
  as different system prompts, model parameters, or agent harnesses. A run
  records what happened when a specific config was used to execute a
  specific task. A runner is the script that executes a run. Once you have
  collected one or more runs, you need to evaluate the results to see how
  well the model (or config) did. This is done by a grader, which produces a
  grade. Each grader runs a sequence of checks."
- **Our assessment**: This is the most directly reusable artifact in the
  post: a compact, orthogonal vocabulary for eval-suite construction that
  cleanly separates "what to test" (task), "what's being tested" (config),
  "what happened" (run), and "how good was it" (grade/check). The
  eval-vs-task and grader-vs-check distinctions in particular map onto a
  design decision many ad hoc eval scripts blur together (mixing "did it
  run" with "was it good"). Notably the example task named in the
  definition itself — "Generate an SVG of a pelican riding a bicycle" — is
  Willison's own long-running informal benchmark (see
  `blog-simonwillison-kimi-k3-pelican-benchmark.md` and
  `blog-simonwillison-pelicanmaxxing.md`), used here as the canonical
  illustration of what a "task" is.

### Claim 2: Evals can optionally be grouped into Suites purely as an on-disk organizing mechanism, distinct from the Eval/Task/Config/Run/Grade vocabulary
- **Evidence**: Stated in the README's "Vocabulary used by this project"
  section, and operationalized later in the CLI (the `smevals serve` and
  `smevals build` commands both accept `EVAL_OR_SUITE...` and treat any
  directory that is not itself an Eval as a Suite to be searched
  recursively).
- **Confidence**: settled (directly stated in the tool's own reference
  documentation, and reflected consistently in the command-line interface
  section of the same document)
- **Quote**: "Evals can optionally be grouped into Suites of related Evals,
  primarily as a mechanism for organizing them on disk."
- **Our assessment**: A minor but practically useful design choice — Suites
  carry no semantic weight of their own (no suite-level scoring or
  aggregation described beyond directory grouping), which keeps the core
  vocabulary from Claim 1 uncontaminated by an organizational concept. The
  `smevals build` command's stated behavior of adding/refreshing Evals into
  a shared output directory without disturbing already-built Evals "so one
  site can aggregate Evals from many repositories" is the practical payoff
  of treating Suites as directory structure rather than a first-class
  scoring unit.

### Claim 3: smevals deliberately separates running an eval from grading it, so that a grader can be edited and re-applied to already-collected runs without re-executing the (potentially expensive) model calls
- **Evidence**: Stated explicitly in the README as a design rationale, and
  demonstrated in the worked example: the haiku eval is graded once with a
  naive three-line checker, and later re-graded with an LLM-judge checker
  via `--regrade`, reusing the original runs without regenerating them.
- **Confidence**: settled (directly stated design rationale, backed by a
  concrete before/after worked example in the same source)
- **Quote**: "`smevals` deliberately separates running the evals from
  grading them, which means that after you have updated a grader you can run
  it against the existing logged results like this: `uvx smevals grade . --regrade`"
- **Our assessment**: This is the structural decision that makes the rest of
  the tool's design (multiple coexisting graders, `--regrade`, grading being
  a pure function of on-disk Run data) coherent. It also has a direct cost
  argument: model calls are the expensive, slow, non-reproducible part of an
  eval; grading logic is cheap to iterate on and should be freely
  re-runnable against fixed evidence. This is the same underlying principle
  as `blog-langchain-better-harness-evals.md` Claim 12 (evals become
  regression tests) but applied one layer down — here it's the run/grade
  split itself, not just the eval-as-a-whole, that is made independently
  re-usable.

### Claim 4: A Run whose Runner process exits non-zero is marked as a "failed Run" — a harness-level error distinct from a bad model response — and failed Runs are permanently excluded from grading, reports, and `-n` sample-size targets
- **Evidence**: Stated as a Runner-contract rule in the README, and repeated
  independently in the `smevals run` and `smevals grade` command
  descriptions later in the same document.
- **Confidence**: settled (directly stated, load-bearing contract rule,
  restated consistently across three separate sections of the tool's own
  reference documentation)
- **Quote**: "A Run whose Runner exits non-zero is a failed Run: a
  harness-level error such as a network failure, not evidence about the
  model. Failed Runs stay on disk for debugging but are never graded, are
  excluded from reports, and do not count towards `-n` targets." ...
  "Exit non-zero only for infrastructure problems; exit 0 whenever the
  output is a real model response you want judged, however bad."
- **Our assessment**: This is a precise, easy-to-miss design rule with real
  evaluation-integrity consequences: it forces Runner authors to distinguish
  "the harness broke" (crash, timeout, network error — not evidence about
  the model) from "the model responded badly" (a real, gradeable data point
  that must exit 0 so it gets judged rather than silently discarded). Get
  this backwards — e.g., a Runner that exits non-zero because a model
  refused a task or produced malformed output — and the eval suite would
  quietly under-count exactly the failure modes it exists to measure. This
  is directly relevant to the guide's evaluation-methodology material on
  distinguishing infrastructure failures from capability signal.

### Claim 5: A Checker can emit a JSON object with up to five recognized keys — score, metrics, tags, notes, and details — each aggregated differently by smevals' reporting, and tags are explicitly "open vocabulary and presence-only"
- **Evidence**: Stated in the "The Checker contract" section of the README,
  which defines each key's type and aggregation behavior in turn.
- **Confidence**: settled (directly specified output schema from the tool's
  own reference documentation)
- **Quote**: "`tags` - a list of short labels, e.g. `[\"wearing_a_hat\",
  \"correct_bicycle_frame_shape\"]`. Tags are open vocabulary and
  presence-only: an absent tag means \"not observed\", not \"false\". They
  are normalized to lowercase snake_case, and the Grade records the union of
  all its Checks' tags. Reports aggregate them as counts and shares, and the
  web UI uses them for filtering."
- **Our assessment**: The presence-only semantics for tags is a subtle but
  important design choice: it lets a Checker report positive observations
  ("this SVG has a hat on the pelican") without being forced to enumerate
  and check every possible negative observation, and it means an absent tag
  is not itself asserted evidence of absence. Combined with `metrics`
  (numeric/boolean, aggregated as mean±stderr or rate) and `score` (the
  single number used for pass/fail), this three-tier output schema lets a
  single Checker report a scalar verdict, structured measurements, *and*
  open-ended qualitative observations in one process invocation — useful
  guidance for anyone designing a custom LLM-as-judge checker script that
  needs to report more than a single pass/fail number.

### Claim 6: A Grade's score is the last score value emitted by any Check in sequence — not an average or a first-Check value — and is forced to null (rather than falling back to a stale earlier value) if a later Check fails without emitting its own score
- **Evidence**: Stated as an explicit scoring rule under "Outcomes and
  scores" in the README, directly following the description of how Checks
  in a Grader execute in order and share a workspace.
- **Confidence**: settled (directly specified scoring algorithm)
- **Quote**: "The Grade's score is the last `score` emitted by any Check -
  typically the final, most expensive Check. However, if any Check fails
  without emitting a score of its own, the Grade's score is null: a stale
  score from an earlier Check never stands in for one that did not run."
- **Our assessment**: This rule is designed to prevent a specific silent
  failure mode: a cheap early Check (e.g., "does the output contain valid
  XML") emitting a passing score, followed by an expensive later Check (e.g.,
  an LLM-judge rubric) crashing or erroring out — without this rule, a naive
  "use the last non-null score" implementation could report the cheap
  Check's score as if it were the full grading pipeline's verdict. Forcing
  the score to null in that case makes a partially-completed grading run
  visibly incomplete rather than silently misleading. This is the same
  category of integrity concern as Claim 4 (failed Runs must not be
  silently counted as evidence), applied to the grading stage instead of
  the running stage.

### Claim 7: `smevals run -n N` treats N as a target sample count per task/model pair rather than an absolute number of new runs to execute, making repeated invocations idempotent once the target is met and safely resumable if interrupted
- **Evidence**: Stated as the `-n` flag's semantics in the `smevals run`
  command reference, including the interaction with balanced-pass execution
  order and with failed-Run exclusion (Claim 4).
- **Confidence**: settled (directly specified CLI flag behavior)
- **Quote**: "`-n N` is a target sample size: each task/model pair is topped
  up to at least N successful Runs, executing only the shortfall, so
  re-running the same command is a no-op once the target is met and an
  interrupted session can be resumed by repeating it. Runs execute in full
  passes over the pairs - interrupting partway leaves balanced samples
  rather than many Runs of the first Task and none of the last. Failed Runs
  (a non-zero Runner exit) do not count toward the target: re-running the
  command executes replacements for them, attempting each pair's shortfall
  once per invocation, so a persistently failing Runner never retries in a
  loop."
- **Our assessment**: This is a genuinely well-thought-out piece of
  operational design for anyone running evals against flaky or
  rate-limited model APIs: idempotent re-invocation, balanced-pass execution
  (so an interrupted run doesn't leave one task heavily sampled and another
  untouched), and a one-shortfall-attempt-per-invocation cap that prevents a
  broken Runner from looping forever trying to hit its target. This level of
  attention to interruption/resume semantics is not something ad hoc
  eval scripts typically get right on a first pass.

### Claim 8: Multiple Graders can coexist against the same set of Runs, each writing into its own `grades/<name>/` subdirectory, enabling e.g. a cheap deterministic grader and an expensive LLM-judge grader to be run side by side without interfering with each other
- **Evidence**: Stated in the "Runs and Grades on disk" section of the
  README, describing the on-disk layout under `grades/<grader>/`.
- **Confidence**: settled (directly specified on-disk data model)
- **Quote**: "Multiple Graders coexist: each grades into its own
  `grades/<name>/` directory, so an eval can have e.g. a cheap deterministic
  `default` grader and an LLM-judge `judge` grader side by side."
- **Our assessment**: This directly enables a cost-tiered grading strategy —
  run a fast, free structural check (e.g., "is this valid XML") on every
  Run as a cheap first pass, and reserve an expensive LLM-judge grader for
  Runs that pass the structural check, without those two grading concerns
  needing to be fused into one Grader/Checker pipeline. It also means a
  grading rubric can be revised and re-applied (per Claim 3) without
  disturbing a separately-maintained, already-computed alternate grading
  pass.

### Claim 9: The `smevals` README is deliberately written to be readable by both humans and coding agents, and is bundled with the tool itself via a `smevals docs` command so an agent can retrieve the full spec without needing external web access
- **Evidence**: Stated directly in the Prime Radiant announcement, and
  operationalized in Willison's own post as the literal first step of the
  "10 second version" of how to use the tool.
- **Confidence**: emerging (a stated design intent, corroborated by the
  README's own structure — which is written as a dense contract
  specification with explicit environment-variable names and JSON schemas
  rather than prose — but not independently tested here against an actual
  agent's ability to build a correct eval from the README alone)
- **Quote**: "The smevals README is designed for both humans and agents. A
  coding agent that reads that document should have everything it needs to
  know in order to construct an initial eval." ... "That README is also
  bundled with the tool, and is available using the `smevals docs`
  command."
- **Our assessment**: This is a notable instance of "agent-native" tool
  design: rather than writing separate agent-facing instructions (a skill,
  an MCP tool description, a CLAUDE.md snippet) alongside human-facing docs,
  smevals bundles one README that is deliberately dense and contract-precise
  enough (exact env var names, exact JSON key names, exact exit-code
  semantics) to serve as the only specification an agent needs, retrievable
  in-session via a CLI subcommand rather than requiring the agent to fetch a
  web page. Willison's own two-step workflow — "tell your coding agent to
  run `uvx smevals docs`... then tell it to build you an eval suite" —
  demonstrates this is the intended and expected primary usage pattern for
  the tool, not merely a documentation nicety.

### Claim 10: In Willison's own worked example, a coding agent's first-pass grader (checking only "exactly three non-empty lines") was explicitly under-specified, and had to be manually redirected toward the actual intended criteria (5-7-5 syllable structure and subject adherence) via a follow-up instruction
- **Evidence**: Willison's own narration of building a haiku eval with a
  coding agent: the first grader Codex built only checked line count; a
  follow-up prompt ("Improve the grader to check for the right consonants
  and vowels using gpt-5.5") produced a second checker that counts syllables
  via an LLM judge and checks for the 5-7-5 pattern and subject presence.
- **Confidence**: anecdotal (a single first-hand narrated session, not a
  controlled or repeated trial)
- **Quote**: "The first version of the grader that Codex built for me only
  checked that the response contained exactly three non-empty lines." ...
  "I told Codex: `Improve the grader to check for the right consonants and
  vowels using gpt-5.5`"
- **Our assessment**: Worth flagging precisely because the instruction given
  ("check for the right consonants and vowels") does not literally describe
  what the resulting checker does (it counts *syllables* via an LLM judge
  and checks the 5-7-5 pattern, not consonant/vowel counts) — the agent
  correctly inferred haiku structure was the actual intent behind an
  imprecise instruction. This is a small but concrete illustration of a
  broader pattern relevant to the guide's harness-engineering material:
  an agent's first-pass output against an under-specified grading
  instruction was structurally adequate (three lines) but semantically
  shallow, and required a human to notice the gap and redirect toward the
  real acceptance criteria — the same "spec issues surface only once you
  see the naive implementation" dynamic documented elsewhere in this corpus
  for harness and prompt design generally.

### Claim 11: Willison frames smevals as his third attempt, across "several years," at finding an eval-framework design he is satisfied with
- **Evidence**: Willison's own closing statement in his link-blog post,
  describing his multi-year history of iterating on eval tooling design.
- **Confidence**: anecdotal (self-reported personal history, not
  independently verifiable, though consistent with Willison's long public
  track record of eval-related posts tagged `evals` on his blog, cited in
  the Prospector's triage comment as 45 posts)
- **Quote**: "I've been trying to figure out an approach I like for evals
  for several years now. `smevals` is my third iteration on the idea and it
  feels right to me."
- **Our assessment**: This framing matters for how the guide should weight
  this source: it is not a first attempt or a quick prototype, but the
  product of multiple prior discarded designs by a practitioner with an
  unusually large public track record of hands-on model evaluation work.
  That does not make the vocabulary or design decisions in Claims 1-9
  correct or complete, but it is a meaningfully stronger prior than an
  unproven first-iteration framework — and Willison is explicit that he
  considers this iteration provisional too ("looking forward to expanding
  this more in the future"), not a finished, settled design.

### Claim 12: The motivating problem for building smevals is the widening gap between rising frontier-model prices and rapidly improving inexpensive/local model capability, creating a need to systematically identify the cheapest model adequate for a given task category
- **Evidence**: Stated as the opening motivation in the Prime Radiant
  announcement, with specific named price comparisons.
- **Confidence**: anecdotal (named price comparisons are not sourced to a
  pricing table or citation within the post itself, and pricing is a
  fast-moving target that may already be stale)
- **Quote**: "Frontier models continue to improve at an impressive rate, but
  those improvements are often accompanied by increases in price as well.
  GPT-5.5 and 5.6 Sol are twice the price of GPT-5.4. Claude Fable 5 is
  twice the price of Claude Opus 4.8. Even Google's inexpensive Gemini 3.5
  Flash-Lite model has increased in price from Gemini 3.1 Flash-Lite."
- **Our assessment**: This is the "why build this at all" framing, and it
  positions smevals not as a general-purpose eval framework for any
  question, but specifically as tooling for the "which is the cheapest
  adequate model for category X" decision — a distinct use case from, say,
  safety evaluation or regression testing of a single fixed harness. The
  guide should note this framing when citing smevals: its worked example
  (comparing `gpt-4.1-mini`, `gpt-5.5`, and `gpt-5.4-nano` on the same haiku
  task) is a direct illustration of this cost/capability comparison use
  case, distinct from (though usable for) the harness-regression-testing use
  case documented in `blog-langchain-better-harness-evals.md`.

## Concrete Artifacts

### Eval directory layout (README, "Building an Eval")
```
my-eval/
├── eval.yaml            # name and description
├── tasks/               # one YAML file per Task
├── configs/              # one YAML file per Config
├── graders/              # one YAML file per Grader
├── checkers/             # custom Checker executables (by convention)
├── run-llm               # Runner executable (any name, any location)
└── runs/                 # created by smevals run - never edit by hand
```

### Complete worked haiku-eval example (README, "Example Eval: Grading Haikus")
```yaml
# my-eval/eval.yaml
name: haiku
description: >-
  Can the model write a haiku on demand? Graded on structure:
  the reply must be exactly three lines.
```
```yaml
# my-eval/tasks/pelicans.yaml
name: pelicans
prompt: Write a haiku about pelicans. Reply with only the haiku, three lines.
```
```yaml
# my-eval/configs/default.yaml
name: default
runner: ../run-llm
model: gpt-4.1-mini
```
```bash
# my-eval/run-llm (chmod +x)
#!/usr/bin/env bash
set -euo pipefail

llm -m "$SMEVALS_MODEL" "$SMEVALS_PROMPT"
llm logs -c --json > log.json
```
```yaml
# my-eval/graders/default.yaml
name: default
checks:
  - checker: ../checkers/three-lines
    required: true
scoring:
  pass_threshold: 1.0
```
```python
# my-eval/checkers/three-lines (chmod +x)
#!/usr/bin/env python3
import json, os, pathlib, sys

raw = (pathlib.Path(os.environ["SMEVALS_RUN_DIR"]) / "output.txt").read_text()
lines = [line for line in raw.strip().splitlines() if line.strip()]
print(json.dumps({
    "score": 1.0 if len(lines) == 3 else 0.0,
    "metrics": {"line_count": len(lines)},
    "notes": f"{len(lines)} non-empty line(s)",
}))
sys.exit(0 if len(lines) == 3 else 1)
```
```bash
smevals run my-eval -g                 # run every task, grade as each finishes
smevals run my-eval -m gpt-4.1-nano -m gemini-2.5-flash -g   # more models
smevals run my-eval -n 5 -g            # top every task up to five graded runs
smevals report my-eval                 # markdown report in the terminal
smevals serve my-eval                  # live web UI on http://127.0.0.1:7001
```

### Improved LLM-judge grader for the same eval (Prime Radiant announcement, "Improving the grader")
```yaml
# graders/default.yaml, second iteration
name: default
checks:
  - checker: ../checkers/three-lines
    required: true
  - checker: ../checkers/haiku-judge
    model: gpt-5.5
    required: true
scoring:
  pass_threshold: 0.8
```
```json
// JSON schema passed to the haiku-judge checker's structured-output call
{
  "type": "object",
  "properties": {
    "line_syllables": {
      "type": "array",
      "items": {"type": "integer"},
      "minItems": 3,
      "maxItems": 3
    },
    "follows_575": {"type": "boolean"},
    "subject_present": {"type": "boolean"},
    "poetic_quality": {"type": "number", "minimum": 0, "maximum": 1},
    "notes": {"type": "string"}
  },
  "required": ["line_syllables", "follows_575", "subject_present", "poetic_quality", "notes"],
  "additionalProperties": false
}
```

### Runner contract (README, "The Runner contract")
```
Env vars provided to every Runner invocation:
  SMEVALS_MODEL       - the model to use, from the Config or -m option
  SMEVALS_TASK        - the Task's name
  SMEVALS_PROMPT      - the Task's prompt, only set if the Task has one
  SMEVALS_TASK_<KEY>  - every scalar key of the Task, uppercased
  SMEVALS_RUN_DIR     - absolute path to the Run's directory

Contract:
  - stdout captured as output.txt (the model's response)
  - stderr captured as stderr.txt
  - non-zero exit -> Run marked "failed": never graded, excluded from
    reports, does not count toward -n targets
  - any other files written to the working directory are kept as
    Run artifacts
```

### Checker contract (README, "The Checker contract")
```
Env vars provided to every Checker invocation:
  SMEVALS_RUN_DIR     - absolute path to the Run directory being graded
  SMEVALS_CHECK       - the full Check configuration as JSON
  SMEVALS_CHECK_<KEY> - every scalar key of the Check, uppercased
  SMEVALS_TASK, SMEVALS_TASK_<KEY> - the Task's name and scalar keys

Exit code 0 = pass, non-zero = fail.
Optional JSON on stdout, up to five keys:
  score   - float 0.0-1.0
  metrics - object of numbers/booleans (aggregated as mean+-stderr / rate)
  tags    - list of short labels, open-vocabulary, presence-only
  notes   - human-readable string, never aggregated
  details - structured diagnostics, kept but ignored by aggregation
```

### Runs/Grades on-disk layout (README, "Runs and Grades on disk")
```
runs/<task>/<config>/<model>/<timestamp>/
├── run.yaml         # the record: full task, resolved config, timing, exit code
├── output.txt       # the model's response (runner stdout)
├── stderr.txt       # only present if the runner wrote to stderr
├── ...               # any other artifacts the runner wrote
└── grades/
    └── <grader>/
        ├── grade.yaml     # outcome, score, tags, per-check results
        ├── grader.yaml    # snapshot of the Grader that produced this Grade
        └── ...            # artifacts written by Checkers
```

### Full CLI surface (README, "Commands")
```
smevals run EVAL [-m MODEL]... [-c CONFIG] [-t TASK]... [-n N] [-g [GRADER]] [--runs-dir DIR]
smevals grade EVAL [-g GRADER] [--regrade] [--runs-dir DIR]
smevals report EVAL [-g GRADER] [--by-task] [--json] [--runs-dir DIR]
smevals serve EVAL_OR_SUITE... [-p PORT] [--host HOST] [-g GRADER]
smevals build EVAL_OR_SUITE... [-o DIR] [-g GRADER]
smevals docs
```

## Cross-References

- **Corroborates**:
  - `blog-langchain-better-harness-evals.md` (Claim 12, "Once our agent
    handles a case correctly, we don't want to lose that gain. The eval
    becomes a regression test.") — smevals' run/grade separation (Claim 3
    here) and multi-grader coexistence (Claim 8 here) are a concrete
    mechanism for exactly this pattern: a fixed set of Runs can be re-graded
    by an evolving Grader without re-incurring model-call cost, so the same
    Runs can serve first as an optimization target and later as a
    regression check as the Grader (or the definition of "correct")
    matures.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` (Claim 6, unit
    evals as "the 'Pytest' for LLMs... automated, assertion-based checks
    that catch regressions") — smevals' Checker contract (exit code +
    optional JSON score/metrics output, Claim 5 and Concrete Artifacts here)
    is a directly comparable, more fully specified implementation of the
    same "assertion-based automated check" concept that post names but does
    not itself specify a contract for.
- **Contradicts**: None found. smevals' vocabulary (eval/task/config/run/
  runner/grader/grade/check/checker) is a distinct naming scheme from the
  Thoughtworks three-layer architecture (persona/unit/observability, per
  `blog-thoughtworks-anand-agent-evaluation-framework.md`) and from
  LangChain's optimization-set/holdout-set framing (per
  `blog-langchain-better-harness-evals.md`), but these describe different
  organizing concerns (a file-format and CLI-tool vocabulary here, vs. an
  evaluation-layer taxonomy and an overfitting-prevention methodology in the
  other two) rather than conflicting claims about the same question — this
  is a conditioning/framing difference, not a contradiction per MINER.md
  §4a.
- **Extends**: `blog-simonwillison-kimi-k3-pelican-benchmark.md` (Claim 5,
  the pelican benchmark's correlation with general model quality has
  "mostly severed"; Claim 6, its biggest limitation is not measuring
  "agentic tool calling or long-horizon reliability... the thing that
  matters most") and `blog-simonwillison-pelicanmaxxing.md` (a rigorous
  statistical study of the same benchmark) — smevals' own vocabulary
  definition (Claim 1 here) uses "Generate an SVG of a pelican riding a
  bicycle" as its canonical example Task, and its Config concept explicitly
  allows testing "agent harnesses" as a first-class parameter alongside
  system prompts and model parameters — directly addressing the tool-calling/
  harness-testing gap that Willison himself names as the pelican benchmark's
  weakness in the Kimi K3 note. smevals is best read as Willison's own
  proposed replacement infrastructure for eval categories the pelican
  benchmark cannot cover.
- **Novel**: The full Runner/Checker process-contract specification
  (environment variable names, stdout/exit-code semantics, the five-key
  Checker JSON output schema, the failed-Run exclusion rule) is new to the
  corpus — no existing source note documents a concrete, load-bearing
  process-boundary contract for eval execution and grading at this level of
  specificity. The "grading is a pure function of already-collected Run
  data, re-runnable without re-executing the model" design principle
  (Claim 3) and the idempotent target-sample-count semantics of `-n`
  (Claim 7) are also new to the corpus.

## Guide Impact

- **Chapter 04 (Evaluating Models & Prompts)**: Add the eval/task/config/
  run/runner/grader/grade/check/checker vocabulary (Claim 1) as a candidate
  standard vocabulary for the guide's own discussion of eval-suite design,
  replacing or supplementing looser terms like "test case" and "eval
  script." Cite the run/grade separation of concerns (Claim 3) as a
  named design principle: build eval infrastructure so that grading logic
  can be revised and re-applied to already-collected model outputs without
  re-paying for new model calls.
- **Chapter 04**: Add the Runner/Checker contract details (Claim 4, Claim 5,
  Claim 6, Concrete Artifacts) as a worked reference example of how to
  specify process boundaries for custom eval tooling — specifically the
  failed-Run-vs-bad-response exit-code distinction (Claim 4) and the
  null-score-on-incomplete-grading rule (Claim 6), both of which prevent
  specific silent-failure modes that a naive custom eval script is likely
  to get wrong on a first attempt.
- **Chapter 03 (Testing & Reliability)**: Cite Claim 7 (`-n` as an
  idempotent target sample count with balanced-pass execution and capped
  retry-on-failure) as a concrete operational pattern for anyone building
  eval-running infrastructure against flaky or rate-limited model APIs.
- **Chapter 05 (Tools & Frameworks)**: Add `smevals` itself as a named,
  concrete tool option for practitioners building eval suites, alongside
  the existing DeepEval/ragas/TruLens/LangSmith/Langfuse/Helicone landscape
  documented in `blog-thoughtworks-anand-agent-evaluation-framework.md`,
  with the caveat (per Claim 11/12 and Extraction Notes) that it is a
  newly-released, single-maintainer-lineage tool without independent
  third-party validation yet.
- **Chapter 07 (Reasoning chains and harness evaluation, per Prospector
  triage)**: Cite the Config concept's explicit inclusion of "agent
  harnesses" as a testable parameter (Claim 1) and the agent-native README
  design (Claim 9) as an example of eval tooling built to be operated by a
  coding agent end-to-end, from `uvx smevals docs` through eval construction
  and execution.

## Extraction Notes

- Willison's own post (`simonwillison.net/2026/Jul/31/smevals/`) is a short
  link-blog entry; per MINER.md §1 this note followed both substantive
  outbound links — the full Prime Radiant announcement and the tool's
  GitHub README — since nearly all of the technically citable content lives
  in those two pages, not in Willison's own short framing text. Both linked
  pages were fetched as raw HTML/Markdown (not via a summarizing WebFetch
  pass) so every `Quote` field above could be verified character-for-character.
  This was necessary: an initial summarizing WebFetch pass on Willison's own
  post fabricated a quotation mark around a phrase ("it feels right to
  me.") that is not quoted in the source's raw HTML — that fabricated quote
  was caught and discarded before writing this note, and the raw-HTML
  version (unquoted prose) is what Claim 11 cites instead.
- The Prime Radiant announcement page and Willison's own blog post share
  byline authorship (both attributed to Simon Willison) and share the exact
  same vocabulary bullet list verbatim — this is not two independent
  sources corroborating each other, it is one author's writing duplicated
  across two properties. Cross-references above treat the vocabulary
  content as originating from a single source, not two.
- Did not follow the linked static-site example build
  (`static.simonwillison.net/static/2026/smevals-haiku-build/`), the linked
  screenshot image, the linked Hacker News-style GitHub Actions Test badge,
  or the gist containing the full `haiku-judge` checker script
  (`gist.github.com/simonw/fdf3fea4e2b0d910a014339211ab5901`) — these are
  demonstrations/build artifacts and a full code listing rather than prose
  containing additional claims; the system prompt and JSON schema the gist
  produces were already quoted directly from the announcement page's prose,
  which reproduces the relevant portions inline.
- No contradiction with any existing source note was identified; none filed
  (see Cross-References → Contradicts above for the reasoning).
