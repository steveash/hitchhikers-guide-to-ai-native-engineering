---
source_url: https://www.thoughtworks.com/insights/blog/architecture/engineering-the-harness-a-practical-pattern-for-reliable-coding-agents
source_type: blog-post
title: "Engineering the harness: A practical pattern for reliable coding agents"
author: Jaya Simha Reddy Nandyala and Prabina Pani (Thoughtworks)
date_published: 2026-09-29
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: emerging
issue: "#3809"
---

# Engineering the harness: A practical pattern for reliable coding agents

> Thoughtworks post framing `Agent = Model + Harness` and splitting the harness into pre-action Guides, post-action Sensors, and selective human gates, illustrated with a three-microservice shared-harness example and a 6-phase RED/GREEN delivery pipeline; contributes a concrete "promote prose rules to mechanical sensors" heuristic and "earn every rule" harness-hygiene discipline.

## Source Context

- **Type**: blog-post
- **Author credibility**: Two Thoughtworks practitioners; the post carries a disclaimer that views are the authors' own. No affiliation detail or credentials beyond byline are given.
- **Scope**: Conceptual pattern plus one worked (simplified, hypothetical) multi-repo example and a pipeline sketch. Provides no metrics, no code, no real-project results. Does not cover eval of the harness itself.

## Extracted Claims

### Claim 1: Agents fail on systems-level correctness, not local correctness, and this is a harness gap rather than a model-quality gap
- **Evidence**: Hypothetical example: an agent renames a field in one service unaware that two downstream services consume it. No data.
- **Confidence**: anecdotal
- **Quote**: "This persistent gap between raw model intelligence and reliable software delivery is not primarily a model-quality issue."
- **Our assessment**: Plausible and consistent with other harness-centric sources, but asserted rather than measured.

### Claim 2: Agent = Model + Harness, where the harness supplies environment, tool constraints, context boundaries and feedback loops
- **Evidence**: Definitional framing.
- **Confidence**: settled (as terminology in our corpus)
- **Quote**: "Agent = Model + Harness"
- **Our assessment**: Same definition as the HumanLayer note; adds the "auditable delivery system" framing.

### Claim 3: A production harness has two enforcement layers, Guides (pre-action) and Sensors (post-action), separated by selective human gates
- **Evidence**: Architectural argument; the pipeline example.
- **Confidence**: emerging
- **Quote**: "Guides (Pre-action steering): Mechanisms that constrain and direct the agent before it takes action or writes code."
- **Our assessment**: Useful organizing taxonomy (feedforward vs feedback). The post says "two layers" in the heading but lists three numbered items; the gates are effectively a third element.

### Claim 4: Monolithic instruction files cause attention dilution and context rot; scope instructions by path/domain and use progressive disclosure
- **Evidence**: Assertion; no measurements.
- **Confidence**: emerging
- **Quote**: "Loading monolithic instruction files into every session rapidly fills the context window, causing "attention dilution" and context rot."
- **Our assessment**: Corroborated by HumanLayer's context-rot citation (Claim 13) and short-CLAUDE.md advice (Claim 3).

### Claim 5: Least-privilege tools convert behavioral guidance into structural enforcement; prompt text asking for restraint is fragile
- **Evidence**: Example: Q&A/verification agent given read-only tools.
- **Confidence**: emerging
- **Quote**: "Least-privilege tools convert behavioral guidance into structural enforcement."
- **Our assessment**: Sound, well-aligned with hooks-as-deterministic-control (HumanLayer Claim 7).

### Claim 6: "Ask before deciding" — record explicit defaults instead of letting the agent silently guess on skipped optional inputs
- **Evidence**: Assertion.
- **Confidence**: anecdotal
- **Quote**: "A default is visible and inspectable, a guess is hidden and risky."
- **Our assessment**: Nice, cheap heuristic; the behavior (asking clarifying questions) is the kind of thing Google's behavioral evals test (Google Claim 3).

### Claim 7: Human confirmation gates should be reserved for irreversible or high-blast-radius decisions
- **Evidence**: Assertion; multi-repo example.
- **Confidence**: emerging
- **Quote**: "human confirmation gates are reserved for irreversible or high-blast-radius choices, such as multi-repository scope changes, schema migrations or public API modifications."
- **Our assessment**: Aligns with tiered-oversight in the Gordon/Kamelman note (Claim 5). Post does not say how blast radius is detected beyond dependency-graph scanning.

### Claim 8: Sensors should wrap tests/linters/type checkers/architecture rules in the agent loop instead of relying on agent self-assessment
- **Evidence**: Assertion.
- **Confidence**: settled
- **Quote**: "sensors run automatically to evaluate correctness rather than relying on the agent's self-assessment."
- **Our assessment**: Widely held; corroborated by HumanLayer Claim 8.

