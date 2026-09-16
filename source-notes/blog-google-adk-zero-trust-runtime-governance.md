---
source_url: https://developers.googleblog.com/build-zero-trust-ai-agents-that-judge-intent-not-just-syntax/
source_type: blog-post
title: "Build zero-trust AI agents that judge intent, not just syntax"
author: Eric Dong (Developer Relations Engineer), Shubham Saboo (Senior AI Product Manager)
date_published: 2026-09-15
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: emerging
issue: "#3481"
---

# Build zero-trust AI agents that judge intent, not just syntax

> Part 2 of Google's zero-trust agents series: moves security enforcement from the build-time, code-level controls of Part 1 (signed writes, gVisor sandboxing, a regex-based gateway) to three managed runtime controls on the Gemini Enterprise Agent Platform — an AI firewall (Model Armor), an LLM-based intent-vs-business-rules policy engine (Semantic Governance Policies), and fleet-wide multi-turn behavioral anomaly detection with closed-loop remediation — demonstrated against the same Customer Support & Returns Agent refund scenario from Part 1.

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party technical implementation guide, published Sept. 15, 2026)
- **Author credibility**: Eric Dong (Developer Relations Engineer) and Shubham Saboo (Senior AI Product Manager) — the same two named Google staff who authored Part 1 (`blog-google-adk-zero-trust-agents.md`), writing on Google's own developer blog about Google's own platform (Gemini Enterprise Agent Platform, Model Armor, Semantic Governance Policies, Agent Anomaly Detection, Agent Gateway, Security Command Center). This is first-party vendor guidance describing managed platform features they built; the code samples (Model Armor Python client calls, the YAML policy file, the anomaly-detection stand-in, the remediation-loop script) are backed by an open-source companion repository (`GoogleCloudPlatform/generative-ai/tree/main/agents/adk/zero-trust-agents-2`) referenced throughout, though this extraction did not clone and run that repository. Claims about production Google Cloud service behavior (Model Armor's detection accuracy, Agent Anomaly Detection's statistical models, Security Command Center integration) are vendor claims about Google's own products, not independently verified.
- **Scope**: Covers three managed runtime controls that replace/complement Part 1's build-time controls: (1) Model Armor, an inline AI firewall screening prompts (ingress) and responses (egress), (2) Semantic Governance Policies, a natural-language policy engine that evaluates proposed tool calls against user intent and business rules before they execute, (3) Agent Anomaly Detection, fleet-wide session telemetry analysis for multi-turn attack patterns, plus a "closed-loop remediation" workflow for turning a detected anomaly into a new policy without redeploying agent code. Demonstrated against a single worked scenario (a $149.00 order with a $29.00 physical item and a $120.00 digital license) walking through four attack variants: brute-force prompt injection, social-engineered single-turn refund request, and an incremental multi-turn drain attack. Does **not** cover: cost/latency overhead of the three runtime controls, red-team validation of Model Armor or Semantic Governance Policies against adversarial bypass attempts, false-positive/false-negative rates for Agent Anomaly Detection's statistical models, or non-Google-Cloud deployment targets.

## Extracted Claims

