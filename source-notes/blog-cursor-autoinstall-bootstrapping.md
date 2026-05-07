---
source_url: https://cursor.com/blog/bootstrapping-composer-with-autoinstall
source_type: blog-post
title: "Bootstrapping Composer with autoinstall"
author: "Shomil Jain, Joshua Warner & Andrew Zhai (Cursor Research)"
date_published: 2026-05-06
date_extracted: 2026-05-07
last_checked: 2026-05-07
status: current
confidence_overall: emerging
issue: "#551"
---

# Bootstrapping Composer with autoinstall (Cursor Research)

> Cursor introduces the "autoinstall" pattern — using an earlier Composer model
> version to automatically configure working RL training environments from raw
> repository checkouts — demonstrating that broken training environments waste
> compute and degrade reward signal quality, and that the self-bootstrapping
> cycle (each Composer trains the next) is now an operational reality.

## Source Context

- **Type**: blog-post (Cursor Research, May 6, 2026; 6-minute read; three named
  authors from the Cursor engineering team)
- **Author credibility**: Shomil Jain, Joshua Warner, and Andrew Zhai are Cursor
  Research engineers writing about a production system they operate. This is a
  first-party description of the mechanism used to prepare RL training environments
  for Composer 2. As with other Cursor engineering posts, there is a commercial
  incentive to present favorably, but the technical specificity — named stages,
  retry counts, validation criteria, concrete repo example, quantitative Terminal-Bench
  results — is consistent with genuine engineering documentation. The Terminal-Bench
  numbers (61.7% vs 47.9%) are independently consistent with those reported in
  `blog-cursor-composer2-technical-report.md`.
- **Scope**: Covers the design and implementation of autoinstall — the environment
  bootstrapping system used to prepare Composer 2 training environments — including
  the two-stage process, validation logic, complex dependency mocking, and Terminal-Bench
  performance evidence. Does NOT cover: the broader RL training pipeline architecture
  (covered in `blog-cursor-real-time-rl.md`), model architecture or pretraining
  (`blog-cursor-composer2-technical-report.md`), or harness monitoring and improvement
  (`blog-cursor-continual-harness-improvement.md`). Does NOT include implementation
  code, environment count, or total compute savings from autoinstall.

## Extracted Claims

### Claim 1: Broken RL training environments waste compute and degrade learning signal — the model debugs setup instead of solving problems

- **Evidence**: Direct authorial statement of the core motivation for building
  autoinstall. Two quotes capture the problem from different angles.
- **Confidence**: emerging (first-party operational observation; mechanism is
  theoretically sound — an agent stuck configuring its environment cannot receive
  reward signal for the actual task)
- **Quote**: "if the environment is broken at the start, the model wastes tokens
  debugging setup instead of learning to solve problems"
- **Our assessment**: This is the foundational claim that motivates the entire post.
  The mechanism is clear: in RL training, the agent must take actions in an environment
  to receive reward. If the environment is broken (missing dependencies, unconfigured
  test runners, broken build toolchains), every rollout starts with debugging, not with
  the task the model is being trained on. The wasted compute is real: "The failure to
  correctly set up the environment makes training inefficient and can waste compute for
  no reward signal." For practitioners building RL training pipelines for coding agents:
  environment quality is not a secondary concern — it is a prerequisite for the reward
  signal to be meaningful.

### Claim 2: Autoinstall uses earlier Composer model versions to create working RL training environments from unconfigured repository checkouts

- **Evidence**: The autoinstall system is defined explicitly. The Composer 1.5 → Composer 2
  relationship is described as the specific production instantiation.
- **Confidence**: emerging (first-party description of a production system; the
  mechanism is clearly defined; no third-party verification of the claimed scope)
- **Quote**: "a system that uses earlier Composer models to automatically create working
  RL environments from unconfigured repository checkouts"
- **Our assessment**: This is the core architectural claim. "Autoinstall" is not a generic
  term for automated installation — it is a specific Cursor system where the previous
  model generation is used as the bootstrapping agent for the next generation's training
  environments. "During training of the most recent version of the model, Composer 2, we
  used its predecessor, Composer 1.5, to manage this process." This operationalizes the
  future-looking statement in `blog-cursor-composer2-technical-report.md` which anticipated
  that "previous Composer instances will play a large role in many other aspects of the
  training process." The autoinstall post confirms this is now operational, at least for
  environment setup. The transferable principle for practitioners: agent systems that reach
  sufficient capability can be turned back on the training pipeline to improve the next
  generation — not just a research direction, but a deployed practice.

