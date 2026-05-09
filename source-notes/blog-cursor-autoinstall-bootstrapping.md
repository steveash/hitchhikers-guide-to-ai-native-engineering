---
source_url: https://cursor.com/blog/bootstrapping-composer-with-autoinstall
source_type: blog-post
title: "Bootstrapping Composer with Autoinstall"
author: "Shomil Jain, Joshua Warner & Andrew Zhai (Cursor Research)"
date_published: 2026-05-06
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: emerging
issue: "#551"
---

# Bootstrapping Composer with Autoinstall (Cursor Research)

> Cursor's account of how earlier Composer model versions automatically bootstrap
> production-quality RL training environments — a two-stage goal-setter/executor system
> that eliminates broken-environment compute waste and achieves 61.7% on Terminal-Bench
> (vs. 47.9% for Composer 1.5).

## Source Context

- **Type**: blog-post (Cursor Research, published May 6, 2026; 6-minute read; three named
  authors — Shomil Jain, Joshua Warner, and Andrew Zhai from Cursor Research)
- **Author credibility**: First-party Cursor Research account describing a production
  system they built and deployed for training Composer 2. The post is operational, not
  marketing: it describes concrete implementation details (stage counts, retry limits,
  mocking strategies, benchmark numbers). Commercial incentive to present favorably is
  real, but the technical specificity and matching of Terminal-Bench numbers with the
  independently extracted Composer 2 technical report (issue #194) are consistent with
  genuine engineering documentation. Treat as emerging: directionally reliable for named
  patterns.
- **Scope**: Covers the motivation for autoinstall (broken environments waste RL compute),
  the two-stage goal-setter/executor architecture, the discard-after-five-retries quality
  filter, full-stack mocking capabilities, a concrete Celo blockchain example, Terminal-Bench
  validation, and a forward-looking extension of the bootstrapping pattern. Does NOT cover
  the broader Composer 2 training recipe (model selection, RL algorithm, pretraining) — those
  are in `blog-cursor-composer2-technical-report.md`. Does NOT describe the implementation
  language, infrastructure, or code for the autoinstall system.

## Extracted Claims

### Claim 1: Broken training environments waste RL compute by forcing the model to debug setup instead of learning problem-solving skills

- **Evidence**: Direct statement from the authors as the motivating problem: models cannot
  receive meaningful reward signal if the environment is unusable from the start.
- **Confidence**: emerging (first-party statement of a training-efficiency principle; the
  mechanism is theoretically sound, though the quantitative waste is not measured)
- **Quote**: "if the environment is broken at the start, the model wastes tokens debugging
  setup instead of learning to solve problems"
- **Our assessment**: This is the foundational claim for the entire autoinstall system. The
  framing matters: environment quality is not a preprocessing concern — it is a reward
  engineering concern. A broken environment does not produce zero reward; it produces
  misleading negative reward (the model is penalized for setup failures rather than task
  failures). For practitioners building RL-trained agents: invest in environment fidelity
  as a first-class training objective, not an afterthought.

### Claim 2: Autoinstall is a system that uses earlier Composer model versions to automatically create working RL training environments from unconfigured repository checkouts

- **Evidence**: Direct definition from the authors. Composer 1.5 specifically managed the
  autoinstall process during Composer 2's training — making this a deployed, operational
  system, not a design proposal.
- **Confidence**: emerging (first-party operational account; the system is described as
  deployed for Composer 2 training)
- **Quote**: "a system that uses earlier Composer models to automatically create working
  RL environments from unconfigured repository checkouts"
- **Our assessment**: The key design insight is that an existing capable model can
  bootstrap a better model's training environment. This is a concrete operationalization
  of the "use the model to improve itself" loop that is often discussed abstractly. The
  self-referential bootstrapping — Composer 1.5 preparing Composer 2's training ground —
  makes this a named, deployable pattern, not just a principle.

### Claim 3: Stage One (goal setting) has a Cursor agent propose 10 setup commands with expected output descriptions, exploring readmes, makefiles, and language-specific tools

- **Evidence**: Explicit description of the first stage's input, output, and exploration
  strategy — concrete enough to reproduce.
- **Confidence**: emerging (first-party operational description; specific enough to be a
  real design, not marketing abstraction)
- **Quote**: "we give the Cursor agent the codebase at a fixed checkout and ask it to
  propose 10 commands and a high-level description of the output that should run if the
  environment were correctly set up"
- **Our assessment**: The goal-setting stage is a specification-generation step: instead
  of asking the agent to "set up the environment," you ask it to first define what a
  correctly configured environment looks like. This separates planning from execution and
  produces a verifiable specification. The exploration strategy (readmes, makefiles, uv,
  clippy) shows that the goal-setter is domain-aware, not generic. Practitioners designing
  multi-agent environment-setup pipelines should consider separating the "what does done
  look like?" step from the "make it done" step.

### Claim 4: Stage One agents explore readmes, makefiles, and language-specific tooling (e.g., uv for Python, clippy for Rust) to identify setup commands

- **Evidence**: Explicit list of exploration strategies from the post.
- **Confidence**: emerging (first-party operational detail)
- **Quote**: "The agent will explore any readme or makefiles for the environment, as well
  as try typical language-specific commands such as project managers like uv or linters
  like clippy."
- **Our assessment**: The named tooling (uv, clippy) makes this concrete: the goal-setter
  is not running generic "find setup commands" logic — it is reasoning about the language
  and framework of the codebase. This is ecosystem-aware setup detection. The implication
  for practitioners: automated environment setup agents need to be prompted or fine-tuned
  with awareness of the target language's toolchain conventions.

### Claim 5: Stage Two (execution) uses a separate Composer agent to implement the environment against three of the ten proposed targets, with success validated by running the commands and matching outputs

- **Evidence**: Explicit description of the second stage's input (three selected target
  commands from the first agent's ten), process (explore and configure the environment),
  and validation (commands must run AND output must match the target description).
- **Confidence**: emerging (first-party operational description)
- **Quote**: "we provide a separate Composer agent with the initial state of the environment
  as well as three target commands selected from the proposed 10. The agent will then
  explore the codebase, calling tool calls to get the environment set up so that the
  commands can run."
- **Our assessment**: The two-stage separation is the key architectural decision: the agent
  that proposes success criteria is different from the agent that implements them. This
  prevents the executor from gaming its own success criteria. The dual validation (commands
  run AND output matches description) is a two-signal check: syntactic success (commands
  execute without error) plus semantic success (output matches expected description). This
  is a stronger quality bar than just "the command exits 0."

### Claim 6: Environments that fail setup after five execution attempts are discarded entirely

- **Evidence**: Explicit discard threshold stated in the post.
- **Confidence**: emerging (first-party operational parameter; specific enough to be a real
  engineering threshold, not an estimate)
- **Quote**: "If, after five repetitions of this process, the agent has not been able to set
  up the environment to a satisfactory degree, we discard the environment."
- **Our assessment**: The five-retry discard rule is a quality filter: the training corpus
  only contains environments the execution agent successfully configured. This means
  autoinstall is a selective, not exhaustive, process — some repositories are too hard to
  automate and are simply excluded from training. For practitioners: quality-filter your
  training environments rather than accepting all setups with degraded quality. A stricter
  quality bar on training inputs is preferable to noisy training signal from marginal setups.

### Claim 7: Composer handles complex project dependencies through full-stack mocking including fake database tables, MinIO configs, Docker containers, and placeholder files

- **Evidence**: Explicit enumeration of mocking capabilities — fake DB tables, placeholder
  images, MinIO/S3 mock configs, Docker sidecar containers, and startup scripts for
  long-running services.
- **Confidence**: emerging (first-party capability list; corroborated by the Celo example
  in the same post)
- **Quote (mocking files and tables)**: "it will mock missing files, create placeholder
  images, or even create fake database tables"
- **Quote (cloud services and containers)**: "Composer often mocks these as well, creating
  MinIO configs or Docker containers to get these to work."
- **Our assessment**: The breadth of mocking capability is striking: this is not "create a
  stub file" but full-stack infrastructure simulation. MinIO for S3-compatible object
  storage and Docker for sidecar services means the agent can configure a plausible
  development environment for projects with external service dependencies. For teams building
  agent training environments: the mocking breadth needed for real-world repos extends far
  beyond file stubs into infrastructure services.

### Claim 8: Autoinstall draws direct inspiration from Cursor's production cloud agent feature that automates environment setup for users

- **Evidence**: Explicit statement of inspiration from the post.
- **Confidence**: emerging (first-party attribution of design lineage)
- **Quote**: "Like many aspects of our model development, autoinstall is inspired by
  production Cursor systems."
- **Quote (cloud agents)**: "In Cursor cloud agents, we have a feature that automates the
  setup of cloud environments for users, to allow their agents to work on projects in a
  mock environment."
- **Our assessment**: This is a notable pattern: production user-facing features directly
  inform model training infrastructure. The cloud agent environment setup (a product feature)
  became the template for training environment setup (a research infrastructure component).
  This bidirectional transfer — product → training → better product — is a structural
  advantage for teams that deploy both research and product simultaneously.

### Claim 9: The Celo blockchain monorepo required multi-dependency install plus authentication flow mocking, solved by the agent using web search to find sparse documentation and iterating to create a mock user

- **Evidence**: Detailed case study within the post: Stage 1 used web commands to search the
  project's documentation site; Stage 2 failed on iteration 1 and succeeded on iteration 2
  by creating a mock user.
- **Confidence**: anecdotal (single real-world example from the authors; illustrative but not
  statistical)
- **Quote (project requirement)**: "requires managing a large set of dependencies for install
  and then mocking an authentication flow for testing"
- **Quote (Stage 1 web search)**: "it also used web commands to search the project's
  documentation site for further setup commands"
- **Quote (Stage 2 iteration 2)**: "on a second iteration it found that it could create a
  mock user to start the application locally and satisfy the requirement."
- **Our assessment**: The Celo example demonstrates three important behaviors: (1) web search
  augments the goal-setter when local documentation is sparse, (2) the executor can recover
  from failures by changing strategy (creating a mock user vs. attempting real auth), and (3)
  the system successfully handles non-trivial multi-step setup that would be challenging to
  automate with fixed scripts. The multi-retry recovery (fail on iteration 1, succeed on
  iteration 2) validates the five-retry threshold as practically useful rather than
  wastefully generous.

### Claim 10: Terminal-Bench scores validate the autoinstall approach — Composer 2 achieves 61.7% vs. 47.9% for Composer 1.5

- **Evidence**: Benchmark comparison with Terminal-Bench, described as measuring a model's
  ability to set up developer environments — directly measuring what autoinstall improves.
- **Confidence**: emerging (first-party benchmark numbers; Terminal-Bench numbers match those
  independently reported in `blog-cursor-composer2-technical-report.md` Claim 4, confirming
  consistency)
- **Quote (scores)**: "Composer 2 now scores significantly higher on Terminal-Bench (61.7%
  versus 47.9% for Composer 1.5)"