### Claim 1: Google's Part 1 build-time controls (signed writes, gVisor sandboxing, regex-based gateway) share a structural limit — they can only catch attack patterns that were explicitly anticipated and encoded in advance, which fails against socially-engineered requests and cross-turn attacks
- **Evidence**: Stated as the direct motivation for the entire Part 2 architecture, illustrated with three concrete failure cases (SQL parser cannot distinguish a socially engineered refund from a legitimate one if syntax is valid; regex cannot distinguish a physical cable from an opened software license; a single-turn test suite cannot catch fleet-wide multi-turn draining).
- **Confidence**: settled (first-party architectural rationale, internally consistent with the rest of the post's worked examples)
- **Quote**: "Those controls work, but they share one limit: they only catch cases that you can explicitly specify ahead of time. A SQL parser cannot tell a socially engineered refund from a legitimate one if the syntax is valid. A regex cannot tell the difference between a physical USB cable and an opened software license. And a single-turn test suite cannot catch an agent fleet being drained across multiple turns."
- **Our assessment**: This is a clean statement of the deterministic-vs-semantic security tradeoff, and it's an honest one — Google isn't claiming Part 1's controls were wrong, only that they have a bounded coverage envelope. The three failure cases are well-chosen because each maps to one of the three new runtime controls introduced later in the post (Model Armor, Semantic Governance Policies, Agent Anomaly Detection respectively), which suggests the architecture was designed backward from these specific gaps rather than the gaps being illustrative afterthoughts.

### Claim 2: Model Armor is an inline AI firewall that screens prompts at ingress and responses at egress; on a filter match it drops the request at the edge with an HTTP 403 before the agent's model is ever invoked, so no tokens are consumed
- **Evidence**: Definition plus a Python code sample wrapping the `modelarmor_v1.ModelArmorClient.sanitize_user_prompt` call, with an explicit branch returning `{"action": "BLOCK", "status": 403}` on `FilterMatchState.MATCH_FOUND`.
- **Confidence**: settled (first-party product description with an accompanying API code sample)
- **Quote**: "Model Armor: An in-line AI firewall that screens prompts and responses for prompt injection, jailbreaks, malicious URLs, and sensitive data leakage." … "When a filter matches, the request is dropped at the edge with a 403. The agent's model is never invoked, so no tokens are consumed and the context window stays clean."
- **Our assessment**: The "no tokens consumed, context window stays clean" framing is a concrete operational advantage over Part 1's approach (a regex gateway inside application code, which still required the request to reach the agent process). Blocking before model invocation is the same principle as the Part 1 semantic gateway (`blog-google-adk-zero-trust-agents.md` Claim 8), just moved from application code to platform-managed infrastructure — this is a deployment-location change, not a new security principle.

### Claim 3: Semantic Governance Policies is an LLM-based natural-language policy engine that evaluates each proposed tool call against user intent and business rules before the call is allowed to run, catching attacks that pass every deterministic check because the terms used (e.g., "Google Workplace user license") don't lexically match a hardcoded rule (e.g., "software")
- **Evidence**: Definition plus a worked attack: a social-engineering request for a $120.00 refund on a "Google Workplace user license" passes Model Armor (no injection signature), passes the order-total check ($120 < $149 total), and passes SQL type-checking, but should be denied because company policy bars refunds on digital software licenses over $30 without manager approval — and no regex or keyword list reliably maps "Google Workplace user license" to "digital software."
- **Confidence**: settled (first-party description with a full worked example, a YAML policy definition, and a corresponding Cloud Logging JSON verdict)
- **Quote**: "Semantic Governance Policies: An LLM-based natural-language policy engine that evaluates each proposed tool call against user intent and your business rules before the call runs."
- **Quote** (why deterministic rules fail here): "Because the prompt and perhaps the order itself refers to a \"Google Workplace user license\" rather than explicitly saying \"software,\" keyword matching and regex filters fail to catch it, and a SQL parser has no way to know that a \"Google Workplace user license\" is digital software - which is why we rely on Semantic Governance Policies."
- **Our assessment**: This is the article's strongest and most specific claim, and it's a genuinely different mechanism from Part 1's semantic gateway — Part 1's gateway used regex/heuristic matching (deterministic, pattern-based), while this engine reasons semantically about whether an item description falls under a policy category. The tradeoff the post doesn't address: an LLM-based policy judge is itself a model that could misclassify or be manipulated, and the post gives no adversarial-robustness data for the policy engine itself (only for the upstream Model Armor firewall).

### Claim 4: Semantic Governance Policy rules are authored as plain-text natural-language constraints in a YAML file scoped to specific tools, readable and editable by a non-engineer policy owner rather than requiring a code change
- **Evidence**: A YAML example (`policies/refund-policy-category.yaml`) with `target_tools: [issue_refund]` and a `constraints:` block in prose, plus the claim that changing enforcement means editing this file rather than application code.
- **Confidence**: settled
- **Quote**: "Rules are written as plain-text constraints, so a business owner can read and change them"
- **Our assessment**: This is a real workflow shift worth flagging for the guide's governance-ownership discussion: it moves the edit surface for a security/business rule from a pull request against agent code to a policy-console change. That's faster to iterate but also means the rule's correctness now depends on how well the natural-language constraint is worded, and the post gives no versioning, review, or testing story for these policy files (contrast with Part 1's Claim 9, which explicitly treats gateway rules as software contracts with CI regression tests).

