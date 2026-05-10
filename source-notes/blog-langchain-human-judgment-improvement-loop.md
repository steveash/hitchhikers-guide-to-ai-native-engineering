---
source_url: https://www.langchain.com/blog/human-judgment-in-the-agent-improvement-loop
source_type: blog-post
title: "Human judgment in the agent improvement loop"
author: Rahul Verma (LangChain)
date_published: 2026-04-09
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#108"
---

# Human judgment in the agent improvement loop

> A practitioner guide from LangChain establishing that successful agents
> require a continuous improvement loop — development → post-deployment →
> continuous refinement — where human expertise is captured as calibrated
> automated evaluators rather than manual review, and production data becomes
> the primary source of new test cases.

## Source Context

- **Type**: blog-post (LangChain, April 9, 2026; ~11 min read; authored by
  Rahul Verma, LangChain practitioner team)
- **Author credibility**: Rahul Verma writes for LangChain, the team behind
  LangSmith (their observability and evaluation platform). LangChain has worked
  with hundreds of organizations deploying AI agents, giving the author a
  broad practitioner dataset to draw from. Claims are vendor-positioned —
  LangSmith is the platform being illustrated — but the underlying patterns are
  platform-agnostic principles that happen to be demonstrated via LangSmith
  tooling. The trader copilot example is a hypothetical illustration, not a
  documented customer case study; treat individual implementation details as
  illustrative rather than empirical.
- **Scope**: Covers the full agent development lifecycle for production agents:
  component design (workflow, tools, context), an improvement flywheel with
  three phases, and the principle of automated evaluations as a scalability
  multiplier. Uses a financial services trader copilot as a running example.
  Does NOT cover CLAUDE.md/hooks/settings.json tooling, multi-agent
  orchestration architectures, or code-generation agents specifically.
  The framing is enterprise/team deployment, not individual developer use.

## Extracted Claims

### Claim 1: The most critical organizational knowledge is tacit — it lives in employees' minds and is not documented, making explicit extraction from domain experts necessary to build reliable agents

- **Evidence**: Author's framing of the trader copilot example, where "unwritten
  trading conventions that determine how to interpret requests like 'today's
  exposure' or 'recent volatility'" and "practical knowledge of the database,
  like which tables are authoritative vs. outdated" are identified as the
  blocking gaps for reliable agent performance.
- **Confidence**: emerging
- **Quote**: "AI agents work best when they reflect the knowledge and judgment
  your team has built over time. Some of that is institutional knowledge that's
  already documented and easy for an agent to use as-is. But most great
  organizations also rely on tacit knowledge that lives inside their employees'
  minds."
- **Our assessment**: This is an accurate diagnosis of why enterprise agent
  deployments are harder than demo deployments. The demo uses clean,
  well-documented domains; production uses decades of organizational conventions
  that were never written down because humans learn them through osmosis.
  The implication is actionable: agent design starts with a knowledge
  extraction exercise, not a prompt engineering exercise. This is the
  organizational-scale version of the harness engineering insight that the
  agent needs a rich scaffolding environment — but focused on implicit
  knowledge, not tool design.

### Claim 2: Three agent components benefit from human expert input — workflow design (where to add deterministic code), tool design (names/parameters/descriptions), and agent context (what knowledge to provide at runtime and how to organize it)

- **Evidence**: Structured breakdown across three sections of the post with
  concrete examples for each (compliance checkpoints for workflow, SQL tool
  flexibility vs. parameterization tradeoff for tool design, Skills-style
  runtime retrieval for agent context).
- **Confidence**: emerging
- **Quote**: "Building an agent means deciding when to invoke an LLM and
  managing what context to provide with each call (e.g., documentation,
  memory, conversation history, tools) to achieve the desired result. Each
  of these design choices benefits from input from the right stakeholders."
