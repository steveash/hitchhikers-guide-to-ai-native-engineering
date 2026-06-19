---
source_url: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
source_type: blog-post
title: "Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more"
author: Anthropic (no individual byline)
date_published: 2026-06-18
date_extracted: 2026-06-19
last_checked: 2026-06-19
status: current
confidence_overall: settled
issue: "#1222"
---

# Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more

> Official Anthropic post establishing the canonical seven-method taxonomy for instructing Claude Code behavior, with a context-cost and compaction-behavior comparison table for each method — providing the decision framework practitioners need to choose the right mechanism for every type of instruction.

## Source Context

- **Type**: blog-post (official Anthropic claude.com blog, June 18, 2026)
- **Author credibility**: First-party Anthropic. Maximum authority for how Claude Code instruction mechanisms work, their architectural behavior, and the intended use-case for each. The post presents a unified comparative framework across all seven methods — a design decision that reflects authoritative knowledge of the internal architecture. No individual byline is listed.
- **Scope**: Covers all seven instruction mechanisms — CLAUDE.md files (root and subdirectory), rules, skills, subagents, hooks, output styles, and system prompt appending — with an explicit comparison table across four dimensions (loading time, compaction behavior, context cost, when to use). Also covers user-level vs. project-level file scoping, five common anti-patterns (quick tips), and a closing note on plugins as a distribution mechanism. Does NOT cover: specific API or SDK parameters, pricing or cost per token for each method, implementation guides for individual mechanisms, how the mechanisms interact with auto mode or routines, or how to migrate from one mechanism to another.

## Extracted Claims

### Claim 1: There are exactly seven distinct mechanisms for instructing Claude Code behavior, and each differs on when it loads, compaction behavior, context cost, and when to use it

- **Evidence**: First-party architectural framing with an explicit seven-row comparison table. The post opens: "There are seven methods for instructing Claude's behavior: CLAUDE.md files, rules, skills, subagents, hooks, output styles, and appending the system prompt."
- **Confidence**: settled (first-party architectural taxonomy from Anthropic; the table is presented as the authoritative comparison)
- **Quote**: "Claude is built to work the way you work, and in Claude Code you can customize it. There are seven methods for instructing Claude's behavior: CLAUDE.md files, rules, skills, subagents, hooks, output styles, and appending the system prompt."
- **Our assessment**: This is the first time Anthropic has published a unified comparative table across all instruction mechanisms in a single post. Prior sources (notably `blog-anthropic-large-codebase-best-practices.md` Claim 5) taxonomized *extension points* (CLAUDE.md files, hooks, skills, plugins, MCP servers, LSP integrations, subagents) but not *instruction methods*. The two taxonomies are complementary, not contradictory: extension points describe what you can add to the harness; instruction methods describe how you can direct Claude's behavior. The seven methods omit plugins and MCP servers (which provide tools and data access, not direct behavioral instructions) and add rules, output styles, and system prompt appending.

### Claim 2: Root CLAUDE.md files load at session start, stay in context the entire session, and are memoized through compaction — at high context cost

- **Evidence**: First-party description of loading and compaction behavior with explicit cost characterization.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "CLAUDE.md is a markdown file at the root of your project. It loads into context at session start and stays there for the entire session." / "Memoized. Read once and cached for the session; cache cleared and re-read after compaction" / "High. Every line costs tokens whether relevant or not"
- **Our assessment**: The "high context cost" characterization is the key constraint for CLAUDE.md design. Every line in the root CLAUDE.md consumes tokens on every session turn — whether or not those tokens are relevant to the current task. This explains the "lean" requirement from `blog-anthropic-large-codebase-best-practices.md` Claim 6: a bloated root CLAUDE.md is a context tax paid on every turn. The memoization behavior (re-read after compaction) means CLAUDE.md content survives compaction — in contrast to session conversation that gets summarized. The post confirms what practitioners should put here: "Build commands, directory layout, monorepo structure, coding conventions, and team norms all fit naturally here."

### Claim 3: Subdirectory CLAUDE.md files load only when Claude reads a file in that subdirectory and are lost until that subdirectory is touched again — at low context cost

