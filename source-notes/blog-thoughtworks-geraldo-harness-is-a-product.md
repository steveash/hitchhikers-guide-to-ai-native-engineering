---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/harness-is-a-product
source_type: blog-post
title: "The harness is a product"
author: Cecilia Geraldo
date_published: 2026-11-04
date_extracted: 2026-11-05
last_checked: 2026-11-05
status: current
confidence_overall: emerging
issue: "#4537"
---

# The harness is a product

> Thoughtworks essay (Technology Radar Vol. 35 companion) arguing the agent harness needs an accountable owner, an eval-gated change process, and three explicit preconditions before it may self-improve; mostly argument, with a few concrete, checkable practices.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, Generative AI / Platforms)
- **Author credibility**: Cecilia Geraldo, Lead Consultant at Thoughtworks. The essay accompanies Technology Radar Vol. 35, where "harness engineering at scale" is one of four themes. Practitioner/consultancy authority; no named deployments, code, or metrics are given.
- **Scope**: Defines the harness, argues for product-style management, proposes a test strategy (golden set), gates for self-improvement, enterprise-harness concerns (identity, platform ownership, shadow IT), and three ownership questions. It does not provide implementation detail, data, or case studies.

## Extracted Claims

### Claim 1: The harness is "everything between the model and the work", enumerated as eight components
- **Evidence**: Definition by assertion; no empirical support. Note the triage comments said "seven"; the page lists eight bullets (instructions/skills, tools, permissions/sandboxes, context policy, state, orchestration, evaluation, telemetry).
- **Confidence**: emerging
- **Quote**: "The right way to understand the harness is that it’s everything between the model and the work. It’s neither the model nor the application; it’s the layer that decides how the two meet."
- **Our assessment**: Useful as a checklist. Notably it counts evaluation and telemetry as parts of the harness, which many definitions (e.g. "Agent = Model + Harness") leave out. We buy it as a taxonomy, not as a finding.

### Claim 2: In agentic systems, concerns once spread across framework, platform team and CI collapse into one artifact that nobody may own
- **Evidence**: Argument from experience; no data.
- **Confidence**: anecdotal
- **Quote**: "In an agentic system, though, they collapse into one artifact a small team can change in an afternoon; and, what’s becomes particularly problematic as it's used at scale, one no one may be accountable for."
- **Our assessment**: Plausible and consistent with other Thoughtworks pieces on accountability. The mechanism (cheap to change, hence under-governed) is the interesting part.

### Claim 3: An unmanaged harness decays into "configuration debt with a system prompt"
- **Evidence**: Composite scenario ("a folder of Markdown, a handful of wrapper scripts..."), not a reported case.
- **Confidence**: anecdotal
- **Quote**: "Without those, what you think of as a harness is really just configuration debt with a system prompt."
- **Our assessment**: A memorable name for a real failure mode. Attributes a product needs, per the author: users (developers and agents), versions, dependencies, a roadmap, quality gates, an owner.

### Claim 4: Package-style distribution (Agent Plugins, marketplaces, Agent Package Manager) makes harness versioning and ownership mandatory
- **Evidence**: Cites Radar Vol. 35 entries; reasoning from supply-chain analogy.
- **Confidence**: emerging
- **Quote**: "A copied prompt has no version, no provenance and no upgrade path; a package does."
- **Our assessment**: Good contrast between copy-pasted prompt fragments and pinned packages. Whether these standards stick is not evidenced here.

### Claim 5: Common harness metrics (tokens, acceptance rate, tests passed) are activity metrics, not quality measures
- **Evidence**: Assertion; the article gives reasons (non-determinism, drifting task mix, eval cost) but no data.
- **Confidence**: emerging
- **Quote**: "They can tell you the system is busy, but not whether it’s actually better."
- **Our assessment**: Aligns with the Duolingo reversal reported in the token-crisis note. Reasonable.

