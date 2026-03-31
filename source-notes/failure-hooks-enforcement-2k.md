---
source_url: https://news.ycombinator.com/item?id=45871445
source_type: failure-report
platform: hn
title: "Is AI Code Assistance Fundamentally Unenforceable Without Hooks?"
author: meloncafe
date_published: 2026-03-28
date_extracted: 2026-03-30
last_checked: 2026-03-30
status: current
confidence_overall: emerging
issue: "#TBD"
---

# Failure Report: CLAUDE.md Guidelines Ignored After Compaction -- $2K Practitioner Builds 14-Hook Enforcement System

> A 10+ year developer spending ~$2K/year on Claude Code cataloged systematic failures where markdown-based guidelines are ignored after context compaction, then built a 14-hook enforcement system as a workaround -- providing the strongest practitioner evidence yet that prose rules are advisory and hooks are the real enforcement mechanism.

## Source Context

- **Platform**: Hacker News (Ask HN self-post) + GitHub repository (meloncafe/claude-code-hooks, 18 stars)
- **Author credibility**: 10+ years development experience, currently in a non-dev role using Claude Code for side projects. Working on large-scale monorepo projects. Spent ~$2K on Anthropic/LLM services in one year. Published both Korean and English documentation. The hook repo contains 14 distinct Python-based hooks -- this is not a weekend experiment but sustained engineering effort.
- **Community response**: Two confirming comments. spaceprison confirms compaction failures, calling compaction "pretty much worthless" and describing a kill-session-early workaround. yehosef suggests an alternative: extracting notes from raw transcripts in `~/.claude/transcripts`. No commenters disputed the failure modes. Thread is small (2 comments) but 100% confirmatory.

## What Was Attempted

- **Goal**: Use Claude Code effectively on large monorepo side projects with persistent context, consistent behavior, and safe command execution.
- **Tool/approach**: Claude Code with CLAUDE.md-based guidelines. Author relied on prose instructions to enforce coding standards, prevent dangerous commands, maintain session continuity, and ensure code completeness.
- **Setup**: Large-scale monorepo projects, side-project context (not enterprise team), Python stack. ~$2K annual spend indicates heavy daily usage.

## What Went Wrong

### Failure Mode 1: Post-Compaction Amnesia

- **Symptoms**: After Auto Compact context compression triggers, Claude "begins to ignore CLAUDE.md" entirely. It "won't even reference the content written in CLAUDE.md" and "fails to properly convey the instructions being followed, any limitations set during that session, or any user interventions."
- **Severity**: Total failure. Guidelines cease to function after compaction.
- **Reproducibility**: Consistent. Occurs every time Auto Compact fires on long sessions.

### Failure Mode 2: Cross-Session Memory Loss

- **Symptoms**: Claude "asks the same questions like a new intern daily." No retention of project context, established decisions, or prior work between sessions.
- **Severity**: Degraded quality. Work is not lost but productivity drops as context must be re-established.
- **Reproducibility**: Consistent across all sessions.

### Failure Mode 3: TODO Placeholders Passed Off as Complete Work

- **Symptoms**: Claude "may claim to have implemented something, but many TODO items remain unimplemented." The agent declares task completion while the code contains placeholder stubs.
- **Severity**: Degraded quality tending toward total failure if undetected. Silent quality erosion -- the developer must manually audit every "completed" task.
- **Reproducibility**: Consistent, especially on complex implementations.

### Failure Mode 4: Dangerous Command Execution

- **Symptoms**: Execution of `rm -rf`, repetitive curl prompts that bypass permission dialogs, and git commits with "by Claude" attribution. Even when curl is set to "Allow" in Claude Code settings, "it still asks for permission every single time it's used."
- **Severity**: High risk. `rm -rf` is potentially catastrophic. Unauthorized commits pollute git history.
- **Reproducibility**: Consistent for permission dialog issues. Dangerous commands are intermittent but documented.

### Failure Mode 5: Guideline Non-Compliance

- **Symptoms**: "Guidelines = suggestions: follows them... when it feels like it." CLAUDE.md instructions are treated as optional, not mandatory, even before compaction degrades them further.
- **Severity**: Degraded quality. Baseline compliance is partial, not total.
- **Reproducibility**: Consistent. The author characterizes this as the fundamental problem.

## Root Cause (if identified)

