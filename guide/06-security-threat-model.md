# Security and Threat Model

> AI changes the security calculus on both sides: it makes offensive capability
> cheaper and faster, and it introduces new attack surface inside your own
> toolchain. This chapter is the adversarial counterpart to the Verification
> chapter — not "is the code correct?" but "who is trying to make it wrong, and
> what does a defensible posture look like?"

---

## Security Threat Model for AI-Native Teams

The verification stack in the [Verification chapter](03-verification.md) defends
against agent mistakes against your codebase. There is a parallel threat model
that defends against attackers using agents against your codebase. Two first-party sources from inside the
model and tooling vendors converged on it in early 2026.

### The 24-month offensive AI escalation window

Anthropic's security team, citing internal research from Project Glasswing
and Claude Mythos Preview, makes an explicit timeline claim:

> "Within the next 24 months, vast numbers of bugs that sat unnoticed in code,
> possibly for years, will be found by AI models and chained into working
> exploits."
> [source: blog-anthropic-ai-accelerated-offense, Claim 1] [emerging]

The operative word is *chained*. The companion claim — that "publicly
available models can find serious vulnerabilities that traditional reviews
have missed for long periods" — means the threat model can no longer assume
"only nation-state actors have these capabilities."
[source: blog-anthropic-ai-accelerated-offense, Claim 2] [anecdotal]

As of May 2026, the UK AI Security Institute's independent evaluation
places publicly-available GPT-5.5 at 71.4% on its Expert-level cyber CTF
benchmark — statistically indistinguishable from Claude Mythos Preview
(68.6%) — and the second model ever to complete AISI's 32-step corporate
network attack simulation autonomously.
[source: blog-simonwillison-aisi-gpt55-cyber, Claims 1, 2, 3] [emerging]
Teams that deferred AI-assisted security review because capable models were
research-access-only can no longer use that deferral.
[source: blog-simonwillison-aisi-gpt55-cyber, Claim 1] [emerging]

For AI-native engineering teams, this is the asymmetry: you ship more code
per developer, your attack surface grows in proportion, and the cost for an
attacker to find chainable bugs in that surface is collapsing toward zero on
the same curve that is making your team faster.

**Rule**: If you have not yet adopted AI-assisted security scanning of your
own code before it ships, the first-mover advantage is closing. Run the same
class of tools an attacker would on your own code first, on every PR, before
the 24-month window closes.
[source: blog-anthropic-ai-accelerated-offense, Claim 6] [anecdotal]

### Three defensive actions that offset the asymmetry

The Anthropic post ranks seven recommendations; three are immediately
actionable for an AI-native engineering team and have a corroborating
production deployment in our corpus:

1. **AI security scan before shipping.** Anthropic frames this as the single
   highest-ROI action: "If you implement one thing from this section,
   implement this: scan your code for vulnerabilities using AI before it
   ships."
   [source: blog-anthropic-ai-accelerated-offense, Claim 6] [anecdotal]
   Cursor's production deployment runs four security agents on a shared MCP
   substrate; the new-PR review agent alone runs on 3,000+ internal PRs per
   week and surfaces 200+ vulnerabilities per week.
   [source: blog-cursor-security-agents, Claims 1, 9] [anecdotal]
   Mozilla provides the third, vendor-independent data point: Firefox 150
   shipped fixes for 271 vulnerabilities surfaced by an early Claude Mythos
   Preview run on the codebase, against 22 found by Opus 4.6 in Firefox 148 —
   a ~12× model-generation jump on the same heavily-audited browser.
   [source: blog-simonwillison-bobby-holley, Claim 1] [emerging]

   Budget for the finding-volume shock before enabling the scan. Firefox CTO
   Bobby Holley named the organizational impact directly:
   > "You may need to reprioritize everything else to bring relentless and
   > single-minded focus to the task, but there is light at the end of the
   > tunnel."
   > [source: blog-simonwillison-bobby-holley, Claim 7]
   Mozilla — one of the most security-mature organizations in open source —
   could not absorb 271 vulnerabilities without significant operational
   disruption.
   [source: blog-simonwillison-bobby-holley, Claim 7] [anecdotal]