### Claim 3: The autoinstall two-stage process separates goal-setting from execution using two different agent instances

- **Evidence**: The two stages are described explicitly with distinct agent roles. Stage 1
  (goal-setting) uses one agent; Stage 2 (execution) uses a separate agent.
- **Confidence**: emerging (mechanism described in operational detail; the two-agent
  separation is explicit)
- **Quote (Stage 1)**: "we give the Cursor agent the codebase at a fixed checkout and ask
  it to propose 10 commands and a high-level description of the output that should run if
  the environment were correctly set up"
- **Our assessment**: Stage 1 produces a contract: 10 candidate setup commands plus an
  expected output description. Stage 2 takes three of those commands as targets and attempts
  to execute them. The separation of goal-setting and execution into two agent instances
  mirrors the generator/evaluator split described in `blog-anthropic-harness-long-running.md`
  — one agent specifies the success criteria, another tries to meet them. The two-agent
  design may also reduce mode collapse: the goal-setting agent doesn't know which three
  of its ten commands will be selected for execution, preventing the executor from "gaming"
  by proposing trivially easy targets.

### Claim 4: Stage 2 (execution) selects three of the ten proposed commands and validates the environment against the Stage 1 expected output; after five failed retries the environment is discarded

- **Evidence**: The execution phase and discard policy are described explicitly.
- **Confidence**: emerging (operational procedure described; specific retry count is
  defined)
- **Quote (execution)**: "we provide a separate Composer agent with the initial state of
  the environment as well as three target commands selected from the proposed 10"
- **Quote (validation)**: "we test that all three commands run and that the output matches
  the target description from the first agent"
- **Quote (discard policy)**: "If, after five repetitions of this process, the agent has
  not been able to set up the environment to a satisfactory degree, we discard the
  environment"
- **Our assessment**: The discard policy is a quality filter: environments that cannot be
  configured after five attempts are excluded from the training pool rather than contributing
  broken signal. Five retries is a meaningful budget — it allows the agent to learn from
  partial failures within a rollout without committing infinite compute to intractable
  environments. The validation mechanism (all three commands run + output matches expected
  description) creates a functional test that verifies the environment is genuinely working
  at the level the goal-setting agent specified, not just that installation steps completed.

### Claim 5: The autoinstall agent handles complex dependency scenarios by mocking missing components — fake database tables, placeholder images, MinIO configs for S3 folders, Docker containers for sidecars

- **Evidence**: Multiple categories of mocking behavior are described explicitly. The Celo
  blockchain project is the named real-world example demonstrating complex auth flow mocking.
- **Confidence**: emerging (first-party description of observed capabilities; the Celo
  example provides concrete corroboration)
- **Quote (mocking)**: "it will mock missing files, create placeholder images, or even
  create fake database tables"
- **Quote (sidecar mocking)**: "Some projects require installing additional components that
  are needed to run tests, such as S3 folders or missing sidecar containers. Composer often
  mocks these as well, creating MinIO configs or Docker containers to get these to work."
- **Our assessment**: The breadth of mocking behavior is notable. Mock strategies span:
  filesystem (missing files, placeholder images), data storage (fake DB tables), cloud
  services (MinIO for S3), and container infrastructure (Docker containers for sidecar
  services). This is not lightweight test-fixture mocking — it is full-stack environment
  emulation. For practitioners who build RL training environments: the scope of mocking
  required to make real-world repositories trainable is substantially larger than
  installing listed dependencies. Authentication flows, cloud service integrations, and
  missing binaries may all require bespoke mocking strategies.

### Claim 6: The Celo blockchain monorepo (celo-org/celo-monorepo) demonstrates autoinstall handling sparse documentation, multi-dependency management, and authentication flow mocking

- **Evidence**: The Celo example is described as the concrete case study, with specific
  challenges identified.