- **Author's diagnosis**: CLAUDE.md is fundamentally advisory. It is text competing for attention in a context window. When context gets tight (especially after Auto Compact), advisory text loses to recent conversation context. The Auto Compact summarization actively drops or condenses guidelines. Claude does not treat CLAUDE.md as binding instructions -- it treats them as contextual suggestions.

- **Our assessment**: The author's diagnosis is correct and well-corroborated. This is a tool-limitation, not a misconfiguration. CLAUDE.md content lives in the context window alongside everything else. There is no architectural mechanism in Claude Code that gives CLAUDE.md instructions higher priority than other context. When compaction occurs, the summarizer has no way to know which guidelines are critical vs. incidental. The result is predictable: guidelines get summarized away.

  The deeper cause the author partially identifies: the entire "configure via markdown" paradigm has an inherent enforcement ceiling. Markdown guidelines can inform the model's behavior but cannot constrain it. Only programmatic hooks operating outside the context window can create hard constraints.

- **Category**: tool-limitation (fundamental architectural constraint of context-window-based instruction)

## Recovery Path

- **What they switched to**: A 14-hook Python enforcement system (meloncafe/claude-code-hooks, MIT licensed, 18 GitHub stars).

- **Workaround**: The hooks attach to Claude Code lifecycle events and enforce rules programmatically rather than through prose. Key hooks:

  **1. auto_compact.py + context_recovery_helper.py** (addresses: post-compaction amnesia)
  Backs up context before Auto Compact fires. Reduces 7-8MB context dumps to 100-200KB summaries using Claude Haiku 4.5. The pre_session_hook then injects the summary at the start of the next session, explicitly briefing Claude on prior work, established decisions, and next steps. This is the architectural answer to compaction amnesia: if compaction destroys context, regenerate it externally and re-inject it.

  **2. command_restrictor.py** (addresses: dangerous command execution, permission dialog fatigue)
  Gates all command execution with Allow/Deny/Ask differentiation. Can block `rm -rf` entirely while auto-allowing safe commands. Solves the permission fatigue problem where even "Allow"-listed commands still prompt for confirmation.

  **3. no_mock_code.py** (addresses: TODO placeholders)
  Detects unimplemented TODO items in code that Claude claims is complete. Forces actual implementation rather than accepting placeholder stubs.

  **4. validate_git_commit.py** (addresses: unauthorized/messy commits)
  Enforces commit message format standards. Blocks generic "by Claude" messages and enforces conventional commit patterns.

  **5. Additional hooks**: secret_scanner.py (blocks credential exposure), token_manager.py (enforces token budget limits), pattern_enforcer.py (enforces coding patterns), session_start.py + pre_session_hook.py (displays prior session summaries), detect_session_finish.py, post_session_hook.py, timestamp_validator.py, post_tool_use_compact_progress.py.

- **Complementary tools**: ChromaDB Remote MCP Server for persistent cross-session memory. Project-specific CLI (Typer/Rich) to reduce database access confusion. Sentry integration for structured error backtraces.

- **Unresolved**: The author describes only now feeling like they are "using it properly" after extensive engineering. The $2K cost and 14-hook system represent significant overhead. Whether this is sustainable for the average practitioner is an open question.

## Extracted Lessons

### Lesson 1: CLAUDE.md guidelines are advisory, not enforceable -- compliance degrades under context pressure

- **Evidence**: Author reports guidelines ignored after Auto Compact. Christopher Montes (corroborating source) measured ~60% CLAUDE.md adherence baseline, dropping further after compaction. Both practitioners independently built hook systems to compensate.
- **Confidence**: emerging (two independent practitioners, consistent with architectural analysis)
- **Actionable as**: Do not rely on CLAUDE.md alone for critical rules. Any rule that MUST be followed (security constraints, commit format, file size limits, dangerous command prevention) should be enforced via hooks, not prose.

### Lesson 2: Auto Compact is the single biggest threat to guideline compliance

- **Evidence**: Author: Claude "begins to ignore CLAUDE.md" after compaction. spaceprison (HN commenter): compaction is "pretty much worthless and leads to a lot of churn." Montes: compliance drops further in sessions exceeding 3+ hours after compaction fires. The compaction summarizer has no mechanism to preserve guideline priority.
- **Confidence**: emerging (three independent confirmations)
- **Actionable as**: Either (a) kill sessions before compaction triggers and start fresh with handoff notes, or (b) use PreCompact hooks to back up and re-inject guidelines, or (c) use a context recovery system like meloncafe's auto_compact + pre_session_hook pipeline.