- **Quote (benchmark definition)**: "a benchmark that includes tests of a model's ability
  to set up developer environments"
- **Our assessment**: The benchmark choice is apt: Terminal-Bench directly measures what
  autoinstall trains for (environment setup capability). The 13.8 percentage point improvement
  (47.9% → 61.7%) is a meaningful signal that autoinstall-trained environments improve exactly
  this skill. The corroboration with the Composer 2 technical report (which independently
  reports the same numbers) increases confidence in the figures.

### Claim 11: The model-bootstrapping pattern extends beyond environment setup — future Composer versions will use prior models for run management, data preprocessing, and architecture tuning

- **Evidence**: Forward-looking statement from the authors within the autoinstall post itself.
- **Confidence**: anecdotal (stated as an anticipated future direction, not a deployed
  capability; no timeline given)
- **Quote**: "previous Composer instances will play a large role in many other aspects of
  the training process, including run management, data preprocessing, and architecture tuning"
- **Our assessment**: This is the most strategically significant claim in the post. If the
  model-bootstrapping pattern generalizes from environment setup to run management and
  architecture tuning, it implies a self-improving training pipeline where model capability
  compounds across generations: each generation is trained in better environments, with better
  data, on a better-tuned architecture — all prepared by the previous generation. This is an
  agentic training flywheel, not just a one-time bootstrapping trick.