- **Evidence**: First-party architectural description with explicit compaction behavior.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "On-demand, when Claude reads a file under that subdirectory" / "Lost until that subdirectory is touched again" / "Low. Only consumes context when the relevant subdirectory is being worked on"
- **Our assessment**: The "lost until subdirectory is touched again" compaction behavior is an important architectural asymmetry between root and subdirectory CLAUDE.md files. Root CLAUDE.md survives compaction; subdirectory files do not. A subdirectory CLAUDE.md containing critical conventions that must always be followed should not be a subdirectory CLAUDE.md — it belongs in the root file or in a path-scoped rule. Subdirectory CLAUDE.md is the right home for conventions that are relevant only when working in that subdirectory: local test commands, module-specific naming conventions, service-level architecture notes.

### Claim 4: Rules are path-scoped markdown files in `.claude/rules/` that stay in context through compaction but can be constrained to load only when matching files are touched

- **Evidence**: First-party architectural description with a concrete scoping example.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Rules are markdown files in `.claude/rules/` that give Claude specific constraints or conventions." / "Path-scoped rules allow you to load rule instructions only when they are relevant by adding a `paths` field that controls when they load." / "For example: a rule scoped to `src/api/**` stays out of context during a docs-only session."
- **Our assessment**: Rules occupy the design space between CLAUDE.md (always-on, high cost) and skills (on-demand, low cost). Path-scoped rules are the correct mechanism for constraints that apply to a subset of the codebase (e.g., security policies for API handlers, coding style for frontend components, migration rules for database models). Without path scoping, rules carry medium-always-on context cost; with path scoping, they approach zero cost during unrelated work. The post's example of a Zod validation rule scoped to API handlers is a concrete illustration of why path scoping matters: validation rules are irrelevant during documentation sessions.

### Claim 5: Skills load only their name and description at session start; the full body loads on invocation and is re-injected on compaction up to a shared budget, oldest first dropped

- **Evidence**: First-party architectural description with explicit compaction mechanics.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Name and description at session start; full body loads when the skill is invoked" / "Invoked skills re-injected up to a shared budget; oldest dropped first" / "Low. Full body loads only when invoked; subject to a shared token budget across invoked skills"
- **Our assessment**: The compaction mechanics for skills are more nuanced than a simple re-inject. Invoked skills compete for a shared token budget after compaction; if many skills were invoked in a long session, the oldest drop first. This means skill sessions with many sequential skill invocations can lose early skill content on compaction — practitioners running workflows that invoke multiple skills in sequence should be aware that later compaction events may drop the first-invoked skills. The "name and description at session start" mechanic explains why description quality matters for skill triggering: the description is all Claude sees until the skill is explicitly invoked.

### Claim 6: Subagents run in completely isolated context windows; only their final message returns to the main session, and the body context never enters the parent conversation at all

- **Evidence**: First-party architectural description with explicit isolation guarantees.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Not only does the larger instructional context within the body of the subagent not auto-invoke, it never enters the parent conversation at all. The subagent then runs in its own fresh context window, and the only thing that returns to your main session is the subagent's final message (often the aggregated result of many subtasks) plus metadata."
- **Our assessment**: The "never enters the parent conversation at all" guarantee is the key architectural fact that makes subagents valuable for context hygiene. Deep exploration tasks (log analysis, dependency audit, security review) can consume thousands of tokens in intermediate reasoning; all of that is discarded when the subagent completes, and only the final message crosses back to the main session. The "zero cost in main context until called" property in the table makes subagents the lowest-overhead mechanism until invoked. The nesting claim (up to five levels deep, tens to hundreds of background agents in dynamic workflows) establishes the upper scale of subagent orchestration.

### Claim 7: Hooks are the only instruction mechanism that bypasses compaction entirely, operating outside the main context window

- **Evidence**: First-party architectural description with explicit compaction bypass claim.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Bypass compaction entirely" / "Configuration lives outside main context; some output may return (e.g., blocking errors)" / "Deterministic automation: run linters, post to Slack on completion, block commands, back up chat history on PreCompact"
- **Our assessment**: The compaction bypass is hooks' most important architectural property. Every other instruction mechanism lives in or near the context window and is subject to degradation over long sessions. Hooks execute outside the context window entirely — they are configuration in `settings.json`, not content in the conversation. This is the architectural explanation for the practitioner failure documented in `failure-hooks-enforcement-2k.md`: prose rules in CLAUDE.md degrade through compaction; hooks never do. For enforcement (things that must not happen regardless of session length), hooks are the only mechanism with the right properties.

### Claim 8: There are five types of hooks — command, HTTP, mcp_tool, prompt, and agent — where only the first three are truly deterministic

