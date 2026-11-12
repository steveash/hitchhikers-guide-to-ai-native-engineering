---
source_url: https://blog.jetbrains.com/ai/2026/11/air-in-jetbrains-ides-ga/
source_type: blog-post
title: "JetBrains IDEs Transformed for the Agentic Era of Development – With Air"
author: Dominique Rolink
date_published: 2026-11-11
date_extracted: 2026-11-12
last_checked: 2026-11-12
status: current
confidence_overall: emerging
issue: "#4675"
---

# JetBrains IDEs Transformed for the Agentic Era of Development – With Air

> The GA announcement (IDE version 2026.3) for Air in JetBrains IDEs: moves the EAP plugin to shipped, and adds Code Notes (line-level review feedback sent back to agent sessions), presets, notifications, quota/cost visibility, and states known gaps (agent-created worktrees untracked, cross-provider quota view unfinished).

## Source Context

- **Type**: blog-post (official JetBrains AI blog, GA product announcement; trusted feed `jetbrains-ai`). The page `<title>` reads "Air in JetBrains IDEs: Run and Review AI Coding Agents".
- **Author credibility**: JetBrains staff describing their own product. Authoritative for what shipped and for stated data-handling behavior; no independent evidence, benchmarks, or usage data. The one statistic is second-hand from Atlassian.
- **Scope**: Key features, migration from AI Assistant, Junie Lite free tier, FAQ. Does not cover: measurements of IDE-tool benefit (see the Netflix note), enterprise governance details, pricing numbers.

## Extracted Claims

### Claim 1: With agents writing more code, the bottleneck moves to review (vendor-cited statistic from Atlassian)
- **Evidence**: A second-hand figure attributed to the "Atlassian State of Developer Experience Report 2026"; not independently checked by us.
- **Confidence**: emerging
- **Quote**: "As agents write more code, individual productivity goes up, but the bottleneck moves to review. 49% of developers now spend four or more hours a week reviewing AI output and correcting prompts (Atlassian State of Developer Experience Report 2026)."
- **Our assessment**: Attribute the number to Atlassian, not JetBrains. The "individual productivity goes up" half is asserted without support. The review-bottleneck framing is common in the corpus; the figure itself should be verified at the Atlassian primary source before use.

### Claim 2: Owning agent output means understanding it, deciding whether it belongs, and being able to maintain it afterwards
- **Evidence**: JetBrains' stated belief; design rationale for the review panel.
- **Confidence**: anecdotal
- **Quote**: "We believe this means you need to understand what changed, decide whether it belongs in your codebase, and be able to maintain it after the session ends."
- **Our assessment**: A concise three-part definition of "review" (comprehension, acceptance, maintainability). Opinion, but a useful framing; echoes the EAP note's Claim 3.

