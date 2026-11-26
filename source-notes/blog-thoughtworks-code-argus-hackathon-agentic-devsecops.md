---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/building-code-argus-hackathon-to-agentic-devsecops
source_type: blog-post
title: "Building Code Argus: From hackathon idea to agentic DevSecOps"
author: Sarath Kumar, Divyansha Jain and Surya Borusu (Thoughtworks)
date_published: 2026-11-25
date_extracted: 2026-11-26
last_checked: 2026-11-26
status: current
confidence_overall: anecdotal
issue: "#4971"
---

# Building Code Argus: From hackathon idea to agentic DevSecOps

> A three-person Thoughtworks hackathon team describes an agentic DevSecOps pipeline built on "the LLM proposes and deterministic code disposes": a code-only orchestrator, four LLM calls per hero flow, deterministic gates ahead of a cross-vendor Critic, and a list of concrete build failures (stub gates that always passed, hallucinated fixes, silently dropped graph edges).

## Source Context

- **Type**: blog-post (Q&A interview with the builders, Thoughtworks Insights)
- **Author credibility**: The three-person team that built Code Argus during the AI/works™ Innovation Hackathon (2026). First-hand build experience; Thoughtworks staff. The article is Thoughtworks-published and shows no sign of independent evaluation.
- **Scope**: Design rationale, failure reports, knowledge-base architecture (Neo4j + pgvector), scope decisions, and roadmap. It does NOT include benchmarks, fix-success rates, false-positive rates, code, or an independent evaluation. The cost figure (~$0.12/run) and the "dogfood" claim are author-reported and unverified.

## Extracted Claims

### Claim 1: The orchestrator should be pure code that routes on typed state; the LLM is spent only where genuine reasoning is required
- **Evidence**: Architecture description; the hero flow is said to have exactly four LLM calls (Triage, Fix, Critic on a different model, Reviewer). Git ops, build/test/scan execution, event routing, dedup, prioritization and story selection are deterministic. No code or traces shown.
- **Confidence**: emerging
- **Quote**: "The principle is that the LLM proposes and deterministic code disposes. An LLM call is spent only where genuine reasoning is required."
- **Our assessment**: Strong, specific statement of the deterministic-spine pattern; consistent with other sources in the corpus (see Cross-References). Self-reported from a hackathon-scale system, so treat it as a design pattern, not proof of production robustness.

### Claim 2: Deterministic gates run before the LLM Critic, so a red build or unsafe scan loops back to Fix at zero LLM cost, with a bounded loop and a safe fallback
- **Evidence**: Design description: at most three fix iterations, then deferral to a Jira story rather than a broken PR.
- **Confidence**: emerging
- **Quote**: "A failing test or an unsafe scan delta loops straight back to Fix without spending an LLM call, and the fix loop is bounded (at most three iterations, then it defers to a Jira story instead of opening a broken PR)."
- **Our assessment**: Ordering cheap deterministic checks before expensive LLM review is a sound cost/verification pattern. The "fail to a ticket, not a broken PR" fallback is a useful concrete escape hatch. The cap of three is an unjustified choice, not tuned from data.

### Claim 3: "No new vulnerabilities" should be a computed claim (delta SARIF of baseline vs. post-fix scan), not an asserted one
- **Evidence**: Described as the mechanism; no example output. The source text has a stray quotation mark in this passage (the opening quote before "No" is missing in the source).
- **Confidence**: emerging
- **Quote**: "a delta SARIF (baseline vs post-fix scan) proves it."
- **Our assessment**: A good concrete verification pattern: diff the scanner's before/after output instead of asking an LLM whether the patch is safe. It only proves absence of new findings the scanner can detect, so "proves" is stronger than warranted.

### Claim 4: Gates that were stubs always reported green; routing never inspected results — found only by internal review
- **Evidence**: First-person failure report. Fix: wired real runners and moved deterministic gates ahead of the Critic.
- **Confidence**: anecdotal
- **Quote**: "Gates that always said green: An internal review found our test/scan gates were stubs, and routing never inspected results."
- **Our assessment**: Valuable failure mode: a verification pipeline can look complete while its gates are inert. Implies a need for negative tests (deliberately failing input must turn the gate red). The team's response was a repo check banning fakes (see Claim 9).

### Claim 5: A fictional stack trace made the Fix agent invent a whole file; the remedy was real evidence, using a planted one-token bug
- **Evidence**: Demo incident. The planted bug is a one-token change that keeps all 932 tests green.
- **Confidence**: anecdotal
- **Quote**: "An early demo fed the Fix agent a fictional stack trace, and it dutifully invented an entire payment_gateway.py out of nothing."
- **Our assessment**: Concrete hallucination-under-thin-evidence report. Also a useful test-design idea: evaluate with a realistic defect that passes the existing suite. Note the fix is about the evaluation input; it does not show the agent now refuses to fabricate on thin evidence.