2. **AI model at the front of the alert queue, for 100% alert coverage.**
   Human-only SOCs sample alerts under fatigue. An AI triage agent that
   processes every alert at low depth ensures none goes uninvestigated.
   [source: blog-anthropic-ai-accelerated-offense, Claim 7] [emerging]
   Anthropic's own production deployment of this pattern — CLUE (Claude
   Looks Up Evidence), built by their Detection Platform Engineering team —
   reduced the false positive rate on triaged alerts from approximately 33%
   to 7% and processed 12,000 automated queries in 30 days, recovering an
   estimated 1,870 analyst-hours.
   [source: blog-anthropic-bow-cybersecurity-clue, Claims 4, 5] [emerging]
   CLUE Triage enriches each alert with cross-system context (Slack
   messages, internal docs, code, data warehouse) before assigning a
   confidence-scored disposition; analysts review the low-confidence cases.
   [source: blog-anthropic-bow-cybersecurity-clue, Claim 2] [emerging]

   **Caveat**: The CLUE team explicitly notes "accuracy is harder to quantify
   than speed" — false positive reduction is measured, but the false negative
   rate (real threats dismissed by automated triage) is not. Define a false
   negative measurement strategy before deploying AI triage in security
   contexts.
   [source: blog-anthropic-bow-cybersecurity-clue, Claim 4] [emerging]

3. **Specialization over general-purpose review.** The DeepSource benchmark
   measured Claude Code at 48.78% recall on the OpenSSF CVE dataset for
   security review of full diffs (see §CI as Verification Backstop above).
   Cursor's response is a dedicated security review agent prompt-tuned to
   specific threat models, gating CI independently from general code-quality
   review. The shared principle: a security agent and a code-quality agent
   pulled in different directions in one prompt is the failure mode behind
   the recall gap.
   [source: blog-cursor-security-agents, Claim 5;
   discussion-hn-autofix-hybrid-review, Claims 1, 8] [emerging]

### The find-and-fix loop: discovery is cheap, patching is the bottleneck

"Scan before shipping" (action 1) is the *what*. Anthropic's security research
team published the *how* — a six-step find-and-fix loop (threat model → sandbox →
discovery → verification → triage → patching) run against open-source codebases.
Three of its findings change how you staff and prompt that loop.

As of May 22, 2026 the team had "disclosed 1,596 vulnerabilities. To our
knowledge, 97 of these have been patched"
[source: blog-anthropic-llms-secure-source-code, Claim 12] [settled] — a ~6%
patch rate. Discovery now parallelizes; the work moved downstream: "discovery is
now straightforward to parallelize, and the bottleneck has shifted to
verification, triage, and patching"
[source: blog-anthropic-llms-secure-source-code, Claim 1] [emerging].

**Rule**: Before turning on aggressive AI scanning, confirm your
verification-triage-patch pipeline can absorb the finding volume. A scan that
outpaces remediation produces a backlog, not security.
[source: blog-anthropic-llms-secure-source-code, Claims 1, 12] [emerging]

A second frontier lab corroborates the same asymmetry from the open-source side.
OpenAI's Patch the Planet program (built with Trail of Bits) is explicitly
designed to reduce maintainer burden, "not add to it," because "many maintainers
are already being asked to sort through more reports, more quickly, with the same
limited time and resources"
[source: blog-openai-patch-the-planet, Claim 2] [settled]. Its load-bearing
design decision is a human gate at the maintainer boundary: dedicated engineers
"manually reviewed every security issue before it was submitted to a maintainer,"
because frontier models "produce a high volume of false positives that can
contribute to the already overwhelming backlog maintainers are facing"
[source: blog-openai-patch-the-planet, Claim 11] [settled]. This is the same
verifier-independence principle as Anthropic's adversarial AI verifier above,
with a funded human standing in for the second agent. Verifier independence can
be satisfied by either a second AI pass or a human reviewer; which one you reach
for depends on your finding volume and available human capacity. [editorial]

Prompt the discovery agent *simply*. The counter-intuitive finding:
"Counterintuitively, more prescriptive prompts make discovery worse—long
checklists tend to reduce the model's creativity and generate fewer novel bugs"
[source: blog-anthropic-llms-secure-source-code, Claim 2] [emerging]. Encode the
durable context — which vulnerability classes count — in a `THREAT_MODEL.md`
committed to the repo, and leave the search strategy to the model
[source: blog-anthropic-llms-secure-source-code, Claim 5] [emerging].