## Concrete Artifacts

### Autoinstall Two-Stage Process

```
# Cursor Composer Autoinstall — Two-Stage Environment Setup
# Source: Cursor Research blog, May 6, 2026

STAGE 1: GOAL SETTING (Cursor agent)
  Input:   Codebase at a fixed checkout
  Task:    Propose 10 commands + high-level description of expected output
           per command if environment were correctly set up
  Method:  Explore readmes, makefiles, language-specific tooling
           (e.g., uv for Python, clippy for Rust); use web search if docs sparse
  Output:  10 (command, expected-output-description) pairs

STAGE 2: EXECUTION (separate Composer agent)
  Input:   Initial environment state + 3 of the 10 target commands
           (selected from Stage 1 output)
  Task:    Configure the environment so all 3 commands run successfully
           with outputs matching Stage 1 descriptions
  Method:  Explore codebase; call tools to configure; mock as needed
  Validation: Commands must execute AND output must match target description
  Retry limit: 5 iterations; discard environment if not passing after 5

MOCKING CAPABILITIES
  File-level:  Mock missing files, create placeholder images
  Database:    Create fake database tables
  Cloud/S3:    Create MinIO configs (for S3-compatible storage)
  Containers:  Create Docker sidecar containers for long-running services
  Auth:        Mock authentication flows

QUALITY FILTER
  Accept: All 3 commands pass + output matches descriptions
  Discard: Failed after 5 retry iterations
```

