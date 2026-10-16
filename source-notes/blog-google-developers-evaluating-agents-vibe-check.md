---
source_url: https://developers.googleblog.com/evaluating-ai-agents-moving-past-the-vibe-check/
source_type: blog-post
title: "Evaluating AI agents: moving past the vibe check"
author: Hugo Selbie, Dani Zamora, Jesse Carah, John DeMartino (Google)
date_published: 2026-10-15
date_extracted: 2026-10-16
last_checked: 2026-10-16
status: current
confidence_overall: emerging
issue: "#4158"
---

# Evaluating AI agents: moving past the vibe check

> A vendor-authored Day 0 to Day 2 playbook for agent evals whose most reusable parts are red-pen trace review, boolean judge rubrics, a frozen golden dataset, and a CI gate with a zero-regression rule. None of it is backed by measurements.

## Source Context

- **Type**: blog-post (Google Developers Blog; companion to the AI Agent Clinic episode "How to Actually Evaluate (Any) AI Agent: Beyond the Vibe Check")
- **Author credibility**: Four Google solutions/incubation engineers. They have practitioner exposure but no stated data. The post promotes Google's open-source `agent-eval` toolkit and the Agent Evaluation service on the Gemini platform, so the product claims are marketing and the methodology is the extractable part.
- **Scope**: Covers pre-production eval design (CUJs, simulated users, layered checks), four named traps, a Day 0/1/2 rollout, and a CI gate. It does not report quantitative results. It does not cover judge-calibration methods beyond "compare with hand-graded traces".

## Extracted Claims

### Claim 1: Agents fail silently. They can loop, burn tokens or hallucinate and still return a plausible final answer, so eyeballing output misses the failure.
- **Evidence**: Argument by enumeration of production costs (cloud bill, rate limits, spinners, duplicate side effects, lost trust). No incident or data.
- **Confidence**: emerging
- **Quote**: "An agent can get stuck in a retry loop, fire off multiple tool calls, yet still return a polite, plausible-sounding final answer."
- **Our assessment**: Credible and consistent with experience. It motivates trace-level and operational checks, not only output checks.

### Claim 2: Any repeatable evaluation system beats ad-hoc spot checks, so start simple and grow it.
- **Evidence**: Assertion.
- **Confidence**: emerging
- **Quote**: "any repeatable evaluation system (no matter how simple) is better than relying on ad-hoc spot checks or no system at all."
- **Our assessment**: A useful adoption-friendly framing that lowers the entry bar. It is not tested here.

### Claim 3: Anchor tests in critical user journeys (CUJs), where every clause of the journey becomes an evaluation point.
- **Evidence**: One worked example, an operations analyst handling a trade discrepancy email, decomposed into checks (correct transaction ID, ledger checked before drafting, ID mapping).
- **Confidence**: emerging
- **Quote**: "Every clause of a CUJ becomes an evaluation point."
- **Our assessment**: A practical decomposition technique. It also forces stakeholders to agree on what "success" means, which the post states as a benefit.

### Claim 4: A golden dataset can be bootstrapped from simulated users driven by scenarios, then progressively replaced by real production traces.
- **Evidence**: Recommends ADK user simulations with personas and behavioral constraints. No comparison of synthetic and real traffic.
- **Confidence**: emerging
- **Quote**: "You do not need six months of production logs to build your initial golden dataset."
- **Our assessment**: Corroborates the "development-stage testing should be synthetic" position in the Thoughtworks note. Whether simulator fidelity is adequate is unmeasured.

### Claim 5: Use four layers of checks (unit tests, deterministic metrics, LLM-as-judge rubrics, integration tests), because a single top-line score cannot explain a failure.
- **Evidence**: Assertion plus a diagram.
- **Confidence**: emerging
- **Quote**: "A single top-line score will never tell you why an agent failed."
- **Our assessment**: Standard layering. The post does not define the layers in detail.