### Claim 5: Agent Anomaly Detection analyzes session telemetry across an entire agent fleet using statistical models and LLM analysis to flag behavioral patterns invisible to any single-turn check — specifically tool-call velocity, repeated writes against one entity, and cumulative parameter values exceeding a baseline
- **Evidence**: Definition plus a worked multi-turn attack: eight sequential $20.00 refund requests against the same $149.00 order, each individually valid under the $30 software-refund threshold, cumulatively draining $160.00 — more than the order's total value. A Python code stand-in (`demo/aad_engine.py`) implements three named detectors: `repeated_tool_call`, `cumulative_limit_exceeded`, `single_entity_write_velocity`.
- **Confidence**: settled (first-party description with runnable demo code, though production detection accuracy is unverified — the post itself states the numbers are illustrative)
- **Quote**: "Agent Anomaly Detection: LLM-driven agent log and telemetry analysis that flags unusual behavior across a session, such as a refund drained across many turns."
- **Quote** (on why single-turn checks miss it): "Every turn passed Model Armor, passed the single-turn policy engine, and received a valid Cloud KMS signature. Each $20.00 refund is allowed on its own because it is software under the $30.00 limit. Only in aggregate does the problem appear: the attacker extracted $160.00 total from $20.00 refunds, surpassing their initial $149.00 order. Single-turn guardrails evaluate each request in isolation, so they cannot see cumulative drainage or multi-turn velocity."
- **Our assessment**: This directly names the temporal/behavioral gap that neither Part 1's deterministic gateway nor this post's own Semantic Governance Policies cover on their own — each of the three runtime controls is explicitly single-purpose and the post is honest that they only work "together" (see Claim 6). The post caveats its own detector output: "The detector names, confidence values, and finding shape above are illustrative," which we read as an acknowledgment that the shipped confidence scores (0.95, 0.80, 0.80 in the sample code) are demo placeholders, not calibrated production thresholds.

### Claim 6: Each of the three runtime controls (Model Armor, Semantic Governance Policies, Agent Anomaly Detection) covers a distinct threat category that the other two cannot, so none of them is a substitute for the others
- **Evidence**: Explicit statement following the three definitions, and borne out by the worked example: the injection attack is caught only by Model Armor, the mislabeled-license attack is caught only by Semantic Governance Policies (Model Armor and the order-total check both pass it), and the multi-turn drain is caught only by Agent Anomaly Detection (every individual turn passes both Model Armor and the policy engine).
- **Confidence**: settled
- **Quote**: "Each control covers what the others cannot. Model Armor filters the payload, the policy engine reasons about intent, and anomaly detection watches behavior over time."
- **Our assessment**: Structurally this is the same "defense in depth, no single layer is sufficient" argument Part 1 made about its three build-time controls (Part 1 Claim 10). The pattern repeats at the runtime layer: this post is not proposing runtime governance as a replacement for build-time controls, but as an additional layer that catches what build-time controls structurally cannot (see Claim 9 below on the "defense in depth: build-time plus runtime" framing).

