---
source_url: https://www.thoughtworks.com/insights/articles/decision-models-and-the-possibility-of-no-ops
source_type: blog-post
title: "Decision models and the possibility of NoOps"
author: Zichuan Xiong
date_published: 2026-10-12
date_extracted: 2026-10-13
last_checked: 2026-10-13
status: current
confidence_overall: anecdotal
issue: "#4083"
---

# Decision models and the possibility of NoOps

> A Thoughtworks AIOps practitioner reports a four-stage migration from RAG-assisted humans to LLM agents to JEV-style decision models handling all triage, and argues that risk moves from individual events to the AI "control plane" and that humans move from executing tickets to governing decisions — all qualitative, with no metrics.

## Source Context

- **Type**: blog-post (Thoughtworks Insights article; first-hand experience report from an internal AIOps program)
- **Author credibility**: Zichuan Xiong writes on agent control and data/ops topics for Thoughtworks (see the other Xiong notes in this corpus). Claims are from the team's own operations practice; the article presents no data to verify them. The article also advances Thoughtworks' own control plane ("Agentworks"), so there is a vendor-perspective incentive.
- **Scope**: Covers the Q4 2024 – fall 2026 evolution of one AIOps program, a stage table (human role / AI role / main risk), four claimed shifts in ops, and advice for ops leaders, operators, tool builders and managed service providers. Does NOT give throughput, cost, error-rate, escalation-rate or failure-case numbers, nor how the decision models are evaluated, thresholded or monitored for drift.

## Extracted Claims

### Claim 1: The team's AIOps practice moved through four stages, each with a distinct human role and a distinct main risk
- **Evidence**: Author's own program history (Q4 2024 → early fall 2026), summarised in a table. No metrics.
- **Confidence**: anecdotal
- **Quote**: "Our AIOps (AI for IT operations) journey began in Q4 2024 with a modest premise: every ticket a human operator receives carries an AI-suggested response (Fig. 1), referencing a standard operating procedure (SOP) or a past ticket."
- **Our assessment**: The most reusable artifact (see Concrete Artifacts). The "main risk shifts per stage" framing (human throughput → review quality → cost → escalation/oversight) is a useful adoption-ladder lens even though one org's timeline is not a universal sequence.

### Claim 2: At the low-risk-first stage, the emergent risk is rubber-stamp review, not model error
- **Evidence**: Author assertion about Stage 2 (Q3 2025 per heading; text says Q2 2025 was when agents took off).
- **Confidence**: anecdotal
- **Quote**: "the question became whether reviewers were still checking the output or simply approving it."
- **Our assessment**: Consistent with common human-in-the-loop concerns; notable that it is stated as an observed problem but no detection mechanism or rate is given.

### Claim 3: Agents that plan, generate PRs, validate in a sandbox and close tickets work, but token cost becomes the binding constraint
- **Evidence**: Author's experience from Q1 2026 onwards.
- **Confidence**: anecdotal
- **Quote**: "Scaling this approach with multiple rounds of agentic conversation gets expensive quickly, and token consumption has become the headline topic in AI news."
- **Our assessment**: Plausible and in line with the cost-driven motivation for decision models. No figures, so the size of the cost problem is unknown.

### Claim 4: In September 2026 the team moved all triage agents from LLMs to decision models and collapsed every use case into one pattern
- **Evidence**: Decision stated as made ("our AI practice decided"); Figure 6 shows a JEV-based MWAA (Amazon Managed Workflows for Apache Airflow) incident triage example. No before/after results reported.
- **Confidence**: anecdotal
- **Quote**: "In September, our AI practice decided to move all our triage agents from LLMs to decision models and simplify every use case into one pattern: intake, triage, then auto-heal or escalate."
- **Our assessment**: The strongest new fact vs. the JEV notes: a production-ops adoption claim rather than a model review. But it reports a decision, not an outcome — treat the success of the migration as unverified. Note the figure caption describes a "JEV+LLM hybrid", so LLMs may remain in the loop.

### Claim 5: Decision models are cheaper and fit triage because they classify and decide rather than generate text
- **Evidence**: Author assertion; relies on external JEV claims, no cost numbers.
- **Confidence**: anecdotal
- **Quote**: "These fast, specialized models, such as JEV and others often called System 1 models, classify and decide rather than generate open-ended text, at a fraction of the cost of LLMs (Figure 5)."
- **Our assessment**: Corroborates the pricing/classification framing in the Willison and Latent Space notes, but adds no independent measurement.

### Claim 6: Open-weight models also changed the cost structure in early fall 2026
- **Evidence**: One-sentence assertion, no detail on which models.
- **Confidence**: anecdotal
- **Quote**: "In early fall 2026, open-weight models changed the cost structure."
- **Our assessment**: Too thin to rely on; flag as a lead only.

### Claim 7: Risk moves from events to the control plane, which is enumerated as classifiers, drift, agent performance, playbook library, approval gates and logging
- **Evidence**: Reasoned argument by the author, plus Figure 7 (their control plane, "Agentworks"). Author's opinion, not measured.
- **Confidence**: anecdotal
- **Quote**: "That includes the classify and decide components, model drift, agent performance, the playbook library, the approval gates and the logging pipeline."
- **Our assessment**: A useful checklist of what a harness for autonomous ops must govern. The claim that risk "concentrates" there is argument rather than evidence, and the article does not say how any of these components is tested.