- **Confidence**: emerging (specific project cited with named challenges; demonstrates
  the system's capability on a real-world complex case)
- **Quote**: "celo-org/celo-monorepo...is a large blockchain project with several major
  dependencies"
- **Quote (specific challenge)**: "it requires managing a large set of dependencies for
  install and then mocking an authentication flow for testing"
- **Our assessment**: The Celo case is the most concrete evidence in the post that
  autoinstall handles non-trivial repositories. Blockchain monorepos are among the harder
  environment setup challenges: multiple language runtimes, cryptographic toolchains (here
  Foundry is mentioned), complex interdependencies, and test infrastructure that assumes
  live network authentication. The fact that autoinstall succeeds on Celo validates the
  mocking claims in Claim 5 — this is not a system that only works on simple projects
  with standard package managers.

### Claim 7: Environment quality is foundational to training with a full tool set — lint commands, search, and sandboxed shell all require working environments

- **Evidence**: The authors explain why broken environments are specifically harmful for
  Composer's RL training, given the full tool set Composer is trained with.
- **Confidence**: emerging (first-party explanation of the specific training requirements;
  the tool list is named explicitly)
- **Quote**: "This base environment is critical because Composer is trained with a full
  set of tools, including programming language lint commands, search, and sandboxed use
  of shell."
- **Our assessment**: This claim explains why environment setup is more important for
  Composer specifically than for agents with limited tool access. When the model is trained
  to use language-specific linters, file search, and shell execution, all of those tools
  require a working environment to produce meaningful reward signal. A model that can't
  lint because the linter isn't installed, or can't run tests because the test framework
  is misconfigured, cannot learn the correct use of those tools. "Better environments mean
  better training signal." This generalizes: the more tools an agent is trained to use,
  the more critical environment completeness becomes.

### Claim 8: Composer 2 scores 61.7% on Terminal-Bench vs. Composer 1.5's 47.9%, on a benchmark that specifically tests environment setup capability

- **Evidence**: Explicit performance comparison with named benchmark context. Terminal-Bench
  is described as measuring environment setup ability specifically.
- **Confidence**: emerging (first-party numbers, consistent with those reported in
  `blog-cursor-composer2-technical-report.md`; the Terminal-Bench specifics reinforce the
  connection between autoinstall quality and measured performance)
- **Quote**: "Composer 2 now scores significantly higher on Terminal-Bench (61.7% versus
  47.9% for Composer 1.5)"
- **Quote (benchmark description)**: "Terminal-Bench, a benchmark that includes tests of
  a model's ability to set up developer environments."