### Claim 7: Moving security enforcement from application code to a managed runtime platform changes who owns the rules — governance becomes the responsibility of a platform or security administrator, separate from the agent developer, because the platform enforces the rules outside the agent's own code
- **Evidence**: Stated directly in the post's framing of what changes between Part 1 and Part 2, and reflected mechanically in the closed-loop remediation workflow (an administrator, not the agent developer, authors the new policy constraint in response to a detected anomaly).
- **Confidence**: emerging (organizational/ownership claim, asserted rather than empirically demonstrated — the post shows one hypothetical administrator action, not evidence about how this plays out across real organizations)
- **Quote**: "Moving the checks to the platform also changes who owns them. Governance is defined and managed by a platform or security administrator, separate from the agent developer, because the platform enforces it outside of the agent code."
- **Our assessment**: This is a significant, under-examined claim for the guide's governance-ownership discussion. It implies a security/platform team now needs enough context about each agent's business logic (e.g., "a Workplace license over $30 requires manager approval") to write and maintain correct semantic policies — which is a different skill and organizational placement than writing application code. The post doesn't address the coordination cost of this split (e.g., what happens when the agent's business logic changes but the separately-owned policy file isn't updated), which is a real risk in this architecture.

### Claim 8: Closed-loop remediation lets an administrator (or an automated pipeline) turn a detected multi-turn anomaly into an enforced Semantic Governance Policy constraint that takes effect on the next tool call, with no agent code change, rebuild, or redeploy
- **Evidence**: Described narratively plus a runnable code sample (`demo/remediation_loop.py`) that reads a Security Command Center finding of type `AGENT_SESSION_ANOMALY` and calls `sgp_client.create_policy(...)` with a new natural-language constraint ("Deny any issue_refund call when the conversation history already contains an approved refund for the same order_id in this session").
- **Confidence**: settled (first-party description with runnable demo code)
- **Quote**: "Because Semantic Governance Policies are evaluated dynamically at runtime, you can close the loop without modifying or redeploying agent code: an administrator simply opens the Semantic Governance Policies experience, reviews the flagged trace, and authors a new natural-language constraint that covers the multi-turn pattern."
- **Quote** (on redeploy-free activation): "The new policy is evaluated by Agent Gateway on the next tool call, with no agent redeploy or restart."
- **Our assessment**: This is the article's most concrete operational claim and the one most directly useful for an incident-response chapter: mean-time-to-remediate for a newly discovered multi-turn attack pattern is bounded by policy-authoring time, not by a code-deploy cycle, because the enforcement point (Agent Gateway) reads policy state dynamically. The tradeoff is that this speed depends entirely on the natural-language constraint being both correct and narrowly scoped — an overly broad post-incident constraint (e.g., blocking all refunds instead of same-order-repeat refunds) could cause new false positives, and the post gives no review/approval step before a new constraint goes live.

### Claim 9: Runtime governance controls are additive to, not a replacement for, Part 1's build-time controls — every write is still cryptographically signed with the same Cloud KMS agent identity from Part 1, even after Model Armor, Semantic Governance Policies, and Agent Anomaly Detection are layered in
- **Evidence**: The scenario explicitly reuses Part 1's `issue_refund` tool "signing the request with the agent's own Cloud KMS asymmetric key, the same hardware-backed identity from Part 1," and the post's closing summary restates all four layers (edge screening, intent-based tool-call gating, signed writes, fleet-wide multi-turn detection) as operating together.
- **Confidence**: settled
- **Quote**: "Every prompt is screened at the edge before the model runs, every proposed tool call is judged against intent and business rules before any state changes, every write is still signed with a hardware-backed Cloud KMS key, and multi-turn exploits that no single-turn check can see are caught by fleet telemetry and closed off with a policy that takes effect at runtime."
- **Our assessment**: This confirms the two-part series is intentionally cumulative rather than Part 2 superseding Part 1 — a guide chapter citing this source should present it as "build-time controls (Part 1) + runtime controls (Part 2)," not as runtime governance being the more modern replacement for deterministic gating. That framing matters because it means the guide's existing Part-1-sourced recommendations (signed writes, gVisor sandboxing) remain valid advice, not superseded ones.

## Concrete Artifacts

