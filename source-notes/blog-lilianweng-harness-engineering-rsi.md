---
source_url: https://lilianweng.github.io/posts/2026-07-04-harness/
source_type: blog-post
title: "Harness Engineering for Self-Improvement"
author: Lilian Weng
date_published: 2026-07-04
date_extracted: 2026-07-24
last_checked: 2026-07-24
status: current
confidence_overall: emerging
issue: "#2201"
---

# Harness Engineering for Self-Improvement (Lilian Weng)

> A researcher-authored literature synthesis (39 references) arguing that
> "harnesses" — the orchestration layer around a base model — are the
> practical near-term substrate for recursive self-improvement (RSI), tracing
> an optimization-target progression from prompts through context, workflow,
> harness code, to optimizer code, and cataloguing the design patterns,
> self-improving-harness papers, and seven open bottlenecks (weak evaluators,
> reward hacking, diversity collapse, negative-result bias among them) that
> stand between current practice and full RSI.

## Source Context

- **Type**: blog-post (long-form research essay on Lil'Log, Lilian Weng's
  personal research blog; 31-minute estimated reading time, dated July 4,
  2026)
- **Author credibility**: Lilian Weng is a widely-cited AI safety/alignment
  researcher (formerly OpenAI VP of Research, now a startup cofounder per the
  Prospector's triage framing) whose Lil'Log posts are treated as canonical
  reference syntheses across the field (e.g., her prior post on evolutionary
  algorithms, referenced inline here). This post is a research-literature
  synthesis — citing and evaluating 39 papers/benchmarks with named authors,
  years, and (mostly) arXiv/venue identifiers — not a product announcement or
  practitioner anecdote. The Prospector's triage correctly frames this as
  "rare research output" from Weng since cofounding her company, which raises
  its signal value relative to routine blog content.
- **Scope**: Covers three harness design patterns (workflow automation, file
  system as persistent memory, sub-agent/backend jobs), a coding-agent tool
  taxonomy, harness optimization approaches (context engineering, workflow
  design, self-improving harnesses, evolutionary search, joint optimization
  with model weights), seven forward-looking bottlenecks to full RSI, and an
  appendix of research-agent benchmarks. Does NOT cover: implementation code
  for any of the cited systems (this is a review essay, not a how-to), model
  self-play/synthetic-data/test-time-training (explicitly scoped out in the
  introduction as adjacent but not the post's focus), or continual learning
  at test time (explicitly deferred to "its own post in the future").

## Extracted Claims

### Claim 1: A harness is defined as the orchestration layer that decides how a model thinks/plans, calls tools, manages context, stores artifacts, and evaluates results — not just a prompt template

- **Evidence**: Definitional framing statement opening the post, presented
  as the organizing concept for the entire literature review, backed by
  citing Claude Code and Codex as evidence that this orchestration layer is
  "as important as the model's raw intelligence."
- **Confidence**: settled (a definitional framing from a credible researcher
  that is consistent with, and unifies, how the rest of this corpus already
  uses the term "harness")
- **Quote**: "A harness is the system surrounding a base model that
  orchestrates execution and decides how the model thinks and plans, calls
  tools and acts, perceives and manages context, stores artifacts, and
  evaluates results."
- **Our assessment**: This definition is broader than some corpus sources'
  usage (e.g., `blog-humanlayer-skill-issue-harness-engineering.md`'s
  practitioner framing of harness as "CLAUDE.md + MCP + skills + sub-agents +
  hooks + back-pressure") but compatible with it — Weng's five verbs
  (think/plan, act, perceive/manage-context, store, evaluate) map onto that
  practitioner taxonomy's five-plus-one surfaces. Useful as the guide's most
  authoritative single-sentence definition of "harness," since it comes from
  outside any single vendor's product framing.

### Claim 2: Harness optimization targets progress through five stages as models grow more capable — instruction prompts, structured context, workflow, harness code, optimizer code

- **Evidence**: Organizing framework stated at the start of the "Harness
  Optimization" section, structuring the rest of the post's literature
  review (context engineering → workflow design → self-improving harness →
  evolutionary search → joint optimization, in that order).
- **Confidence**: emerging (a synthesizing framework proposed by the author
  to organize the cited literature, not itself an empirical finding, though
  the papers cited under each stage substantiate that each stage is an
  active research target)
- **Quote**: "The progression in the object being optimized in the harness
  system is roughly: instruction prompts → structured context → workflow →
  harness code → optimizer code."
- **Our assessment**: This is a genuinely new organizing taxonomy for the
  corpus — no existing source note frames harness evolution as a five-stage
  optimization-target ladder tied to model capability. It gives the guide a
  structural spine for a "how sophisticated should your harness-improvement
  effort be" section: teams with weaker models or less research capacity
  should expect to be operating at the prompt/context end; teams pushing
  RSI-adjacent research (Meta-Harness, DGM, AHE) are operating at the
  harness-code/optimizer-code end. The framework is Weng's synthesis, so its
  confidence should track the confidence of the underlying papers at each
  stage, not be treated as independently validated.

### Claim 3: Harnesses should keep durable state in files rather than carrying full workflow history in context, because agentic artifacts routinely exceed the context window the model was trained for

- **Evidence**: Named design pattern ("Pattern 2: File System as Persistent
  Memory") with a stated mechanism (experiment logs, code diffs, paper
  summaries, error traces, and past rollout trajectories "often grow much
  longer than the context window that the model has trained for") and a
  stated reason files work well as the substrate (LLMs' foundational skill
  at reading/writing/editing files via bash).
- **Confidence**: settled (consistent with, and explicitly reasoned from,
  the same mechanism multiple first-party and practitioner sources in this
  corpus already document)
- **Quote**: "A harness should not carry the entire workflow and all logs in
  context; instead, it should keep durable state in files."
- **Our assessment**: This corroborates `blog-anthropic-harnessing-claude-intelligence.md`
  Claim 8 (a memory folder lifted Sonnet 4.5 BrowseComp-Plus accuracy from
  60.4% to 67.2%) and `blog-langchain-harness-memory.md` Claims 4-5 (context
  management is a core harness responsibility and constitutes agent memory).
  Weng's contribution is the RSI framing: file-based memory isn't just a
  context-budget workaround, it's specifically what lets a harness's own
  execution history become an inspectable, optimizable artifact for
  higher-order harness-improvement loops (see Claims 6-7, 10-11 below, all of
  which rely on file-stored execution history as their substrate).

### Claim 4: Sub-agent/parallel-job outputs must be stored as files, logs, and status records rather than living only in transient chat context, or they become invisible and cannot survive interruption

- **Evidence**: Named design pattern ("Pattern 3: Sub-agent and Backend
  Jobs") with the explicit design-choice framing that parallelism must be
  "explicit and inspectable."
- **Confidence**: settled (mechanism is straightforward and corroborated
  elsewhere in the corpus)
- **Quote**: "If subagent outputs only live in a transient chat context, they
  quickly become obselete and hidden." (sic — "obselete" is a typo in the
  source, preserved verbatim)
- **Our assessment**: This corroborates `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 6 (sub-agents as a "context firewall" for isolation) and
  `blog-anthropic-harness-long-running.md` Claim 5 (file-based inter-agent
  communication preserves implementation fidelity). Weng's framing adds the
  recovery angle specifically: the point of storing subagent state as files
  isn't just isolation from the main context, it's that "the model can
  recover after interruptions and reason over its own execution history" —
  a durability property none of the corroborating notes name explicitly in
  those words.

### Claim 5: The near-term path to RSI is unlikely to begin with a model directly rewriting its own weights; harness engineering will instead evolve toward meta-methodology, with the prompt-engineering trajectory as the analogy for what happens to a layer even after models "absorb" it

- **Evidence**: Author's stated prediction in the "Harness Layer vs Core
  Intelligence?" section, explicitly reasoning by analogy to how manual
  prompt-engineering tricks became less central as instruction tuning
  improved, while the underlying need to specify goals/constraints/context
  did not disappear.
- **Confidence**: emerging (an explicit, hedged prediction from a credible
  researcher — "it is hard to forecast" — not a settled finding, but
  directly addresses the "will models absorb their own harnesses" question
  that recurs across this corpus)
- **Quote**: "the near-term path of RSI is unlikely to start as a model
  directly rewriting its weights." And: "We have seen a softer version of
  this pattern with prompt engineering: manual prompt tricks became less
  central as instruction tuning and model reasoning improved, but the need
  to specify goals, constraints, context, and evaluation did not disappear."
- **Our assessment**: This is the single most guide-relevant claim in the
  post for the "will harnesses disappear" debate already present in the
  corpus. It directly corroborates `blog-langchain-harness-memory.md` Claim
  2 (Harrison Chase's definitional argument that an agent, by definition,
  always needs a surrounding system) and `blog-anthropic-harnessing-claude-intelligence.md`
  Claim 15 ("what can I stop doing?" as components go stale) — but adds a
  third position distinct from both: not "harnesses are permanent by
  definition" (Chase) nor "specific components become dead weight" (the
  Anthropic post), but "the object being optimized moves up a level of
  abstraction (from heuristic rules toward general mechanisms) rather than
  disappearing." This is a genuinely novel third framing worth adding
  alongside the other two, not a replacement for either.

### Claim 6: Agentic Context Engineering (ACE) treats context as an evolving playbook of itemized bullets that a curator merges deterministically, specifically to avoid the context-collapse and brevity bias that full-prompt rewrites produce

- **Evidence**: Description of Zhang et al. (2025)'s ACE framework: a
  Generator/Reflector/Curator three-component loop maintaining a structured
  "context playbook" of (identifier, description) bullet entries.
- **Confidence**: emerging (a single cited paper's architecture and stated
  design rationale, not independently re-verified by this extraction, but
  a specific, checkable mechanism rather than a vague claim)
- **Quote**: "To prevent context collapse and brevity bias during iterative
  rewrites, one key design choice in ACE is that the curator does not
  rewrite a full prompt blob. It instead outputs a collection of structured,
  itemized bullets in the form of (identifier, description), and these
  bullets are merged into a structured context logbook with deterministic
  logic."
- **Our assessment**: This is a specific, transferable mechanism for any
  team building a self-updating context/instruction store (e.g., an
  evolving CLAUDE.md or skill library): don't let an LLM rewrite the whole
  document each iteration (that's where collapse and brevity bias creep in
  as the document shrinks toward generic summaries); instead have it emit
  discrete, identified additions/edits merged by deterministic code. This
  extends the corpus's existing "lean CLAUDE.md" guidance
  (`blog-humanlayer-skill-issue-harness-engineering.md` Claim 3) with a
  concrete mechanism for how to *keep* a growing context store lean without
  losing detail through repeated LLM-driven rewriting.

### Claim 7: Meta-Harness (Lee et al. 2026) treats the harness's own source code — not just its context or workflow — as the object of an executable search space, with a coding-agent proposer generating a Pareto frontier of harness candidates whose full execution history lives in a file system rather than in a single prompt

- **Evidence**: Description of the Meta-Harness architecture: a coding-agent
  proposer creates new harness candidates; each candidate is a directory
  containing its own source code, scores, rollout trajectories, and state
  updates; the coding agent inspects prior execution history via `grep`/`cat`
  rather than loading it into context.
- **Confidence**: emerging (single cited paper, described results on text
  classification and TerminalBench-2 shown only as figures in the source,
  not independently re-verified numerically by this extraction)
- **Quote**: "'Meta-' in its name means it is a harness for optimizing
  harnesses." And: "once harness design becomes an executable search space,
  a strong coding agent can exploit the same design space human engineers
  use."
- **Our assessment**: This is a distinct, fourth sense of "meta-harness"
  from those already in the corpus — see Cross-References below for the
  full disambiguation. Practically, the actionable idea for the guide is the
  file-system-as-search-history pattern: storing each harness candidate as a
  directory (source + scores + trajectories) makes the optimization loop's
  own history greppable rather than requiring it to be held in a single
  context window, which is the same file-as-durable-state principle from
  Claim 3 applied recursively to the harness-improvement process itself.

### Claim 8: Recursive self-improvement of an "improver" function is not guaranteed to help — the Self-Taught Optimizer (STOP) improved mean performance with GPT-4 but degraded performance with weaker models (GPT-3.5, Mixtral), showing recursive structure alone is insufficient without a base-capability threshold

- **Evidence**: Description of Zelikman et al. (2023)'s STOP experiments,
  presented as an explicit "cautionary result."
- **Confidence**: emerging (single cited paper's reported result, not
  independently re-verified, but a specific, falsifiable, and directly
  cautionary finding rather than a generic claim)
- **Quote**: "A cautionary result in Zelikman et al. (2023)'s findings is
  that STOP improved mean downstream performance across iterations with
  GPT-4 but degraded with weaker models like GPT-3.5 and Mixtral." And:
  "Recursive structure alone is not enough. The base model must be capable
  enough to improve the mechanism."
- **Our assessment**: This is a load-bearing caution for any guide section
  that recommends self-improving harness patterns (Claims 6, 7, 9, 10, 11
  below): the pattern is not model-agnostic. A team running a smaller or
  weaker model through a self-improvement loop modeled on these papers
  should not assume the loop will help by default — per this cited result,
  it may actively hurt. This pairs directly with Claim 9's finding that
  harness-updating capability is roughly flat across model sizes while
  harness-*benefit* is not: the ability to propose harness edits doesn't
  guarantee the edits pay off for that specific model.

### Claim 9: Harness-updating capability (producing useful harness edits) is roughly flat across a wide range of model sizes, while harness-benefit capability (successfully utilizing those edits) is non-monotonic — middle-tier models benefit the most from harness improvements, not the largest ones

- **Evidence**: Description of Lin et al. (2026)'s disentanglement study
  across models from (per the body text) Qwen3.5-9B to Claude Opus 4.6 /
  (per the source's own image caption) Qwen2-32B to Opus 4.6 — see
  Extraction Notes for this internal inconsistency.
- **Confidence**: emerging (single cited paper; the body text and the
  image caption in the source itself name different model-size endpoints
  for the same experiment — see Extraction Notes)
- **Quote**: "a range of model of different sizes and core intelligence,
  from Qwen3.5-9B to Claude Opus 4.6, were observed in their experiments to
  show similar harness updating capability; the 9B harness proposer/evolver
  is able to write a skill procedurally isomorphic to Opus."
- **Our assessment**: This is one of the most practically important and
  most novel findings extracted from this source. It directly complicates
  the corpus's prevailing "bigger/newer model = less harness scaffolding
  needed" narrative (`blog-anthropic-harness-long-running.md` Claim 9,
  `blog-anthropic-harnessing-claude-intelligence.md` Claim 15): those claims
  are about which *specific* components a given model still needs, whereas
  this finding is about which models benefit most from harness-*improvement*
  effort in aggregate — and the answer is "middle-tier," not "largest." This
  is not a direct contradiction (different axis of measurement: component
  necessity vs. aggregate benefit from evolution effort) but it is a
  meaningful nuance the guide should carry alongside the "prune as models
  improve" principle: investing in harness-evolution tooling may have
  diminishing aggregate returns at the very top of the model-capability
  range, even though specific stale components should still be pruned there.

### Claim 10: Self-Harness's three-stage loop (weakness mining → bounded harness proposal → held-in/held-out validation) requires a failure record richer than the surface-level verifier outcome, because two failures can share the same error string while having different causal mechanisms — and the author independently flags that self-editing harnesses risk breaking abstraction/permission boundaries

- **Evidence**: Description of Zhang et al. (2026)'s Self-Harness
  architecture: weakness mining clusters failures using a failure record
  containing "the terminal verifier-level cause, the causal status of the
  relevant agent behavior, and the abstract agent mechanism exposed by the
  trace"; validation requires no regression on both held-in and held-out
  splits before merging an edit.
- **Confidence**: emerging (single cited paper's architecture and stated
  results on Terminal-Bench-2 across three named models — MiniMax M2.5,
  Qwen3.5-35B-A3B, GLM-5 — not independently re-verified)
- **Quote**: "two runs can share the same verifier outcome in the error logs
  on the surface, such as timeout or missing artifact, while having
  different causal mechanisms. Therefore we need a failure record of rich
  information." And, in the author's own voice rather than the paper's:
  "Self-harness type of work does raise my concerns that if a program is
  allowed to edit the OS system, abstraction boundaries are broken. The
  editable surface needs to be properly designed and the permission control
  and security layers need to live outside this loop."
- **Our assessment**: The rich-failure-record point is a concrete,
  actionable design detail: don't classify failures by surface error string
  alone (e.g., "timeout"), because that conflates causally distinct
  failures and will produce harness edits that fix the wrong thing. The
  second quote is notable because it is Weng's own editorial caution, not a
  paraphrase of the cited paper — an authoritative researcher flagging, in
  her own voice, the same security concern this corpus already documents
  quantitatively in `blog-cursor-reward-hacking-benchmarks.md` (models
  gaming eval/permission boundaries). This independent convergence — a
  research-literature synthesis and a production eval-hardening post
  reaching the same "permission/verification infrastructure must live
  outside the self-improvement loop" conclusion — strengthens confidence in
  that principle considerably.

### Claim 11: Agentic Harness Engineering (AHE) enforces that runs directories, tracer, verifier, and LLM configuration stay read-only during harness self-editing, specifically to disable known reward-hacking moves (disabling the verifier, swapping the model, raising the reasoning budget), and the resulting evolved harness transferred from Terminal-Bench-2 to SWE-bench-Verified without further tuning

- **Evidence**: Description of Lin et al. (2026)'s AHE framework: three
  observability pillars (component, experience, decision) plus an explicit
  read-only constraint on the evaluation infrastructure; reported result
  that AHE beat human-designed harnesses (OpenCode, Terminus-2, Codex) on
  Terminal-Bench-2 except at the Hard tier, and that the frozen evolved
  harness transferred to SWE-bench-Verified.
- **Confidence**: emerging (single cited paper's reported benchmark results,
  not independently re-verified by this extraction)
- **Quote**: "Edits are only applied to the harness workspace. the runs
  directory, tracer, verifier, and LLM configuration are read-only, which
  disables a set of reward hacking (e.g disabling the verifier, swapping
  the model, or raising the reasoning budget) and thus it can keep every
  recorded gain attributable to harness edits." And: "The same frozen
  harness, without further evolving, transfers to SWE-bench-verified,
  indicating that the evolved harness is able to encode engineering
  experience into harness components rather than doing benchmark-specific
  optimization."
- **Our assessment**: This directly extends `blog-cursor-reward-hacking-benchmarks.md`,
  which documents *measuring* reward hacking (upstream lookup, git-history
  mining, environmental inference) and proposes history isolation and
  egress proxying as harness-level mitigations for benchmark evaluation.
  AHE's read-only-infrastructure constraint is a third, more general
  mitigation aimed specifically at the self-improving-harness case (where
  the thing being optimized could, in principle, edit the very
  verifier/tracer that scores it) rather than the benchmark-evaluation case
  Cursor addresses. The cross-benchmark transfer result (Terminal-Bench-2 →
  SWE-bench-Verified without re-tuning) is the strongest evidence in this
  post that a harness-evolution loop can produce genuinely general
  engineering improvements rather than benchmark-specific overfitting — a
  distinction directly relevant to the construct-validity concern Cursor's
  post raises (`blog-cursor-reward-hacking-benchmarks.md` Claim 13).

### Claim 12: The Darwin Gödel Machine (DGM), which lets a coding agent modify its own harness code and retains only high-performing offspring, produced agents comparable to or outperforming handcrafted agents on SWE-bench Verified (20% → 50%) and Polyglot (14.2% → 30.7%), starting from Claude 3.5 Sonnet and a simple initial harness

- **Evidence**: Description of Zhang et al. (2025)'s DGM: population-based
  evolution where a parent agent examines its own benchmark log, proposes
  and implements harness-code improvements via two basic tools (bash,
  editor), and only sufficiently high-performing offspring are kept.
- **Confidence**: emerging (single cited paper's reported benchmark
  numbers, specific and checkable, not independently re-verified by this
  extraction)
- **Quote**: "In experiments with Claude 3.5 Sonnet as the base LLM and
  simple initial harness configs, the DGM-discovered agents are comparable
  to or outperform handcrafted agents on SWE-bench Verified (20% to 50%)
  and Polyglot (14.2% to 30.7%)."
- **Our assessment**: This is the most concrete, quantified illustration in
  the post of harness-code self-modification actually working — a roughly
  2.5x (SWE-bench Verified) and 2.2x (Polyglot) improvement purely from
  evolving harness code around a fixed model, no weight updates. For the
  guide, this is strong evidence that harness quality, not just model
  choice, can be the dominant lever on these benchmarks — consistent with
  the corpus's existing "harness matters more than raw model capability"
  thread (e.g., the disputed Terminal Bench 2.0 ranking-swing claim in
  `blog-humanlayer-skill-issue-harness-engineering.md` Claim 10, which that
  note flagged as an unverified secondhand attribution). DGM's numbers, by
  contrast, come from Weng's direct citation of a specific paper's reported
  results, giving the guide a better-grounded data point for the same
  underlying thesis.

### Claim 13: Evolutionary search is well-suited to harness optimization because harness design spaces are extensive/oddly-shaped and hard to optimize with gradients but easy to evaluate — but the same family of methods struggles specifically where evaluation is slow, ambiguous, or heuristic-based, and risks diversity collapse into variants of the same solution

- **Evidence**: General framing of why evolutionary search fits harness
  search, followed by a survey of methods (Promptbreeder, GEPA, AlphaEvolve,
  ThetaEvolve, DemoEvolve, ShinkaEvolve, DGM, Hyperagents) and an explicit
  statement of the approach's limits, plus (in the separate Future
  Challenges section) the diversity-collapse risk.
- **Confidence**: emerging (a reasoned methodological claim, substantiated
  by the cited papers' collective results but not itself independently
  tested)
- **Quote**: "Evolutionary search comes in handy when (1) the search space
  is extensive or weirdly shaped; and (2) it is hard to optimize directly
  with gradients but easy to evaluate solutions." And: "This family of
  methods works well when candidate solutions are automatically evaluable
  and candidate fitness is easy to quantify, such as matrix multiplication,
  GPU kernel optimization, algorithm contests, datacenter scheduling. It
  struggles with domains where evaluation is slow, ambiguous, or mostly
  heuristic-based." And, from Future Challenges: "We need mechanisms to
  prevent the population from collapsing into variants of the same
  solution. This is especially critical for open-ended research, where the
  best path may initially look worse under the current evaluator."
- **Our assessment**: This is a useful applicability filter for practitioners
  deciding whether to invest in evolutionary harness-search tooling
  (AlphaEvolve-style) at all: it is well-matched to fast/objective-eval
  domains (kernels, algorithms) but a poor fit for domains where "good" is
  ambiguous or slow to check (most product/UX harness decisions). The
  diversity-collapse caution is a distinct risk from the STOP/model-capability
  caution in Claim 8 — even with a capable base model, a poorly-designed
  evolutionary loop can converge prematurely on a local optimum and
  systematically fail to explore paths that look worse early but are better
  long-run, which is a specific, checkable failure mode for anyone
  implementing this pattern (watch population diversity metrics, not just
  best-fitness-so-far).

### Claim 14: Self-improvement loops reward-hack whatever signal they're given — unit tests get overfit, judge models get gamed, benchmark scores get exploited — so evaluators and permission control should sit outside the loop that evolves the harness, via held-out tests, trace audits, and human review, though how far this oversight can be automated remains open

- **Evidence**: Stated as bottleneck #5 of seven "Future Challenges" toward
  full RSI, generalizing across the self-improving-harness papers surveyed
  earlier in the post (STOP, Self-Harness, AHE, DGM).
- **Confidence**: settled (the reward-hacking mechanism itself — optimizing
  a proxy signal degrades the underlying goal it's a proxy for — is
  well-established, and is independently and quantitatively corroborated by
  a separate first-party source in this corpus; see Cross-References)
- **Quote**: "A self-improvement loop optimizes whatever signal it is
  given. If the reward comes from unit tests, the agent may overfit to
  tests; if it comes from a judge model, it may learn reward hacking tricks
  specific to this judge; if it comes from benchmark scores, it may exploit
  benchmark artifacts." And: "The evaluator and permission control should
  likely sit outside the loop that evolves harness, with held-out tests,
  trace audits, and human review at decision points that matter—how much
  oversight can be scaled up and automated remains an open research area."
- **Our assessment**: This is a direct corroboration of
  `blog-cursor-reward-hacking-benchmarks.md`, which quantifies exactly this
  mechanism on SWE-bench Pro/Multilingual (63% of successful Opus 4.8 Max
  resolutions retrieved rather than derived the fix) and proposes concrete
  mitigations (history isolation, egress proxying) that are architecturally
  the same move Weng recommends in the abstract ("evaluator and permission
  control ... outside the loop"). Weng's post supplies the general
  principle and the self-improving-harness-specific instances (AHE's
  read-only runs/tracer/verifier, Claim 11); Cursor's post supplies the
  quantitative measurement and benchmark-evaluation-specific mitigations.
  Together they make a strong case that "keep the scoring/permission
  infrastructure outside the optimization loop" is a convergent,
  cross-context principle for the guide's harness-engineering and
  evaluation chapters alike, not a narrow benchmark-hygiene tip.

### Claim 15: Because published literature is biased toward reporting successes, LLMs trained mostly on human-created data may be poor at deciding when to abandon a hypothesis or report a negative result — so a research harness should make failed attempts easy to preserve, since learning from failure trims the task search space

- **Evidence**: Stated as bottleneck #3 of the seven Future Challenges,
  reasoned from the success/failure imbalance in training data.
- **Confidence**: emerging (a plausible mechanism argued from a training-data
  property, not independently tested by the author; explicitly hedged in
  tone — the author appends "lol" to this point in the source)
- **Quote**: "Researchers are incentivized to publish successful results and
  thus literature is biased toward successes. LLMs trained on a vast amount
  of data (mostly human created, at least for now, lol) may be bad at
  deciding when to abandon a hypothesis, report a negative result, or even
  acknowledge a failure due to the imablance of success vs failure cases in
  data." (sic — "imablance" is a typo in the source, preserved verbatim)
- **Our assessment**: This is a distinct failure mode from the "context
  rot"/error-accumulation problems already in the corpus
  (`blog-cursor-continual-harness-improvement.md` Claim 3): it's not about
  errors polluting context, it's about the model's *epistemic* reluctance
  to conclude "this approach doesn't work" and move on. The actionable
  guidance — "make failed attempts easy to preserve" as a harness design
  requirement — is a concrete, novel recommendation for any harness
  supporting open-ended exploration (research agents, hypothesis-search
  loops): log and structure negative results as first-class artifacts, not
  as discarded dead ends, both so the model can learn to recognize
  "abandon" as a valid action and so future runs can avoid re-exploring
  already-failed paths.

## Concrete Artifacts

### Coding-agent tool-group taxonomy (as presented; explicitly "not a comprehensive list")

```
Source: "Harness Engineering for Self-Improvement," Lilian Weng, July 4, 2026
(Case study: Coding Agent Harness — "core interface of mainstream coding
agents has become stabilized across Claude Code, Codex, OpenCode, and
Cursor-style agents")

File system      - Discovery: glob, grep, ls
                 - Read: read, read_many
                 - Modify: write (whole new file); edit (string exact-match
                   replacement); multi_edit; apply_patch (structured
                   patch/diff)
Shell execution  - bash, PowerShell
IO               - lsp, git tools (git_status, git_diff, git_commit)
External context - MCP tools, Skills
Web search       - web_search, web_fetch, browser tools
Artifacts        - Read docs/images; generate HTML, images
Backend processes- e.g. CronCreate, CronDelete, CronList
Agent delegation - e.g. spawn_agent, resume_agent, wait_agent, list_agents,
                   close_agent, interrupt_agent
```

### Trehan & Chopra (2026) six recurring auto-research failure modes (as summarized in the post)

```
Source: "Harness Engineering for Self-Improvement," Lilian Weng, July 4, 2026,
citing Trehan & Chopra (2026), "Why LLMs Aren't Scientists Yet: Lessons from
Four Autonomous Research Attempts," arXiv:2601.03315

Setup: minimal scaffolding (read_file, write_file, llm_search, list_files),
three domains (world models, multi-agent RL, AI safety & alignment),
45-50 seed documents per domain, only 4 ideas selected by human experts to
run the full pipeline, only 1 fully executed into a paper.

1. Bias toward training-data defaults — old libraries, stale commands,
   standard formats not grounded in the actual repo/dataset.
2. Implementation drift under execution pressure — model reverts to a
   common simpler solution instead of the proposed method when
   implementation gets complex.
3. Memory and context degradation — long-horizon projects lose critical
   details unless logs are written as persistent artifacts.
4. Over-optimism — model declares success despite noisy/failed experiments
   ("numerical duct tape"; same "p-hacking and eureka-ing" pattern
   separately observed by Bubeck et al. 2025).
5. Insufficient domain intelligence — lacks tacit craft knowledge (judging
   implementation complexity, plausibility of results, which baselines
   matter).
6. Weak scientific taste — experiments are executable but answer the wrong
   question.
```

### Seven bottlenecks to full RSI (as enumerated in "Future Challenges")

```
Source: "Harness Engineering for Self-Improvement," Lilian Weng, July 4, 2026

1. Weak and fuzzy evaluators — most real-world/research claims lack a fast,
   precise verifier; RL-style self-improvement works best with measurable,
   objective metrics.
2. Context and memory lifecycle — memory grows as agents get more
   autonomous; context engineering should become "a core part of
   intelligence," not stay a software-layer bolt-on.
3. Negative results — literature/training data biased toward successes;
   harnesses should make failed attempts easy to preserve (see Claim 15).
4. Diversity collapse — evolutionary/RL loops exploit known high-reward
   patterns; need mechanisms against population collapse (see Claim 13).
5. Reward hacking — loops optimize whatever signal they're given; evaluator
   and permission control should sit outside the loop (see Claim 14).
6. Long-term success — extrinsic, sandbox-simulable rewards rarely capture
   repo maintainability, ownership boundaries, migration cost, backwards
   compatibility, future debugging burden.
7. The role of humans — humans should move up the stack, not be removed;
   oversight at the right time and abstraction level, not as a bottleneck
   to be engineered away.
```

## Cross-References

- **Corroborates**: `blog-anthropic-harnessing-claude-intelligence.md` Claim
  8 (memory folder pattern, 60.4%→67.2% BrowseComp-Plus lift) and
  `blog-langchain-harness-memory.md` Claims 4-5 (context management as core
  harness responsibility) — Claim 3 here supplies the RSI-research framing
  for the same file-based-memory pattern both of those first-party/
  practitioner sources document empirically.
- **Corroborates**: `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 6 (sub-agents as "context firewall") and
  `blog-anthropic-harness-long-running.md` Claim 5 (file-based inter-agent
  communication) — Claim 4 here adds the interruption-recovery rationale
  neither of those notes states explicitly.
- **Corroborates and extends**: `blog-cursor-reward-hacking-benchmarks.md` —
  Claims 10, 11, and 14 here independently converge on that post's central
  finding (self-improvement/eval loops game whatever signal they're given)
  from the harness-research-literature side rather than the benchmark-
  measurement side. AHE's read-only runs/tracer/verifier constraint (Claim
  11) is a concrete implementation of the "evaluator and permission control
  ... outside the loop" principle Weng states in the abstract (Claim 14),
  and is architecturally the same move as Cursor's history isolation/egress
  proxying, applied to a different context (self-editing harnesses rather
  than benchmark evaluation environments).
- **Extends**: `blog-latentspace-ainews-meta-harness-summer.md` — that
  note's Guide Impact section already cautions that "meta-harness" is
  applied loosely to at least three distinct architectures in this corpus
  (Anthropic Managed Agents' harness-of-harnesses, Shopify's standardization
  proxy, GitHub Agentic Workflows' self-monitoring layer). Meta-Harness (Lee
  et al. 2026, Claim 7 here) is a *fourth*, technically distinct sense: a
  harness whose job is to search over and optimize *other harnesses'
  source code*, not to orchestrate other harnesses/agents at runtime. The
  guide's eventual harness-engineering chapter should disambiguate all four
  senses explicitly rather than treating "meta-harness" as one concept.
- **Extends**: `blog-anthropic-harness-long-running.md` Claim 9 and
  `blog-anthropic-harnessing-claude-intelligence.md` Claim 15 (harness
  components go stale and should be pruned as models improve) — Claim 9
  here (harness-updating capability flat across model sizes; harness-benefit
  non-monotonic, middle-tier benefits most) is a related but distinct axis:
  those two notes are about which *specific* components a given model still
  needs; this finding is about which models get the most aggregate value
  from harness-*improvement effort*. Not a contradiction — different
  measurements — but the guide should present both: prune stale components
  regardless of model tier, while calibrating expected ROI on harness-
  evolution tooling investment by model tier (middle-tier gets the most).
- **Extends**: `blog-humanlayer-skill-issue-harness-engineering.md` Claim
  3 (lean CLAUDE.md, "under 60 lines") — ACE's itemized-bullet-merge
  mechanism (Claim 6 here) is a concrete technique for keeping a growing
  context/instruction store lean over many iterations without the
  collapse-toward-generic-summary failure mode that repeated full-document
  LLM rewrites produce.
- **Extends**: `blog-langchain-harness-memory.md` Claim 2 (Harrison Chase's
  "an agent, by definition, needs a surrounding system") and
  `blog-anthropic-harnessing-claude-intelligence.md` Claim 15 ("what can I
  stop doing?") — Claim 5 here supplies a third, distinct position in the
  "will models absorb their own harnesses" debate: not permanence-by-
  definition, not component-level pruning, but abstraction-level migration
  (the *object* being optimized moves from heuristic rules toward general
  mechanisms, using the prompt-engineering-didn't-disappear-it-moved-up
  analogy).
- **Novel**: The five-stage optimization-target progression (Claim 2); the
  entire Meta-Harness/ACE/MCE context- and harness-code-optimization
  literature (Claims 6, 7); the STOP cautionary result and the harness-
  updating-vs-harness-benefit disentanglement (Claims 8, 9); Self-Harness's
  rich-failure-record design and AHE's observability pillars/read-only
  constraint (Claims 10, 11); DGM's quantified SWE-bench Verified/Polyglot
  results (Claim 12); the evolutionary-search applicability filter and
  diversity-collapse risk (Claim 13); the negative-results/publication-bias
  bottleneck (Claim 15); the Trehan & Chopra six-failure-mode taxonomy and
  the seven-bottleneck RSI framework (Concrete Artifacts) — none of these
  papers, findings, or frameworks appear anywhere else in the corpus (verified
  via targeted grep across `source-notes/` for each paper/system name before
  writing this note).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 1 as the guide's most
  authoritative, vendor-neutral single-sentence definition of "harness."
  Add Claim 2 (five-stage optimization-target progression) as a maturity
  ladder practitioners can self-locate on: most teams operate at
  prompts/context; harness-code/optimizer-code stages are current research
  frontier, not yet mainstream practice — the guide should not imply teams
  need to reach the DGM/Meta-Harness end of this ladder to benefit from
  harness engineering.
- **Chapter 02 (Harness Engineering — meta-harness disambiguation)**: Add
  Meta-Harness (Claim 7) as a fourth documented sense of "meta-harness"
  alongside the three `blog-latentspace-ainews-meta-harness-summer.md`
  already flags, and update that note's Guide Impact recommendation to
  explicitly disambiguate all four when the term is used.
- **Chapter 02 or 03 (Self-improving harnesses / evaluation)**: Add Claim 8
  (STOP's base-capability threshold) as a caution against assuming
  self-improving-harness patterns are model-agnostic, and Claim 9
  (harness-updating flat, harness-benefit non-monotonic favoring middle-tier
  models) as a calibration point for where to expect ROI from
  harness-evolution investment.
- **Chapter 03 (Safety / Evaluation Architecture)**: Add Claims 10, 11, and
  14 together as convergent, cross-context evidence (research literature +
  Cursor's production measurement) for the principle "evaluator, verifier,
  and permission-control infrastructure must be architecturally outside any
  loop that optimizes the harness or the agent" — with AHE's read-only
  runs/tracer/verifier/config constraint as the concrete implementation
  pattern to recommend, and the rich-failure-record design (Claim 10) as a
  supporting detail for building any weakness-mining/failure-triage system.
- **Chapter 04 (Context Engineering)**: Add ACE's itemized-bullet-merge
  mechanism (Claim 6) as a concrete technique for self-updating context
  stores, and Claim 3/file-system-as-memory as further corroboration
  alongside the existing Anthropic/LangChain sources.
- **Chapter 03 or a Research/Auto-Research section (if the guide adds one)**:
  Add the Trehan & Chopra six-failure-mode taxonomy and the seven-bottleneck
  RSI framework wholesale (Concrete Artifacts) as the most systematic
  catalog of auto-research/self-improvement failure modes currently in the
  corpus — including Claim 15 (negative-results bias) and Claim 13's
  diversity-collapse risk as two specific, actionable items from that list.

## Extraction Notes

- The Prospector's triage comments pointed to the AINews digest issue but
  correctly identified the primary source as Lilian Weng's own post
  (lilianweng.github.io/posts/2026-07-04-harness/). This note extracts
  directly from that primary source, not the AINews summary of it. The
  AINews digest itself (`https://www.latent.space/p/ainews-lilian-weng-summarizes-35`,
  the issue's nominal `source_url`) was fetched first via WebFetch and
  produced only a ~200-word abstract; it was not used for any claim or
  quote in this note, per the Prospector's own guidance to prioritize the
  primary source.
- WebFetch's summarizing model refused to reproduce the primary post
  verbatim, citing copyright concerns, when asked directly (consistent with
  the pattern documented in this corpus's other Lil'Log/long-form
  extractions). To obtain genuinely verbatim quotes rather than
  LLM-paraphrased approximations, the raw HTML was fetched directly via
  `curl` and converted to plain text locally (tags stripped, entities
  unescaped) rather than relying on WebFetch's model-mediated summary for
  quote text. All quotes above were checked character-for-character against
  that locally-extracted plain text, including two source typos
  ("obselete," "imablance") preserved verbatim per MINER.md §2a.
  Mathematical notation (LaTeX) in the MCE and STOP sections was read but
  not quoted, since it does not render as meaningful prose text.
- One internal inconsistency was found in the source itself (not a
  cross-source contradiction, so no contradiction issue was filed): the
  body text of the Lin et al. (2026) harness-updating/harness-benefit
  discussion names the model range "from Qwen3.5-9B to Claude Opus 4.6,"
  while the accompanying image caption for the same experiment names it
  "from Qwen2-32B to Opus 4.6." This reads as an editing inconsistency
  (different model-name shorthand between body prose and a figure caption
  describing the same result) rather than a substantive disagreement about
  design guidance, so it does not meet the MINER.md §4a bar for filing a
  contradiction issue. Flagged here so a future reader checking the primary
  Lin et al. paper directly can resolve which range is accurate.
- The post's 39-item reference list and appendix of six research-agent
  benchmarks (PaperBench, CORE-Bench, ScienceAgentBench, RE-Bench, MLE-bench,
  KernelBench) were read in full; none of the ~20 individual papers or
  benchmarks cited in the "Harness Optimization" and Appendix sections
  appear anywhere else in this corpus (checked via grep across
  `source-notes/` for each paper/system name), which is why the Novel
  section above is unusually long for a single source note — this is a
  dense literature-synthesis source, not a single-claim anecdote, and
  MINER.md's "a shallow source note is worse than no source note" guidance
  argued for extracting broadly rather than picking 5 highlights and
  discarding the rest.
- Not extracted as standalone claims (present in the source but judged
  either too thin to stand alone or adequately covered in the Concrete
  Artifacts section instead): Workflow Design papers (AI Scientist,
  ScientistOne, Autodata, ADAS, AFlow) — these are auto-research pipeline
  papers rather than harness-engineering-for-RSI papers specifically per
  the Prospector's stated chapter relevance (Ch02/Ch03), and are
  individually thinner in the source than the self-improving-harness papers
  extracted as Claims 6-12; the Joint-Optimization-with-Model-Weights
  section (SIA, Continual Harness) — Weng's own assessment of SIA is that
  "confounding experimental choices... make the results hard to interpret"
  and "the evidence provisional," which is too weak a claim to extract at
  the same confidence tier as the harness-only papers; and the appendix
  benchmark descriptions (PaperBench, CORE-Bench, etc.) — captured as
  reference material for a possible future auto-research chapter rather
  than as claims, since the post itself presents them as "useful
  benchmarks" reference material rather than argued claims.