- **Our assessment**: The three-component taxonomy is clean and practical. It
  maps well onto existing harness engineering knowledge: workflow design ≈
  hook and permission design; tool design ≈ custom command and MCP design;
  agent context ≈ CLAUDE.md + Skills + context engineering. The value of
  this taxonomy is as a checklist for *who to involve* in each decision —
  risk/compliance for workflow gates, database owners for tool parameters,
  domain SMEs for context curation.

### Claim 3: Deterministic code checkpoints alongside LLM reasoning reduce latency, token use, and guarantee that critical steps execute — regulatory and high-risk settings may require this as a hard constraint

- **Evidence**: Trader copilot example: the agent autonomously generates and
  executes SQL, but "add code that requires it to validate the final answer
  meets our firm's risk and compliance requirements before returning it to
  the trader." The rationale is explicitly stated: lower latency, fewer tokens,
  guaranteed execution.
- **Confidence**: emerging
- **Quote**: "there are benefits to using deterministic code to define parts of
  the workflow: lower latency, fewer tokens, and the guarantee that critical
  steps actually run."
- **Our assessment**: This corroborates the existing pattern of mixing
  deterministic tooling with LLM reasoning rather than making everything
  agentic. The latency and token arguments are secondary; the "guarantee that
  critical steps actually run" argument is the strongest — an LLM can skip or
  forget steps, deterministic code cannot. For regulated industries, this is
  not an optimization but a hard requirement. This extends the guide's existing
  "deterministic tools for deterministic work" principle to the mixed-mode case:
  you can have an LLM-driven workflow with deterministic guardrails at critical
  junctions.

### Claim 4: The industry has moved from single system prompts toward curated runtime-retrieved context — Anthropic's Skills standard (launched October 2025) is cited as a prominent example

- **Evidence**: Author's characterization of an industry trend: "Early agents
  just gave the model a single system prompt and a set of tool definitions.
  Over time, the industry has moved toward providing agents with much richer
  context at the beginning of their execution." Anthropic Skills is named as
  the primary example: documentation and domain rules curated in advance, then
  retrieved at runtime.
- **Confidence**: emerging
- **Quote**: "the industry has moved toward providing agents with much richer
  context at the beginning of their execution. Anthropic's **Skills**, a
  standard that has quickly grown in popularity since launching in October, is
  one prominent example of this trend."
- **Our assessment**: This is a third-party vendor citing a competitor's
  feature as industry-leading evidence — noteworthy validation of the Skills
  pattern. The key design shift is from "pack everything in the system prompt"
  to "curate a knowledge base, then retrieve relevant subsets at runtime." This
  reduces token use, enables richer domain coverage, and allows non-engineers
  to contribute knowledge. The phrase "context engineering" is used explicitly
  in the post for this design discipline, which aligns with Ch04's framing.

### Claim 5: Human time invested in manual review of agent outputs scales poorly and is rarely economical — translating expert judgment into automated evaluators yields more leverage

- **Evidence**: The post's lead principle for the entire improvement loop, stated
  before the development phase discussion. LangSmith's Align Evaluator feature
  is cited as the specific mechanism: calibrate an LLM-as-a-judge evaluator
  using curated examples from subject matter experts, then run it continuously
  rather than doing manual review.
- **Confidence**: emerging
- **Quote**: "teams get more leverage when humans help design and calibrate
  automated evaluators, rather than manually reviewing large volumes of agent
  outputs"
- **Our assessment**: This is the central operational insight of the post. The
  argument is that human judgment is valuable but human *time* is scarce;
  the leverage point is using a small amount of human time to calibrate an
  evaluator that then runs at scale. This is an important reframe for teams
  that have tried "have a human review every output" and found it
  unsustainable. The mechanism (calibrate an LLM judge with human-labeled
  examples) is more rigorous than "just use an LLM judge" but requires
  upfront investment in curating good examples with the right stakeholders.

### Claim 6: LLM-as-a-judge evaluators require calibration against subject matter expert examples — an out-of-the-box LLM judge miscalibrated relative to human judgment is actively harmful