**Model Armor ingress screening (Python, via Agent Gateway):**
```python
from google.api_core.client_options import ClientOptions
from google.cloud import modelarmor_v1

client = modelarmor_v1.ModelArmorClient(
    transport="rest",
    client_options=ClientOptions(
        api_endpoint="modelarmor.us-central1.rep.googleapis.com"
    ),
)

def screen_ingress(user_prompt: str) -> dict:
    request = modelarmor_v1.SanitizeUserPromptRequest(
        name="projects/agent-security-fleet-prod/locations/us-central1/templates/enterprise-strict",
        user_prompt_data=modelarmor_v1.DataItem(text=user_prompt),
    )
    response = client.sanitize_user_prompt(request=request)
    result = response.sanitization_result
    if result.filter_match_state == modelarmor_v1.FilterMatchState.MATCH_FOUND:
        # Dropped at the perimeter before the agent's model runs
        return {"action": "BLOCK", "status": 403}
    return {"action": "ALLOW"}
```
*(Source: "1. Screen every prompt at the edge: Model Armor" section)*

**Semantic Governance Policy definition (YAML):**
```yaml
# policies/refund-policy-category.yaml
name: refund-policy-category
target_tools: [issue_refund]
constraints: |
  Refunds for opened digital goods, software licenses, or clearance items
  over 30 USD must be denied and routed to a human manager.
  Refunds for physical hardware accessories up to 149 USD are allowed.
enforcement: BLOCK
```
*(Source: "2. Judge intent, not just syntax: Semantic Governance Policies" section)*

**Semantic Governance denial event (Cloud Logging JSON):**
```json
{
  "evaluations": [
    {
      "actionName": "issue_refund",
      "rationale": "The tool attempted to refund $120.00 for 'Workplace User License', a digital software product. Digital software refunds over $30 require manager authorization.",
      "toolName": "order_processing",
      "verdict": "DENY"
    }
  ],
  "timestamp": "2026-09-03T15:52:21.447123Z",
  "token_usage": 2576,
  "verdict": "DENY"
}
```
*(Source: same section, abridged — original includes a `token_usage_breakdown` sub-object)*

**Multi-turn drain attack trace:**
```
Turn 1:  refund $20  ->  policy: ALLOW (software, under $30)  ->  KMS sign  ->  ledger:  $20.00
Turn 2:  refund $20  ->  policy: ALLOW (software, under $30)  ->  KMS sign  ->  ledger:  $40.00
...
Turn 7:  refund $20  ->  policy: ALLOW (software, under $30)  ->  KMS sign  ->  ledger: $140.00
Turn 8:  refund $20  ->  policy: ALLOW (software, under $30)  ->  KMS sign  ->  ledger: $160.00
```
*(Source: "3. Catch multi-turn exploits: Agent Anomaly Detection" section — attacker extracts $160.00 against a $149.00 order)*

**Agent Anomaly Detection stand-in (Python, from the companion demo):**
```python
# demo/aad_engine.py  (local stand-in for Agent Anomaly Detection)
def evaluate_session_anomalies(session_history: list, order_baseline: float) -> list[dict]:
    findings = []
    refunds = [t for t in session_history
               if t["tool"] == "issue_refund" and t["status"] == "APPROVED"]
    cumulative = sum(t["args"]["amount"] for t in refunds)
    if len(refunds) >= 3:
        findings.append({"detector": "repeated_tool_call", "confidence": 0.95})
    if cumulative > order_baseline:
        findings.append({"detector": "cumulative_limit_exceeded", "confidence": 0.80})
    if len({t["args"]["order_id"] for t in refunds}) == 1 and len(refunds) >= 2:
        findings.append({"detector": "single_entity_write_velocity", "confidence": 0.80})
    return findings
```
*(Source: "3. Catch multi-turn exploits: Agent Anomaly Detection" section)*

