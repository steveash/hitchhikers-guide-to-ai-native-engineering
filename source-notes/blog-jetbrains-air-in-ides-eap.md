---
source_url: https://blog.jetbrains.com/ai/2026/10/air-in-ides-eap/
source_type: blog-post
title: "A New Agentic Experience: JetBrains Air in IDEs – EAP Now Open"
author: Dominique Rolink, Denis Shiryaev
date_published: 2026-10-01
date_extracted: 2026-10-02
last_checked: 2026-10-02
status: current
confidence_overall: emerging
issue: "#3860"
---

# A New Agentic Experience: JetBrains Air in IDEs – EAP Now Open

> JetBrains' Oct 1, 2026 EAP announcement for Air as an in-IDE plugin argues that parallel-agent orchestration is "fundamentally different" from chat, positions the IDE as the verification-and-ownership layer for agent output, and spells out a data-flow/opt-out control model (no bundled agents, no JetBrains data path for third-party subscriptions).

## Source Context

- **Type**: blog-post (official JetBrains AI blog, EAP product announcement; from trusted feed `jetbrains-ai`)
- **Author credibility**: JetBrains staff writing about their own product. Authoritative for what the plugin does, its availability, and the data-handling statements; not independent evidence. No benchmarks, usage data, or third-party accounts. The "fewer tokens" claim is unquantified.
- **Scope**: Why JetBrains built Air rather than extending AI Assistant chat; three design principles; feature walkthrough (sessions view, double-Ctrl delegation, tab/terminal/chat UI, cloud runs, temporary worktrees); control/data-flow statements; Junie Lite free tier; FAQ. Does not cover: benchmark results, concrete pricing, how the IDE skills/tools work internally, or enterprise policy controls (see `blog-jetbrains-ai-for-teams-organizations.md`).

## Extracted Claims

### Claim 1: Orchestrating concurrent agent tasks is a different interaction problem than chatting, and JetBrains' attempt to bolt agents onto AI chat failed for that reason
- **Evidence**: Vendor's own product-history account (AI Assistant chat → new Air product). No data.
- **Confidence**: anecdotal
- **Quote**: "Orchestrating several tasks concurrently is fundamentally different from having a conversation with AI."
- **Our assessment**: Plausible and consistent with the sessions-as-unit-of-navigation design in the multiproject note. It is a design rationale, not measured. Useful as a vendor-stated reason for session-centric UIs.

### Claim 2: Delegating larger tasks to parallel agents creates a visibility-and-steering requirement
- **Evidence**: Stated premise motivating the UX.
- **Confidence**: emerging
- **Quote**: "You delegate larger tasks and allow agents to work in parallel. This means you need to be able to see what they’re doing and steer them along the way."
- **Our assessment**: Matches the oversight framing in other corpus notes; the novelty is that it's expressed as a UI requirement rather than a policy requirement.

### Claim 3: As agents do more work, verifying and owning the result is the hard part, and that is the IDE's role
- **Evidence**: Argument by assertion; supported by the listed IDE affordances (diffs, navigation, inspections).
- **Confidence**: emerging
- **Quote**: "As agents do more of the work, verifying and owning the result becomes the hard part, and that is what the IDE is for."
- **Our assessment**: Self-interested (an IDE vendor arguing IDEs stay relevant) but the verification-bottleneck premise is independently widespread. Treat the "IDE is the answer" part as positioning.

### Claim 4: JetBrains states agentic development is becoming the norm and that Air is intended to become the primary agentic experience in its IDEs
- **Evidence**: Vendor strategy statement; AI Assistant stays as a separate plugin.
- **Confidence**: anecdotal
- **Quote**: "Agentic development is becoming the norm, and an IDE that keeps agents at arm’s length will struggle to stay relevant."
- **Our assessment**: Industry-trend signal only. Concrete commitment: "Over time, we expect Air to become the primary experience for agentic workflows in JetBrains IDEs." (a hedged, future-tense statement).

### Claim 5: The Air plugin is a conduit for agents/subscriptions the user already has, not an AI provider, and ships with no agents
- **Evidence**: Product design statement; FAQ lists supported agents (Codex, Gemini, GitHub Copilot, Claude Agent, Junie out of the box; others via ACP).
- **Confidence**: emerging
- **Quote**: "The Air plugin for JetBrains IDEs is a conduit for agents and subscriptions you already use. It is not an AI provider, and it ships with no agents installed."
- **Our assessment**: Extends the ACP vendor-neutral pattern from the July note into the IDE. Note the nuance that "ships with no agents" is paired with Junie Lite as a free default after sign-in.

### Claim 6: IDE-native skills and tools are exposed to agents (debugging, profiling, DB exploration, semantic search), which "can" improve results and reduce token use for some tasks
- **Evidence**: None provided; hedged wording.
- **Confidence**: anecdotal
- **Quote**: "This can help agents produce better results and, for some tasks, use fewer tokens."
- **Our assessment**: Unquantified. Compare with JetBrains' own paired-A/B token-saver tests (e.g. ponytail note Claims 1, 4), where advertised savings shrank under measurement; this claim should be held to that standard before citing.

### Claim 7: Session-centric parallel-agent workflow features: cross-project session view with per-session cost, one-keystroke delegation with context attached, temporary worktrees, cherry-pick back
- **Evidence**: Feature descriptions; no screenshots-based or usage evidence in the text we could extract.
- **Confidence**: emerging
- **Quote**: "Keep parallel agent work isolated with temporary worktrees. Start a session from any branch, either on a new branch or in a detached way."
- **Our assessment**: Concrete pattern list for parallel-agent isolation: worktree per session, review in chat, cherry-pick results into the main project. Cost visibility per session ("See what each session costs as you work") is a notable governance affordance at the individual level.

