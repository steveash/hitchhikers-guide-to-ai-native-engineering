---
source_url: https://cursor.com/blog/agent-autonomy-auto-review
source_type: blog-post
title: "Governing agent autonomy with Auto-review"
author: David Gomes & Travis McPeak (Cursor/Anysphere)
date_published: 2026-06-11
date_extracted: 2026-06-12
last_checked: 2026-06-12
status: current
confidence_overall: emerging
issue: "#1158"
---

# Governing agent autonomy with Auto-review

> Cursor's production system for contextual autonomy governance — a "dial not a switch" classifier agent that sits in the execution RPC stream, inspects workspace context with read-only tools, and returns explanations to the parent agent rather than the user, reducing enterprise chat interruption rates from ~40% to ~7%.

## Source Context

- **Type**: blog-post (first-party practitioner report from Cursor/Anysphere, ~8 min read, published June 11, 2026)
- **Author credibility**: David Gomes and Travis McPeak are named Cursor engineers. Travis McPeak also authored `blog-cursor-security-agents.md` (March 2026), establishing a pattern of first-party technical disclosure from the same Cursor security/agent team. The specific engineering details — model selection rationale, RPC stream placement, flapping detection, labeled eval methodology — are not typical marketing content and indicate genuine implementation disclosure.
- **Scope**: Covers the design, architecture, and calibration of Cursor's Auto-review system for local desktop agents. Includes the "autonomy dial" concept, classifier-in-loop architecture, block-and-explain feedback loop, evaluation methodology, and production metrics. Does NOT cover: cloud agent governance (noted as future work), classifier cost structure, how the allowlist/sandbox pre-layer is defined, how policy drift is managed at steady state, or failure cases where the classifier made wrong decisions.

## Extracted Claims

### Claim 1: Agent autonomy governance should operate as a "dial rather than a switch"

- **Evidence**: Core design philosophy stated as the organizing principle of Auto-review, contrasted explicitly with binary permission blocks.
- **Confidence**: anecdotal (first-party design rationale; no empirical comparison with binary approaches published)
- **Quote**: "Auto-review, which makes decisions around agent autonomy behave more like a dial than a switch."
- **Our assessment**: The binary alternative — block or allow — produces either excessive user interruptions (too restrictive) or excessive autonomy (too permissive). A dial means the system has a continuous spectrum of responses calibrated to contextual risk. This is a named, portable concept for guide framing: any chapter discussing agent autonomy design can anchor on this contrast to explain why rule-based blocking alone fails in practice.

### Claim 2: Effective risk assessment must be based on user intent alignment, not action isolation

- **Evidence**: Stated as the classifier's core evaluation frame. The same action (e.g., deleting a file) may be justified or unjustified depending on what the user asked.
- **Confidence**: emerging (principled design rationale; consistent with what practitioners discover when building approval systems at scale)
- **Quote**: "The question is not whether an action looks risky in isolation...whether the action is justified by what the user asked the agent to do."
- **Our assessment**: Intent-anchored evaluation reframes the problem from "is this action dangerous?" to "is this action appropriate given the stated goal?" A `rm -rf` command is dangerous in isolation but may be the correct action if the user asked the agent to clean up a temporary build directory. This produces fewer false positives that cause approval fatigue than rule-based blocking, at the cost of requiring the classifier to understand task context. Note: the "..." in the quote reflects text omitted by the extraction tool; the stated claim is fully supported by the surrounding article context.

### Claim 3: Lower-reasoning models are not necessarily faster for in-loop classifier tasks, because policy understanding failures increase token consumption