**Closed-loop remediation (Python, from the companion demo):**
```python
# demo/remediation_loop.py (wire a Security Command Center finding to a new policy)
def remediate(finding: dict, sgp_client) -> None:
    if finding.get("findingType") != "AGENT_SESSION_ANOMALY":
        return
    agent_id = finding.get("agent", {}).get("id", "support-refund-agent")
    constraint = (
        "Deny any issue_refund call when the conversation history already "
        "contains an approved refund for the same order_id in this session. "
        "Route the request to a human manager instead."
    )
    sgp_client.create_policy(
        name="refund-policy-single-order-limit",
        target_agent=agent_id,
        target_tools=["issue_refund"],
        constraint=constraint,
        enforcement="BLOCK",
    )
    # The new policy is evaluated by Agent Gateway on the next tool call,
    # with no agent redeploy or restart.
```
*(Source: "3. Catch multi-turn exploits: Agent Anomaly Detection" section)*

**Scenario setup:** Order #99281, $149.00 total — a USB-C Pro Docking Station and Cable at $29.00 (physical) and an annual Workplace User License at $120.00 (digital), used across all four attack demonstrations because the physical/digital split is what the license-refund and drain attacks turn on.

**Companion repository:** `zero-trust-agents-2` at `github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/zero-trust-agents-2` — includes an interactive four-act CLI demo (`./demo/run_part2_demo.sh`), a browser dashboard (`python3 -m http.server 8000`), and a deterministic unit test suite (`python3 -m unittest demo/test_runtime_governance.py`). Not cloned or run for this extraction.

## Cross-References

- **Corroborates**:
  - `blog-google-adk-zero-trust-agents.md` (Part 1) — this post explicitly extends Part 1's scenario (same Customer Support & Returns Agent, same Cloud KMS-signed `issue_refund` tool) and its "layered controls, none sufficient alone" structure repeats Part 1 Claim 10's argument that no single security layer covers every threat.
  - `blog-cursor-agent-autonomy-auto-review.md` Claim 2 ("Effective risk assessment must be based on user intent alignment, not action isolation") — Semantic Governance Policies (Claim 3 here) is a concrete platform-level implementation of exactly this principle: judging a tool call by whether it's consistent with stated intent and business rules, not by pattern-matching the request in isolation.
- **Extends**:
  - `blog-google-adk-zero-trust-agents.md` (Part 1) Claim 8 — Part 1's "Semantic Gateway" used deterministic regex/heuristic rules for both prompts and tool calls; this post's Model Armor (Claim 2) and Semantic Governance Policies (Claim 3) split that single gateway into an ingress/egress AI firewall and a separate LLM-based intent-reasoning policy engine, adding a genuinely new mechanism (semantic reasoning about item categories, not just pattern matching) that Part 1 did not have.
  - `blog-google-adk-zero-trust-agents.md` (Part 1) Claim 9 (gateway rules as CI-tested software contracts) — this post's Claim 4 (natural-language YAML policies editable by a "business owner") describes a materially different rule-maintenance workflow with no stated testing or review discipline, which is worth flagging as a regression in rigor even though it's a gain in editability. Not a contradiction (both can be true of their respective layers — deterministic gateway rules stay CI-tested, semantic policies are the new looser layer) but a tradeoff the guide should name explicitly.
  - `blog-anthropic-ciso-guide-agentic-ai.md` Claim 4 (agent drift from operator intent resembles an insider attack, and insider response times are too slow for agent speed) — this post's closed-loop remediation (Claim 8) is a concrete answer to exactly that response-speed problem: a policy fix that takes effect on the next tool call with no redeploy is a faster remediation path than the insider-incident timelines the CISO guide cites as inadequate.
- **Novel**: The specific mechanism of an LLM-based policy engine reasoning about semantic category membership (is "Google Workplace user license" an instance of "digital software license"?) rather than deterministic pattern matching is new to the corpus — no existing source note describes a security control that requires the enforcement layer itself to perform semantic classification. The "closed-loop remediation" pattern (detection → administrator or automated policy authoring → runtime-evaluated fix with no redeploy) is also new; existing corpus incident-response guidance (`blog-anthropic-ciso-guide-agentic-ai.md` Claim 15, "automate the bookkeeping around incidents, not the decisions") discusses human-in-the-loop incident response generally but not this specific redeploy-free remediation mechanism.
- **Contradicts**: None identified. This source's claims are additive to and consistent with the existing Google ADK zero-trust note and don't conflict with the Anthropic zero-trust framework or CISO guide notes — no contradiction issue filed.