### Claim 6: A Critic from a different vendor's model, a delta-SARIF proof, a bounded loop and mandatory human merge together mitigate hallucinated fixes that pass tests
- **Evidence**: Design rationale; no data on how often the Critic catches anything. Cross-vendor Critic setup hit a Gemini 404 on the first model string and then free-tier rate limits; settled on the `gemini-flash-latest` alias.
- **Confidence**: anecdotal
- **Quote**: "Hallucinated fixes that pass tests: mitigated by an independent Critic on a different vendor's model, the delta-SARIF proof, a bounded loop and mandatory human merge."
- **Our assessment**: Cross-vendor independence is asserted as a risk control, not measured. Using a floating alias (`gemini-flash-latest`) trades reproducibility for availability, which is in tension with the article's own determinism theme.

### Claim 7: Least privilege should be enforced in code: each role's toolset physically cannot call what the role disallows
- **Evidence**: Design description with two examples (Triage can't patch; Reviewer can't push). Also: the LLM never executes git or scan operations, it emits artifacts that deterministic helpers execute.
- **Confidence**: emerging
- **Quote**: "Over-privileged agents: least privilege is enforced in code. The toolset handed to each role physically cannot call what its role doesn't allow (Triage can't patch; the Reviewer can't push)."
- **Our assessment**: Matches the structural-enforcement-over-prompting position. Adds the pattern of per-role toolsets plus versioned per-flow "skill" playbooks with least-privilege tool access (added after hackathon judge feedback).

### Claim 8: Prompt-injection scanning of external inputs and PII redaction (Presidio) are applied before external text enters prompts; source code is deliberately left uncensored
- **Evidence**: Design description only; no detection rates.
- **Confidence**: anecdotal
- **Quote**: "PII leakage: Presidio redaction on runtime/log data entering prompts (source stays intact; an agent can't reason over a censored diff)."
- **Our assessment**: Useful scoping decision (redact runtime/log data, not code). Contrasts with the broader-scrubbing approach of the Heimdall gateway. The injection-guard claim is stated in a single sentence with no detail.

### Claim 9: "Defer scope, never fake substance," enforced by a repo check banning fakes and stubs from production code
- **Evidence**: Stated governing principle; the stub-gates incident (Claim 4) is the motivating failure. The check's implementation is not shown.
- **Confidence**: anecdotal
- **Quote**: "a feature that isn't built is honestly absent (an explicit NotImplementedError, or simply not wired), never a facade that looks done."
- **Our assessment**: A specific, transferable mitigation for agent-generated code, which tends to fill gaps with plausible stubs. Worth noting as a mechanical rule rather than a prompt instruction.

### Claim 10: Agents never merge, and scheduled scans file deduplicated tickets rather than unsolicited PRs; a human promotes a ticket before autonomous fixing starts
- **Evidence**: Scope decisions in the "wouldn't do" list.
- **Confidence**: emerging
- **Quote**: "unsolicited PRs are a higher-risk default than tickets"
- **Our assessment**: A clear autonomy ladder: scan → ticket → (human labels Ready-for-build) → autonomous fix → PR → human merge. Reasonable and easy to adopt.

### Claim 11: Graph retrieval answers relationship questions (callers/blast radius) that vector search cannot reliably enumerate; a single Code Analyst component fronts graph + vector
- **Evidence**: Architecture description: Tree-sitter parse, Neo4j for symbols and edges, pgvector for 768-dim embeddings, typed query in, one structured RetrievalResult out. No retrieval-quality numbers (the team lists expanding "the retrieval-quality eval harness" as future work).
- **Confidence**: emerging
- **Quote**: "Vector search is great at finding similar text, but it can't reliably enumerate every caller of a function; a graph does that exactly"
- **Our assessment**: Reasonable and widely held reasoning; the evidence is the team's design rather than an A/B comparison. The Code Analyst "single door" idea (agents never touch the DBs directly) is a clean seam.

### Claim 12: Silent data loss in indexing: cross-file CALLS edges vanished when the callee file was indexed after the caller; two-pass indexing fixed it
- **Evidence**: First-person failure report with root cause (Cypher MATCH found no node, so the edge silently disappeared) and fix (upsert all symbols first, edges second; filter external library calls).
- **Confidence**: anecdotal
- **Quote**: "When a caller's file was indexed before the callee's, the Cypher MATCH found no node and the edge just vanished."
- **Our assessment**: Real limitation of order-dependent graph ingestion, and a genuine, reusable bug pattern. Low relevance unless the guide covers code-graph retrieval.

### Claim 13: A pinned-dependency break in a model's remote code forced an embedding-model swap
- **Evidence**: Failure report: jina-embeddings-v2-base-code used HuggingFace custom code importing a function removed in transformers 5.x. Switched to BAAI/bge-base-en-v1.5 (same 768 dims, Apache-2.0, no remote code).
- **Confidence**: anecdotal
- **Quote**: "This was a crash, not a preference, so we switched to BAAI/bge-base-en-v1.5"
- **Our assessment**: Operational lesson: models that require remote/custom code are a supply-chain and compatibility liability. Minor for the guide.