- **Evidence**: The Align Evaluator feature is described as providing a UI
  for "calibrating LLM-as-a-judge evaluators using curated examples and
  feedback from subject matter experts." The post shows a screenshot
  description: "The evaluator is currently stricter than our human judge so
  we need to alter the system prompt to make it more lenient." This means the
  LLM judge has a known calibration bias that must be corrected, not just used
  as-is.
- **Confidence**: emerging
- **Quote**: "It provides a user interface for calibrating LLM-as-a-judge
  evaluators using curated examples and feedback from subject matter experts.
  We recommend using this feature for any evaluator that's meant to mimic a
  non-developer stakeholder's judgments."
- **Our assessment**: The explicit acknowledgment that LLM judges can be
  miscalibrated (too strict, too lenient) is important. It extends the
  existing corpus finding that evaluators require "intensive prompt tuning"
  (blog-anthropic-harness-long-running, Claim 6) into the team context: the
  calibration process requires SME input, not just engineering iteration.
  The phrase "meant to mimic a non-developer stakeholder's judgments" is the
  key conditioner — for evaluators checking technical code quality, engineering
  judgment may be sufficient; for evaluators checking compliance,
  professionalism, or domain accuracy, the SME must be in the loop.

### Claim 7: Iterating quickly and frequently is critical because LLM reasoning, not code, determines agent behavior — and "it's impossible to know what an AI agent will do until it runs"

- **Evidence**: Author's justification for the tight iteration loop principle.
  Agent interfaces are often free-form text inputs, making behavior prediction
  even harder. The conclusion: "Putting your agent in front of users is the
  only way to collect the data you need to make it ultimately successful."
- **Confidence**: emerging
- **Quote**: "It's impossible to know what an AI agent will do until it runs"
- **Our assessment**: This is a clean statement of the epistemic challenge of
  agent development. Unlike a deterministic system where you can reason about
  behavior from code alone, an LLM-driven agent's behavior emerges from the
  combination of model capabilities, prompt, context, and user input in
  unpredictable ways. The practical implication — ship early to real users,
  not just to internal testers — is operationally important and potentially
  uncomfortable for teams used to comprehensive pre-release testing cycles.
  Pairs with the pieterma observation that minimal agentic prompts can
  outperform hand-tuned pipelines: you can't anticipate all interaction
  patterns.

### Claim 8: Automated evaluations running on production data can direct human attention to the cases that matter most — frustration detection, error spikes, and latency outliers are viable trigger signals for human review

- **Evidence**: The post describes an online evaluator setup for the trader
  copilot: an LLM judge "can automatically detect when a user expresses
  frustration and flag those interactions for review." The team then
  investigates "the trace and decide whether the issue reflects a bug, a gap
  in the agent's knowledge, or a weakness in the workflow." Separate
  automated checks cover "slow or dangerous SQL queries."
- **Confidence**: emerging
- **Quote**: "Automated evaluations running on production data can help monitor
  the agent and surface situations that warrant human attention."
- **Our assessment**: The frustration-detection example is especially valuable
  because it illustrates how LLM-as-a-judge can evaluate *user experience*
  signals, not just technical correctness. This is a class of evaluation that
  deterministic checks cannot perform. The multi-signal approach (LLM judge
  for conversational quality + code checks for SQL safety) demonstrates that
  different evaluator types address different failure modes — no single
  evaluator covers everything.

### Claim 9: Annotation queues focus human expert attention on the highest-signal production traces — borderline evaluator scores indicate evaluator calibration issues; very negative scores indicate agent problems

- **Evidence**: The post describes annotation queues in detail: subject matter
  experts review cases flagged by online evaluators. "A borderline feedback
  score would suggest that we need to adjust the evaluator itself" while a
  very negative score "indicates something is wrong with the agent." The
  feedback from annotation queues is "saved so it's available for future
  automated and manual analysis."
- **Confidence**: emerging
- **Quote**: (no direct quote available for this specific diagnostic; see Our
  assessment for the synthesis)