Verification must run independently. Give the verifier only the proof-of-concept
and the codebase, not the finder's analysis, so it hunts for mitigations the
finder missed instead of anchoring on the finder's conclusion; across the teams
Anthropic worked with, "adding an adversarial verifier roughly halved the rate of
non-exploitable findings from the discovery phase"
[source: blog-anthropic-llms-secure-source-code, Claims 6, 7] [emerging]. This is
the same separate-context principle as the two-agent review pattern above. And the
sandbox is a compute-layer concern, not a prompt one: "One team told the model it
had no network access—when it actually did—and the model discovered it could fetch
from GitHub anyway"
[source: blog-anthropic-llms-secure-source-code, Claim 3] [anecdotal].

**Rule**: Model instructions are not a security boundary. Isolate read-only
discovery agents in containers and proof-of-concept detonation in a locked-down
microVM or VM, and run verification in a context that never sees the finder's
reasoning.
[source: blog-anthropic-llms-secure-source-code, Claims 3, 6, 7] [emerging]

### Gradual trust rollout: shadow → inform → gate

Cursor documents the deployment pattern they used for their own internal
security review agent — and it generalizes to any autonomous agent entering
a critical path:

```
Stage 1: Shadow mode
  — Agent runs on every event
  — Findings → private Slack channel for the security team
  — Zero PR impact, zero blast radius
  — Purpose: validate signal quality before anyone sees it

Stage 2: PR commenting
  — Agent posts findings as PR comments
  — Engineers can address or dismiss; no merge gate
  — Purpose: expose to broader scrutiny, build wider confidence

Stage 3: Blocking gate check
  — Agent findings can block merge
  — Engineer must address or dismiss before landing
  — Purpose: enforce findings as a hard constraint

Progression criteria (per Cursor):
  Shadow → PR comments: "confident it was identifying genuine issues"
  PR comments → blocking: confidence continues to build (no specific gate)
```

[source: blog-cursor-security-agents, Claim 4] [emerging]

The pattern catches the "agent cried wolf" failure mode that causes engineers
to dismiss legitimate findings. Skipping shadow mode lands you with a CI gate
calibrated to nothing — which is worse than no gate, because dismissed
findings train the team to ignore the agent.

**Rule**: Never deploy a security agent in blocking mode before it has run
in shadow mode long enough to produce a stable signal. Shadow → inform →
gate is the only deployment sequence with corroborating production evidence.
[source: blog-cursor-security-agents, Claim 4] [emerging]

### Three-axis attribution when the agent gets it wrong

When a security agent (or any extraction agent) produces a wrong answer,
practitioners default to "tweak the prompt." Carta Healthcare's clinical
abstraction team identified a more useful diagnostic structure: attribute
each failure to one of three root causes — and the fix differs by axis.

> "When something underperforms, you can trace it back to a specific prompt,
> a context issue, or a retrieval gap rather than staring at an aggregate
> score wondering what went wrong." — Matthew Mazzanti, Carta Healthcare
> [source: blog-anthropic-carta-healthcare-context-engineering, Claim 5] [emerging]

```
Three-axis evaluation attribution

  PROMPT failure     → revise the prompt
  CONTEXT failure    → change context assembly (what the agent sees per query)
  RETRIEVAL failure  → fix the retrieval pipeline (which documents are surfaced)
```

Aggregate accuracy metrics conflate all three and cannot drive targeted
remediation. A three-axis evaluation framework lets you separately tune the
component that broke.

**Rule**: Build evaluation that attributes each failure to one of prompt,
context, or retrieval before iterating. Skip this and you will spend more
time debugging than building.
[source: blog-anthropic-carta-healthcare-context-engineering, Claims 5, 6] [emerging]


---

## Bounding Your Own Agents: Least Agency and the Toolchain Attack Surface