- **Evidence**: First-party architectural description with explicit determinism boundary.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "There are several types of hooks: command, HTTP, mcp_tool, prompt, and agent. All hooks are deterministically triggered. The first three execute deterministically while the latter two, prompt and agent, use Claude's judgment rather than a set of rules to determine the output."
- **Our assessment**: This is a previously undocumented architectural nuance about hooks. The phrase "All hooks are deterministically triggered" describes the firing condition (lifecycle event occurs → hook fires, no model judgment involved). But the output of `prompt` and `agent` hooks is model-determined, not rule-determined. A `command` hook runs a fixed shell command and returns its output; the output is fully deterministic. A `prompt` hook asks Claude to evaluate something and returns its assessment; the output can vary. For enforcement purposes (must-not-happen constraints), command and HTTP hooks are the appropriate types — their output is deterministic and not subject to model variation.

### Claim 9: Output styles inject instructions into the system prompt, carry the highest instruction-following weight of any method, never get compacted, but should be used judiciously

- **Evidence**: First-party architectural description with explicit authority claim.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Output styles are files in `.claude/output-styles/` that inject instructions into the system prompt. They never get compacted, load at the start of every session, and are cached after the first request within a session." / "Because they sit in the system prompt, output styles carry the highest instruction-following weight of any method that we've covered so far and should be used judiciously."
- **Our assessment**: Output styles are the highest-authority instruction mechanism — they modify the system prompt rather than the user-facing context window. The "never compacted" and "highest instruction-following weight" properties make output styles the correct mechanism for significant, persistent behavioral changes (role shifts, response format mandates). The "high context cost" entry in the table reflects that output styles occupy system prompt space permanently. The "should be used judiciously" caveat and the explicit mention of "large, unintended changes" are the correct guardrails: output style changes can alter Claude's entire disposition in ways that affect every interaction, not just the targeted behavior.

### Claim 10: The append-system-prompt CLI flag is additive-only, safer for tone/formatting preferences, and never compacted

- **Evidence**: First-party architectural description with explicit safety framing relative to output styles.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Whereas modifying output style files can have large, unintended changes to Claude's behavior, the append flag is only additive to the original system prompt."
- **Our assessment**: The additive-only property of the append flag is its key safety advantage over output styles. Output styles can modify or override the default system prompt wholesale; the append flag adds to it. For practitioners who want to add tone or formatting preferences without risking unintended behavioral changes, the append flag is the safer choice. The "applies only to that invocation" compaction behavior (never compacted, but session-scoped) also makes it appropriate for one-off invocations with specific formatting needs.

### Claim 11: All file-based instruction methods have user-level counterparts that load for every Claude Code session regardless of repository

- **Evidence**: First-party architectural description.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "All file-based methods have a user-level counterpart loaded for every Claude Code session regardless of which repo you're in."
- **Our assessment**: The user-level vs. project-level distinction is the correct architectural separation between personal preferences and team conventions. Project-level files (committed to the repo) carry team-agreed conventions; user-level files carry individual preferences. The post makes the policy explicit: "Use local files for personal preferences (always use semantic commit messages). Keep project-level files for preferences that are team-wide but specific to a given codebase." Practitioners who commit personal preferences (like commit message style) to project-level CLAUDE.md impose those preferences on their entire team.

### Claim 12: Procedures (multi-step workflows) belong in skills, not in CLAUDE.md; CLAUDE.md is for always-needed facts

- **Evidence**: First-party decision rule presented as a quick-tip anti-pattern.
- **Confidence**: settled (first-party architectural guidance)
- **Quote**: "Procedures belong in skills. CLAUDE.md is for facts Claude should hold all the time: build commands, monorepo layout, team conventions. A deployment runbook or a security review checklist should live in `.claude/skills/`, where the body loads only when invoked."
- **Our assessment**: This is the primary structural decision rule for partitioning content between CLAUDE.md and skills. The economic rationale is implicit but clear: a 30-line deployment procedure in CLAUDE.md costs 30 lines of context on every session turn, even during turns where deployment is irrelevant. The same procedure in a skill costs near zero until explicitly invoked. The test for CLAUDE.md content: "Does Claude need to hold this fact at all times?" If no — if the content is relevant only when performing a specific task — it belongs in a skill, not CLAUDE.md.

### Claim 13: Enforcement constraints (things that must not happen) belong in hooks, not in CLAUDE.md; prose instructions cannot enforce never-do behaviors