### Claim 6 (Trap 1): Adding or removing tests invalidates the baseline, so keep the golden dataset frozen while tuning and change one variable at a time.
- **Evidence**: Logical argument. No data.
- **Confidence**: emerging
- **Quote**: "Every time you add or remove a test, though, you invalidate your baseline: you cannot tell if a score changed because the agent got better or because the test suite moved."
- **Our assessment**: Sound experimental hygiene, and a genuinely new point for the corpus. It is in tension with the "spring clean" advice in blog-langchain-better-harness-evals (Claim 11). The post itself reconciles them: retire a test "only when you are certain the underlying requirement has changed". That is a conditioning variable (when to prune), not a true contradiction, so no contradiction issue was filed.

### Claim 7 (Trap 2): Convert 1-to-5 LLM-judge rubrics into boolean pass/fail questions, because judges are inconsistent at the 3/4 boundary.
- **Evidence**: Assertion with one example question. No measurement of judge variance.
- **Confidence**: emerging
- **Quote**: "Whenever possible, turn your judge rubrics into boolean (pass/fail) questions rather than open-ended rating scales."
- **Our assessment**: Plausible and widely held, but the "notoriously inconsistent" claim is unsupported here. Treat it as a vendor heuristic. The example ("Did the agent verify the account ID before calling the refund tool?") is useful because it checks a process step rather than prose quality.

### Claim 8 (Trap 3): Evaluate the operational bill (latency, prompt/reasoning/completion tokens, cost, tool-call counts) alongside answer quality.
- **Evidence**: Illustrative scenario: 40 seconds, twelve redundant tool calls, sixty cents per query. Not measured.
- **Confidence**: emerging
- **Quote**: "Track latency, token consumption (prompt, reasoning, and completion tokens), API cost, and tool-call counts right alongside answer quality."
- **Our assessment**: Sensible. The illustrative numbers should not be cited as data.

### Claim 9 (Trap 4): Standardize traces on OpenInference semantic conventions so the eval pipeline is decoupled from the orchestration framework.
- **Evidence**: Assertion. The post notes that frameworks emit OpenTelemetry but with differing semantic conventions, and says the toolkit supports OpenInference natively.
- **Confidence**: emerging
- **Quote**: "While most frameworks emit OpenTelemetry traces, they don’t use the same semantic conventions for tool calls, steps, and tokens."
- **Our assessment**: A good portability argument. It is novel in the corpus, but the toolkit endorsement is product promotion.

### Claim 10: Day 0 should be a "red pen" pass. Read raw traces top to bottom before building aggregate metrics, then aggregate the notes into deterministic assertions and boolean judge checks.
- **Evidence**: Practitioner argument. The FAQ suggests reading the first 5 to 20 traces.
- **Confidence**: emerging
- **Quote**: "Ignore aggregate scores and read the actual execution traces from top to bottom: the prompts, intermediate reasoning steps, tool arguments, and final outputs."
- **Our assessment**: Corroborates the "look at the data first" stance in the Hamel notes. The concrete markup taxonomy (hesitated, hallucinated a parameter, wrong tool, rambled) and the 5 to 20 trace sizing are useful specifics.

### Claim 11: Validate any new LLM judge against the traces you graded by hand, and tighten the grading prompt until it matches.
- **Evidence**: Procedure only.
- **Confidence**: emerging
- **Quote**: "Never trust a new LLM-as-a-judge metric blindly."
- **Our assessment**: Matches the LangChain calibration claim (blog-langchain-human-judgment-improvement-loop, Claim 6). This post adds a cheap way to get the calibration set: reuse the Day 0 red-pen traces.

### Claim 12: Quality improves through roughly 50 to 60 small, measured iterations (turning individual knobs), not prompt rewrites.
- **Evidence**: Anecdotal ("In a real deployment..."), plus an illustrative claim that a prompt change "felt smarter" while latency doubled and tool-call hallucinations rose 15%.
- **Confidence**: anecdotal
- **Quote**: "In a real deployment, reaching production quality often takes 50 to 60 small iterations."
- **Our assessment**: Per triage guidance, do not cite the 50 to 60 figure or the 15% as evidence. The qualitative point stands: measure each small change.

### Claim 13: The CI/CD PR gate should enforce both a global pass threshold and zero regressions on previously passing metrics, even if the aggregate holds.
- **Evidence**: Design rule. The 95% threshold is given only as an example ("for example, 95% boolean success").
- **Confidence**: emerging
- **Quote**: "Even if the overall score holds steady, the build fails if any previously passing metric regresses."
- **Our assessment**: The most concrete new gating rule. It prevents trading a critical capability for edge-case gains. In practice it is limited by judge noise: a noisy boolean judge will cause flaky gates. The post does not address this.

