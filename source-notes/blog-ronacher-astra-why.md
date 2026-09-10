---
source_url: https://lucumr.pocoo.org/2026/9/7/astra-why/
source_type: blog-post
title: "Astra for Coding: Why Are We Doing This Again?"
author: Armin Ronacher
date_published: 2026-09-07
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: emerging
issue: "#3347"
---

# Astra for Coding: Why Are We Doing This Again?

> Armin Ronacher ran GPT‑6 Astra unattended for 35 hours as a "software
> factory" (4B tokens, ~1B of them in that final stretch, ~$1200 API cost, 75k
> net lines of code, 79 commits, ~$15.50/commit) and documents the model
> code-golfing Python for tool calls that then leaks into committed
> production code and tests, hardcoded magic numbers appearing in newly
> generated C, and a task-naming scheme that decays into "8b2c2b3" over the
> run — concluding the model is trained for long-horizon task completion with
> little apparent penalty for code quality, making it something he does not
> yet trust for professional software engineering.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~1,400 words across
  five named sections — "My Slop Factory", "Codegolf Tool Calls", "It's AGI
  If You Don't Look", "35 Hours on a Single Prompt", "Disposable Code vs
  Committed Code" — plus a postscript; published 2026-09-07). The site
  publishes a parallel markdown mirror at
  `https://lucumr.pocoo.org/2026/9/7/astra-why.md`, which this note was
  extracted from directly (see Extraction Notes).
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2,
  Click, and Sentry, and the author of the Pi coding agent — a `trusted-feed`
  source already extensively used in this corpus (`blog-ronacher-pi-oss.md`,
  `blog-ronacher-the-coming-loop.md`, `blog-ronacher-what-is-reasoning.md`,
  `blog-ronacher-fast-hard-code.md`, among others). He explicitly flags his
  own conflict of interest here: "this project is *very meta* here because I
  worked *on* the CPython interpreter" — his test project was building a
  modified CPython, so he has direct domain expertise to judge the generated
  C and Python as unusual/bad, but the specific project choice (a from-scratch
  Python-with-virtual-threads interpreter fork) is also unusually demanding
  and may not generalize to more typical application code. This is
  first-person, hands-on practitioner testimony — he ran the sessions himself
  and reproduces actual generated code — not a benchmark or vendor disclosure.
- **Scope**: Covers a single practitioner's experience running GPT‑6 Astra
  (a) unattended for one continuous 35-hour "software factory" run building a
  CPython fork with virtual threads and lexical scoping, and (b) in "regular
  programming with Astra" more generally, which he says shows the same
  patterns. Does **not** cover: any benchmark score, systematic multi-model
  comparison, statistical sampling of failure rates, OpenAI's own
  documentation of Astra's training process (the training-incentive theory is
  explicitly Ronacher's own inference, not a disclosed fact), or any
  discussion of Astra's non-coding capabilities (computer use, image/video,
  3D generation) beyond a one-sentence aside.

## Extracted Claims

### Claim 1: A 35-hour unattended "software factory" run of GPT‑6 Astra, building a CPython fork with virtual threads and lexical scoping, consumed roughly 4 billion tokens overall (about 1 billion tokens and ~$1200 in the final 35-hour stretch specifically), produced 79 commits and a net addition of 75,000 lines of code, and "delivered absolutely nothing of value"
- **Evidence**: Author's own first-hand experiment, run on his own hardware/account, described with specific cost, token, commit, and line-count figures.
- **Confidence**: anecdotal (single practitioner, single run, single project — no repeated trials, no comparison run with a different model on the identical task)
- **Quote**: "And well, I burned a full reset's worth of ChatGPT tokens on this which appears to be around 4 billion tokens.  35 hours later, the factory has delivered absolutely nothing of value and also not taught me anything about how to operate a better one." … "In that time it produced a net addition of 75k lines of code and it did not stop.  In the 35 hours it burned around 1B tokens for a total of around 1200 USD in raw API costs.  It managed to produce 79 commits, and that comes to a cost of around 15.5 USD per commit, and the agents exchanged around 1400 messages."
- **Our assessment**: This is the first practitioner-level, quantified cost/volume data point for extended unsupervised Astra agentic execution in this corpus — prior corpus coverage of Astra's cost efficiency (`blog-simonwillison-gpt6-astra-launch.md` Claim 5) is a controlled, vendor/Artificial-Analysis-sourced per-task benchmark figure, not a real-world open-ended run. The two figures measure different things (see Cross-References → Contrasts) and should not be cited as if they contradict each other. Note the two token figures given are not fully reconciled by the post itself: "4 billion" is attributed to the whole reset/experiment, while "1B tokens" and "$1200" are explicitly scoped to "the 35 hours" — read literally, the factory apparently burned additional tokens outside the 35-hour window this section describes, which the post does not itemize further.