- **Our assessment**: The Terminal-Bench selection is notable. The authors chose this
  specific benchmark to validate autoinstall's contribution, not CursorBench. Terminal-Bench
  directly measures environment setup capability — the exact task autoinstall automates.
  The 13.8 percentage-point improvement (47.9% → 61.7%) on this benchmark is the strongest
  evidence that autoinstall meaningfully improves Composer's capability in the domain it
  was designed to serve. The causal inference is partial (other training improvements also
  contributed to Composer 2's gains), but the choice of benchmark is deliberate evidence
  alignment. For practitioners: if you are training agents on environment setup tasks,
  measuring performance on environment setup benchmarks validates whether your training
  environments are actually teaching the capability.

### Claim 9: The autoinstall bootstrapping pattern creates a self-improving cycle — each Composer generation improves the quality of environments for the next

- **Evidence**: Authors explicitly describe the generational improvement and future
  extension of the pattern.
- **Confidence**: anecdotal (the claim about Composer 2 improving autoinstall quality
  is forward-looking; no quantitative comparison between Composer 1.5-generated and
  Composer 2-generated environments is provided)
- **Quote**: "This indicates that Composer 2 will provide an improved base for autoinstall"
- **Quote (broader vision)**: "previous Composer instances will play a large role in many
  other aspects of the training process, including run management, data preprocessing, and
  architecture tuning"
- **Our assessment**: The self-improvement cycle is presented as an emergent property of
  the bootstrapping design: if Composer 2 is better at environment setup than Composer 1.5
  (as Terminal-Bench demonstrates), then Composer 2 should generate higher-quality training
  environments for Composer 3. The broader vision — past models contributing to run
  management, data preprocessing, and architecture tuning — suggests that Cursor intends
  to expand this pattern beyond environment bootstrapping. This is the practitioner-facing
  version of the "model-assisted training" principle: the agent system is not just the
  product, it is also a tool in the training pipeline. Teams building iterative agent
  systems should consider whether their current generation can contribute to improving
  the next generation's training data quality.

## Concrete Artifacts

### Autoinstall Two-Stage Process

```
# Cursor autoinstall environment bootstrapping (May 2026)
# Source: "Bootstrapping Composer with autoinstall"
# Authors: Shomil Jain, Joshua Warner & Andrew Zhai (Cursor Research)

STAGE 1: GOAL SETTING
  Agent:  Earlier Composer model (Composer 1.5 for Composer 2 training)
  Input:  Codebase at fixed checkout (unconfigured repository)
  Output: 10 proposed setup commands + high-level description of expected
          environment state if correctly configured
  Quote:  "ask it to propose 10 commands and a high-level description of the
          output that should run if the environment were correctly set up"

STAGE 2: EXECUTION
  Agent:  Separate Composer agent instance
  Input:  Initial environment state + 3 target commands selected from Stage 1's 10
  Goal:   Configure the environment until all 3 target commands succeed and output
          matches Stage 1's expected description
  Retries: Up to 5 repetitions; discard environment if still unsatisfactory

VALIDATION CRITERIA
  - All three target commands must run successfully
  - Command output must match target description from Stage 1
  Quote: "we test that all three commands run and that the output matches the
         target description from the first agent"

DISCARD POLICY
  - After 5 failed repetitions: environment discarded from training pool
  Quote: "If, after five repetitions of this process, the agent has not been able
         to set up the environment to a satisfactory degree, we discard the environment"
```

### Environment Mocking Capabilities

```
# Autoinstall environment mocking patterns (Cursor, May 2026)
# Source: "Bootstrapping Composer with autoinstall"

FILESYSTEM MOCKING
  - Mock missing files
  - Create placeholder images

DATA STORAGE MOCKING
  - Create fake database tables

CLOUD SERVICE MOCKING
  - Create MinIO configurations (for S3 folder dependencies)
  Quote: "Some projects require installing additional components that are needed
         to run tests, such as S3 folders or missing sidecar containers."

CONTAINER MOCKING
  - Deploy Docker containers for missing sidecar services
  Quote: "Composer often mocks these as well, creating MinIO configs or Docker
         containers to get these to work."

AUTHENTICATION MOCKING
  - Mock authentication flows for testing (demonstrated on Celo blockchain project)
  Quote: "it requires managing a large set of dependencies for install and then
         mocking an authentication flow for testing"
```

### Terminal-Bench Performance

```
# Terminal-Bench results (Cursor Research, May 2026)
# Source: "Bootstrapping Composer with autoinstall"

                    Terminal-Bench
Composer 2            61.7%
Composer 1.5          47.9%
Delta                 +13.8 pp

Terminal-Bench: "a benchmark that includes tests of a model's ability to set up
developer environments" — directly measures the capability autoinstall trains.

Note: The same numbers appear in blog-cursor-composer2-technical-report.md (Claim 4).
This post attributes the Terminal-Bench improvement specifically to autoinstall's
role in improving environment quality during Composer 2 training.
```

## Cross-References

- **Corroborates**: `blog-cursor-composer2-technical-report.md` Claim 2 — that note states
  "RL training uses realistic Cursor sessions with the same tools and harness the deployed
  model uses" as the core design principle for Composer 2. The autoinstall post is the
  concrete mechanism for making that principle achievable: broken environments would
  violate the production-identical fidelity that Claim 2 describes. Autoinstall is the
  upstream system that enforces environment fidelity before RL training begins.

- **Corroborates**: `blog-cursor-composer2-technical-report.md` Claim 4 — the Terminal-Bench
  numbers (61.7% vs 47.9%) are cited in both sources. The technical report presents them as
  part of the overall Composer 2 benchmark results; this post contextualizes them as evidence
  of autoinstall's specific contribution to environment-setup capability.

- **Extends**: `blog-cursor-composer2-technical-report.md` — the technical report contains
  a forward-looking statement that "we anticipate in future runs, previous Composer instances
  will play a large role in many other aspects of the training process." This post is the
  concrete operational implementation of that anticipation for environment bootstrapping,
  published approximately five weeks after the technical report. It demonstrates that the
  anticipated self-bootstrapping pattern is operational, not just projected.

- **Extends**: `blog-cursor-real-time-rl.md` — that post describes the 5-hour RL checkpoint
  cycle (data collection → reward computation → weight update → CursorBench gate → deploy)
  but does not detail how training environments are prepared. Autoinstall is the upstream
  environment preparation step that enables the RL pipeline described in that post to operate
  on working environments. Together, the two posts describe the full RL preparation stack:
  autoinstall (environment setup) → real-time RL (training on working environments) →
  CursorBench gate → deploy.

- **Extends**: `blog-anthropic-harness-long-running.md` — that note's Claim 2 establishes
  environment fidelity as a "first-class design principle" in the abstract. The autoinstall
  post is the concrete production implementation of this principle in Cursor's RL pipeline,
  and extends it with a specific mechanism for enforcing fidelity at scale (automated
  bootstrapping + validation + discard policy).

- **Novel**: The following patterns are new to the corpus:
  - **Two-stage bootstrapping for RL training environments** — goal-setting agent proposes
    targets, execution agent implements them; the two-agent separation prevents the executor
    from trivializing targets. No other source describes this pattern.
  - **Past model bootstrapping current model's training environments** as a named,
    deployed operational pattern — "autoinstall" as a specific system is novel; the
    technical report anticipated it but did not describe it mechanistically.
  - **Validate-and-discard quality filter for training environments** — 5-retry limit
    with explicit discard of intractable environments is a specific engineering discipline
    not described elsewhere in the corpus.
  - **Full-stack environment mocking for RL** — mocking DB tables, MinIO/S3 configs,
    Docker sidecar containers, and auth flows as prerequisites for training signal quality
    is not described in any other source note.
  - **Self-improving bootstrapping cycle as an operational pattern** — the generational
    improvement (each Composer improves the next's environments) is described as a deployed
    reality, not just a design goal.

## Guide Impact

- **Chapter 02 (Harness Engineering — RL training environment quality)**: Add autoinstall
  as the canonical example of making environment quality a first-class RL training concern.
  Cite Claim 1 as the foundational motivation ("broken environments waste compute for no
  reward signal") and Claims 3-5 as the concrete implementation pattern (two-stage
  bootstrapping, validate against expected output, discard-after-5). This is the most
  specific public description of RL training environment preparation in our corpus —
  existing sources state the principle (train in production-identical environments) but
  do not explain how to achieve it operationally.

- **Chapter 02 (Harness Engineering — bootstrapping with previous model versions)**:
  Add the "use past model to bootstrap current training" pattern as a specific harness
  design principle for teams building iterative agent training pipelines. Cite Claim 2
  and Claim 9: once an agent model reaches sufficient capability, the previous generation
  can contribute to the next generation's training data quality. This is an operational
  form of curriculum generation that does not require human-crafted examples.

- **Chapter 02 (Harness Engineering — tool-aware environment requirements)**: Cite
  Claim 7 alongside `blog-cursor-composer2-technical-report.md` Claim 2 as converging
  evidence that training with a full tool set imposes strong constraints on environment
  completeness. The more tools an agent uses, the more carefully its training environments
  must be configured. The Celo example (Claim 6) shows the extent of mocking required
  for a real-world project.

- **Chapter 03 (Safety and Verification — training environment fidelity as eval design)**:
  The validate-and-discard approach (Claim 4) is a quality assurance pattern applicable
  beyond RL training: any automated environment setup workflow should validate outcomes
  against expected criteria and discard rather than proceed on broken setups. The
  "output matches expected description" validation criterion is a lightweight functional
  test that applies to harness setup in general.

## Extraction Notes

- Blog post read in full via WebFetch. The tool provided partial summaries on initial
  requests; verbatim quotes were extracted via targeted follow-up prompts. All quotes
  in this note are verified against source page responses before inclusion.
- The post does not specify how the three commands are selected from the ten proposed
  by Stage 1 (random selection, quality heuristic, or human curation is not stated).
- The post does not provide the total number of environments processed by autoinstall
  or what fraction pass the 5-retry validation threshold.
- The post does not specify whether autoinstall is run on a curated set of repositories
  or the full universe of public repositories. The Celo project example suggests real-world
  projects are used, but selection criteria are not described.
- No contradictions to file: all claims are additive to existing corpus content. The
  Terminal-Bench numbers (61.7% vs 47.9%) are consistent with `blog-cursor-composer2-technical-report.md`
  (Claim 4). The "previous instances will play a large role" statement in the technical
  report is now operationalized rather than contradicted.