### Claim 14: Per-run cost of about $0.12 from incident to PR, because the expensive model is used only for reasoning (author-reported)
- **Evidence**: A single vendor-reported figure; no workload, model mix or token counts given. Per-run LLM spend is also capped by a budget, and a double build/test (inner gate + outer CI) is accepted as defense-in-depth.
- **Confidence**: anecdotal
- **Quote**: "a full incident-to-PR run lands around $0.12 because the expensive model is only touched for reasoning, never for mechanics."
- **Our assessment**: Do not cite as a benchmark. The directional claim (deterministic mechanics reduce spend) is plausible.

### Claim 15: Scope can widen with evidence: a scan that only relays other tools' findings does no reasoning, so a standards-judge LLM call was added as a logged decision
- **Evidence**: Anecdote from building the scheduled-scan flow; each flow also had an explicit LLM-call budget.
- **Confidence**: anecdotal
- **Quote**: "a scan which only relays other tools' findings does zero reasoning of its own"
- **Our assessment**: Shows per-flow LLM-call budgets treated as a design artifact that can be revised deliberately.

## Concrete Artifacts

Hero-flow LLM call inventory (Thoughtworks article, orchestrator section; paraphrased structure):

```
LLM calls (4): Triage (diagnose) -> Fix (propose patch) -> Critic (different vendor model) -> Reviewer (writes PR body)
Deterministic (0 LLM): git ops, build/test/scan execution, event routing (GitHub event type selects scenario),
                       dedup, prioritization, story selection, orchestrator routing on typed state
Gate order: build/test + delta SARIF -> (fail: back to Fix, max 3 iterations, then Jira story) -> Critic -> Reviewer -> human merge
```

Adoption contract (article, "technical overheads" answer): repos declare a small `.argus/` directory with config for build/test/scan commands and a `standards.md` ruleset. Observability: every LLM call, tool call and token cost visible in Langfuse. Idempotent branch/PR/Jira operations plus advisory locks to avoid duplicate outputs on retries.

Failure symptoms reported verbatim by the authors:

```
Gemini 404: "no longer available to new users"
Hallucination: Fix agent "invented an entire payment_gateway.py" from a fictional stack trace
```

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-nandyala-pani-engineering-the-harness.md` Claim 5 (least-privilege tools convert behavioral guidance into structural enforcement) and Claim 8 (sensors wrap tests/linters rather than relying on agent self-assessment). Code Argus gives a concrete security-pipeline instance of both.
  - `blog-google-adk-2-0-deterministic-workflows.md` Claim 2 (use deterministic code when the workflow can be mapped in advance) and Claim 6 (programmatic routing in code, not by the LLM); Code Argus's typed-state orchestrator is the same idea.
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 1 (deterministic jobs → agent job → safe-output jobs). Code Argus also runs as a GitHub Action container.
  - `blog-anthropic-llms-secure-source-code.md` Claim 6 (independent verification) and Claim 10 (patch validation ladder: tests, then fresh adversarial check). Code Argus's cross-vendor Critic after deterministic gates parallels this.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**:
  - `blog-thoughtworks-heimdall-ai-control-plane.md` Claim 5 (PII scrubbing, fail-closed). Code Argus scopes redaction to runtime/log data and intentionally leaves source code intact.
  - `blog-cursor-rollouts-security-reviewer.md` (AI security review in the PR lifecycle): Code Argus is a different design that opens fixes in CI rather than reviewing PRs.
- **Novel**: Delta-SARIF as a computed "no new vulnerabilities" proof; the stub-gates-always-green failure and the repo check banning fakes; cross-vendor Critic placed after deterministic gates; scheduled scans filing tickets instead of PRs; per-role toolsets that cannot call disallowed tools; graph+vector retrieval behind a single typed Code Analyst interface.

## Guide Impact

- **Ch02 (harness)**: Add Code Argus as a worked example of a code-only orchestrator with exactly four LLM calls, alongside the ADK 2.0 and GHAW deterministic-workflow sources; mark as anecdotal, self-reported.
- **Ch03/Ch04 (verification)**: Add the gate-ordering pattern (deterministic gates → LLM Critic, bounded loop, fall back to a ticket) and a warning that gates must be tested to actually fail (the stub-gates incident, Claim 4). Suggest the delta-scan technique (baseline vs. post-fix SARIF) as a computed safety check.
- **Ch06 (security)**: Cite Claims 7, 8 and 10 as an example of least-privilege-in-code, redaction scoped to runtime data, and ticket-before-PR autonomy ladder. Do not present the injection-guard claim as validated.
- **Cost guidance**: The $0.12 figure should not be cited as a benchmark.

## Extraction Notes

- Fetched the page HTML directly and read the full Q&A text (all eight questions). Quotes were copied from the extracted page text. The article has no sub-pages to follow beyond related-article teasers (not read).
- The source contains a typographical glitch (a stray closing quote after "No new vulnerabilities"); Claim 3 quotes only the unaffected fragment.
- Triage comments suggested Ch07 and other chapters; mapping above is based on the topic and should be confirmed against the current guide structure by the Smith.
- All numbers (932 tests, $0.12, 768 dims, three iterations) are author-reported.