### Claim 9: Sensors follow "silent success, verbose failure"
- **Evidence**: Design rule; no measurements.
- **Confidence**: emerging
- **Quote**: "Sensors follow the "silent success, verbose failure" rule:"
- **Our assessment**: Matches HumanLayer's finding that raw verification output flooding context is a failure mode (Claim 8).

### Claim 10: Repeated prose rules should be promoted into mechanical sensors (custom lint rule, type check, architecture test)
- **Evidence**: Assertion.
- **Confidence**: emerging
- **Quote**: "Prose is the starting point; where a rule can be reliably encoded, mechanical enforcement is the stronger option."
- **Our assessment**: Actionable and novel in our corpus as an explicit promotion heuristic.

### Claim 11: A shared multi-repo harness with impact analysis and a blocking confirmation gate prevents cross-service drift
- **Evidence**: Hypothetical billing/checkout/invoicing example; the post itself says it "can work when dependencies are known and accessible to the harness."
- **Confidence**: anecdotal
- **Quote**: "This simplified example illustrates how the pattern can work when dependencies are known and accessible to the harness."
- **Our assessment**: Illustrative only. The caveat matters: undocumented consumers defeat impact analysis.

### Claim 12: A 6-phase pipeline (ANALYZE, BLUEPRINT, RED, GREEN, REFACTOR, REVIEW) separates human feedback (consequential decisions) from automated feedback (mechanically correctable failures)
- **Evidence**: Pipeline description; no results reported.
- **Confidence**: anecdotal
- **Quote**: "If the REVIEW phase detects an untested acceptance criterion, it does not interrupt a human."
- **Our assessment**: Concrete reference design; unvalidated.

### Claim 13: The harness itself must be treated as versioned, peer-reviewed software, with every rule earned and pruned as models improve
- **Evidence**: Assertion.
- **Confidence**: emerging
- **Quote**: "Unearned rules add noise, dilute model attention and degrade output quality."
- **Our assessment**: Consistent with HumanLayer's short-config stance and its over-fitting finding (Claims 3, 10). The "prune as models improve" point is the useful part.

## Concrete Artifacts

```
Source: Nandyala & Pani, "Engineering the harness" (Thoughtworks, 2026-09-29)

Agent = Model + Harness

Six-phase delivery pipeline:
ANALYZE   - structured intake (Jira tickets, technical context), explicit defaults for missing inputs
BLUEPRINT - architecture agent designs cross-repo file plan; multi-repo confirmation gate (human)
RED       - test agent writes failing acceptance tests
GREEN     - implementer agent writes minimal code until RED tests pass
REFACTOR  - polish structure/conventions while tests stay green
REVIEW    - automated review agent checks coverage vs acceptance criteria;
            untested criterion -> auto-route back to RED/GREEN (no human)

Example system: billing-service (owns discount_rate),
checkout-service (consumes), invoicing-service (consumes).
Unconstrained: rename to promotional_discount in billing-service only -> silent drift.
Shared harness: impact analysis -> blocking multi-repo gate -> coordinated update + multi-service tests.
```

## Cross-References

- **Corroborates**:
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 1 (agent = model + harness), Claim 8 (verification and output flooding), Claim 13 (context rot).
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5 (tiered manual/semi-automated/automated oversight) for selective gates.
- **Contradicts**: None found. Its "prose rules should become sensors" stance sits in mild tension with HumanLayer Claim 2's emphasis on CLAUDE.md as the first surface, but that is sequencing (prose first, then promote), not a contradiction.
- **Extends**:
  - `blog-google-anatomy-harness-engineering.md` — Google covers evaluating the harness (behavioral evals, Claims 3, 10-12); this post covers designing it (guides/sensors/gates). "Ask before deciding" is the design counterpart of Google's clarifying-question eval.
  - `blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 1 (functionally complete but operationally fragile) — same failure class, with a structural remedy.
- **Novel**: The guides/sensors/gates taxonomy as a named pattern; "promote prose to mechanical sensor" rule; "earn every rule" with traceability to a past failure; explicit-defaults-over-guesses; automated REVIEW→RED/GREEN loop vs human gate split.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Consider adding the Guides/Sensors/Human-gates taxonomy as an organizing frame, citing this note alongside HumanLayer Claim 1.
- **Chapter 03 (Verification)**: Add "silent success, verbose failure" and the prose-to-sensor promotion heuristic as sensor design guidance (this note Claims 9-10).
- **Chapter 04 (Context Engineering)**: Add least-privilege tools and path-scoped progressive disclosure as structural (not prompt-based) context controls (Claims 4-5).
- Treat evidence as emerging: no measurements support any claim, so present as practitioner guidance.

## Extraction Notes

- Read the full article (fetched raw HTML and stripped tags); no sub-pages followed—it links only to unrelated Thoughtworks posts.
- The post is short and light on evidence; the billing-service example is explicitly hypothetical.
- Triage comments compared it to Google's harness piece; no genuine contradiction found, so no contradiction issue was filed.