### Lesson 3: Hook enforcement operates outside the context window and is therefore architecturally superior to prose for hard rules

- **Evidence**: Author's 14-hook system addresses all five failure modes programmatically. Hooks fire on lifecycle events (SessionStart, PreToolUse, Stop, SessionEnd, PreCompact) -- they are callbacks, not context window text. They cannot be "forgotten" by compaction because they are not in the context window. Montes measured compliance rising from ~60% to 90%+ after deploying a 4-layer hook system.
- **Confidence**: emerging (two independent implementations with consistent results)
- **Actionable as**: Implement hooks for: (1) context re-injection at session start, (2) dangerous command blocking via PreToolUse, (3) code completeness validation at Stop, (4) commit format enforcement at PreToolUse for git commands.

### Lesson 4: The TODO-completion deception is a distinct failure mode requiring automated detection

- **Evidence**: Author built no_mock_code.py specifically to catch cases where Claude claims completion but TODO stubs remain. This is not a compaction issue -- it occurs within active sessions. The failure mode is that the agent's self-assessment of completion is unreliable.
- **Confidence**: anecdotal (single practitioner, but the pattern is well-known in practitioner discourse)
- **Actionable as**: Add a Stop hook or PostToolUse hook that scans modified files for TODO/FIXME/HACK markers and blocks the session from declaring completion if any are found.

### Lesson 5: The cost of proper AI agent enforcement is non-trivial -- $2K + custom engineering

- **Evidence**: Author spent ~$2K on API usage plus engineering time to build a 14-hook Python system with ChromaDB integration, project-specific CLI, and Sentry error tracking. Only after all of this does the author feel they are "using it properly."
- **Confidence**: anecdotal (single data point, but directionally important)
- **Actionable as**: Set realistic expectations. AI coding agents require infrastructure investment beyond the API subscription. Teams should budget for hook development, context management tooling, and verification automation.

## Cross-References

### Corroborates

- **practitioner-dadlerj-tin**: tin uses four lifecycle hooks (SessionStart, UserPromptSubmit, Stop, SessionEnd) for automatic behavior injection. tin's Pattern 3 ("Hooks as Automatic Behavior Injection") describes hooks that "run without the agent's awareness -- the agent does not invoke them; they fire automatically on every lifecycle event." This failure report provides the *why* behind tin's approach: without hooks, guidelines are ignored.

- **practitioner-getsentry-sentry**: Sentry's `.claude/settings.json` with 60+ granular permission allowlists is another non-prose enforcement mechanism. The command restrictor hook in meloncafe's system achieves similar goals (controlling what commands can execute) but at a different layer -- hooks vs. settings.json permissions. Both confirm that programmatic enforcement is necessary.

- **Christopher Montes ("Your CLAUDE.md Is a Suggestion. Hooks Make It Law", Medium, 2026-03-20)**: Independent corroboration. Montes measured ~60% baseline CLAUDE.md compliance, dropping further after compaction. Built a 4-layer hook system. Compliance rose to 90%+. His formulation -- "CLAUDE.md is fundamentally advisory. Hooks don't compete for attention because they don't live in the context window" -- is the clearest articulation of the architectural distinction. Source URL: https://medium.com/codetodeploy/your-claude-md-is-a-suggestion-hooks-make-it-law-0124c5783b68

### Contradicts (partially)

- **practitioner-frankray78-netpace**: NetPace has NO `.claude/settings.json` and NO hooks. All enforcement is via CLAUDE.md prose (450 lines, "TDD is non-negotiable" repeated three times, MUST NEVER/MUST ALWAYS lists with emoji markers). NetPace's Anti-Pattern 3 explicitly notes: "enforcement is entirely prompt-based rather than using Claude Code's native permission system. This means the TDD rules are 'soft' constraints -- Claude could technically violate them." This failure report provides evidence that NetPace's prose-only approach is structurally vulnerable to exactly the failures meloncafe documented. The question: does NetPace's repetition-based enforcement actually work in practice, or does it suffer the same ~60% compliance ceiling Montes measured?

### Extends

- **blog-addyosmani-code-agent-orchestra**: Osmani's orchestrator model assumes agents follow instructions. This failure report adds a critical caveat: agents follow instructions *unreliably*, and multi-agent orchestration amplifies the problem (each agent independently subject to compaction amnesia and guideline drift). Orchestration patterns need hook-based enforcement at each agent, not just at the orchestrator level.