### Celo Blockchain Monorepo Case Study

```
# Celo (celo-org/celo-monorepo) — Autoinstall Example
# Source: Cursor Research blog, May 6, 2026

PROJECT REQUIREMENTS
  - Large set of dependencies for install
  - Authentication flow mocking for testing
  - Sparse project documentation

STAGE 1 (Goal Setting)
  - Agent went through docs and code to find key installation commands
  - Documentation was sparse → agent used web search on the project's
    documentation site to find further setup commands
  - Agent identified that Foundry (related repository) was also needed
    → used web search to read Foundry's documentation

STAGE 2 (Execution)
  Iteration 1: Failed to get the test application running
  Iteration 2: Found that creating a mock user allowed starting the
               application locally → satisfied the requirement

OUTCOME: Successfully set up the environment (2 iterations, within the 5-retry limit)
```

### Terminal-Bench Validation

```
# Terminal-Bench Scores — Composer 2 vs. Composer 1.5
# Source: Cursor Research blog, May 6, 2026
# Also reported in: blog-cursor-composer2-technical-report.md (Claim 4)

Metric: Terminal-Bench (measures ability to set up developer environments)
  Composer 2:   61.7%
  Composer 1.5: 47.9%
  Delta:        +13.8 percentage points
```

## Cross-References

- **Corroborates**: `blog-cursor-composer2-technical-report.md` Claim 2 — That note
  establishes "training inside a production-identical harness" as the primary mechanism for
  closing train-test mismatch, with Quote: "RL training uses realistic Cursor sessions" with
  "equivalent tools, structures, and environments matching real problems." Autoinstall is the
  operational system that realizes this principle for Composer 2: it converts unconfigured
  repository checkouts into realistic, functional RL training environments.

- **Corroborates**: `blog-cursor-composer2-technical-report.md` Claim 4 — The Terminal-Bench
  numbers (61.7% Composer 2, 47.9% Composer 1.5) reported in this autoinstall post are
  confirmed identically in that technical report's Claim 4 benchmark table. Cross-source
  consistency increases confidence in these figures.

- **Corroborates**: `blog-anthropic-harness-long-running.md` Claim 2 — That note's Claim 2
  establishes the generator/evaluator architectural split as "a strong lever," with Quote:
  "Separating the agent doing the work from the agent judging it proves to be a strong lever."
  The autoinstall two-stage design instantiates this same principle: the goal-setting agent
  (Stage 1) sets success criteria; the execution agent (Stage 2) implements them. The two
  agents have different roles and are prevented from conflating planning with execution. This
  structural parallel is reinforced by `blog-cursor-real-time-rl.md`'s separate-agent reward
  computation model.