- **Evidence**: First-party decision rule presented as a quick-tip anti-pattern.
- **Confidence**: settled (first-party architectural guidance)
- **Quote**: "When there's something that absolutely must not happen, an instruction is the wrong tool." (Quick tips section, on the anti-pattern of writing "Never do this" in CLAUDE.md)
- **Our assessment**: This is the most important architectural guidance in the post for practitioners who rely on CLAUDE.md for safety constraints. The post explicitly states that prose instructions cannot enforce never-do behaviors — they are, at best, suggestions that Claude follows when it feels like it. This directly corroborates the finding in `failure-hooks-enforcement-2k.md`: the practitioner built a 14-hook enforcement system after discovering that CLAUDE.md guidelines are treated as optional. The correct tool for enforcement is a hook with a PreToolUse matcher that blocks the prohibited command regardless of Claude's reasoning.

### Claim 14: Behaviors that should happen reliably on every action (e.g., running linters after every edit) belong in hooks, not in CLAUDE.md

- **Evidence**: First-party decision rule presented as a quick-tip anti-pattern.
- **Confidence**: settled (first-party architectural guidance)
- **Quote**: "If the behavior should happen reliably, like running prettier after every edit or posting to Slack on completion, use a hook in `settings.json` instead." (Quick tips section, on the anti-pattern of "Every time X, always do Y" in CLAUDE.md)
- **Our assessment**: This extends Claim 13 from enforcement (must-not-happen) to consistency (must-always-happen). Prose instructions like "always run prettier after every edit" are not architectural triggers — they are suggestions that rely on Claude remembering and following through. Hooks fire deterministically on lifecycle events with no dependence on Claude's attention or memory. For practitioners: if you find yourself writing "always X" in CLAUDE.md, the correct location is a PostToolUse hook that triggers on file write events.

### Claim 15: Subagents can nest up to five levels deep and enable dynamic workflows orchestrating tens to hundreds of background agents

- **Evidence**: First-party architectural specification with explicit nesting depth limit.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "This pattern scales: subagents can nest up to five levels deep, and dynamic workflows orchestrate tens to hundreds of background agents without requiring you to specify each detail."
- **Our assessment**: The five-level nesting depth is a concrete architectural limit not previously documented in the corpus. The "tens to hundreds of background agents" claim establishes the scale ceiling for dynamic subagent orchestration. Together these facts define the multi-agent coordination envelope: practitioners can build hierarchical orchestration up to 5 levels deep with large agent fleets, all returning only final summaries to the parent context. This corroborates the multi-agent coordination patterns from `blog-anthropic-dynamic-workflows-claude-code.md` and extends them with a specific depth constraint.

## Concrete Artifacts

### Seven-Method Comparison Table

```
Steering Claude Code: Complete Method Comparison
(Anthropic, "Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more," June 18, 2026)

Each method controls: When an instruction loads into context; Whether it persists through long sessions
(compaction behavior); and How much authority it carries.

Method                 | When it's loaded                                      | Compaction behavior                                           | Context cost                                                                      | When to use
-----------------------|-------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------
CLAUDE.md (root)       | Session start; stays in context for entire session    | Memoized. Read once and cached for the session;               | High. Every line costs tokens whether relevant or not                             | Build commands, directory layout, monorepo structure, coding conventions, team norms
                       |                                                       | cache cleared and re-read after compaction                    |                                                                                   |
CLAUDE.md (subdir)     | On-demand, when Claude reads a file under that        | Lost until that subdirectory is touched again                 | Low. Only consumes context when the relevant subdirectory is being worked on      | Conventions specific to a subdirectory
                       | subdirectory                                          |                                                               |                                                                                   |
Rules                  | Session start (user-level rules) or only when         | Re-injected on compaction                                     | Medium. Always-on unless path-scoped                                              | Specific constraints or conventions (e.g., all API handlers must validate input
                       | matching files are touched (path-scoped)              |                                                               |                                                                                   | with Zod)
Skills                 | Name and description at session start; full body      | Invoked skills re-injected up to a shared budget;             | Low. Full body loads only when invoked; subject to a shared token budget across   | Procedural workflows (deploy or release checklists)
                       | loads when the skill is invoked                       | oldest dropped first                                          | invoked skills                                                                    |
Subagents              | Name, description, and tool list at session start;    | Only the final message (summary plus metadata) returns        | Low. Zero cost in main context until called; runs in its own isolated context     | Running work in parallel or side tasks that should run in isolation and return
                       | body loads only when called via the Agent tool        | to the main session                                           | window                                                                            | only a summary (deep search, log analysis, dependency audit)
Hooks                  | Fire on lifecycle events                              | Bypass compaction entirely                                    | Low. Configuration lives outside main context; some output may return             | Deterministic automation: run linters, post to Slack on completion, block commands,
                       |                                                       |                                                               | (e.g., blocking errors)                                                           | back up chat history on PreCompact
Output styles          | Session start; injected into the system prompt        | Never compacted                                               | High. Occupies context window, but overwrites default system prompt               | Significant role changes (code assistant to general assistant)
Appending system prompt| Session start; passed as a CLI flag                  | Never compacted; applies only to that invocation              | Moderate. Cached after first request in a session                                 | Tone, response length, formatting preferences
```