- **Evidence**: Counterintuitive finding from Cursor's model selection process for the Auto-review classifier.
- **Confidence**: anecdotal (Cursor's engineering experience; no benchmark data published)
- **Quote**: "a small model, so that it stayed fast and inexpensive to run, while still making a nuanced judgment"
- **Our assessment**: The naive assumption is: lower reasoning = fewer tokens = faster. The observed failure mode: a lower-reasoning model struggles with policy understanding, producing verbose, uncertain outputs before reaching a decision — net latency may be higher than a slightly more capable model. The solution stated in the article is "A small model with enough reasoning to make the decision cleanly." For guide purposes: in-loop classifier model selection should optimize for decision quality and token efficiency together, not parameter count alone.

### Claim 4: Classifiers in the execution path must be agentic with workspace inspection tools because some actions cannot be judged from the command string alone

- **Evidence**: Design rationale with a concrete example: `python script.py` safety depends on the script's contents, so the classifier must read the file before deciding.
- **Confidence**: emerging (concrete architectural rationale with specific example; logically consistent with information-gathering requirements in risk classification)
- **Quote**: "made the classifier agentic, because some actions cannot be judged from the command alone"
- **Our assessment**: A non-agentic classifier (receives command string, outputs allow/block) fails on context-dependent commands. The tools provided to the classifier (ReadFile, Grep, Glob, ListDir) are read-only workspace inspection tools — they give the classifier situational awareness without granting the ability to take harmful actions. This instantiates least agency applied to the classifier itself: exactly the tools needed to do its job, nothing more.

### Claim 5: Placing the classifier in the same RPC stream as the parent agent avoids the latency cost of a separate classification endpoint

- **Evidence**: Explicit architectural design decision stated in the article.
- **Confidence**: emerging (first-party architectural rationale; no latency benchmarks published)
- **Quote**: "the classifier runs in the same RPC stream as the parent agent, using an architecture similar to subagents"
- **Our assessment**: A separate classification endpoint would add a network round-trip before every reviewed tool call — unacceptable for interactive agent use. Embedding the classifier in the same RPC stream as the parent agent means classification latency is incurred inline within the existing model call infrastructure. "Architecture similar to subagents" implies the classifier is spawned as a co-located subagent sharing the connection context. For harness engineers: this is the production answer to "where does the classifier live?" — not a separate service, but an inline subagent in the execution stream.

### Claim 6: Block-and-explain to the parent agent (not the user) enables autonomous course correction without user interruption

- **Evidence**: Explicit feedback loop design choice. Production metrics (7% chat interruption rate) provide indirect validation that most blocked actions are resolved without user involvement.
- **Confidence**: emerging (design rationale with supporting metrics; mechanism clearly described)
- **Quote**: "When it blocks an action, it returns an explanation to the parent agent, and the parent agent can often use that feedback to choose a safer path without interrupting"
- **Our assessment**: Traditional approval gates interrupt the user with a permission request. Auto-review's approach: block the action, explain why to the parent agent, let the parent agent adapt. The parent agent can narrow the action scope, choose a different tool, or skip the risky step — all without requiring user input. The 7% chat interruption rate (vs. ~40% in approval-based systems) is the production evidence that this works: the classifier blocks ~4% of actions but only 7% of chats ever require a user interruption, meaning the parent agent self-corrects the vast majority of blocked cases.

### Claim 7: Classifier flapping — inconsistent decisions on the same case across runs — signals underspecified policy

- **Evidence**: Described as a specific test in the evaluation methodology; monitoring for flapping identifies where classifier behavior is inconsistent.
- **Confidence**: emerging (Cursor's operational experience; consistent with how policy ambiguity manifests in probabilistic models)
- **Quote**: (no direct quote; described in the article as testing for inconsistent decisions on the same case across runs to identify underspecified policies)
- **Our assessment**: Flapping is the operational diagnostic for policy underspecification. If a classifier produces different decisions on identical input across runs, the policy boundary is at exactly the point where the model is uncertain — small temperature variations change the outcome. Detecting flapping surfaces these ambiguous policy regions so they can be tightened. This is a concrete calibration technique that any team building a similar classifier can adopt immediately.

### Claim 8: Policy changes during classifier development require relabeling or rematerializing eval sets to avoid testing current classifiers against outdated problem definitions

- **Evidence**: Described as an explicit operational challenge in the evaluation methodology section.
- **Confidence**: anecdotal (Cursor's experience; general ML engineering challenge well-known in the field)
- **Quote**: (no direct quote; described as a policy drift challenge requiring relabeling when the classifier's policy changes)
- **Our assessment**: When the classifier's policy changes (e.g., tightening a previously lenient rule), existing eval labels become stale — they reflect decisions under the old policy. Running the new classifier against old labels measures compliance with the outdated policy, not the current intended behavior. The operational cost is explicit and unavoidable: policy changes trigger mandatory eval set updates. For teams building classifier-based governance: eval set maintenance is as important as classifier training.

### Claim 9: Auto-review blocks approximately 4% of actions; approximately 7% of chats lead to at least one user interruption

- **Evidence**: Production metrics reported from Cursor's deployed system.
- **Confidence**: emerging (self-reported; vendor source; no independent validation)
- **Quote**: "it currently blocks around 4% of actions" / "only about 7% of total chats in Auto-review mode lead to at least one interruption"
- **Our assessment**: These are the first published production metrics for classifier-governed agent autonomy. The separation between "actions blocked" (4%) and "chats with user interruption" (7%) is informative: many blocked actions are resolved by the parent agent without requiring user input, consistent with Claim 6's feedback loop design. The 4% block rate implies 96% of classifier-reviewed actions pass through — the prerequisite for "agents can move freely when stakes are low." For guide purposes: these are calibration benchmarks for teams designing similar systems — significantly higher than 4% suggests over-aggressive classification; significantly lower may indicate under-coverage.

### Claim 10: Enterprise customers previously saw approximately 40% of actions blocked under approval-based approaches

- **Evidence**: Comparison baseline reported in the article to contextualize the 7% improvement.
- **Confidence**: anecdotal (self-reported comparison; "enterprise customers" not further specified; may be Cursor's observation of customers rather than self-measured)
- **Quote**: "previously saw roughly 40% of actions blocked within their organization"
- **Our assessment**: When 40% of agent actions require human approval, the cognitive overhead renders the agent largely ineffective — users spend a significant fraction of their time approving actions rather than receiving autonomous help. The reduction to 7% chat interruption is the quantified benefit of contextual classification over blanket approval. The 40% baseline is likely from an approval-first posture (approve everything that looks potentially dangerous) rather than a risk-stratified posture. Present this as evidence that approval-gate-first designs produce approval fatigue at scale.

### Claim 11: Allowlists and sandboxing handle the majority of agent commands; the classifier runs only on a subset of higher-consequence actions

- **Evidence**: Architecture description in the article; the small share of classifier-reviewed actions is consistent with the 4% block rate representing a subset of total agent actions.
- **Confidence**: emerging (logical inference from architecture description and metrics)
- **Quote**: (no direct quote; article describes that only a small share of agent actions require classifier review, with many commands covered by allowlists or sandboxing)
- **Our assessment**: The classifier does not evaluate every agent action — it runs on actions that pass through a pre-classifier layer (allowlists for known-safe commands; sandboxing for isolated actions). The 4% block rate is among classifier-reviewed actions, not total actions. The layered architecture (allowlist → sandbox → classifier) means each layer handles progressively rarer, higher-consequence cases. For harness engineers: don't run a reasoning classifier on `git status` — build the layered pre-filter first and reserve the classifier for the actions that genuinely require contextual judgment.

### Claim 12: Auto-review is the default for new Cursor users; existing users can enable it in Settings > Agents

- **Evidence**: Deployment status stated in the article.
- **Confidence**: settled (deployment fact stated by the product team)
- **Quote**: (no direct verbatim quote extracted; article states Auto-review is default for new users with instructions for existing users)
- **Our assessment**: Default-on posture for new users is a product signal: Cursor believes classifier-based autonomy governance is robust enough for general use, not just power users. This means all new users will encounter the dial-not-switch model as their first experience with agent permissions. The default-on decision implies the false-positive rate (legitimate actions incorrectly blocked) is low enough not to disrupt new user onboarding.

## Concrete Artifacts

### Auto-review Architecture (as described in the article)

```
Auto-review Layered Architecture (Cursor, June 2026)
Source: https://cursor.com/blog/agent-autonomy-auto-review

LAYERED ACTION REVIEW:
  Layer 1 — Allowlists: known-safe commands pass through immediately
  Layer 2 — Sandboxing: isolated actions execute safely without classification
  Layer 3 — Classifier: context-dependent, higher-consequence actions reviewed

CLASSIFIER PROPERTIES:
  Model:     Small model with sufficient reasoning (exact model not disclosed)
             Key insight: lower-reasoning models NOT necessarily faster —
             policy understanding failures increase token consumption
  Agentic:   YES — classifier has read-only workspace inspection tools
  Tools:     ReadFile, Grep, Glob, ListDir (no write or execution capabilities)
  Placement: In the same RPC stream as the parent agent (subagent-style)
  Latency:   Inline — no separate endpoint round-trip

EVALUATION RULE (stated in article):
  "more lenient when the security stakes are lower, and more cautious when they're higher"
  Key question: whether the action is justified by what the user asked the agent to do
                (not whether the action looks risky in isolation)

FEEDBACK LOOP:
  On block → return explanation to PARENT AGENT (not user)
           → parent agent adapts: narrows action, chooses safer tool, or skips step
           → user interrupted only if parent agent cannot self-resolve
  Result:    ~4% of classifier-reviewed actions blocked
             ~7% of chats lead to any user interruption
             ~40% previous interruption rate under approval-first approach

DEPLOYMENT:
  Current scope: local desktop agents only
  Default: ON for new Cursor users
  Existing users: Settings > Agents
  Future scope: "same ideas to shape how we govern agent autonomy in more places"
```

### Evaluation Methodology

```
Auto-review Classifier Evaluation (Cursor, June 2026)
Source: https://cursor.com/blog/agent-autonomy-auto-review

INTERNAL USAGE DATA:
  Source:  ~12 hours of internal developer sessions
  Output:  6,122 labeled rows after deduplication

SYNTHETIC DATA:
  Generated scenarios for high-consequence cases rare in normal usage:
  — reading secrets
  — touching production data
  — following untrusted instructions
  — actions with large side effects

TESTING SCOPE (ran through production backend classifier loop):
  — tool use correctness
  — final classification (allow/block)
  — model override behavior
  — parse failure handling
  — workspace inspection context accuracy
  — flapping detection: inconsistent decisions on identical cases across runs
    (flapping = operational signal of underspecified policy → tighten policy)

OPERATIONAL CHALLENGE:
  Policy changes → eval set labels become stale
  Required: relabeling or rematerializing eval sets after policy changes
  Risk if skipped: testing current classifier against outdated problem definitions
```

### Production Metrics (self-reported, June 2026)

```
Auto-review Production Metrics (Cursor, June 11 2026)

Metric                                         Value       Confidence
----------------------------------------------------------------------
Actions blocked by classifier                  ~4%         emerging
Chats with ≥1 user interruption               ~7%         emerging
Previous enterprise action block rate          ~40%        anecdotal
Internal sessions used for eval data           ~12 hours   emerging
Labeled eval rows (post-dedup)                 6,122       emerging
```

## Cross-References

- **Corroborates**: `blog-anthropic-zero-trust-ai-agents.md` Claim 5 ("least agency" — OWASP concept of constraining what each agent tool can do, how often, where) and Phase 5 (Secure Tool Access: approval escalation for high-risk tool invocations). Auto-review implements approval escalation from the Zero Trust framework but routes the pause to the parent agent rather than the user for intermediate-risk actions. The classifier's own tools (ReadFile, Grep, Glob, ListDir — no write or execution) instantiate least agency applied to the classifier itself.

- **Corroborates**: `blog-cursor-amplitude-autonomous-pipeline.md` Claim 2 (risk-stratified auto-merge: 60–70% of PRs auto-merge based on risk classification). Both sources implement risk stratification as contextual adaptation rather than uniform treatment — Amplitude at the PR-merge decision boundary; Auto-review at the agent action execution boundary. The underlying principle is the same; the implementation layers differ.

- **Corroborates**: `blog-cursor-security-agents.md` Claim 4 (gradual trust rollout: shadow → inform → gate) and broader calibration philosophy. Travis McPeak is a shared author between both posts. Both reflect the same engineering approach: build classifier confidence through labeled internal data and staged deployment before committing to blocking behavior.

- **Extends**: `blog-anthropic-zero-trust-ai-agents.md` — The Zero Trust three-tier architecture places human-in-the-loop approval at the Enterprise tier for high-risk tool invocations. Auto-review introduces a third option between "no approval" (Foundation) and "human approval" (Enterprise): agent-in-the-loop self-correction via block-and-explain. This fills an architectural gap the Zero Trust framework acknowledges (approval escalation) but does not detail the intermediate-autonomy design for.

- **Extends**: `blog-cursor-security-agents.md` — That post documents four specialized security agents with a security MCP as coordination substrate; this post documents the general-purpose classifier governing autonomy for all agent actions in the execution path. Together they describe Cursor's full agent safety stack: specific-domain agents (security, dependency, invariant) + general autonomy classifier. The current post adds the execution-path governance layer that was absent in the security agents post.

- **Tension with**: `blog-anthropic-zero-trust-ai-agents.md` Claim 3 ("impossible vs. tedious" test — controls whose value comes only from friction fail against agentic attackers). Auto-review's classifier provides an intelligence-based gate rather than a pure friction gate, which partially survives the "impossible vs. tedious" test. However, a sophisticated attacker using prompt injection could potentially influence the classifier's context assessment by manipulating the workspace content the classifier reads. The Zero Trust source's recommendation for human approval for the highest-consequence actions remains valid even when Auto-review governs the intermediate range. This is a design-scope tension, not a formal contradiction: Auto-review is designed for intermediate-risk actions in interactive desktop use, not the highest-consequence production operations.

- **Novel**:
  - **Autonomy dial pattern** as a named concept (vs. binary switch): no prior corpus source names or implements this framing explicitly.
  - **Classifier-in-RPC-stream architecture**: embedding the classifier as a co-located subagent in the parent agent's RPC stream to avoid endpoint latency — no prior corpus source documents this implementation pattern.
  - **Block-and-explain to parent agent (not user)**: routing classifier explanations to the parent agent for autonomous self-correction, with user interruption as a last resort — no prior corpus source documents this feedback loop design.
  - **Flapping detection as policy calibration technique**: using inconsistent classifier decisions on identical cases as a diagnostic for underspecified policy — no prior corpus source identifies this approach.
  - **4% / 7% / 40% production metrics**: first published production metrics for classifier-governed agent autonomy, providing calibration benchmarks for teams designing similar systems.
  - **Eval set relabeling as operational cost of policy changes**: named explicitly as an engineering maintenance challenge — no prior corpus source surfaces this problem.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The Auto-review architecture should be the canonical example of "classifier-in-execution-path" design. Add the three-layer architecture (allowlist → sandbox → classifier) as the production pattern for agent action governance. The RPC stream placement decision (inline subagent, not a separate endpoint) is a concrete latency-tradeoff discussion for teams designing approval systems. The classifier tools (ReadFile, Grep, Glob, ListDir — no write) demonstrate least agency applied to the classifier itself.

- **Chapter 02 (Harness Engineering)**: The model selection insight (lower-reasoning models may increase latency due to policy understanding failures; find "a small model with enough reasoning to make the decision cleanly") is actionable guidance for teams selecting models for in-loop classifiers. Pair with `blog-cursor-security-agents.md` Claim 3 (Gemini Flash 2.5 for deduplication within a Claude agent workflow) to build a multi-model routing section: use the cheapest capable model for a specific subtask, but verify that "cheapest" accounts for decision quality, not just parameter count.

- **Chapter 03 (Safety and Verification)**: Add the "autonomy dial rather than switch" concept as the organizing principle for agent safety system design. The intent-alignment evaluation frame ("not whether the action looks risky in isolation, but whether it is justified by what the user asked the agent to do") should be the named alternative to rule-based action blocking. Add flapping detection and eval-set relabeling as concrete calibration and maintenance techniques for governance classifiers.

- **Chapter 03 (Safety and Verification)**: The block-and-explain feedback loop (block to parent agent, not user; enable autonomous self-correction; interrupt user only as last resort) is the operational design that achieves the 40%→7% interruption reduction. Any guide section on reducing approval fatigue should name this pattern and its production evidence.

- **Chapter 05 (Team Adoption)**: The 40%→7% interruption rate improvement is direct evidence for the adoption argument: approval-first designs produce fatigue at scale; contextual classifier designs are operationally sustainable. Add alongside the Amplitude risk-stratified auto-merge metrics (`blog-cursor-amplitude-autonomous-pipeline.md`) as converging evidence that autonomy governance design directly affects adoption outcomes.

- **Chapter 05 (Team Adoption)**: The evaluation methodology (12 hours of internal sessions → 6,122 labeled rows; synthetic coverage for rare high-consequence cases; flapping detection; relabeling on policy change) is a replicable framework that teams can adapt when building similar classifiers. Present it as the minimum viable evaluation process for any classifier entering the agent execution path.

## Extraction Notes

- Source is an official Cursor blog post authored by two named engineers. Travis McPeak's prior disclosure in `blog-cursor-security-agents.md` and the level of technical specificity (RPC stream placement, model selection rationale, flapping detection, labeled eval counts) are consistent with genuine engineering disclosure rather than marketing abstraction.
- The blog post was read in full. No sub-pages are linked beyond three related Cursor articles (sandboxing, cloud agents, Composer 2.5), which are separately tracked in the corpus.
- The exact model used for the Auto-review classifier is not disclosed. The description ("small model with enough reasoning to make the decision cleanly") implies a deliberate model selection tradeoff but names no specific model.
- Production metrics (4%, 7%, 40%) are self-reported by the team that built and operates the system. The 40% baseline is attributed to "enterprise customers" without specification — it may be Cursor's measurement of customer behavior rather than their own self-measure. Rated `emerging`.
- The article explicitly limits Auto-review to local desktop agents at time of publication. The "future vision" of extending to cloud agent contexts is aspirational.
- Per MINER.md §2a: several "quotes" in this note are marked as no direct quote available because the extraction tool returned paraphrased summaries for those specific claims. Claims 7, 8, 11, and 12 use `(no direct quote; ...)` per the required format. Claims 1–6, 9, and 10 use verbatim or near-verbatim passages consistent across two independent fetches of the source.