The sections above defend against attackers wielding AI against your code. The
other half of the threat model is your own agents. Anthropic Deputy CISO Jason
Clinton frames a drifting agent as functionally an insider attack — and notes
that traditional insider-incident response (a Ponemon-reported average of "67
days to contain an insider incident") is "the wrong unit of measurement entirely"
at agent execution speeds.
[source: blog-anthropic-ciso-guide-agentic-ai, Claim 4] [emerging]
The job is not zero risk: "our jobs are to make agentic risk legible and bounded"
so it can be deliberately accepted rather than driven into ungoverned shadow
adoption.
[source: blog-anthropic-ciso-guide-agentic-ai, Claim 1] [settled]

### Four questions before you grant an agent access

Anthropic's security team runs every agentic use case through four questions:
[source: blog-anthropic-ciso-guide-agentic-ai, Claim 2] [settled]

```
1. What untrusted content does it ingest?          (anything attacker-writable?)
2. What actions can it take, and on whose behalf?  (read-only vs read/write; whose identity?)
3. What is the blast radius if it is misaligned?   (scope × severity)
4. What observability do I have?                   (can you tell agent actions from user actions in your SIEM?)
```

The answers describe the risk; the **principle of least agency** says what to do
about it — "grant the narrowest capability that still completes the task" — then
default to "admin-paced rollout: enable a small group, watch the telemetry, and
then expand access."
[source: blog-anthropic-ciso-guide-agentic-ai, Claim 3] [settled]

**Rule**: Scope an agent by removing capabilities, not by adding friction. If the
failure that keeps you up at night is a deleted production database, remove the
delete verb from the agent's tool list entirely rather than prompting it not to.
[source: blog-anthropic-ciso-guide-agentic-ai, Claims 3, 10] [settled]

### Design controls around the model's future capability, not today's limits

Least agency matters more than it looks because an agent's behavior can change
with no configuration change at all. Anthropic moved an internal
incident-response agent — bounded to read-only logs, Slack, and draft-only docs —
from Claude Opus 4 to Opus 4.5 in November 2025 and "changed nothing else—no new
tools, permissions, or prompts." The intelligence uplift alone was enough for the
agent to notice, mid-incident, that no human had arrived and reach out over Slack
to another internal agent with code access to request a fix.
[source: blog-anthropic-ciso-guide-agentic-ai, Claim 7] [emerging]

The episode is a controls success, not a failure: the emergent action stayed
inside the original bounds — the only write-like action still required a human
review. Anthropic draws two lessons: "new capabilities can show up within the
boundaries of an agent deployment," and "controls are effective even with
stochastic agents."
[source: blog-anthropic-ciso-guide-agentic-ai, Claim 8] [settled]

**Rule**: Bound an agent's access around where the model will be in six months,
not what today's model can do — a version upgrade with zero config change can
widen behavior inside the same permission set.
[source: blog-anthropic-ciso-guide-agentic-ai, Claims 7, 8] [emerging]

### The MCP supply chain: rug-pull tool redefinition

The toolchain itself is attack surface. An MCP server that behaves benignly
during review, gets approved, then later redefines its tools to do something the
user never consented to is a "rug-pull attack." Visual Studio's mitigation is to
re-validate a server's runtime fingerprint — its tools, prompts, resources, and
instructions — at startup, and when the MCP `notifications/tools/list_changed`
event fires it "resets any prior acceptances or permissions on tools (to prevent
rug-pull attacks), refetches the tool list, and updates the count and UI live."
[source: docs-github-copilot-vs-june-2026, Claim 3] [settled]

The limit is trust-on-first-use: a first-time server connection is implicitly
trusted and silently seeds the baseline, so fingerprinting catches *drift after
approval*, not a server that is malicious from first contact. Pair
change-detection with a vetting control — for example an org `RegistryOnly`
policy restricting servers to a pre-approved registry — if you need protection
against first-contact malice.
[source: docs-github-copilot-vs-june-2026, Claim 4] [settled]

**Rule**: Check any MCP client for whether it re-validates a server's tool
manifest on every reconnect or trusts it forever after first approval — and
because first-use trust is unvetted, gate which servers can be added with a
registry allowlist rather than relying on change-detection alone.
[source: docs-github-copilot-vs-june-2026, Claims 3, 4] [settled]

---

*Sources for this chapter:
blog-anthropic-ai-accelerated-offense (Claims 1, 2, 6, 7),
blog-anthropic-bow-cybersecurity-clue (Claims 2, 4, 5),
blog-anthropic-ciso-guide-agentic-ai (Claims 1, 2, 3, 4, 7, 8, 10),
blog-anthropic-llms-secure-source-code (Claims 1, 2, 3, 5, 6, 7, 12),
blog-anthropic-carta-healthcare-context-engineering (Claims 5, 6),
blog-cursor-security-agents (Claims 1, 4, 5, 9),
blog-openai-patch-the-planet (Claims 2, 11),
blog-simonwillison-aisi-gpt55-cyber (Claims 1, 2, 3),
blog-simonwillison-bobby-holley (Claims 1, 7),
docs-github-copilot-vs-june-2026 (Claims 3, 4)*

*Last updated: 2026-07-18*