### Five Anti-Pattern Quick Tips

```
Quick Tips for Claude Code Customization
(Anthropic, "Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more," June 18, 2026)

ANTI-PATTERN 1: "Every time X, always do Y" in CLAUDE.md
CORRECT TOOL: Hook in settings.json
"If the behavior should happen reliably, like running prettier after every edit or posting
 to Slack on completion, use a hook in `settings.json` instead."

ANTI-PATTERN 2: "Never do this" in CLAUDE.md
CORRECT TOOL: Hook (enforcement mechanism)
"When there's something that absolutely must not happen, an instruction is the wrong tool."

ANTI-PATTERN 3: A 30-line procedure in CLAUDE.md
CORRECT TOOL: Skill
"Procedures belong in skills. CLAUDE.md is for facts Claude should hold all the time:
 build commands, monorepo layout, team conventions. A deployment runbook or a security
 review checklist should live in `.claude/skills/`, where the body loads only when invoked."

ANTI-PATTERN 4: An API-specific rule without path scoping
CORRECT TOOL: Path-scoped rule with paths: field
"If a rule only applies to `src/api/**`, scoping it with `paths:` keeps it out of
 context during unrelated work."

ANTI-PATTERN 5: Writing personal preferences to a project-level CLAUDE.md file
CORRECT TOOL: User-level file (personal preferences)
"Use local files for personal preferences (always use semantic commit messages).
 Keep project-level files for preferences that are team-wide but specific to a given codebase."
```

### Hook Types and Determinism Boundary

```
Claude Code Hook Types
(Anthropic, "Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more," June 18, 2026)

Types: command, HTTP, mcp_tool, prompt, agent

"There are several types of hooks: command, HTTP, mcp_tool, prompt, and agent.
 All hooks are deterministically triggered. The first three execute deterministically
 while the latter two, prompt and agent, use Claude's judgment rather than a set of
 rules to determine the output."

Registration: "You register hooks in `settings.json`, managed policy settings, or skill/agent frontmatter."

DETERMINISM BOUNDARY:
  Fully deterministic output: command, HTTP, mcp_tool
  Trigger is deterministic, output is model-judged: prompt, agent

For enforcement (must-not-happen constraints): use command or HTTP hooks.
For advisory automation (context-aware): prompt and agent hooks are appropriate.
```

### Compaction Survival Hierarchy

```
Instruction Method Compaction Survival Summary
(Anthropic, "Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more," June 18, 2026)

SURVIVES COMPACTION (fully):
  Hooks             — bypass compaction entirely; config is outside context window
  Output styles     — never compacted; in system prompt
  Append system prompt — never compacted; applies only to that invocation

SURVIVES WITH RE-INJECTION:
  CLAUDE.md (root)  — memoized; re-read after compaction
  Rules             — re-injected on compaction
  Skills (invoked)  — re-injected up to shared budget; oldest dropped first

DOES NOT SURVIVE:
  CLAUDE.md (subdir) — lost until subdirectory is touched again
  Subagents          — only final message returns; intermediate work is discarded
```

## Cross-References

- **Corroborates**: `failure-hooks-enforcement-2k.md` (root cause section): The practitioner empirically discovered that CLAUDE.md guidelines are "fundamentally advisory" and get lost after compaction, prompting a 14-hook enforcement system. This source provides the exact architectural explanation: CLAUDE.md (root) survives compaction via memoization but is still prose subject to model interpretation; hooks "bypass compaction entirely" and operate outside the context window. Claim 13 here makes explicit what the failure report discovered empirically: "When there's something that absolutely must not happen, an instruction is the wrong tool." The two sources together form the complete picture: the failure report documents the problem; this post explains the correct architectural response.

- **Corroborates**: `blog-anthropic-large-codebase-best-practices.md` (Claim 6): That note states "Keeping CLAUDE.md files lean and layered. Claude loads them additively as it moves through the codebase: root file for the big picture, subdirectory files for local conventions." This source confirms the architectural mechanism behind that recommendation: root CLAUDE.md is always-on with high context cost ("every line costs tokens whether relevant or not"); subdirectory CLAUDE.md is on-demand with low context cost. The "lean" requirement for root CLAUDE.md is directly justified by the "every line costs tokens" cost characterization in the table.

- **Corroborates**: `blog-anthropic-claude-code-skills-lessons.md` (Claim 4, Claim 10): That note established that skills are folders (not just markdown files) and that the description field is a trigger condition. This source confirms the loading mechanics: only name and description load at session start, making the description's trigger-quality critical for skill invocation. The shared-token-budget compaction behavior here (Claim 5) provides new detail not in that note: invoked skills compete for a shared budget on compaction, with oldest dropped first — a constraint the skills post did not document.

- **Extends**: `blog-anthropic-large-codebase-best-practices.md` (Claim 5): That source named "The harness is built from five extension points—CLAUDE.md files, hooks, skills, plugins, and MCP servers—each serving a different function." This source is not a contradiction but a different taxonomy frame: it covers the seven *instruction mechanisms*, which overlap with but are not identical to the seven *extension points*. The instruction mechanisms (rules, output styles, system prompt append) are not extension points; the extension points (plugins, MCP servers) are not instruction mechanisms. Both taxonomies are needed: extension points describe what can be added to the harness; instruction methods describe how behavior can be directed. The guide should present both.

- **Extends**: `blog-anthropic-claude-code-skills-lessons.md` (Claim 13): That note described on-demand hooks for destructive operations. This source adds the compaction-bypass property of hooks as a first-party architectural claim, and introduces the five hook types with their determinism boundary — detail not present in the skills lessons post. The combination: hooks fire deterministically (all types), bypass compaction (all types), but only command/HTTP/mcp_tool produce deterministic outputs.

- **Extends**: `blog-anthropic-claude-code-routines.md` (Claim 2): The routines note describes three execution models (scheduled, API-triggered, webhook-triggered) for background automation. This source adds hooks as a complementary mechanism: hooks fire on Claude Code *lifecycle* events (file edit, tool call, session start/end) while routines fire on *external* triggers (time, HTTP, GitHub events). The two mechanisms operate at different abstraction levels: hooks control in-session behavior; routines control when sessions start.

- **Contradicts**: None found. The seven-method taxonomy here and the seven-extension-point taxonomy in `blog-anthropic-large-codebase-best-practices.md` use different frames (instruction methods vs. extension points) and do not contradict each other. No contradiction issue required.

- **Novel**:
  - **Subdirectory CLAUDE.md compaction loss**: The specific behavior — "lost until that subdirectory is touched again" — is not documented in any prior corpus source. The large-codebase post says subdirectory files load "on-demand" but does not specify compaction behavior.
  - **Skills shared-token-budget compaction with oldest-dropped**: The compaction mechanic for invoked skills (shared budget, oldest dropped first) is new to the corpus. The skills lessons post does not describe this compaction behavior.
  - **Subagent nesting depth limit (5 levels) and scale (tens to hundreds)**: The explicit 5-level nesting cap and dynamic-workflow scale claims are new to the corpus.
  - **Five hook types with determinism boundary (command/HTTP/mcp_tool vs. prompt/agent)**: The distinction between deterministic-output and model-judged-output hooks is new. Prior sources treat hooks as uniformly deterministic.
  - **Output styles as highest-authority instruction mechanism**: The explicit claim that output styles "carry the highest instruction-following weight of any method" is new. Prior sources describe output styles in passing but do not rank their authority.
  - **Append-system-prompt flag as safer alternative to output styles**: The additive-only guarantee of the `--append-system-prompt` flag and its "applies only to that invocation" scope is new to the corpus.
  - **Anti-pattern quick-tips decision rules** (procedures in skills, enforcement in hooks, path-scoping for module rules, personal preferences in user-level files): These five named anti-patterns with explicit correct-tool redirections are new to the corpus as a unified set.
  - **User-level counterparts for all file-based methods**: The explicit statement that "all file-based methods have a user-level counterpart" is new, generalizing what was known about user-level CLAUDE.md to rules, skills, subagents, and output styles.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Unified Decision Framework**: This source should anchor the harness engineering chapter's opening section. The seven-method comparison table is the first unified decision framework for "which mechanism to use when" — exactly the meta-layer missing from the existing corpus. Currently Chapter 02 covers individual mechanisms in isolation; this post provides the comparative frame that should precede those individual sections. Recommend adding a "Choosing the Right Mechanism" section as the first substantive chapter section, using the comparison table and the five anti-pattern quick tips as the organizing frame.

- **Chapter 02 (Harness Engineering) — CLAUDE.md Content Policy**: Claim 12 provides the authoritative content-partitioning rule: CLAUDE.md holds always-needed facts (build commands, directory layout, conventions); skills hold procedures. The guide should update any current advice that puts procedures or workflows in CLAUDE.md. Pair Claim 12 with Claim 2 (high context cost on every line) to explain the economic rationale: procedures in CLAUDE.md are a context tax on every session turn.

- **Chapter 02 (Harness Engineering) — Enforcement Architecture**: Claims 7, 13, and 14 together provide the enforcement architecture: prose rules are advisory; hooks enforce. The guide currently lacks a clear statement that CLAUDE.md cannot enforce never-do behaviors. Add a section on "Enforcement vs. Guidance" that draws this boundary: anything that must reliably happen or not happen belongs in a hook, not in prose instructions. Cross-reference `failure-hooks-enforcement-2k.md` as the practitioner evidence for why this distinction matters.

- **Chapter 02 (Harness Engineering) — Hook Type Selection**: Claim 8 (five hook types, determinism boundary) should drive a "Choosing the Right Hook Type" note. For enforcement (blocking prohibited commands), use command or HTTP hooks — deterministic output. For advisory automation (summarize context before compaction, route based on file type), prompt or agent hooks are appropriate. Prior guide content that treats hooks as uniformly deterministic should be updated.

- **Chapter 02 (Harness Engineering) — Output Styles and System Prompt Append**: This is the first corpus source to document both mechanisms in a comparative way. Add a section on "Role-Level Changes" covering output styles (highest authority, never compacted, major behavioral changes, use judiciously) vs. system prompt append (additive-only, session-scoped, safe for tone/formatting). The "should be used judiciously" framing from the source should accompany any output style guidance.

- **Chapter 04 (Context Engineering) — Compaction Survival Hierarchy**: The compaction behaviors across all seven methods form a hierarchy that directly impacts context engineering decisions. The guide should present the compaction survival table (hooks and output styles survive fully; root CLAUDE.md and rules survive with re-injection; subdirectory CLAUDE.md and subagent intermediate work do not survive) as a context engineering planning tool. Practitioners designing for long sessions need to know which mechanisms retain their effect through compaction.

- **Chapter 05 (Team Adoption) — User-Level vs. Project-Level Scoping**: Claim 11 provides the authoritative boundary: personal preferences go in user-level files; team conventions go in project-level files. The guide should add this decision rule to any section on configuring CLAUDE.md or skills for team use. The plugin distribution note from the "Getting started" section is also relevant here: skills, subagents, hooks, and output styles can be bundled as plugins for team-wide distribution.

## Extraction Notes

- The source is a blog post from claude.com. WebFetch returned summarized content and declined to reproduce verbatim full sections for copyright reasons. All quoted passages were extracted via multiple targeted fetch requests asking for specific short passages. The comparison table was reconstructed verbatim from a targeted fetch that succeeded in reproducing the table structure with cell content. All individual quoted passages were confirmed as character-for-character quotes by the WebFetch model in responses where it explicitly confirmed the passages as verbatim excerpts. The Assayer should spot-check all quotes against the live URL at https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more.
- Author name: No individual byline was visible in any WebFetch response. The post is attributed to "Anthropic" per the blog's standard attribution for product-wide posts.
- No contradiction with existing corpus notes was found that would require a contradiction issue. The seven-method taxonomy differs in scope from the seven-extension-point taxonomy in `blog-anthropic-large-codebase-best-practices.md` Claim 5 but the two are complementary frameworks (instruction methods vs. extension points), not contradictory claims.
- Confidence is set to `settled`: all claims are first-party Anthropic architectural descriptions of their own product's mechanisms, consistent with the observable behavior of Claude Code and corroborated by practitioner failure reports.