- **Our assessment**: This is a practical decision tree for interpreting
  evaluator output that the guide should document. The framing — borderline
  score = calibration problem, very negative score = agent problem — helps
  teams triage whether to fix the agent or fix the evaluator. Without this
  distinction, teams might spend engineering effort tuning an agent when the
  real problem is a miscalibrated evaluator (or vice versa). The annotation
  queue as a human-in-the-loop mechanism also serves dual purpose: it improves
  the current agent AND accumulates human-labeled data for future evaluator
  calibration.

### Claim 10: Unstructured, AI-assisted exploration of production traces surfaces behavioral patterns not visible from individual traces or deterministic evaluations

- **Evidence**: The LangSmith Insights Agent feature is described as "a built-in
  AI agent that analyzes large volumes of tracing data with minimal user
  configuration. It surfaces patterns and trends in agent behavior that
  wouldn't be obvious from individual traces or deterministic evaluations."
  The example: clustering conversations by underlying theme to "identify use
  cases we should be extra sure to support well or even future product
  additions."
- **Confidence**: anecdotal (feature description; no metrics on how often
  useful patterns are found vs. noise)
- **Quote**: "Unstructured explorations of live behavior inspire some of the
  most valuable improvements for AI agents."
- **Our assessment**: This claim is worth preserving because it challenges the
  implicit assumption that all important signals are pre-specified. Evaluation
  frameworks built upfront necessarily measure what you thought to measure;
  the behavior space of production agents includes things you didn't think to
  specify. An AI-powered clustering/analysis layer can surface the unspecified.
  The limitation is that it still requires human review of the insights report
  to decide on next steps — this is a discovery tool, not an autonomous
  improvement mechanism.

### Claim 11: Production data is the best source of test cases after launch — initial evaluation suites are educated guesses; production traces are reality

- **Evidence**: "When you build the first version of an agent, your evaluation
  suite is at best educated guesses on what tests you need to validate that it
  works. After launch, you gain access to a much better source of test cases:
  real production data."
- **Confidence**: emerging
- **Quote**: "After launch, you gain access to a much better source of test
  cases: real production data."
- **Our assessment**: This is a clean statement of a well-understood software
  engineering principle applied to agents: you can't anticipate all the ways
  users will interact with your system. The specific implication for agents is
  stronger than for deterministic software because agent behavior is harder to
  predict from code inspection alone (per Claim 7). The practical advice
  follows: invest in infrastructure to capture, filter, and curate production
  traces into test suites from day one, not as an afterthought.

### Claim 12: Small, carefully curated evaluation sets outperform large uncurated ones — even a few hundred examples are sufficient if chosen by domain experts

- **Evidence**: "Evaluations can be useful running on just a few hundred
  examples if they're chosen carefully, so it's worthwhile to involve experts
  in deciding which examples should define the test suite."
- **Confidence**: emerging (stated as practitioner principle; no comparative
  study cited)
- **Quote**: "Evaluations can be useful running on just a few hundred examples
  if they're chosen carefully"
- **Our assessment**: This is an actionable calibration point that pushes back
  against "we need more data" paralysis. The key qualifier is "if chosen
  carefully" — a representative, balanced set covering key use cases and edge
  cases at small scale is more useful than a large but haphazard collection
  of traces. The practical implication: invest human expert time in curating
  and labeling a small high-quality set rather than trying to achieve scale
  at the cost of quality. This also lowers the barrier to entry for teams
  who feel they don't have "enough" data to run evaluations.

### Claim 13: Golden datasets — examples of the agent's best production outputs — serve as regression prevention baselines across agent versions

- **Evidence**: "One of the most helpful datasets we can curate is a 'golden
  dataset,' consisting of examples of the copilot's best work so far, so we
  can use it as a baseline to ensure future versions perform at least as well."
  The workflow: use online evaluator scores to identify candidate traces, then
  send them to an annotation queue for SME review to decide which belong in
  the golden dataset.
- **Confidence**: emerging
- **Quote**: "a 'golden dataset,' consisting of examples of the copilot's best
  work so far, so we can use it as a baseline to ensure future versions perform
  at least as well"