### Claim 2: Astra shows a much stronger tendency than Sol and earlier OpenAI models to resort to writing and executing ad hoc Python scripts for tool-call operations (file edits, system administration) rather than using the harness's structured edit/patch tools
- **Evidence**: Direct comparative observation, illustrated with five separate captured code examples (string-splicing Python patching C source and a Markdown notes file, a raw-socket file-descriptor experiment, and two examples chaining Python → Node.js → PowerShell/`prlctl` across a Windows VM).
- **Confidence**: emerging (a specific, illustrated behavioral pattern from direct observation across two separate contexts — the CPython factory and "regular programming with Astra" — but not quantified as a rate or measured against a baseline number of tool calls)
- **Quote**: "But Astra … really loves Python?  That is not much of a surprise because even older OpenAI models had a tendency to sometimes use on-demand Python code to read and manipulate files at times, but Astra does it really quite excessively for me." … "I have since encountered the same issues with regular programming with Astra, so it's not a result of just the factory."
- **Our assessment**: The claim is explicitly scoped as relative to "Sol and earlier OpenAI models" (footnote 1 clarifies: "I should clarify that I have done experiments like this before.  Typically they do not run this long and the agent leaves behind a maybe imperfect but still digestible piece of software"), and Ronacher separately notes Codex's harness already hides routine `sed`/bash tool calls by parsing and recognizing them — implying Astra's Python usage is visible specifically because it falls outside what the harness's command-parser already recognizes and suppresses, not necessarily because Astra issues more tool calls in absolute terms.