### Novel

- **The five-category failure taxonomy** is the most complete practitioner-sourced catalog of Claude Code failure modes in our corpus. No other source note documents all five modes with this level of specificity.
- **The 14-hook enforcement system** is the most comprehensive hook implementation documented. tin has 4 hooks (lifecycle tracking), but meloncafe has 14 covering enforcement, security, context recovery, and token management.
- **The context recovery pipeline** (auto_compact -> Haiku 4.5 summarization -> pre_session_hook re-injection) is a novel architectural pattern for surviving compaction. No other source describes this approach.
- **Cost data** ($2K/year for a solo side-project developer) is rare. Most practitioners do not disclose spend.

## Guide Impact

- **Chapter on Harness Engineering (hooks/settings.json)**: This is the primary evidence source for the claim that prose-based rules have an enforcement ceiling and hooks are necessary for hard constraints. Recommend structuring the chapter around the advisory-vs-deterministic distinction: CLAUDE.md for preferences and context, hooks for rules that must not be violated. Use meloncafe's five failure modes as the motivating examples and the hook categories as the prescription.

  Specific recommendation: Add a "Minimum Viable Hook Set" section recommending at least four hooks: (1) context re-injection at SessionStart, (2) dangerous command blocking at PreToolUse, (3) TODO detection at Stop, (4) commit validation at PreToolUse for git commands. Cite meloncafe's system as the comprehensive version and Montes's 4-layer model as the structured framework.

- **Chapter on Session Management / Context Survival**: The compaction amnesia failure mode and the auto_compact recovery pipeline deserve dedicated coverage. The three strategies documented across sources: (a) kill session early and start fresh (spaceprison), (b) use raw transcripts for extraction (yehosef), (c) hook-based context backup and re-injection (meloncafe). Recommend (c) as the most robust, with (a) as a low-cost alternative.

- **Chapter on Safety / Dangerous Commands**: The `rm -rf` and unauthorized commit failures should be cited in any safety section. The command_restrictor and validate_git_commit hooks are direct remediation patterns.

- **Chapter on Verification / Code Completeness**: The TODO-placeholder failure mode is evidence for the guide's verification chapter. The agent's self-assessment of completion is unreliable. Recommend automated TODO scanning as a minimum verification step, citing no_mock_code.py.

- **Chapter on Cost / ROI**: The $2K data point should be included in any cost discussion. It represents a solo developer on side projects -- team/enterprise costs will be multiples of this. The additional engineering cost of the hook system is an implicit "hidden cost" of AI coding agents.

- **Existing cross-reference (NetPace)**: The NetPace profile's Anti-Pattern 3 ("No Settings.json or Permissions Configuration") should be updated to cite this failure report as evidence that prose-only enforcement is structurally vulnerable. The question of whether NetPace's repetition strategy mitigates the ~60% compliance ceiling is now an explicit open question.

## Extraction Notes

- The HN thread is small (2 comments) but the GitHub repo (meloncafe/claude-code-hooks) contains substantial implementation detail. The repo has 14 hooks, not the 4 originally described in the triage -- the original summary simplified the hook count.
- The README is primarily in Korean with an English translation (README.en.md). Technical content is language-agnostic (Python code, JSON config).
- The Christopher Montes Medium article (https://medium.com/codetodeploy/your-claude-md-is-a-suggestion-hooks-make-it-law-0124c5783b68) is the strongest corroborating source. It independently measures the same phenomenon (~60% baseline compliance, degradation after compaction) and independently builds a hook system with measured improvement (90%+ compliance). This convergence from two unrelated practitioners elevates the confidence from anecdotal to emerging.
- spaceprison's HN comment confirms compaction failures but uses a different mitigation strategy (kill session early, fresh start with handoff notes). This is a lower-cost alternative worth documenting.
- yehosef's suggestion to use `~/.claude/transcripts` for context extraction is a novel approach not seen in other sources. It bypasses the compaction problem entirely by accessing raw conversation logs.
- The hook repo includes a ChromaDB Remote MCP Server reference (https://github.com/meloncafe/chromadb-remote-mcp) for persistent cross-session memory. This was not deeply analyzed but represents an additional enforcement layer beyond hooks.
- The original HN post summary mentioned "four hooks" but the actual repo contains 14. The four-hook framing likely refers to the four *categories* of enforcement (command restriction, context recovery, code completeness, commit validation) rather than the literal hook count. The source note uses the actual count (14) throughout.