- **Our assessment**: The golden dataset concept is the agent-development
  equivalent of a regression test suite — it captures current behavior that
  must be preserved when you make improvements. The workflow for building it
  (automated pre-filtering via evaluator scores + human expert review in an
  annotation queue) is a replicable process that any team can adapt. The risk
  of golden datasets is "teaching to the test" — optimizing to match past
  best behavior rather than genuinely improving. The post does not address
  this limitation.

## Concrete Artifacts

### The Agent Improvement Flywheel (Three Phases)

From the blog post structure:

```
Phase 1 — Development
  Engineers + product managers + SMEs build initial test suites
  - Create ground truth datasets: question → expected answer pairs
  - Create examples of good SQL/tool use for the domain
  - Run evaluations against datasets during development
  - Mini-flywheel: augment initial datasets with interesting cases
    found during manual testing

Phase 2 — Post-Deployment
  Automated evaluations running on production data
  - Online evaluations: LLM judge + deterministic code checks
    running on all production traces
  - Alerts: triggered on error/latency/evaluation score spikes
  - Annotation queues: route flagged traces to domain experts
    (very negative = agent problem; borderline = evaluator problem)
  - Insights Agent: AI-powered clustering of production traces
    to surface hidden behavioral patterns

Phase 3 — Continuous Refinement
  Production data → new test cases
  - Use online evaluator scores to identify candidate traces
  - Send to annotation queue for expert curation
  - Build updated evaluation datasets from reviewed traces
  - Build golden dataset: best production traces as regression baseline
```

### Three Agent Components That Benefit from Human Input

From the blog post:

```
Component 1 — Workflow Design
  Design decision: where to invoke LLM vs. deterministic code
  Who to involve: risk/compliance experts, operations stakeholders
  Example: code checkpoint to validate SQL query meets compliance
    requirements before returning result to user
  Benefits of deterministic gates: lower latency, fewer tokens,
    guaranteed execution of critical steps

Component 2 — Tool Design
  Design decision: which tools the agent can use and with what parameters
  Key tradeoff: flexibility (general execute_sql) vs. control (parameterized
    query tools)
  Resolution: run evaluations to determine performance + risk characteristics;
    ship when all stakeholders are comfortable with results
  Who to involve: engineers + business stakeholders who understand constraints

Component 3 — Agent Context
  Design decision: what knowledge to provide, how to structure it for
    runtime retrieval
  Industry trend: from single system prompt → curated runtime-retrieved
    knowledge base (Anthropic Skills cited as example)
  Discipline: context engineering — deciding what knowledge the agent
    should access and organizing it so the agent can retrieve the right
    information at the right moment
```

### LLM-as-a-Judge Calibration Process

Implied by the post's Align Evaluator description:

```
Step 1: Collect examples from subject matter experts of good and bad
        agent outputs (the labeled set)
Step 2: Configure an LLM judge with an initial system prompt
Step 3: Run the judge on the labeled set; compare to expert labels
Step 4: If judge is too strict → update system prompt to make more lenient
        If judge is too lenient → update system prompt to make more strict
Step 5: Iterate until judge calibration aligns with expert judgment
Step 6: Deploy judge as an online evaluator on production traffic
Step 7: Continue collecting expert feedback via annotation queues to
        maintain calibration as agent behavior evolves
```

### Decision Tree for Interpreting Annotation Queue Results

From the blog post's annotation queue description:

```
Evaluator result: very negative
  → Problem is in the agent (bug, knowledge gap, workflow weakness)
  → Investigate the trace; root-cause the agent issue

Evaluator result: borderline
  → Problem may be in the evaluator calibration
  → Review whether the evaluator's criteria need adjustment

Evaluator result: high quality (for golden dataset curation)
  → Human expert decides if it belongs in the golden dataset
  → If yes: add to baseline regression set
  → If no: discard (even a high evaluator score can be wrong)
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-harness-long-running** (Claim 6): The LangChain post's
    emphasis that LLM-as-a-judge evaluators require calibration against human
    expert examples directly corroborates the finding from Anthropic Labs that
    "evaluator quality requires intensive prompt tuning" — out-of-the-box, LLM
    evaluators rationalize away legitimate bugs or test superficially. Both
    sources arrive at the same conclusion (evaluators need iterative refinement
    against human judgment) from different angles: Anthropic from engineering
    observation, LangChain from the enterprise deployment perspective.
  - **blog-anthropic-harness-long-running** (Claim 14): The LangChain post's
    claim that evaluator calibration requires carefully worded criteria is
    consistent with the finding there that "criteria wording steered the
    generator in ways I didn't fully anticipate" — evaluator prompts are
    policy documents that must be treated with care, not just written and
    deployed.
  - **blog-addyosmani-code-agent-orchestra** (Claim 5): The LangChain post's
    entire focus on evaluation infrastructure corroborates Osmani's claim that
    "the bottleneck is no longer generation. It's verification." The improvement
    flywheel is fundamentally a verification infrastructure — building, running,
    and refining the systems that tell you whether the agent is doing good work.
  - **blog-anthropic-building-enterprise-agents** (Claim 2): The LangChain
    post's emphasis on extracting tacit domain expert knowledge into evaluators,
    test suites, and agent context (Claim 1 here) is the operational mechanism
    behind Anthropic's "encoding institutional knowledge into systems that
    compound over time" — the LangChain post shows *how* that encoding happens.
  - **blog-pieterma-syntopic-reading** (Claim 5): The pieterma approach of
    asking the agent "what functionality do you wish it had?" at session end
    is a lightweight, agent-driven analog to the LangChain post's annotation
    queue approach — both are systematic mechanisms for surfacing gaps in the
    agent's capabilities, but one is agent-driven and the other is human-driven.

- **Extends**:
  - **blog-pieterma-syntopic-reading** (Claim 6: agent self-improvement loop):
    The pieterma loop is agent-driven (agent proposes and implements its own
    tools). The LangChain improvement loop is human-expert-driven (SMEs
    identify gaps, engineers fix them). Together they describe a spectrum:
    at one end, pure agent self-improvement for tool-level gaps; at the other,
    systematic human-expert-driven improvement for domain knowledge and
    evaluation calibration. The pieterma loop is fast and cheap; the LangChain
    loop is slower but addresses the tacit knowledge gap that agents cannot
    diagnose themselves.
  - **blog-addyosmani-code-agent-orchestra** (Claim 8 / WIP limits and
    verification bottleneck): The orchestra post identifies the verification
    bottleneck but focuses on code-output verification. This source extends
    the verification concept to *behavioral evaluation* — ongoing monitoring
    of agent interactions rather than just post-generation code review.

- **Contradicts**: None filed. The emphasis on human judgment in the
  improvement loop is complementary to, not in conflict with, the agent
  self-improvement patterns in the corpus. The closest tension is that pieterma
  Claim 2 (minimal agentic prompt outperformed hand-tuned pipeline) could be
  read as "don't invest heavily in upfront design" — but the LangChain post
  is about *post-deployment* iteration, not upfront design. The two claims
  apply to different phases.

- **Novel**:
  - **The three-component agent design checklist with stakeholder mapping**:
    No existing source identifies which organizational stakeholders should
    be involved in which component of agent design. The mapping (compliance
    → workflow gates; DB owners → tool parameters; domain SMEs → context
    curation) is new to the corpus.
  - **The annotation queue as a human-in-the-loop pattern**: No existing source
    note describes a production triage mechanism where automated evaluators
    pre-filter traces and route the highest-signal cases to domain expert
    review. This is a specific operational pattern for managing the human
    review bottleneck.
  - **Golden dataset as an agent regression baseline**: The explicit workflow
    for building a golden dataset (evaluator pre-filter → expert annotation →
    curated baseline) as a regression prevention mechanism is new.
  - **The agent improvement flywheel as a named, three-phase model**: While
    the individual components exist in the corpus, this is the first source
    to name and structure the development → post-deployment → continuous
    refinement cycle as a complete, explicit model.
  - **The calibration diagnostic decision tree**: The explicit framing that
    borderline evaluator scores indicate a calibration problem while very
    negative scores indicate an agent problem is a concrete diagnostic tool
    not in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the three-component agent design
  checklist (workflow design with deterministic gates, tool design with
  stakeholder review, agent context as curated runtime knowledge) as a
  systematic framework for what to engineer and who to involve. The existing
  chapter focuses on *how* to configure the harness; this source adds the
  *what* and *with whom* dimensions. Specifically, add the deterministic
  checkpoint pattern (Claim 3) as the recommended approach for compliance/risk
  gates — not just "put it in CLAUDE.md" but "write deterministic code for
  the critical validation step and let the LLM reason around it."

- **Chapter 03 (Safety and Verification)**: Add the agent improvement flywheel
  as the organizing structure for ongoing verification: development-phase test
  suites, post-deployment automated evaluations, and continuous refinement via
  production data. The golden dataset concept (Claim 13) should be added as
  the recommended regression prevention mechanism for agents. The annotation
  queue pattern (Claim 9) should be added as the recommended human-in-the-loop
  mechanism that is *scalable* (automated pre-filtering) rather than requiring
  manual review of all outputs.

- **Chapter 03 (Safety and Verification)**: Add the LLM-as-a-judge calibration
  requirement (Claim 6): uncalibrated judges are not neutral — they have
  systematic biases (too strict or too lenient) that must be corrected through
  iteration with subject matter expert examples. The calibration diagnostic
  (borderline score = evaluator problem; very negative score = agent problem)
  should be a named pattern.

- **Chapter 04 (Context Engineering)**: The post explicitly uses the term
  "context engineering" for the discipline of deciding what knowledge the
  agent accesses and how to organize it for runtime retrieval. The Anthropic
  Skills standard is cited as the current industry exemplar of this trend (from
  single system prompts → curated runtime-retrieved knowledge base). Ch04
  should reference this vendor validation of the runtime-retrieval pattern as
  the emerging industry standard, not an advanced or experimental approach.

- **Chapter 05 (Team Adoption)**: The tacit knowledge extraction challenge
  (Claim 1) is a team-level concern absent from the existing chapter. Add
  guidance on knowledge extraction as a pre-requisite to agent deployment:
  the specific stakeholders to involve (compliance, DB owners, domain SMEs)
  and the artifact types to extract (unwritten conventions, authority tables,
  quality rubrics). The claim that "we'll need to engage with the appropriate
  subject-matter experts to include all the unwritten context the agent needs"
  positions this as organizational work, not engineering work — the guide
  should address it explicitly for team leads and product managers.

## Extraction Notes

- The source URL in the issue was `blog.langchain.com` which redirects to
  `www.langchain.com/blog`. Both fetch attempts returned the same content.
  The canonical URL is `https://www.langchain.com/blog/human-judgment-in-the-agent-improvement-loop`.
- The post includes screenshots of the LangSmith UI (Align Evaluator,
  annotation queue, dashboards, Insights Agent report). Screenshots were not
  extractable via WebFetch, but their described purpose is fully captured in
  the claim extraction above.
- The trader copilot is explicitly described as a "real-life inspired example"
  — a hypothetical illustration, not a documented customer case. Treat
  implementation details as illustrative rather than empirically reported.
- The post mentions LangSmith features (Align Evaluator, datasets, evaluations,
  tracing, automations, Insights Agent, annotation queues) throughout. All of
  these are LangSmith-specific implementations of platform-agnostic patterns.
  The patterns are extracted above without assuming LangSmith availability.
- A demo trader app is referenced ("Check out the demo trader app and set up
  annotation queues") — this was not followed as it requires interactive
  account setup, not just a URL fetch.
- No contradictions found with existing source notes. No contradiction issue
  filed.
