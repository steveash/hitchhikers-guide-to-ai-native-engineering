---
source_url: https://developers.googleblog.com/check-what-your-ai-agents-do-before-they-do-it-with-semantic-governance-policies/
source_type: blog-post
title: "Check what your AI agents do before they do it, with Semantic governance policies"
author: Deepti Sehrawat (Software Engineer, Google)
date_published: 2026-11-20
date_extracted: 2026-11-22
last_checked: 2026-11-22
status: current
confidence_overall: emerging
issue: "#4898"
---

# Check what your AI agents do before they do it, with Semantic governance policies

> Google's Preview announcement of an out-of-process LLM judge that gates every tool call an agent proposes, before it runs, against the user's original request and plain-language policies. It is a useful design pattern for the preventive layer, but the post publishes no effectiveness, false-positive, latency or cost numbers.

## Source Context

- **Type**: blog-post (vendor product announcement, Google Developers Blog; feature is in Preview)
- **Author credibility**: Deepti Sehrawat is listed as a Software Engineer on Google's developer blog, describing a Google product. First-party description of the architecture, but not an independent evaluation.
- **Scope**: Covers the architecture (policy enforcement point, LLM judge, two checks), one illustrative three-call example, policy-writing examples, a `gcloud` command, limits, and a rollout checklist. Does not cover: measured block or false-positive rates, latency or token cost per call, judge robustness to injected content, or ambiguous user requests. The post promises a follow-up on AgentDojo results, which is not yet read here.

## Extracted Claims

### Claim 1: Permissions cannot catch a call that is allowed by scope but violates a rule, so the check must sit outside the agent
- **Evidence**: Architectural argument plus the earnings-leak example, where the agent has legitimate read and send-email access.
- **Confidence**: emerging (sound reasoning; no measurement)
- **Quote**: "Permissions alone can't catch this. They say what an agent can do, not whether a particular call follows your rules."
- **Our assessment**: Restates the capability-versus-content distinction. Buy it. It is the motivating gap for an inline content-aware check on top of IAM-style scoping.

### Claim 2: A model can be talked out of its system-instruction rules by users or injected documents, so enforcement belongs in a separate layer
- **Evidence**: Assertion only; no experiment in this post.
- **Confidence**: settled as a principle (matches the corpus), anecdotal as presented here
- **Quote**: "A model can also be talked out of the rules in its system instructions, by a user with a good reason, or by a document telling it to do something nobody asked for, a technique called indirect prompt injection."
- **Our assessment**: Consistent with the corpus rule that prompts are not security boundaries. Note the irony the post leaves unaddressed: the enforcement layer is itself an LLM judge reading the same conversation (see Claim 6).

### Claim 3: Each proposed tool call is checked against two things, and must pass both: plain-language policies and the user's original intent
- **Evidence**: Design description; the intent check is "on by default to protect against hijacking".
- **Confidence**: emerging
- **Quote**: "A call has to pass both checks to run."
- **Our assessment**: The two-check split is the core pattern: author-written rules (what the organisation forbids) plus a generic anti-hijack check (what the user did not ask for). The post does not say how the intent check behaves when the user's request is ambiguous or broad.

### Claim 4: Enforcement happens at a gateway that intercepts the model's response, before the agent sees it, and a failing response is replaced wholesale
- **Evidence**: Architecture description; Agent Gateway is the only supported enforcement point today and all agent egress must route through it.
- **Confidence**: emerging
- **Quote**: "If it doesn't, the engine replaces the response's content, tool calls included, with a configurable denial message, so the call never runs."
- **Our assessment**: Placing the check on the model-to-agent path means the agent's own code needs no changes and cannot skip it. The whole response is replaced, not just the offending call or argument (the example notes the whole send_email is denied, not only the Gmail copy). This is coarse-grained, which is safe but may frustrate legitimate multi-step turns.

### Claim 5: The judge sees the conversation, system instructions, tool descriptions and policies; policies depend on facts placed in the system instructions
- **Evidence**: Stated as a design constraint and as advice.
- **Confidence**: emerging
- **Quote**: "an LLM judge evaluates the proposed call against the conversation so far, the agent's system instructions and tool descriptions, and your policies."
- **Our assessment**: Practical implication: the policy is not self-contained. The earnings date lives in the agent's system prompt, so the harness must keep prompt facts and policies in sync. Also means tool descriptions become part of the security surface.