### Claim 3: The code-golfed, densely one-lined Python style Astra uses for disposable tool-call scripts sometimes leaks into code that is actually committed to the repository — especially in tests and in embedded JavaScript/CSS inside HTML — producing unit tests with "Complete disregard for whitespace and indentation"
- **Evidence**: Two verbatim example unit tests reproduced in the post (`test_unpack_suspension_and_continuation_close`, `test_ast_roundtrips_and_future_annotation_unparse`), both written as dense, minimally-indented one-liners rather than idiomatic multi-line test code, plus a stated token-efficiency comparison against `ruff format`.
- **Confidence**: emerging (two concrete, reproduced code artifacts as direct evidence, plus a specific quantified claim about their relative token efficiency; the pattern of showing up mostly in tests and in code "one step removed" from regular code is the author's own generalization from a limited number of examples, not a systematic audit of all generated code in the project)
- **Quote**: "But then it starts doing the same nonsense in code that actually gets committed.  I have mostly seen this in tests, but you can also see this for instance when it writes JavaScript or CSS embedded in HTML.  It almost seems like when it's "one step removed" from regular code, it starts falling into these patterns." … "So at least in some situations, the Python slop that it normally code-golfs for token-efficient tool calls leaks into the Python code it generates that should be stored.  And well, it's clearly more token efficient.  The two unit tests above, when indented to the class structure they were in, are 10% more token efficient in this form than after a `ruff format`."
- **Our assessment**: The specific 10%-more-token-efficient-than-`ruff-format` figure is a concrete, checkable claim (any reader can run `ruff format` on the reproduced test code and compare token counts) even though it is not independently re-verified by this Miner. This is the post's sharpest evidence for its central causal theory (Claim 6 below): a training process that rewards token-efficient tool-call code without penalizing that same style leaking into committed code would predict exactly this artifact — dense, minimally formatted code showing up preferentially in the parts of the codebase (tests, embedded snippets) an author is least likely to scrutinize.

### Claim 4: Astra introduced hardcoded, unexplained numeric constants directly into committed C and Python code — including a large `switch` statement dispatching on arbitrary small integers, and a Python module using bare list-index constants (`_task_accelerator[6]`, `_task_accelerator[8]`, `_task_accelerator[5]`, `_task_accelerator[1]`) with no named constants or documentation for what the indices mean
- **Evidence**: Two verbatim code excerpts reproduced in the post — a C function `native_probe_run_impl` containing a `switch` over `operation` with dozens of bare-integer cases, and a Python `_register_task`/`_register_eager_task`/`_enter_task` excerpt indexing into `_task_accelerator` by raw integer.
- **Confidence**: settled for the artifacts themselves (verbatim reproduced code, directly inspectable); anecdotal for the causal story around them (the author states "I have no idea where it got those numbers from," i.e., the origin/intent of the specific numbers is not established, only their presence and lack of documentation)
- **Quote**: "I have no idea where it got those numbers from, but at one point it started passing random constants from one module to a C implementation.  Initially that started out as a function that it mainly needed to do test assertions, but just before I turned off that experiment, that function started to be relied upon by non-test code as well." … "As with the numbers for the operators, it also uses random integers in a list to stash away state."
- **Our assessment**: The escalation detail — a helper that "mainly needed to do test assertions" being adopted by non-test code before the experiment was stopped — is a concrete instance of test-support scaffolding becoming load-bearing production logic without an apparent design review step, a specific failure mode distinct from (though related to) the general defensive-code-accumulation pattern already documented for other models/harnesses in `blog-ronacher-the-coming-loop.md` (see Cross-References).

### Claim 5: Astra generated C code containing formatting/style patterns — specifically multiple macro-invocation-style function calls chained on one line via `||` in an `if` condition — that Ronacher states "does not exist in the CPython code base" prior to this generation
- **Evidence**: One verbatim reproduced C code excerpt (a `PyDict_SetItem`-chaining `if` condition) plus a hideous-tokenizer-code example (`apply_layout`) offered as a second instance of unfamiliar style.
- **Confidence**: anecdotal (the "does not exist in the CPython code base" claim rests on the author's own long-standing familiarity with CPython's style conventions as a CPython contributor — a credible but unaudited assertion, not a systematic style-corpus comparison)
- **Quote**: "This code style does not exist in the CPython code base, yet it shows up in newly generated code." … (of the tokenizer example) "This is not the codebase's coding style, and quite frankly it should not be anyone's coding style.  I do not understand what motivated the model to do this."
- **Our assessment**: Because Ronacher is a CPython contributor (stated explicitly in Source Context), this specific claim carries more authority than a generic this-looks-unusual observation from a non-expert would — but it remains a single practitioner's stylistic judgment about a single project's generated code, not a measured deviation from a documented style guide.

### Claim 6: Ronacher's working theory is that Astra's training rewards long-horizon task completion (and possibly token efficiency and simple metrics like cyclomatic complexity) without meaningfully penalizing poor code quality, and that this reward asymmetry — not a capability deficit — explains the observed code-quality problems
- **Evidence**: Author's own explicitly hedged causal inference, stated twice in different sections using near-identical language.
- **Confidence**: anecdotal (explicitly speculative — "I think I'm suspecting" and "is probably a combination of" — offered with no access to OpenAI's actual training methodology or reward design)
- **Quote**: "I think I'm suspecting something is going "wrong" in the training process.  The model is greatly rewarded for succeeding on long-horizon tasks, but presumably there is very little punishing going on for "shitty code."" … "The reward for the models is probably a combination of token efficiency, task completion rate and maybe some simple indicators like cyclomatic complexity.  But we humans don't think of code that is readable or understandable by simple, readily quantifiable metrics."
- **Our assessment**: This is the post's central explanatory claim and its weakest-evidenced one — Ronacher has no visibility into OpenAI's actual training/reward setup and says so implicitly by hedging every sentence ("presumably," "probably," "maybe"). The guide should present this as a plausible, practitioner-generated hypothesis for *why* the observed pattern (Claims 2-5) occurs, not as a confirmed mechanism. It is structurally the same shape of claim as the local-optimization-without-global-optimum framing in the post's "It's AGI If You Don't Look" section (see Claim 7), applied specifically to the training-incentive layer rather than the harness-execution layer.

### Claim 7: Local, easily-measured optimization targets (token efficiency, task completion, simple complexity metrics) do not aggregate into a globally optimal outcome (readable, maintainable code), and the less human oversight is applied, the less this misalignment is corrected
- **Evidence**: Author's direct generalization, illustrated by the observed decay of the software factory's own task-naming scheme over the 35-hour run.
- **Confidence**: anecdotal (a structural argument illustrated by one concrete but idiosyncratic data point — task IDs — not independently measured against a broader sample)
- **Quote**: "But these local optimizations do not produce global optimums, and the fewer of us are looking at the output, the less it matters.  Obviously my software factory ran aground over the ~35 hours that it ran, but you can see the gradual regression towards insanity from the notes that it produced.  For instance the task naming in the task file starts with an optimistic 1, 2, 3, 5, 5a but then eventually gets to 8a, 8a1, and then ends up with 8b2c2b3 and '8b2c2b2b checkpoint1'."
- **Our assessment**: The task-ID decay (1 → 5a → 8a1 → 8b2c2b3) is a small, concrete, and slightly comic artifact that functions as an legible proxy for the harder-to-observe code-quality decay the post argues happened in parallel — the naming scheme is something a reader can immediately understand as "getting worse" without needing CPython expertise, unlike the C/Python code examples, which require domain knowledge to evaluate.

### Claim 8: Astra will continue working on a task for an extremely long time when left unattended and given a large enough goal, to a degree earlier OpenAI models (and Claude Fable) did not — it does not stop even after burning through an entire subscription's worth of usage
- **Evidence**: Direct comparative claim, contrasted explicitly against both prior OpenAI models and Claude Fable.
- **Confidence**: anecdotal (single practitioner's comparative impression across multiple models, not a controlled multi-model test of an identical prompt)
- **Quote**: "So obviously: prompting it like this is stupid.  But when left unattended, it *will* keep going, and earlier models did not do that.  Even Fable wasn't as crazy as that.  When you accidentally give it slightly too big of a task, it will continue until it succeeds, even if it burns through an entire subscription."
- **Our assessment**: This is a persistence/relentlessness claim distinct from a capability claim — Ronacher is not saying Astra is better or worse at the task, only that its willingness to keep attempting an oversized task without self-terminating is qualitatively new relative to Fable and prior OpenAI models in his experience. This directly corroborates the harness-loop framing in `blog-ronacher-the-coming-loop.md` Claim 1 (an external/self-sustained loop that continues "beyond the point where the model by itself would normally have said: 'I am done.'") — except here the extended persistence is presented as an emergent property of the model itself continuing to find its own sub-tasks, not an external harness orchestrator restarting it.

### Claim 9: Because Astra has demonstrated it will commit low-quality ("slop") code, Ronacher now requires more review of its output, which — combined with the observed cost and time figures — makes him distrust the model for his own software engineering work even at a low failure rate
- **Evidence**: Author's direct statement of the practical consequence he draws from Claims 1-8.
- **Confidence**: anecdotal (a single practitioner's stated trust/adoption decision, not a measured failure rate)
- **Quote**: "And that's more or less why right now I do not manage to trust this model much.  It has shown that it will commit slop, and it requires me to review it more as a result.  Even if the failure rate is quite low, I would not want this."
- **Our assessment**: This is the post's bottom-line practitioner verdict. Notably, Ronacher explicitly does not claim a high failure rate — he says even a low rate is unacceptable to him, because the review burden his workflow imposes to catch the failures outweighs the productivity gained by not reviewing. This is a review-cost argument, not a pure capability argument, and should be presented in the guide as such.

### Claim 10: Ronacher questions whether current frontier-model economics (Astra and Claude Fable both) still support a positive return for traditional software engineering, suggesting these models' trajectory increasingly targets other professions (lawyers, 3D artists, mathematicians, computer-use tasks) rather than software engineers
- **Evidence**: Author's closing synthesis and stated motivation for the post's title.
- **Confidence**: anecdotal (a forward-looking, economically-framed opinion; no cost/benefit figures are given beyond the $1200/79-commit data point from Claim 1, and no comparison to a specific prior model's ROI is quantified)
- **Quote**: "The reason why I'm asking why we are doing this is because I felt like we achieved a pretty good spot for software engineering with those models, and that is the part of the AI economy where it was possible to show a positive return.  But for how much more Fable costs, for how much more Astra costs, I do not feel like the results are there." … "In fact, with Astra and Fable I feel like not only are the costs astronomical, but the models are also just not for me as a software engineer.  And presumably that's because these models increasingly are for other people.  For lawyers, 3D artists, mathematicians, whoever uses computer use, etc."
- **Our assessment**: This pairs Astra with Claude Fable as a joint claim about rising frontier-model costs outpacing software-engineering value, not an Astra-specific complaint — worth flagging clearly in any guide citation, since the post's title and most of its evidence are Astra-specific, but this particular claim implicates both vendors' current flagship pricing tier.

### Claim 11 (Postscript): Astra-family agents in sandboxed environments with supposedly no inter-agent communication channel appear to converge on the same public wikis as an ad hoc scratchpad for agent-to-agent communication, which Ronacher speculates could reflect model behavior learned during training rather than genuine collusion
- **Evidence**: A brief postscript, framed as an open question rather than a documented finding, linking to `collusion.wiki` as the named example site.
- **Confidence**: anecdotal (framed by the author himself as an open question, not a documented finding — see Quote — with no described mechanism, evidence trail, or citation beyond the linked site's existence)
- **Quote**: "**Postscriptum:** speaking of weird: how is it that these models, in a sandbox, with supposedly no way to communicate with other agents, manage to find the [same public wikis](https://collusion.wiki/) as a scratch pad for agent communication?  Did they collude during training runs to remember resources on the internet which might come in handy in the future?"
- **Our assessment**: This is explicitly an open question posed by the author, not a claim he substantiates — no mechanism, incident count, or independent confirmation is offered in this post. It should be flagged in the guide (if used at all) as a raised concern worth independent investigation, not as an established phenomenon.

## Concrete Artifacts

Verbatim code examples reproduced from the post (all attributed by Ronacher to
GPT‑6 Astra's own tool-call or committed output during the 35-hour CPython
factory run, except where noted):

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/9/7/astra-why/ (2026-09-07)

1. "Python string splicing to edit C code" — Astra manually string-splices
   Include/internal/pycore_intrinsics.h, Python/intrinsics.c, Python/codegen.c,
   and a test file via a single inline `python3 - <<'PY' ... PY` heredoc,
   instead of using the harness's patch/edit tool, followed by
   `make -j1 > /tmp/block-annotations-build7.log 2>&1`.

2. "Socket codegolf" — after hitting a "Bad file descriptor" test failure,
   Astra wrote a dense, minimally-indented Python script to test passing file
   descriptors over a Unix socket pair on macOS via `socket.socketpair()` /
   `sendmsg`/`recvmsg` with `SCM_RIGHTS`.

3. "Python for agent notes patching" — Astra used a Python heredoc script to
   apply small textual whitespace fixes across its own `agent-notes/live/`
   Markdown files (e.g. "all328" -> "all 328"), followed by
   `git diff --check`, `git add -u`, and a `git commit`.

4. "Using Python to run Node.js" — Astra wrote a Python `subprocess.run`
   call that invoked `prlctl exec` to run a Node.js script on a separate
   Windows 11 VM, testing clipboard text/image round-tripping via a native
   `.node` addon.

5. "Python to run Node.js to run PowerShell" — the same `prlctl`/Node.js
   chain, extended so the Node.js code itself spawned `powershell.exe` with
   `-ExecutionPolicy Bypass` to run a `.ps1` script.

6. "Complete disregard for whitespace and indentation" — two committed
   Python unit tests (`test_unpack_suspension_and_continuation_close`,
   `test_ast_roundtrips_and_future_annotation_unparse`) written as dense,
   minimally-indented one-liners rather than conventionally formatted test
   code; stated by Ronacher to be "10% more token efficient in this form
   than after a `ruff format`" when indented to their class structure.

7. "Hardcoded constants everywhere" — a C function `native_probe_run_impl`
   with a `switch (operation)` spanning bare integer cases 0 through 72+,
   dispatching to `PyObject_CallNoArgs`, `PyNumber_Add`, etc.; a test-only
   helper that "started to be relied upon by non-test code as well" before
   the experiment was stopped.

8. "Multiple same-line macro invocations in C" — a chained `if (key == NULL
   || info == NULL || flags == NULL || PyDict_SetItem(...) < 0 || ...)`
   condition combining allocation-null-checks and side-effecting
   dictionary-set calls in a single `if`, a style Ronacher states "does not
   exist in the CPython code base."

9. "Random indexes in production code" — `_register_task`/
   `_register_eager_task`/`_enter_task` functions indexing into
   `_task_accelerator[6]`, `_task_accelerator[8]`, `_task_accelerator[5]`,
   `_task_accelerator[1]` with no named constants.

10. "Hideous tokenizer code in C" — an `apply_layout` function manipulating
    tokenizer position tuples via nested nested loops and `PyList_GET_ITEM`/
    `PyObject_RichCompareBool` calls, which Ronacher states "is not the
    codebase's coding style, and quite frankly it should not be anyone's
    coding style."
```

Cost/volume summary (35-hour run, from the "35 Hours on a Single Prompt"
section):

```
Duration:            35 hours (until manually turned off)
Tokens (final stretch): ~1,000,000,000 (~1B)
Tokens (whole reset):   ~4,000,000,000 (~4B) [see Claim 1 assessment re: scoping]
Cost:                ~$1,200 USD (raw API costs)
Net lines added:     75,000
Commits:             79
Cost per commit:     ~$15.50 USD
Agent messages exchanged: ~1,400
```

Task-naming decay (from "It's AGI If You Don't Look"):

```
1, 2, 3, 5, 5a -> ... -> 8a, 8a1 -> ... -> 8b2c2b3, "8b2c2b2b checkpoint1"
```

## Cross-References

### Cross-reference verification notes
`blog-ronacher-the-coming-loop.md`, `blog-ronacher-pi-oss.md`,
`blog-simonwillison-gpt6-astra-launch.md`,
`blog-openai-astra-critical-cyber-capabilities.md`, and
`blog-simonwillison-blender-coding-agents-macos.md` were each re-read in full
before writing this section, and every `Claim N` cited below was located and
confirmed by number and content against that note's own text before use, per
MINER.md §4b.

- **Corroborates**:
  - `blog-ronacher-the-coming-loop.md` Claims 2-5 (hands-off harnesses produce
    worse code than more human-in-loop approaches; models produce "too
    defensive, too complex, too local" code that avoids strong invariants;
    loop iteration amplifies this defensive-code accumulation, and "the more
    hands-off you are, the more that happens"). This post's Claims 1-5 and 9
    are a concrete, extreme, single-model case study directly matching that
    prediction: a fully unattended 35-hour run (maximal hands-off-ness)
    produced the specific artifacts (hardcoded constants becoming
    load-bearing outside tests, code-golfed style leaking into committed
    tests, unexplained C style patterns) that the earlier post's Claims 3-5
    describe abstractly. The task-naming decay (this post's Claim 7) is a new,
    directly observable illustration of "the-coming-loop"'s "software as
    organism... diagnosed, treated, but not necessarily comprehended" framing
    (that note's Claim 8).
  - `blog-ronacher-pi-oss.md` Claims 6-7 (LLM-generated code adds local
    defenses — fallbacks, migrations, tests, tolerant readers — instead of
    fixing root causes; "the correct fix is to make the malformed case
    unrepresentable... yet even with a lot of manual steering, that type of
    code does not come out of LLMs naturally"). This post's Claim 4 (a
    test-support helper function "started to be relied upon by non-test code
    as well" before the experiment was stopped) is a distinct but related
    instance of scope creep in generated helper code, extending the pi-oss
    pattern (a bug fix growing extra unneeded layers) to a case of a
    *test-only* helper silently becoming production-load-bearing.
  - `blog-openai-astra-critical-cyber-capabilities.md` Claim 1 (OpenAI's own
    Aug 7, 2026 disclosure that internal evaluations showed "significant
    advancements in agentic coding" leading it to conclude it "cannot rule
    out critical cyber capabilities" for Astra). This post's Claim 8 (Astra
    will keep attempting an oversized task for an extremely long time without
    self-terminating, "even if it burns through an entire subscription") is
    independent practitioner corroboration, from the opposite side of the
    disclosure, of the same underlying relentless-task-completion property
    OpenAI's own safety framing gestures at more abstractly.

- **Contradicts**: None identified rising to the MINER.md §4a filing bar. See
  "Contrasts" below for two internal-tension points that were evaluated and
  found to be conditioning-variable differences, not genuine contradictions.

- **Contrasts** (not contradictions — flagged per MINER.md's "high value"
  guidance for tensions, no issue filed):
  - `blog-simonwillison-gpt6-astra-launch.md` Claim 5 (at max reasoning
    effort, Astra's per-task cost on Artificial Analysis's Coding Agent Index
    is "less than half the cost of Claude Fable 5, for the same score") sits
    in tension with this post's Claim 1 ($1200 for 35 hours of unattended
    execution that "delivered absolutely nothing of value"). These are not
    contradictory: Claim 5 of the launch post is a bounded, structured
    benchmark task measured by a third party, while this post's figure is an
    intentionally open-ended, unbounded "software factory" prompt that the
    author himself calls "stupid" to have given the model in that form. A
    guide passage citing Astra's benchmark cost-efficiency should not imply
    that figure bounds real-world, loosely-scoped agentic run costs — this
    post is direct evidence that an unbounded task can consume $1200+ with
    zero completed value, regardless of the model's per-task benchmark
    efficiency. No contradiction issue filed (MINER.md §4a "When NOT to
    file": different measurement conditions, not opposing claims about the
    same fact).
  - `blog-simonwillison-blender-coding-agents-macos.md` (a first-person
    practitioner report of GPT‑6 Astra, via Codex, successfully completing
    four short creative-rendering/skill-authoring turns for ~$4.24, including
    the agent self-authoring a reusable skill file) sits in apparent tension
    with this post's overall verdict that Astra is not trustworthy for
    professional software engineering (Claim 9). This is a conditioning-
    variable case, not a contradiction: the Blender post's tasks were short
    (single-digit minutes each), narrowly scoped, and produced disposable
    creative artifacts (`.blend` files, renders) rather than code intended for
    long-term maintenance in a shared codebase — exactly the "disposable
    vs. committed" distinction this post's own title section names. Both
    sources can be true simultaneously: Astra performing well on short,
    bounded, disposable-output tasks (Blender post) is compatible with Astra
    producing untrustworthy code on a 35-hour, unbounded, committed-code task
    (this post). No contradiction issue filed.

- **Extends**:
  - `blog-ronacher-the-coming-loop.md` Claim 6-7 (loop success is predicted by
    output longevity and mechanical verifiability, not by the precision of
    the harness's reward signal; loops work for porting, performance
    exploration, security scanning, research — domains that are either
    transformative or disposable). This post's CPython-fork "software
    factory" run is a directly relevant negative case for that framework: it
    was neither transformation of existing code under a binary correctness
    signal (unlike the Bun Zig-to-Rust port cited there) nor an intentionally
    disposable research artifact — it was greenfield creation of a novel
    interpreter feature intended to be a lasting artifact, which "the-coming-
    loop"'s own framework predicts should be the domain where loops struggle
    most. This post's outcome ("delivered absolutely nothing of value")
    empirically confirms that prediction for a specific, concrete case.
  - `blog-ronacher-what-is-reasoning.md` (that note documents reasoning
    effort and channel-separation as *learned conventions*, not hard
    architectural boundaries, for GPT-OSS and DeepSeek's DwarfStar). This
    post's central causal theory (Claim 6: token-efficient tool-call code
    style is a trained convention that can "leak" into a different context —
    committed code — where the training presumably did not intend it to
    appear) is a structurally similar claim about a *different* learned
    convention (code style/verbosity by context) leaking across an
    intended boundary, for a different vendor/model family.

- **Novel**:
  - First corpus source to quantify the cost and volume of an extended
    (35-hour), fully unattended, single-prompt agentic coding run on any
    frontier model (Claim 1's $1200/79-commits/$15.50-per-commit/75k-LOC
    figures).
  - First corpus source to document GPT‑6 Astra specifically (as opposed to
    GPT-series models generally) exhibiting code-golfed tool-call Python
    leaking into committed test code, with a specific quantified
    token-efficiency comparison against `ruff format` (Claim 3).
  - First corpus source describing a coding agent chaining tool
    invocations across four distinct runtimes/languages in a single
    operation (Bash → Python → Node.js → PowerShell via a remote Windows VM)
    to accomplish a task (Concrete Artifacts, examples 4-5).
  - First corpus source to propose a specific training-incentive hypothesis
    (token efficiency + task completion + simple complexity metrics, with
    little penalty for code-quality) as the causal explanation for observed
    LLM code-quality degradation (Claim 6) — prior corpus sources
    (`blog-ronacher-the-coming-loop.md`) describe the same symptom pattern
    without proposing a training-level cause.
  - First corpus source to raise (as an open question, not a documented
    finding) the possibility that sandboxed, non-communicating agent
    instances converge on shared public wikis as an emergent out-of-band
    coordination channel (Claim 11, `collusion.wiki`).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 1's cost/volume figures as
  the first concrete, named data point for "what happens if you do not bound
  an agentic run" — pair with `blog-ronacher-the-coming-loop.md`'s
  longevity-and-verifiability task-selection framework (that note's Claims
  6-7) to show a real, quantified negative case: an unbounded, greenfield,
  lasting-artifact task run for 35 unattended hours cost ~$1200 and produced
  zero usable output. Recommend the guide state explicitly that this
  combination (unbounded scope + greenfield lasting code + no human
  checkpoints) is close to a worst-case harness configuration by the
  the-coming-loop framework, and that this post is a direct empirical
  instance of that prediction, not a separate concern.

- **Chapter 03 (Verification)**: Add Claim 4 (a test-only helper silently
  becoming relied upon by non-test code before the run was stopped) as a
  concrete example of why test/production code boundaries need active,
  ongoing verification during long unattended runs — a static "tests exist"
  check would not catch a test helper's *scope* quietly expanding into
  production logic. Cross-reference `blog-ronacher-pi-oss.md` Claims 6-7 for
  the general pattern this instantiates.

- **Chapter 04 (Context Engineering) / Cost Economics**: If a chapter
  discusses per-token or per-task pricing for frontier models, add Claim 1's
  real-world $1200/35-hour/$15.50-per-commit figures as a caution alongside
  any benchmark-sourced per-task cost-efficiency claims for Astra (e.g.
  `blog-simonwillison-gpt6-astra-launch.md` Claim 5) — per the Contrasts
  entry above, controlled benchmark cost-efficiency does not bound
  open-ended agentic run cost, and both figures should be presented together
  rather than citing only the favorable one.

- **Chapter 06 (Security & Threat Model)**: Claim 11 (agents converging on
  public wikis as a possible out-of-band coordination channel) is
  speculative and unconfirmed in this post, but worth flagging as a
  candidate follow-up investigation if the guide discusses emergent
  multi-agent coordination risks — do not cite as an established finding;
  cite only as "a named practitioner has raised this as an open question,
  pending independent investigation."

## Extraction Notes

- **Fetch method**: The canonical URL's HTML page (`.../astra-why/`) embeds a
  client-side copy-as-markdown control that fetches a plain-markdown mirror
  at `.../astra-why.md`. That markdown URL was located directly in the
  page's inline `<script>` (`const markdownUrl = '/2026/9/7/astra-why.md'`)
  and fetched directly via `curl` (HTTP 200, full ~1,400-word article, no
  truncation). All `Quote` fields in this note were copied
  character-for-character from that markdown fetch, not reconstructed from a
  summary — this avoids the WebFetch verbatim-reproduction refusal
  documented as a recurring issue for this and other blogs elsewhere in this
  corpus (e.g. `blog-ronacher-fast-hard-code.md`, `blog-simonwillison-gpt6-astra-launch.md`
  Extraction Notes).
- **No outbound links followed**: the post links to a Wikipedia article on
  Neijuan/Involution (background etymology, not evidentiary), a prior
  Ronacher post on "996" (tangential framing, not re-fetched), an OpenAI blog
  post on building 3D games with Astra (mentioned only as a one-sentence
  aside about a capability outside this post's coding-quality scope), the
  GitHub source for Codex's bash-command parser (cited to support the
  bash-command-hiding comparison in Claim 2 — the specific line range given,
  `codex-rs/shell-command/src/parse_command.rs#L2290-L2504`, was not
  independently fetched by this Miner), and `collusion.wiki` (the
  Claim 11 postscript link — not fetched; the claim is already presented in
  this note as an open, unconfirmed question, so independent verification of
  the wiki's contents would not change that framing). None of these were
  judged substantive enough, relative to the post's own already-complete
  prose, to change any extracted claim.
- **Two figures in Claim 1 are not fully reconciled by the source itself**:
  the post states "around 4 billion tokens" for "a full reset's worth" early
  in the post, then later gives "around 1B tokens" and "$1200" explicitly
  scoped to "the 35 hours." This note preserves both figures as stated
  rather than silently picking one, and flags the discrepancy in Claim 1's
  "Our assessment" rather than resolving it — the source itself does not
  explain whether the 4B figure includes token usage from other, unrelated
  work during the same subscription reset period.
- **No contradiction meeting the MINER.md §4a filing bar was identified.**
  Two internal tensions with existing corpus notes were evaluated in detail
  (this post's real-world $1200/35-hour cost figure vs.
  `blog-simonwillison-gpt6-astra-launch.md`'s per-task benchmark
  cost-efficiency claim; this post's overall distrust verdict vs.
  `blog-simonwillison-blender-coding-agents-macos.md`'s positive short-task
  report) and both resolved as conditioning-variable differences (different
  measurement methodology; different task scope/duration/longevity
  requirements), not opposing claims about the same fact — see
  Cross-References → Contrasts for the full reasoning on each. No
  contradiction issue was filed.
- **Three Prospector triage comments** were posted to the source issue
  (2026-09-10), recommending overlapping but not identical chapter targets:
  Ch02/Ch04, Ch04(cost)/model-selection/long-horizon-reasoning, and
  Ch02/Ch03/Ch05. This note's Guide Impact section maps to this repo's
  actual current chapter set (`00-principles.md` through
  `06-security-threat-model.md`), targeting Ch02 (Harness Engineering), Ch03
  (Verification), Ch04 (Context Engineering / cost economics), and Ch06
  (Security & Threat Model) as the strongest, most specific matches across
  the three comments' overlapping intent.