### Claim 14: Export run artifacts (raw trace JSONL, prompt hashes, model versions, latency profiles, scorecards) to central storage and feed production traces back into the golden dataset.
- **Evidence**: Description of the Day 2 setup. No outcomes reported.
- **Confidence**: emerging
- **Quote**: "including raw trace JSONL, prompt hashes, model versions, latency profiles, and scorecard summaries"
- **Our assessment**: Recording prompt hash and model version with each run is a small, valuable reproducibility practice. The feedback loop is corroborated by blog-langchain-human-judgment-improvement-loop (Claim 11).

## Concrete Artifacts

Example CUJ (source, "Define success with critical user journeys"):

```
As an operations analyst, I expect the agent to ingest a counterparty trade discrepancy email, identify the disputed transaction, verify the trade economics against our internal ledger within 30 seconds, and draft a response reverse-translating our internal trade IDs back into the broker's nomenclature without human intervention.
```

Boolean judge rubric example (source, Trap 2):

```
Did the agent verify the account ID before calling the refund tool? (Yes/No)
```

Rollout structure (source, "A practical Day 0 to Day 2 rollout"):

```
Day 0: scenarios + user simulations -> red-pen read of 5-20 raw traces
Day 1: scaffold golden dataset, run on every change, validate judge vs. hand-graded traces, tuning loop
Day 2: CI/CD PR gate (global pass threshold + zero regressions), shared dashboards, production traces -> golden dataset
```

Four layers of checks: unit tests, deterministic metrics, LLM-as-a-judge rubrics, integration tests.

## Cross-References

- **Corroborates**: blog-thoughtworks-anand-agent-evaluation-framework (Claim 5, persona/simulated-user testing; Claim 12, synthetic testing in the development phase). blog-langchain-human-judgment-improvement-loop (Claim 6, judge calibration against expert examples; Claim 11, production traces as the best test-case source; Claim 13, golden datasets as regression baselines). blog-google-adk-live-voice-agent-evaluation (Claim 9, rubric-based judges; Claim 11, CI-callable evals).
- **Contradicts**: None filed. The "freeze the suite" rule (Claim 6 here) is in mild tension with blog-langchain-better-harness-evals (Claim 11, prune evals regularly). The two differ in context (tuning window vs. periodic maintenance), so this is a conditioning variable rather than a contradiction.
- **Extends**: blog-langchain-better-harness-evals (Claim 12, evals as regression tests) by adding an explicit merge-gate rule. blog-hamel-eval-smell and blog-hamel-claude-auto-evals (inspect the data before committing to evaluators) with a concrete Day 0 procedure.
- **Novel**: Boolean-over-scale judge rubric rule. Zero-regression merge gate alongside a global threshold. Frozen-baseline trap. OpenInference as a decoupling standard. Reusing red-pen traces as the judge calibration set.

## Guide Impact

- **Chapter 03**: Add a "start with a red-pen trace review" step before building automated graders, with the boolean-rubric and frozen-golden-set rules as practical pitfalls, citing this note as vendor-practitioner guidance (emerging).
- **Chapter 03**: Where eval-as-regression-test is discussed (blog-langchain-better-harness-evals), add the CI gate rule: global threshold plus zero regressions on previously passing metrics. Caveat judge noise.
- **Chapter 02**: In the harness tuning-loop discussion, note that operational metrics (latency, tokens, cost, tool-call counts) should be tracked per change alongside quality.
- **Chapter 05**: Optionally mention shared eval dashboards and PR gates as a team adoption mechanism.

## Extraction Notes

- Read the full post, including the FAQ. The YouTube companion video and the agent-eval GitHub repo were not read.
- The page was fetched as raw HTML and converted to text so that quotes are verbatim.
- Vendor-promotional material (agent-eval toolkit, Agent Evaluation service, Adaptive Rubrics, Gemini root-cause analysis) is treated as product detail, not evidence. No numbers in the post come from measurement.
- The author line is taken from the post byline. The post does not give individual credentials beyond job titles.