### Claim 6: Start with a task-based golden test set of 20–30 real jobs, versioned with the harness, with regression on every meaningful change
- **Evidence**: Proposal ("You could, for example, start with..."), not validated by reported results.
- **Confidence**: emerging
- **Quote**: "This could be the 20 or 30 jobs the agent is expected to do, with a mechanism for scoring each one."
- **Our assessment**: The concrete number is a heuristic, not an empirical finding. "Version that set alongside the harness, so a change and its evidence travel together" is the actionable part. The article also says to "run a regression on every meaningful change, not only on releases", and warns that "an evaluation set that was representative in March could well be misleading by June".

### Claim 7: Cost and latency are first-class eval metrics; keep sampled human review for what evals cannot score
- **Evidence**: Assertion.
- **Confidence**: emerging
- **Quote**: "A harness that improves output while doubling spend hasn’t improved the product."
- **Our assessment**: Sensible; fits the cost framing in the token-crisis note.

### Claim 8: Evals need an owner and review cadence, or they become "human-in-the-loop theater"; "without an eval, there’s no change"
- **Evidence**: Assertion by analogy to release-gating test suites.
- **Confidence**: emerging
- **Quote**: "The rule should clear: without an eval, there’s no change."
- **Our assessment**: Strong as a policy rule (the typo "should clear" is in the original). It is stricter than most sources, which treat evals as helpful rather than a hard merge gate. Practical cost for small teams is not discussed.

### Claim 9: Self-improving harness loops can drift ("changes that look like learning but behave like entropy"); they need a feedback flywheel tied to real signals
- **Evidence**: Argument; no incident cited.
- **Confidence**: anecdotal
- **Quote**: "Without this signal, self-improvement is a model editing its own job description and calling the result progress."
- **Our assessment**: Signals listed: findings, incidents, eval failures, cost anomalies and human takeovers. Overlaps with Cursor's anomaly-driven loop.

### Claim 10: Three preconditions for safe harness self-improvement: eval harness, provenance, rollback path; "automate the proposal and keep the approval"
- **Evidence**: Prescriptive rule; no experiment.
- **Confidence**: emerging
- **Quote**: "The rule is that you should automate the proposal and keep the approval."
- **Our assessment**: The three preconditions as written on the page: "An evaluation harness, so improvement is measured rather than asserted." / "Provenance, so every self-authored change can be attributed, reviewed and reverted." / "A rollback path, so a bad iteration costs an afternoon rather than a quarter." This resolves the triage gap (the list was lost in text extraction). The rule is consistent with LangChain's and Cursor's human-review steps.

### Claim 11: Running an enterprise harness resembles platform engineering: golden paths, sandbox defaults, plugin allow-lists with provenance, central model routing, version-attributed telemetry, deprecation policy
- **Evidence**: Author says early signs are visible in "some instances of platform teams"; no named organization.
- **Confidence**: anecdotal
- **Quote**: "a runtime without a deprecation policy is one that nobody can safely depend on."
- **Our assessment**: Useful checklist. Telemetry that "can tell you which harness version produced a particular output" is a specific, implementable requirement.

### Claim 12: Agent identity is "the most pointed and urgent issue", and is a harness decision, not a model decision
- **Evidence**: Assertion.
- **Confidence**: emerging
- **Quote**: "An agent acting on someone's behalf needs a clear answer to whose permissions it's using, what it may do without asking and what evidence is left behind."
- **Our assessment**: Three-part question (whose permissions, what without asking, what evidence) is a compact review checklist. The article offers no mechanism; see the Anthropic and Thoughtworks authority notes for substance.

### Claim 13: A harness slower or less capable than a weekend DIY one will be routed around, so paved roads must be genuinely faster
- **Evidence**: Assertion.
- **Confidence**: emerging
- **Quote**: "Paved roads only work when they are genuinely faster to travel."
- **Our assessment**: Restates the shadow-IT/paved-roads note; corroboration, not new evidence.