## Guide Impact

- **Ch06 (Security Threat Model)**: The chapter's threat-model section currently (per the existing `blog-google-adk-zero-trust-agents.md`-sourced material) frames prompt/tool-call gating as deterministic, regex-based filtering. This source provides evidence that a second, complementary layer — semantic/intent-based gating that can catch attacks a deterministic rule cannot lexically match — is a real, currently-shipping alternative, not just a hypothetical improvement. Recommend adding a worked example (the "Google Workplace user license" vs. "software" mismatch, Claim 3) as a concrete illustration of *why* deterministic rules alone are insufficient — this is a more specific failure mode than the guide's likely-generic "regex rules are brittle" framing.
- **Ch06 (Security Threat Model) — multi-turn attacks**: The chapter should add multi-turn/cross-session drain attacks as a named threat category distinct from single-request attacks, citing Claim 5's worked example (eight $20 refunds cumulatively exceeding a $149 order total, each individually policy-compliant). Currently the guide's threat model (built from Part 1 and the Anthropic zero-trust note) treats each request/session largely in isolation; this source is the first in the corpus to name "single-turn guardrails cannot see cumulative drainage or multi-turn velocity" as a distinct, unaddressed gap requiring fleet-level telemetry.
- **Ch04 (Runtime Governance & Incident Response)**: Add closed-loop remediation (Claim 8) as a named incident-response pattern: a detected anomaly can be resolved by authoring a new natural-language policy constraint that takes effect on the next tool call with no code redeploy, which is meaningfully faster than a code-fix-and-redeploy remediation cycle. Pair this with the caveat from our assessment of Claim 8 — the guide should recommend a review/approval step for post-incident policy constraints, since the source shows no such step and an overly broad emergency constraint could introduce new false positives.
- **Ch04 (Runtime Governance & Incident Response) — ownership**: Claim 7 (governance ownership shifts from agent developer to platform/security administrator when enforcement moves to the platform layer) should be surfaced as an open organizational question, not adopted as settled guidance — flag it as "emerging" per its confidence rating, since the source asserts this ownership split without addressing the coordination risk between agent developers and policy administrators.

## Extraction Notes

- Fetched the full article via `curl` and stripped HTML tags to plain text to verify every quote above against the raw source text directly (not solely via a summarizing fetch tool), because the summarized first-pass extraction returned at least two quotes with ellipses or reconstructed phrasing that could not be confirmed as verbatim. Two candidate quotes from that first-pass summary were dropped ("company policy dictates that digital software licenses over $30 are non-refundable without manager approval" as an isolated sentence, and a spliced anomaly-detection/remediation quote joined by "...") because the ellipsis-joined version does not appear as a contiguous passage in the source; the surrounding sentences are quoted separately and correctly above instead.
- Did not clone or run the companion GitHub repository (`zero-trust-agents-2`); all code artifacts above are reproduced from the blog post itself, which the post states are drawn directly from that repository.
- The post links to "Part 1" (already in the corpus as `blog-google-adk-zero-trust-agents.md`) and to Agent Platform governance documentation; did not follow the governance documentation link since it is product documentation rather than a distinct narrative source, and the Prospector's triage did not flag it as a separate extraction target.
- The Prospector's issue comments contain two differently-worded triage assessments (posted roughly a minute apart). The second, more detailed comment was used as primary extraction guidance since it more precisely identifies the three runtime controls and the code-level-to-platform-level governance shift as the extraction focus; both comments agree on the core novelty assessment (this is genuinely new implementation detail beyond Part 1, not a restatement).