### Claim 3: Air shipped GA in 2026.3, bringing agents into the existing IDE with a single place to track, review, and give feedback
- **Evidence**: Release statement; not independently verified.
- **Confidence**: emerging
- **Quote**: "This is why we shipped Air in JetBrains IDEs, with the 2026.3 release."
- **Our assessment**: Status change from the EAP note (#3860): EAP to GA. The post also says "Air in JetBrains IDEs is available from version 2026.3."

### Claim 4: Agents get IDE code intelligence through the IDE's MCP server and built-in skills; the debugger is limited to IntelliJ IDEA and CLion
- **Evidence**: Feature statement only; no measurements in this post (the separate Netflix post gives 20–30% efficiency measurements for a related IDE-intelligence tool).
- **Confidence**: emerging
- **Quote**: "Through the IDE’s MCP server and built-in skills, agents can check inspections, run your build and run configurations, query your databases, and use the IDE’s own refactorings. In IntelliJ IDEA and CLion, they can also drive the debugger."
- **Our assessment**: The concrete capability list is new relative to the EAP note, which only said IDE skills "can help agents produce better results". Treat as unmeasured here.

### Claim 5: The developer has access to the same IDE tools the agent uses to verify its work
- **Evidence**: Design statement.
- **Confidence**: anecdotal
- **Quote**: "You retain access to the exact same tools to inspect and verify their work."
- **Our assessment**: The symmetric-tooling idea (human and agent verify with the same inspections/debugger) is a notable verification pattern, though the post does not say how mismatches are handled.

### Claim 6: Code Notes let reviewers annotate specific lines and send them back to the session with code context, including for terminal agents
- **Evidence**: Feature description.
- **Confidence**: emerging
- **Quote**: "Leave Code Notes on specific lines to request changes or ask questions, and send them back to the session with the code context attached."
- **Our assessment**: New in GA versus the EAP note. A line-level review-comment-to-agent loop in the IDE, analogous to PR-review-comment autofix in the Cognition notes but local and pre-commit. Related quote: "Code Notes also work with Air’s terminal agents, so you can review their outputs in the IDE and steer the next iteration without giving up your terminal workflow."

### Claim 7: Parallel sessions get notifications and per-agent local Git worktrees, but worktrees agents create themselves are not tracked yet
- **Evidence**: Feature description with an explicit stated gap.
- **Confidence**: emerging
- **Quote**: "Worktrees that agents create on their own aren’t tracked in Air yet, but we’re working to make this a reality."
- **Our assessment**: Honest limitation: isolation works when the human/IDE creates the worktree, not when an agent does (a common pattern with CLI agents). Future-tense promise, not shipped. Also: "Notifications tell you when an agent needs you."

### Claim 8: Presets save agent, model, and instructions per task type
- **Evidence**: Feature description.
- **Confidence**: anecdotal
- **Quote**: "Save the agent, model, and instructions you use for a type of task as a preset."
- **Our assessment**: Minor workflow convenience, but it reifies "task-type to agent/model/instructions" routing in UI.

### Claim 9: Session cost and remaining JetBrains AI quota are visible in the IDE; the same view for Codex, Claude, and Copilot subscriptions is not yet shipped
- **Evidence**: Feature description with stated work-in-progress.
- **Confidence**: emerging
- **Quote**: "We’re working on the same view for Codex, Claude, and Copilot subscriptions."
- **Our assessment**: Cost visibility is first-party-only at GA; the multi-provider case is the one practitioners using their own subscriptions care about. Also: "Users in organizations get a link to JetBrains Console for analytics or managing their team’s AI use."

### Claim 10: Air does not auto-start agents or send code to a provider; data handling depends on the chosen agent
- **Evidence**: FAQ statement; unaudited.
- **Confidence**: emerging
- **Quote**: "Air does not automatically start agents or send your code to an AI provider. You choose and authorize an agent before using it."
- **Our assessment**: Consistent with the EAP note's data-flow claim (Claim 9 there). The post is careful to add that downstream handling "depends on the agent and provider you select."

### Claim 11: Agent support is broad and subscription-flexible; Claude subscriptions work only via the terminal surface
- **Evidence**: FAQ list and instructions.
- **Confidence**: emerging
- **Quote**: "Claude Agent in Air’s chat view requires a JetBrains AI subscription or an Anthropic API key."
- **Our assessment**: Refines the claude-subscriptions note (Claim 1 there says subscriptions are supported via the bundled Claude Agent): at GA, subscription login is documented for Claude Code in the terminal tab ("select Terminal instead of Chat"), while chat needs a JetBrains AI subscription or API key. Possible tension, but likely a change in wording/product state rather than a clear contradiction, so no issue filed. FAQ agent list: Codex, Claude Agent, Claude Code, Gemini, GitHub Copilot, DeepSeek, OpenCode, Cursor, Pi, Grok, Kimi, Kilo, plus others via ACP.

### Claim 12: AI Assistant remains supported as a separate plugin until early 2027; chat history converts to Junie sessions
- **Evidence**: Migration statement.
- **Confidence**: emerging
- **Quote**: "AI Assistant is still available and supported as a separate plugin until early 2027."
- **Our assessment**: A concrete deprecation window for teams planning migration. Also: "Your previous AI Chat conversations will be automatically converted to Junie sessions".

### Claim 13: Junie Lite is free without a JetBrains AI subscription, with terms subject to change; code completion does not use AI quota
- **Evidence**: Announcement with caveat.
- **Confidence**: anecdotal
- **Quote**: "Fair use applies. Terms and available models may change."
- **Our assessment**: Do not hard-code free-tier terms in the guide. The post also states "Code completion ... does not count against your JetBrains AI quota."

### Claim 14: With remote development, Air and agents run on the backend alongside the code
- **Evidence**: FAQ.
- **Confidence**: anecdotal
- **Quote**: "When you connect to a remote backend, Air and your agents run on the backend alongside your code."
- **Our assessment**: Minor but practical for remote-dev teams; note no cloud-runs discussion in this GA post (the EAP note covered them).

## Concrete Artifacts

```
Setup steps quoted from the FAQ (JetBrains blog, GA post):
- Claude subscription in Air: "Open the agent menu and select Manage Agents, then for Claude, select Terminal instead of Chat. Start a new session to open Claude Code in a full-screen editor tab, and then log in with your Claude subscription."
- Restore AI Assistant: "press Shift twice, search for “Open AI Assistant”, and follow the prompts."
- Disable Air: "You can disable Air itself in Settings | Plugins and restart the IDE."
- Quick questions: "use Junie with the Lite or Luna model and set Effort to Off."
```

```
GA feature list (paraphrased summary, not a quote):
1. Sessions across projects with notifications (needs input / unread results)
2. Per-agent local Git worktrees (agent-created worktrees not tracked yet)
3. Presets (agent + model + instructions)
4. Review panel + IDE inspections/tests/debugger + Code Notes sent back to session (also terminal agents)
5. Session cost + JetBrains AI quota/reset date; commit-message drafting
6. Tool-window layout on the right or editor tab
```

## Cross-References

- **Corroborates**: `blog-jetbrains-air-in-ides-eap.md` Claim 3 (verification and ownership as the hard part) and Claim 9 (no data to JetBrains unless an agent is authorized); `blog-jetbrains-air-acp-local-models.md` Claim 1 (ACP connects third-party agents).
- **Contradicts**: None found. Minor tension noted in Claim 11 against `blog-jetbrains-air-claude-subscriptions-multiproject.md` Claim 1 (subscription use) is a wording/product-state difference, not a filed contradiction.
- **Extends**: `blog-jetbrains-air-in-ides-eap.md` Claim 6 (IDE tools exposed to agents) by listing concrete capabilities and the IntelliJ/CLion debugger restriction; Claim 7 there (worktrees, per-session cost) by adding the known worktree gap and quota view; Claim 4 there (Air to be primary experience) by confirming GA. `blog-jetbrains-netflix-ide-intelligence-agents.md` Claim 4 (20–30% efficiency with IDE intelligence) supplies the measurement this post lacks, though for a different tool.
- **Novel**: Code Notes review loop; stated gap on agent-created worktrees; presets; AI Assistant sunset window (early 2027); Atlassian 49% review-time statistic (second-hand); Claude subscriptions documented via terminal only.

## Guide Impact

- **Verification / review chapter**: Cite Claims 2, 5, and 6 as a vendor example of a local, pre-commit line-level review-and-steer loop (Code Notes) where human and agent share IDE verification tools; flag as vendor-stated and unmeasured.
- **Daily workflows / parallel agents chapter**: Add the caveat in Claim 7 (IDE-created worktrees tracked, agent-created ones not) to the worktree-per-session pattern from the EAP note, and mention presets (Claim 8).
- **Team adoption / tooling chapter**: Record the AI Assistant support window to early 2027 (Claim 12) and that cross-provider cost view is not yet available (Claim 9). Avoid hard-coding Junie Lite terms.
- **Statistics hygiene**: if the Atlassian 49% figure is used, cite Atlassian, after checking the primary report.

## Extraction Notes

- The WebFetch tool returned 403; the page was fetched via curl and tags stripped, then read in full (~900 words plus FAQ). Quotes were copied from that extracted text with curly apostrophes preserved. No sub-pages followed; the Atlassian report was not independently checked.
- Cross-reference claim numbers were verified against headings in the cited notes.
- Per the triage, only items new relative to the EAP note were emphasized.