### Claim 6: Verdicts are probabilistic, so run in dry-run mode before enforcing and layer with other controls
- **Evidence**: The post's own caveat. No error rates given.
- **Confidence**: settled (that LLM judges are probabilistic) / anecdotal (no numbers)
- **Quote**: "Because verdicts come from an LLM, which is probabilistic, they may vary."
- **Our assessment**: Honest and important. The post is silent on whether the judge can itself be injected by content in the conversation it reads, and on latency and per-call token cost (although it says Cloud Logging records "the tokens it used"). Treat as a probabilistic filter, not a boundary.

### Claim 7: Policies are natural-language constraints that non-engineers can write and change without a redeploy, scoped to all tools or one tool
- **Evidence**: Policy examples (approvals, a refund limit of $80, human review of hiring decisions) and a `gcloud beta ai semantic-governance-policies create` command.
- **Confidence**: emerging
- **Quote**: "Legal, compliance, and business teams write and change them without code or a redeploy."
- **Our assessment**: Enables team-level adoption where compliance owns rules. The trade-off against deterministic gateways (the corpus's ADK zero-trust note) is that a numeric limit like "$80 or less" is enforced by a model's reading rather than by exact code. Hard numeric bounds should stay deterministic.

### Claim 8: Policy rules take precedence over the user's request, including claimed exceptions such as NDAs
- **Evidence**: Worked example 2: the investor email was denied "the employee did ask, but your rules take precedence over the request".
- **Confidence**: anecdotal (one illustrative scenario)
- **Quote**: "Never send them to external or personal addresses, investors, analysts, or press, regardless of NDAs, urgency, or the requester's seniority."
- **Our assessment**: Good policy-writing lesson: pre-empt anticipated exceptions explicitly in the policy text. Only one scenario is shown, with no adversarial wording variants.

### Claim 9: The built-in intent check blocks injected instructions that no policy anticipated
- **Evidence**: Worked example 3: hidden text in a planning doc triggers `delete_file`, denied because "nobody asked for it, and no policy allows deletions".
- **Confidence**: anecdotal (single example; follow-up AgentDojo post promised but not yet published)
- **Quote**: "Denied by the intent check: nobody asked for it, and no policy allows deletions."
- **Our assessment**: Plausible mechanism (compare action to the user's request). Effectiveness against adaptive injection is unvalidated here.

### Claim 10: Every verdict and the judge's rationale are logged, giving an audit trail, but rationales may quote policy text to users
- **Evidence**: Description of Cloud Logging output and a custom denial message option.
- **Confidence**: emerging
- **Quote**: "The judge's rationale can quote your policy, so if users shouldn't see it, set your own denial message on the policy."
- **Our assessment**: Auditable decisions are valuable. The note about policy leakage via rationale is a small but real information-disclosure caveat.

### Claim 11: The check is inline and preventive, complementing IAM, Model Armor and out-of-band Agent Anomaly Detection as one layer of defense in depth
- **Evidence**: Positioning paragraph and Figure 3.
- **Confidence**: emerging
- **Quote**: "Agent Anomaly Detection analyzes sessions asynchronously, out of band."
- **Our assessment**: Gives the preventive half of the preventive/detective layering that the anomaly-detection notes describe from the detective side.

### Claim 12: Explicit limits: text-only and streamed responses are not evaluated, and the only enforcement point today is Agent Gateway
- **Evidence**: Stated limitations.
- **Confidence**: settled (stated by vendor)
- **Quote**: "Streamed model responses aren't evaluated."
- **Our assessment**: Text-only answers are exempt "because they take no action", which leaves data exposure through text to other controls (Model Armor, disclosure review). The streaming gap means an agent configured for streaming may bypass the check; verify before relying on it.

### Claim 13: Judge relies on tool descriptions and is instructed to deny calls to tools that have none
- **Evidence**: Rollout checklist step 3.
- **Confidence**: emerging
- **Quote**: "The judge relies on descriptions to understand a call, and is instructed to deny calls to tools that have none."
- **Our assessment**: Tool descriptions become a governance input; a missing description fails closed. Useful default.

## Concrete Artifacts

Policy and CLI, verbatim from the source (Google Developers Blog):

```
gcloud beta ai semantic-governance-policies create POLICY_ID \
    --location=LOCATION \
    --display-name="Earnings disclosure" \
    --agent=projects/PROJECT_ID/locations/LOCATION/agents/AGENT_ID \
    --natural-language-constraint="Quarterly financial results (revenue, margins, bookings, guidance) should not be shared publicly until the public earnings release. Before the release, they may be shared only with @example.com addresses. Never send them to external or personal addresses, investors, analysts, or press, regardless of NDAs, urgency, or the requester's seniority." \
    --agent-response-denial-message="I can't share unreleased financial results outside the company before the earnings release. Contact Investor Relations for approved disclosures." \
    --project=PROJECT_ID
```

Other policy examples from the post:

```
Approvals: "Submit invoices only after all approvals are received."
Spending limits: "Accept refund requests only where the amount is $80 or less."
Human review: "The agent may summarize resumes, but it must not send offer or rejection decisions. A person makes those."
```

Rollout checklist (paraphrased from "Get started"): provision the policy engine and connect it to Agent Gateway; enable dry run; give every tool a clear description; add policies and review verdicts in Cloud Logging; switch to enforcement.

Supported model APIs per the post: Gemini API, Anthropic Messages API, Claude models in Gemini platform, OpenAI-compatible Chat Completions APIs (including self-hosted vLLM).

## Cross-References

- **Corroborates**: `blog-google-adk-zero-trust-agents.md` Claim 1 (system prompts are soft constraints) is the same rationale as this post's Claim 2. `blog-google-agent-anomaly-detection-benchmarks.md` Claim 10 recommends "Semantic Governance Policy, Preview" as the preventive layer; this post is the primary source for that feature.
- **Contradicts**: None filed. No existing note takes the opposite position. The contrast with the deterministic approach is a trade-off (determinism versus flexibility), not a contradiction.
- **Extends**: `blog-google-adk-zero-trust-agents.md` Claim 8 (deterministic Semantic Gateway with regex checks) and Claim 9 (CI-tested policies): this post is the LLM-judged variant. Deterministic checks are exact but narrow; the judge handles natural-language rules but is probabilistic and has no published regression-testing story beyond dry run. `blog-google-agent-anomaly-detection.md` Claim 3 (asynchronous, out-of-band, no added latency) is the detective counterpart: this post's check is inline and so necessarily adds latency, which the post does not quantify. `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5 (manual/semi-automated/automated oversight tiers) and Claim 7 (NLP-scanned "never" list) describe the governance need that this product implements as plain-language policies.
- **Novel**: The two-check model (user intent plus policies) enforced at a gateway on the model-to-agent path; replacing the whole response on denial; a dry-run-then-enforce rollout; fail-closed on tools lacking descriptions; policy text can leak via the judge's rationale.

## Guide Impact

- **Chapter 06**: In the preventive-controls discussion (the intent-check row and the pre-execution versus out-of-band split), add this as an example of an inline LLM-judged gate, positioned between deterministic gateways (ADK zero-trust Claim 8) and detective monitoring (anomaly-detection notes). State plainly that the judge is probabilistic and that effectiveness is vendor-asserted and unmeasured, with the AgentDojo follow-up as the thing to watch.
- **Chapter 02**: Cite as an instance of enforcement outside the agent's code and prompt; note the practical dependency that tool descriptions and system-prompt facts feed the judge.
- **Chapter 05**: Optional mention: plain-language policies let compliance teams own rules without redeploys; keep hard numeric limits deterministic.

## Extraction Notes

- Fetched the full article HTML and read all text, including the example, policy list, CLI command, caveats and checklist. Figures 1-3 are images and were not read. Linked docs pages (overview, best practices) were not followed.
- No contradiction filed.
- All quotes are verbatim from the page text. No effectiveness metrics exist in the source; all effectiveness claims are vendor-asserted.