- **Extends**: `blog-cursor-real-time-rl.md` — That note documents Cursor's real-time RL
  pipeline (Claim 1: production user tokens as training signal; Claim 2: ~5-hour checkpoint
  cycle with CursorBench gate). Autoinstall is the upstream environment preparation step that
  enables these RL loops: without working environments, the RL pipeline described in that note
  cannot collect meaningful reward signal. The two posts together reveal Cursor's full training
  stack: autoinstall prepares environments → real-time RL trains on them → CursorBench gates
  deployment.

- **Extends**: `blog-cursor-composer-self-summarization.md` — Both posts describe training
  infrastructure components built on Cursor's RL training loop. Self-summarization addresses
  long-context trajectory management during training; autoinstall addresses environment quality
  before training episodes begin. Together they show Cursor's strategy of solving training
  infrastructure bottlenecks with trained sub-components rather than engineered fixes.

- **Novel**: The following patterns are new to the corpus:
  - **Model-bootstrapping as a named deployed system**: Using an earlier model version (Composer
    1.5) to prepare the training environment for the next version (Composer 2) is described as
    a production operational pattern, not a research prototype.
  - **Two-stage goal-setter/executor environment setup**: Separating specification (10 proposed
    commands) from implementation (executor validates 3 of them) is a new pattern for automated
    environment bootstrapping.
  - **Validate-and-discard quality filter with explicit retry limit**: The five-iteration discard
    threshold creates a quality floor on the training environment corpus.
  - **Full-stack mocking scope for RL environments**: MinIO configs, Docker containers, fake DB
    tables, and auth flow mocking for RL training environments — extends well beyond file stubs.
  - **Self-improving training flywheel claim**: The forward-looking extension to run management,
    data preprocessing, and architecture tuning (Claim 11) is the first articulation in this
    corpus of a compounding model-bootstrapping strategy across training pipeline components.

## Guide Impact

- **Chapter 02 (Harness Engineering — environment fidelity for RL)**: Add a dedicated section
  on training environment preparation as a first-class RL engineering concern, anchored by
  Claim 1 (broken environments waste RL compute) and the autoinstall system as the reference
  implementation. The key practitioner message: "what does a working environment look like?"
  is as important an engineering question as "what does a correct solution look like?"

- **Chapter 02 (Harness Engineering — agent bootstrapping pattern)**: Add the two-stage
  goal-setter/executor pattern (Claims 3–5) as a reusable design for automated environment
  setup. The discard-after-five-retries threshold (Claim 6) should be noted as a quality-filter
  design decision, not just an implementation detail.

- **Chapter 02 (Harness Engineering — model-bootstrapping as training strategy)**: Claim 11
  (extending bootstrapping to run management, data preprocessing, architecture tuning) should
  be flagged as a forward-looking section: the model-bootstrapping pattern has potential beyond
  environment setup; teams building multi-generation training pipelines should track whether
  Cursor publishes on these extensions.

- **Chapter 03 (Safety and Verification — training eval alignment)**: The Terminal-Bench
  result (Claim 10) shows that training specifically for environment setup improves a benchmark
  that directly measures that capability. This is a concrete example of eval-training alignment:
  when the benchmark measures what the training targets, the result is informative. Cite alongside
  `blog-cursor-cursorbench.md` for the principle that benchmark design should mirror training
  objectives.

## Extraction Notes

- Blog post is 6 minutes (~900 words); fully read. No paywalled sections. No substantive
  linked sub-pages followed (the Celo project reference links to GitHub, not additional
  research content).
- The WebFetch tool returned a summarized rendering rather than fully verbatim text. All
  quoted passages were verified via targeted re-fetches requesting specific passages. Where
  the tool returned paraphrases, the quotes were re-requested with explicit verbatim
  instructions before being included in this note.
- The Terminal-Bench numbers (61.7% vs. 47.9%) are independently corroborated in
  `blog-cursor-composer2-technical-report.md` Claim 4, increasing confidence they are
  accurately transcribed.
- No contradictions to file: all claims are additive to the existing corpus. The
  environment-fidelity principle corroborates (not contradicts) existing notes.
- The forward-looking statement in Claim 11 is from this post itself, not from the Composer
  2 technical report. The technical report source note does not contain this quote and should
  not be cited for it.