### Claim 8: The human role shifts from executing tickets to governing decisions, creating new roles
- **Evidence**: Author prediction/opinion.
- **Confidence**: anecdotal
- **Quote**: "Operators no longer do the work. They set the boundaries the system works within, supply the context it reasons over and judge whether it is behaving as intended."
- **Our assessment**: Consistent with the "delegation of judgment" framing in the five-controllers note. Named roles: context curators, playbook owners, ontology engineers, operators of the AI control system. No evidence on headcount or hiring.

### Claim 9: Stage 4's own main risk is deciding when the system needs a human
- **Evidence**: Stage table row 4 ("Escalation and oversight: deciding when the system needs human intervention"); no mechanism described.
- **Confidence**: anecdotal
- **Quote**: "Observes or supports the system, with no routine intervention at the task level."
- **Our assessment**: Notable gap: the article names escalation as the residual risk but gives no thresholds, calibration, or audit approach. Latent Space's calibrated-confidence escalation claim is the relevant technical complement.

### Claim 10: ITSM tooling and managed-service economics will change as the unit shifts from events to decisions
- **Evidence**: Opinion/prediction.
- **Confidence**: anecdotal
- **Quote**: "expect that within five years most of your business under service-level agreements (SLAs) will be tied to AI workloads."
- **Our assessment**: Speculative, vendor-adjacent business prediction; low value for the guide beyond context.

### Claim 11: Author expects "no-human operations" to create more jobs than it eliminates
- **Evidence**: Stated expectation, no data.
- **Confidence**: anecdotal
- **Quote**: "we expect it to create more jobs than it eliminates."
- **Our assessment**: Record as optimism, not finding. Note tension with the claim that task execution "becomes irrelevant first".

## Concrete Artifacts

Stage table (paraphrased cell content from the source's table; stage names from the article):

```
Stage                                  | Human role                        | AI role                                   | Main risk / constraint
1. Human responds, AI assists          | handles every ticket, authority   | RAG proposes responses from SOPs/incidents| human throughput
2. AI responds to low-risk events      | steps in on low confidence        | LLM agent responds first (deterministic)  | review quality and throughput
3. AI manages the resolution cycle     | oversees workflow and outcomes    | triage, plan, PRs, sandbox validate, close| cost (token consumption)
4. Decision models handle triage       | observes/supports, no task-level  | classify + route: intake→triage→          | escalation and oversight
                                       | intervention                      | auto-heal or escalate                     |
```
Source: Xiong, table in "Decision models and the possibility of NoOps" (abbreviated).

Timeline stated in the article: Stage 1 from Q4 2024; Stage 2 Q3 2025; Stage 3 from Q1 2026; Stage 4 early fall 2026 (all-agent migration decision in September 2026).

Single-pattern flow: `intake → triage → auto-heal or escalate`, applied to "An infrastructure request, an application alert, a data pipeline incident, a change request or a user question".

## Cross-References

- **Corroborates**: `blog-simonwillison-jev-decision-models` (Claim 5: Jev suits classification tasks; Claim 3: pricing undercuts text LLMs) and `blog-latentspace-jev-system-one-for-prod` (Claim 9: calibrated confidence for thresholds and escalation; Claim 16: use-case families incl. real-time intelligence in the loop) — this article is a production-ops use of the same model class.
- **Contradicts**: None found. Note that `blog-simonwillison-jev-decision-models` Claim 8 (explainability concerns) and Claim 9 (bias, avoid high-stakes use) are in tension with replacing task-level human intervention, but the article is silent on them rather than opposing them; not filed as a contradiction.
- **Extends**: `blog-thoughtworks-xiong-five-controllers-one-graph` (Claim 1: agent as delegation of human judgment; Claim 7: loops must close on an external authority) — the control-plane list and "governing decisions" role are the operational counterpart. `blog-thoughtworks-srinivasan-xiong-agent-reliability-operating-model` (Claim 7: failure taxonomy routes failures to owners; Claim 9: continuous control loop) addresses how to govern such a plane; this article lists the components but not the tests.
- **Novel**: The four-stage ops maturity ladder with per-stage risk; the report of a production migration from LLM agents to decision models for triage with the intake→triage→auto-heal/escalate single pattern; the rubber-stamp-review risk at the AI-first stage; named ops roles (context curator, playbook owner, ontology engineer).

## Guide Impact

- **Chapter 02**: Add the control-plane component list (classifiers, drift, agent performance, playbook library, approval gates, logging) as an example checklist of harness elements for autonomous workflows, labelled as a practitioner claim (Claim 7).
- **Chapter 03**: When discussing escalation/confidence handoff, cite this as an example where residual risk is "when to escalate" and note the article gives no mechanism; pair with the Latent Space calibrated-confidence claim.
- **Chapter 05**: Use the four-stage ladder and the rubber-stamp-review risk (Claims 1–2) as an adoption-maturity illustration, and the new roles (Claim 8). Present "no-human operations" as an author's aspiration, not a validated outcome.

## Extraction Notes

- Fetched the full article HTML via curl and read the whole text, including the stage table and all four "paradigm shift" points; the article has no sub-pages. Figures are images (only captions read).
- Source has no quantitative data; all confidence is anecdotal. The stage-2 heading says Q3 2025 while the body says agents took off in Q2 2025 — minor internal inconsistency.
- Stage 1's heading did not appear in the extracted text; its content comes from the intro paragraph and the table.
- Table cells in Concrete Artifacts are abbreviated for layout; direct quotes appear only in the Quote fields.