### Claim 8: Cloud runs let long-running tasks continue with the machine closed, but are gated to orgs with AI seats / a JetBrains AI subscription
- **Evidence**: Feature description and FAQ.
- **Confidence**: emerging
- **Quote**: "a JetBrains AI subscription is currently required for cloud runs and a JetBrains Account is required to access Junie Lite runs."
- **Our assessment**: Consistent with the claim in the claude-subscriptions note that anything off the local machine can't use subscription tokens (Claim 13 there). Mobile steering is "coming soon" — not shipped.

### Claim 9: Control model — with no agents signed in, nothing leaves the machine; third-party subscription data goes directly to that provider, not through JetBrains; the plugin can be disabled
- **Evidence**: Explicit vendor statements; unaudited.
- **Confidence**: emerging
- **Quote**: "Your data goes to your provider, not to JetBrains."
- **Our assessment**: Useful as a data-flow design stance; also "Air adds no new data processing terms." Not independently verified. Org-level enforcement (e.g. blocking the plugin) is not discussed beyond "If your organization doesn’t allow agents, there’s nothing for Air to run and nothing to send."

### Claim 10: Free tier strategy — Junie Lite with a cost-efficient model for everyday tasks, free after JetBrains Account sign-in, with terms subject to change
- **Evidence**: Announcement; footnote caveat.
- **Confidence**: anecdotal
- **Quote**: "We believe we should provide some version of free AI in our IDEs, so we’re offering Junie Lite for free*."
- **Our assessment**: Tier design signal (cheap default agent, bring heavier agents via own subscriptions). Terms explicitly may change, so avoid hard-coding in the guide.

## Concrete Artifacts

```
Availability (JetBrains blog, "A New Agentic Experience: JetBrains Air in IDEs – EAP Now Open"):
- Plugin on JetBrains Marketplace, or natively in 2026.3 EAP builds of JetBrains IDEs
- Install from AI Assistant notification => AI Assistant is disabled to avoid running both
  side by side (re-enable in Settings | Plugins)
- Supported out of the box: Codex, Gemini, GitHub Copilot, Claude Agent, Junie; others via ACP
- Claude subscription usable in Air's terminal surface (full-screen IDE tab)
- Cloud runs: JetBrains AI subscription required; Junie Lite: JetBrains Account required
```

```
Workflow affordances listed in the post (paraphrased summary, not a quote):
1. Sessions view across projects: activity, unread updates, changed files, outgoing commits, per-session cost
2. Double-tap Ctrl -> prompt window -> new agent session with current context attached
3. Session UI choice: editor tab, terminal UI, or graphical chat
4. Local or cloud runs
5. Temporary worktrees per session; cherry-pick back to main project
```

## Cross-References

- **Corroborates**: `blog-jetbrains-air-acp-local-models.md` Claim 1 (ACP lets Air connect to third-party agents) and Claim 4 (harness choice independent of model); `blog-jetbrains-air-claude-subscriptions-multiproject.md` Claim 10 (tasks, not windows, as Air's unit of navigation) and Claim 13 (off-machine runs can't use subscription tokens, matching the cloud-runs requirement here); `blog-jetbrains-ai-for-teams-organizations.md` Claim 2 (rejects vendor lock-in) and Claim 7 (vendor-agnostic via ACP/MCP).
- **Contradicts**: None found. (The "fewer tokens" hedge in Claim 6 is unsubstantiated rather than contradicted; the ponytail note Claim 1 is a caution, not a contradiction.)
- **Extends**: `blog-jetbrains-air-claude-subscriptions-multiproject.md` — moves Air from standalone app to an in-IDE plugin and adds worktree isolation, cloud runs, per-session cost view. `blog-jetbrains-agentic-ai-governance.md` Claim 8 (human oversight as intentional checkpoints) — here oversight is operationalized via IDE review tooling, though this post makes no risk-scoring claims.
- **Novel**: (a) IDE-plugin form factor with the explicit "conduit, not provider" and data-flow opt-out framing; (b) vendor's stated reason that chat UX does not scale to concurrent agents; (c) IDE-exposed tools (debugging, profiling, DB, semantic search) offered to external agents; (d) per-session cost in a multi-agent view.

## Guide Impact

- **Governance/oversight chapter**: Cite Claim 3 and Claim 9 as an example of a vendor placing verification (diff review, inspections) in the IDE and publishing a data-flow stance; flag as vendor-stated, unverified.
- **Multi-agent / parallel orchestration chapter**: Add the worktree-per-session + cherry-back pattern and per-session cost visibility as concrete features (Claim 7), alongside the sessions-over-windows framing from the multiproject note.
- **IDE/tooling landscape**: Record that JetBrains positions Air as intended primary agentic experience with AI Assistant retained separately (Claim 4); note EAP status and that terms (Junie Lite) may change.
- **Token-efficiency discussion**: Do not cite Claim 6's token claim as evidence without measurement.

## Extraction Notes

- Read the full post via raw HTML fetch (not a summarizer) and copied quotes verbatim from the extracted text, including curly apostrophes. The post is short (~1,000 words); no sub-pages followed. No contradiction issue filed.
- Cross-reference claim numbers were checked against the headings in the cited notes.
- Triage comments suggested chapter numbers inconsistently; Guide Impact is therefore by topic rather than chapter number. The "JetBrains Context" and "Air Teams" posts are only linked from this page and were not extracted.