### Claim 14: Three ownership questions: who owns it, how do you know the last change made it better, what is it allowed to touch
- **Evidence**: Framing device.
- **Confidence**: anecdotal
- **Quote**: "How do you know the last change made it better? If the answer is a demo, an anecdote or an acceptance rate, the harness is not yet a product."
- **Our assessment**: Good audit questions. The third (blast radius: "data, tools, credentials and production") is "part of the product definition, not an implementation detail discovered during an incident".

## Concrete Artifacts

No code, configs or metrics in the source. Verbatim checklists:

```
Harness components (Geraldo, "What is an agent harness?"):
The instructions and skills the agent loads.
The tools the agent can call.
The permissions and sandboxes the agent runs inside.
The policy that decides what context the agent sees.
The state the agent carries between steps.
The orchestration that sequences the agent’s steps.
The evaluation that tells you whether it was effective.
The telemetry that tells you what happened when it did not.

Three preconditions for harness self-improvement:
An evaluation harness, so improvement is measured rather than asserted.
Provenance, so every self-authored change can be attributed, reviewed and reverted.
A rollback path, so a bad iteration costs an afternoon rather than a quarter.
```

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-nandyala-pani-engineering-the-harness.md` Claim 13 (harness as versioned, peer-reviewed software) and Claim 2 (Agent = Model + Harness).
  - `blog-langchain-better-harness-evals.md` Claim 12 (evals as regression tests) and Claim 10 (human review before production deployment).
  - `blog-google-anatomy-harness-engineering.md` Claim 6 (suite is to give confidence a change did not make the agent worse).
  - `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` Claim 11 (paved roads) and Claim 9 (unversioned prompts, no telemetry, no quality gates).
  - `blog-thoughtworks-gordon-agentic-authority-overreach.md` Claim 9 (every production agent needs a Designated Principal / named approver).
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 5 (usage metrics do not reliably track value) and Claim 9 (no one owns the aggregate outcome).
- **Contradicts**: None found. Tension to note, not a contradiction: this source's hard rule "without an eval, there’s no change" is stricter than `blog-google-anatomy-harness-engineering.md` Claim 5, which says formal evals come in a second phase after dogfooding. These differ by maturity stage, so no contradiction issue was filed.
- **Extends**:
  - `blog-cursor-continual-harness-improvement.md` Claim 13 (automated loop to remediation): adds explicit gating preconditions (eval, provenance, rollback) and the "automate the proposal and keep the approval" rule.
  - `blog-thoughtworks-kamelman-delegation-architecture.md` Claim 5 and `blog-anthropic-agent-identity-access-model.md`: frames identity as a harness-level decision.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 11 (continuous evaluation): adds a golden-set size heuristic and owner/cadence requirement.
- **Novel**: Treating eval ownership and review cadence as a requirement; the three self-improvement preconditions as a list; the "whose permissions / what without asking / what evidence" identity question; telemetry that attributes outputs to a harness version; the deprecation-policy requirement.

## Guide Impact

- **Chapter 02**: Compare the harness component inventory against this eight-item list; consider adding evaluation and telemetry as explicit harness components if not already present, and add the argument that a copied prompt has no version, provenance or upgrade path for packaging skills/plugins.
- **Chapter 03**: Add the golden-set heuristic (20–30 real jobs, versioned with the harness, regression on every meaningful change) as a vendor-neutral starting point, flagged as a heuristic. Add cost and latency as eval metrics, and a note that eval sets age (that an evaluation set representative in March may be misleading by June).
- **Chapter 05**: Add the three ownership questions as an adoption-readiness check, plus the named-accountable-owner and platform-team ownership points (paired with Gordon Claim 9).
- **Self-improvement guidance (Ch02/Ch03)**: Cite the three preconditions as a gate before enabling automated harness edits.

## Extraction Notes

- Fetched the full rendered page via curl and read it end to end; no paywall. The three self-improvement preconditions, missing from the earlier text extraction, are captured verbatim above.
- The page lists eight components, not seven as stated in one triage comment.
- No linked sub-pages were followed (Radar Vol. 35 entries are only referenced, not read).
- Source is an opinion/argument piece. Claims are graded emerging or anecdotal accordingly; none is backed by data.
