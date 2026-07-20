---
source_url: https://cognition.com/blog/devin-for-terminal
source_type: blog-post
title: "Devin CLI: Start Local, Hand Off to the Cloud"
author: The Cognition Team
date_published: 2026-04-27
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: emerging
issue: "#2072"
---

# Devin CLI: Start Local, Hand Off to the Cloud

> Cognition's announcement of Devin CLI, a from-scratch local terminal
> coding agent (custom Rust rendering, choice of frontier models) whose
> defining feature is a `/handoff` command that transfers the current
> session — repo, branch, conversation context, and uncommitted diff —
> to a cloud Devin VM; official docs fetched alongside the post add the
> concrete harness mechanics the announcement itself only gestures at:
> four permission modes (Normal, Accept Edits, Bypass, Autonomous), an
> OS-sandboxed Autonomous mode, and a subagent system with
> foreground/background execution, cost-tiered model profiles, and
> `AGENT.md`-defined custom subagents interoperable with Claude Code's
> own agent format.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  04.27.26 per the page's byline; byline "By The Cognition Team," no
  individual author named — the same anonymous-team byline pattern as
  `blog-cognition-devin-in-windsurf.md`). This note also draws on four
  official Devin documentation pages fetched as substantive linked
  pages per MINER.md §1: the CLI Quickstart
  (`docs.devin.ai/cli/quickstart`), Essential Commands
  (`docs.devin.ai/cli/essential-commands`), Hand off to cloud Devins
  (`docs.devin.ai/cli/handoff`), and Subagents
  (`docs.devin.ai/cli/subagents`) — reached via the blog post's
  "Watch the film here" link to the CLI marketing page
  (`devin.ai/terminal`), which itself links to the docs site's "Read
  Docs" entry point. Claims below are attributed to whichever specific
  page they came from.
- **Author credibility**: First-party vendor content throughout — a
  product announcement on Cognition's own blog plus Cognition's own
  reference documentation (hosted on Mintlify, "docs.devin.ai"). No
  named customer, practitioner quote, or independent benchmark appears
  in the blog post itself. The documentation pages are more credible as
  *mechanism* descriptions (they are the shipped product's own
  reference manual, falsifiable by installing the tool) but are still
  vendor-authored with no third-party verification in this note.
- **Scope**: Covers the product announcement (local agent rebuilt from
  scratch, model choice, custom Rust terminal rendering), the four
  stated benefits of cloud handoff (parallel agents without worktrees,
  browser-based testing while stepping away, automated PR/review-comment
  handling, sandbox isolation), and — via the docs pages — the CLI's
  permission-mode system, the exact `/handoff` mechanics (what carries
  over to the cloud session), and the subagent system (profiles,
  cost model, custom `AGENT.md` subagents, nesting limits). Does
  **not** cover: any adoption, session-duration, or success-rate
  metric for Devin CLI; a named customer or practitioner testimonial
  (unlike `blog-cognition-devin-desktop.md`'s five named customers);
  the technical implementation of the Rust terminal-rendering library;
  or a worked, step-by-step example of a real `/handoff` session
  (the docs give the command and what carries over, but no transcript).

## Extracted Claims

### Claim 1: Devin CLI's core pitch is running Devin locally where the developer already works, then handing the same session to the cloud when the work outgrows the laptop
- **Evidence**: Opening tagline of the announcement post.
- **Confidence**: emerging (first-party framing of a shipped, named
  product; no adoption or usage data)
- **Quote**: "Run Devin right where you already work. When the work outgrows your laptop, hand the same session off to the cloud." (cognition.com/blog/devin-for-terminal)
- **Our assessment**: This restates, at the CLI-specific level, the same
  local/cloud complementary-roles philosophy already documented in
  `blog-cognition-devin-in-windsurf.md` Claim 5 (local for
  planning/prototyping/iteration, cloud for
  implementation/testing/QA/deployment) — but the operative word here is
  "same session," a stronger and more specific claim than that source's
  one-way "plan locally, delegate to cloud" loop: this post's model is
  session continuity (one session moving location), not a plan handed
  off as a separate artifact to a new cloud session.

### Claim 2: Devin CLI was rebuilt from scratch as a local coding agent with full codebase/tool/environment access, a choice of frontier models (Opus 4.7, GPT-5.5, and Cognition's own SWE-1.6), and a custom Rust terminal-rendering library for UI performance
- **Evidence**: Direct product description under "The full power of Devin,
  now local."
- **Confidence**: emerging (concrete, named engineering choices for a
  shipped product; no benchmark accompanies the "as fast and snappy as
  possible" rendering claim)
- **Quote**: "Devin CLI is a local coding agent with full access to your codebase, your tools, and your environment. Choose between any frontier model, including Opus 4.7, GPT-5.5, and our own SWE-1.6. We wrote a custom terminal rendering library in Rust to make the UI as fast and snappy as possible." (cognition.com/blog/devin-for-terminal)
- **Our assessment**: The named model list (Opus 4.7, GPT-5.5, SWE-1.6)
  is a snapshot as of the 04.27.26 publish date; the CLI's own marketing
  landing page (`devin.ai/terminal`, fetched 2026-07-20) now lists "Opus
  4.8, Fable 5, GPT-5.5, and SWE-1.6" — a newer model set. This is
  ordinary drift on a continuously-updated marketing page, not a
  contradiction between two claims about the same point in time; cite
  the blog post's list only as "supported models as of launch."
  Building a custom Rust terminal-rendering layer purely for perceived
  responsiveness is a concrete engineering investment claim distinct
  from anything previously in this corpus's Cognition cluster.

### Claim 3: Cloud handoff unlocks four capabilities a purely local terminal agent cannot offer: running multiple agents against one codebase without worktree/setup friction, shipping a feature while the agent tests it in its own browser, delegating a bug fix through PR creation and review-comment resolution, and working inside a sandbox instead of the user's own machine
- **Evidence**: Direct bulleted capability list under "Delegate to Devin
  in the cloud."
- **Confidence**: emerging (concrete, named capability list for a
  shipped integration; no example or metric for any of the four items)
- **Quote**: "Run multiple agents against the same codebase without fiddling with worktrees or setup scripts. Ship a feature, then move on while the agent tests it in its own browser. Hand off a bug fix and let Devin open a PR and resolve review comments for you. Stop worrying about rm -rf because the agent works in its own sandbox, not yours." (cognition.com/blog/devin-for-terminal)
- **Our assessment**: The "without fiddling with worktrees or setup
  scripts" framing is a specific, checkable claim about a known pain
  point in local multi-agent workflows (git worktree management)
  that the cloud-handoff model sidesteps by giving each delegated
  session its own VM rather than sharing the developer's working copy.
  The "stop worrying about rm -rf" line is the clearest plain-language
  articulation in this corpus's Cognition cluster of sandbox isolation
  as blast-radius containment for destructive commands specifically —
  see Cross-References for how this corroborates a broader,
  better-evidenced containment argument from a different vendor.

### Claim 4: Devin CLI is deliberately built to be lightweight enough to run on an original VT-100 terminal, the terminal type that has shaped software development interfaces since 1978
- **Evidence**: Postscript line and companion marketing landing page,
  both referencing a demonstration video.
- **Confidence**: anecdotal (a performance/compatibility stunt with a
  video as its only evidence — no benchmark, no definition of "runs on"
  beyond the demonstration existing)
- **Quote**: "P.S. We got Devin running on a VT-100, the terminal that's shaped modern development since 1978. [Watch the film here]" (cognition.com/blog/devin-for-terminal) / "Written in Rust and so performant that it can run on an original VT100." (devin.ai/terminal)
- **Our assessment**: Read alongside Claim 2's Rust-rendering claim, this
  is the marketing proof-point for that engineering investment — a
  hardware-compatibility stunt rather than a benchmarked performance
  number. Treat as illustrative of "very lightweight, low-bandwidth
  terminal protocol" rather than a quantified speed claim.

### Claim 5: Devin CLI does not yet support Knowledge, Playbooks, or Secrets from a user's Devin account — features available only in cloud Devin — though Cognition states it is actively working to add each
- **Evidence**: Direct statement on the official docs Quickstart page,
  under a "Devin CLI vs. Devin" comparison heading.
- **Confidence**: settled (first-party reference documentation stating
  an explicit, current feature gap for a shipped product, not a
  marketing claim)
- **Quote**: "Devin is our cloud-based AI software engineer that runs in a virtual machine. It includes features like Playbooks, Secrets, and Knowledge, and other capabilities that are not available in Devin CLI. Devin CLI does not yet support Knowledge, Playbooks, or Secrets from your Devin account. We're actively working on adding support for each of these and plan to roll them out soon." (docs.devin.ai/cli/quickstart)
- **Our assessment**: This is a specific, falsifiable capability gap
  the blog post itself never mentions — the announcement post frames
  cloud handoff purely as an upgrade path (more compute, sandboxing,
  parallelism), while the docs page discloses that the local CLI is
  also missing account-level features (stored knowledge, reusable
  playbooks, credential secrets) that cloud Devin has. Worth citing
  precisely because it is the one place in this source that names a
  CLI *limitation* rather than a benefit.

### Claim 6: Devin CLI has four built-in permission modes (Normal, Accept Edits, Bypass, Autonomous) plus three agent-modes (Normal, Plan, Ask), each trading off approval friction against blast-radius containment differently
- **Evidence**: Direct enumeration and per-mode description on the
  Essential Commands docs page.
- **Confidence**: settled (first-party reference documentation
  enumerating a shipped, exhaustive mode list with exact slash-command
  syntax for each)
- **Quote**: "Devin CLI has 4 built-in permission modes: Normal, Accept Edits, Bypass, and Autonomous, and 3 agent-modes: Normal, Plan, and Ask." (docs.devin.ai/cli/essential-commands)
- **Our assessment**: This is a more granular permission-mode taxonomy
  than this corpus has previously recorded for any single coding-agent
  CLI — most prior sources describe a binary "ask permission" vs. "skip
  permission" (bypass/yolo) distinction; Devin CLI names four discrete
  points on that spectrum, with Autonomous specifically requiring and
  bound to a sandbox rather than being a synonym for Bypass. See
  Cross-References for how this compares to GitHub Copilot's
  enterprise-managed bypass-permissions control.

### Claim 7: Bypass mode auto-approves all tool calls including shell commands and file writes with no sandbox requirement, while Autonomous mode requires `--sandbox`, is auto-selected and exclusive within sandboxed sessions, and contains shell commands and network access via OS-level sandbox scopes and domain allow/deny lists rather than removing prompts outright
- **Evidence**: Direct comparison table and mode descriptions on the
  Essential Commands docs page.
- **Confidence**: settled (first-party reference documentation
  specifying exact mechanics of two named, mutually exclusive modes)
- **Quote**: "Bypass: Auto-approves all tool calls, including writes and shell commands." / "Autonomous: Roughly equivalent to Accept Edits in the current workspace, with the additional ability to run any shell command within an OS-level sandbox (to contain what those commands can actually touch)." / "Autonomous relies on the sandbox for safety. Without --sandbox, the mode is unavailable — use Bypass if you want unattended execution without OS-level isolation." (docs.devin.ai/cli/essential-commands)
- **Our assessment**: The key distinction the docs draw is not
  "more permissive vs. less permissive" but "trusts the agent
  unconditionally vs. trusts the sandbox" — Bypass removes prompts
  and grants the agent the user's full machine access, while Autonomous
  keeps a form of scoped containment (filesystem write/read scopes,
  network domain allow/deny) active even though most prompts are
  suppressed. This maps directly onto the model-layer-vs-environment
  distinction argued abstractly in `blog-anthropic-how-contain-claude.md`
  Claim 3 (environmental containment should be the primary design
  priority because model-layer defenses will never reach 100%) — Devin
  CLI's Autonomous mode is a concrete, shipped instance of choosing
  environmental (sandbox) containment specifically so that reduced
  prompting doesn't mean reduced safety, rather than Bypass's approach
  of removing containment entirely in exchange for full trust.

### Claim 8: Admin-enforced deny and ask rules configured via Team Settings always take priority over Bypass mode, regardless of the individual user's mode choice
- **Evidence**: Direct statement on the Essential Commands docs page,
  under the Bypass mode description.
- **Confidence**: settled (first-party reference documentation stating
  an explicit precedence rule for a shipped enterprise control)
- **Quote**: "Bypass mode never overrides organization-level permissions configured by your admin via Team Settings. Admin-enforced deny and ask rules always take priority." (docs.devin.ai/cli/essential-commands)
- **Our assessment**: This is a direct structural parallel to
  `docs-github-copilot-enterprise-bypass-permissions.md` Claim 1
  (GitHub enterprise admins can set `disableBypassPermissionsMode` to
  prevent Copilot CLI and VS Code from skipping permission prompts,
  overriding the individual user's local choice) — two independent
  vendors (Cognition and GitHub/Microsoft) both shipping the same
  governance shape: an individual developer's "skip all prompts" mode
  is real and available, but an organization admin can constrain or
  override it centrally. Neither source discloses how the two controls
  compare in granularity (Devin's docs page here does not name a
  specific settings file or key the way the Copilot note's Claim 3
  does for `.github-private/.github/copilot/settings.json`).

### Claim 9: The `/handoff` command transfers a Devin CLI session to a cloud Devin VM by packaging the current git repo and branch, the full conversation context, and any uncommitted diff — and can be invoked with no task description to simply continue the existing work
- **Evidence**: Direct mechanism description and worked example on the
  "Hand off to cloud Devins" docs page.
- **Confidence**: settled (first-party reference documentation
  specifying the exact command syntax and the three named categories of
  state that transfer)
- **Quote**: "The Devin CLI packages up the conversation context and your current git branch, then creates a cloud session that picks up where you left off." / "Repo and branch — so the cloud session clones the right repo and checks out the branch you're on. Conversation context — what you and Devin have been working on in the current session. Uncommitted changes — your work-in-progress diff carries over. Commit or stash anything you don't want sent." (docs.devin.ai/cli/handoff)
- **Our assessment**: This is the first source in this corpus's
  Cognition cluster to specify *exactly* what a local-to-cloud handoff
  carries over, rather than describing the handoff only as a
  user-visible mechanic (contrast `blog-cognition-devin-in-windsurf.md`
  Claim 7, which names a "single click" trigger and a "plan" as the
  handoff artifact but does not enumerate its contents). The explicit
  warning that uncommitted changes are sent by default unless stashed
  is a concrete, actionable operational detail with no equivalent in
  any prior Cognition source in this corpus.

### Claim 10: An open-source "Devin Handoff" plugin lets any coding agent — Claude Code, Codex, Cursor, or plain shell scripts, not only Devin CLI — hand a task off to cloud Devin
- **Evidence**: Direct cross-tool compatibility statement on the "Hand
  off to cloud Devins" docs page, naming three specific competing
  agent products and linking to a public GitHub repository.
- **Confidence**: settled (first-party documentation naming a specific,
  linked, open-source artifact; not independently verified in this note
  beyond confirming the docs page's own claim)
- **Quote**: "Not using the Devin CLI? You can hand off from Claude Code, Codex, Cursor, or any coding agent — and from plain shell scripts — with the open-source Devin Handoff plugin." (docs.devin.ai/cli/handoff, linking to github.com/club-cog/devin-handoff)
- **Our assessment**: This is a notable competitive-posture claim: Devin
  is positioned not only as a competing local coding agent (versus
  Claude Code, Codex, Cursor) but simultaneously as a cloud execution
  *backend* that competitors' own local agents can hand work off to.
  This is new to this corpus — no prior Cognition source describes Devin
  cloud infrastructure as an explicit interop target for rival agent
  tools rather than purely a Devin-native feature.

### Claim 11: Subagents run as independent workers with their own conversation chain (not inheriting the parent's history), can be spawned in the foreground (parent pauses and waits) or background (parent continues, notified on completion), and each subagent consumes its own separate model/inference cost on top of the parent's spend
- **Evidence**: Direct mechanism description on the Subagents docs page,
  including an explicit foreground/background comparison and a stated
  cost model.
- **Confidence**: settled (first-party reference documentation
  describing exact, shipped subagent execution semantics)
- **Quote**: "Subagents let the main agent spawn independent workers to handle subtasks. A subagent shares tools and codebase context with the parent, but operates in its own conversation chain -- it does not inherit the parent's conversation history." / "Subagent Cost: Subagents run as their own agent sessions, each with its own context window and inference calls, so they consume cost independently of the parent." (docs.devin.ai/cli/subagents)
- **Our assessment**: This gives concrete implementation depth to the
  "spin up sub-Devins to investigate in parallel" claim already
  documented in `blog-cognition-auto-triage.md` Claim 3, which named the
  behavior but not its mechanics. The independent-cost detail is a
  specific, actionable warning largely absent from this corpus's
  existing subagent/multi-agent coverage: fanning out into many
  subagents is not "free" parallelism inside one session's context
  budget, but N separate billed sessions.

### Claim 12: Two built-in subagent profiles differ specifically in which model they run — `subagent_explore` (read-only research, restricted to a cheap default model, SWE-1.6 by default) versus `subagent_general` (full tool access including code changes, always inherits the parent's own selected model, so a premium-model parent multiplies cost per general subagent spawned)
- **Evidence**: Direct profile comparison table and an explicit cost
  warning on the Subagents docs page.
- **Confidence**: settled (first-party reference documentation with a
  named comparison table and an explicit warning about cost
  consequences of the design)
- **Quote**: "subagent_general inherits the parent's model. If you are running a premium model, every general subagent runs on that premium model too, with its own context window and inference calls — so a task that fans out into several general subagents multiplies your spend. Ask for an explore subagent (or a custom subagent with a cheaper model: pinned) when the work is research rather than code changes." (docs.devin.ai/cli/subagents)
- **Our assessment**: This is a specific, actionable cost-governance
  detail not found elsewhere in this corpus for any vendor's subagent
  system: the model a subagent uses is determined by which of two
  fixed profiles the parent selects (explore vs. general), not by an
  independent per-subagent model choice, and the only way to get a
  write-capable subagent on a cheaper model is a custom profile with a
  pinned `model:` field (see Claim 13). Enterprise admins can also
  govern the explore-tier default model or disable subagents entirely
  via an org-level "Default subagent model" setting with three states
  (router default, pinned model, or "None" — disables subagents
  entirely), per the same docs page.

### Claim 13: Custom subagent profiles are defined as `AGENT.md` files (YAML frontmatter plus a system prompt) inside a project- or user-scoped `agents/` directory, supporting `model`, `allowed-tools`, `permissions`, and `max-nesting` fields, and Devin CLI automatically imports Claude Code's own `.claude/agents/*.md` subagent files as custom profiles
- **Evidence**: Direct format specification, frontmatter field table, and
  explicit cross-tool import statement on the Subagents docs page.
- **Confidence**: settled (first-party reference documentation
  specifying an exact file format, directory convention, and explicit
  import compatibility with a named competitor's file format)
- **Quote**: "Custom subagents are also imported from Claude Code's agent format: .claude/agents/*.md — Each .md file becomes a subagent profile." / "Claude Code agent files use tools instead of allowed-tools in their frontmatter. Both formats are supported automatically." (docs.devin.ai/cli/subagents)
- **Our assessment**: This directly corroborates and extends
  `blog-sankalp-claude-code-20.md` Claim 4 (Claude Code's custom
  sub-agents live at `.claude/agents/your-agent-name.md`) — Devin CLI
  not only adopts the same directory-plus-frontmatter-plus-system-prompt
  shape for its own native `AGENT.md` format, it explicitly reads
  Claude Code's own agent files as a drop-in import path (auto-detecting
  the `tools` vs. `allowed-tools` frontmatter key difference between the
  two formats). This is a concrete, citable instance of one vendor's
  CLI agent explicitly building interoperability with a rival's
  configuration format, a stronger and more specific claim than the
  general-purpose ACP protocol interoperability documented in
  `blog-cognition-devin-desktop.md` Claim 4 (Devin Desktop supporting
  Codex/Claude Agent/OpenCode as ACP-compatible guest agents) — that
  case is protocol-level agent composition inside an IDE surface, this
  case is file-format-level configuration reuse for a CLI's own
  subagent definitions.

### Claim 14: By default a subagent cannot spawn its own subagents — only the root agent can — but a custom subagent profile can opt in to nested spawning via a `max-nesting` frontmatter field that caps how many levels deep the resulting tree may grow
- **Evidence**: Direct constraint statement and worked example (a
  `max-nesting: 3` chain) on the Subagents docs page.
- **Confidence**: settled (first-party reference documentation
  specifying an exact default constraint and its override mechanism)
- **Quote**: "By default, subagents cannot spawn their own subagents — only the root agent can. Subagent tools (run_subagent and read_subagent) are disabled inside a subagent to prevent unbounded nesting." / "Nested subagents can increase cost significantly. Each level of nesting spawns additional agents with their own context windows and inference calls. Use this feature deliberately." (docs.devin.ai/cli/subagents)
- **Our assessment**: This is a specific, named design guardrail against
  unbounded recursive agent fan-out — a concrete instance of a
  cost/blast-radius control that this corpus has not previously
  documented for any vendor's subagent or sub-workflow system at this
  level of mechanical detail (contrast `docs-ghaw-inline-sub-agents.md`,
  which documents GitHub Agentic Workflows' inline sub-agent format but
  does not, per that note's extracted claims, describe a nesting-depth
  limit or default prohibition on sub-agents spawning further
  sub-agents).

## Concrete Artifacts

### Full opening framing and feature description, verbatim (blog post)
```
Source: cognition.com/blog/devin-for-terminal, "By The Cognition Team," 04.27.26

"Run Devin right where you already work. When the work outgrows your
laptop, hand the same session off to the cloud."

"Devin CLI is a local coding agent with full access to your codebase,
your tools, and your environment. Choose between any frontier model,
including Opus 4.7, GPT-5.5, and our own SWE-1.6. We wrote a custom
terminal rendering library in Rust to make the UI as fast and snappy as
possible."

"When the work outgrows your laptop, hand the session to a cloud agent
with its own computer. Devin keeps working while you don't, so you come
back to a finished PR."

- Run multiple agents against the same codebase without fiddling with
  worktrees or setup scripts.
- Ship a feature, then move on while the agent tests it in its own
  browser.
- Hand off a bug fix and let Devin open a PR and resolve review
  comments for you.
- Stop worrying about rm -rf because the agent works in its own
  sandbox, not yours.

Installation: curl -fsSL https://cli.devin.ai/install.sh | bash

P.S. We got Devin running on a VT-100, the terminal that's shaped
modern development since 1978. [Watch the film here]
```

### Permission-mode reference, verbatim (docs.devin.ai/cli/essential-commands)
```
Devin CLI has 4 built-in permission modes: Normal, Accept Edits, Bypass,
and Autonomous, and 3 agent-modes: Normal, Plan, and Ask.

Normal — Auto-approves read-only tools within the current directory,
  and asks for permission for write/execute operations. (default mode;
  /normal or /mode normal)

Accept Edits — Auto-approves file edits within the workspace while
  still prompting for shell commands and other actions. "We expect
  people to spend most of their time here." (/accept-edits or /mode
  accept-edits)

Bypass — Auto-approves all tool calls, including writes and shell
  commands. (/bypass or /mode bypass; aliases /yolo, /dangerous; can
  also start via `devin --permission-mode bypass`). "Bypass mode never
  overrides organization-level permissions configured by your admin via
  Team Settings. Admin-enforced deny and ask rules always take
  priority."

Autonomous — "Roughly equivalent to Accept Edits in the current
  workspace, with the additional ability to run any shell command
  within an OS-level sandbox (to contain what those commands can
  actually touch)." Started via `devin --sandbox
  --permission-mode autonomous`; is the only mode available when
  running with --sandbox, and is selected automatically.

Bypass vs Autonomous comparison table:
                          Bypass                  Autonomous
Requires --sandbox        No                      Yes (only available
                                                    in sandbox sessions)
Shell commands             Auto-approved,          Auto-approved,
                            unrestricted            contained by the
                                                     sandbox
File writes (edit/write)   Auto-approved anywhere  Still prompt
                                                     (granting a scope
                                                     expands the
                                                     sandbox)
Network access             Unrestricted            Filtered by the
                                                     sandbox's domain
                                                     allow/deny lists
Respects admin Team        Yes                     Yes
  Settings
```

### `/handoff` command mechanics, verbatim (docs.devin.ai/cli/handoff)
```
"When a task outgrows your local machine — or you want Devin to keep
working while you step away — use the built-in /handoff command to
transfer the current session to a cloud Devin session. The cloud
session gets its own VM with a shell, browser, and full repo access,
so it can keep going after you close your laptop."

Example: /handoff fix the flaky integration tests in CI

"The Devin CLI packages up the conversation context and your current
git branch, then creates a cloud session that picks up where you left
off. Track its progress from your terminal or in the Devin web app."

Tip: "Run /handoff without a task description and the cloud session
continues from where you left off automatically."

What carries over:
- Repo and branch — so the cloud session clones the right repo and
  checks out the branch you're on.
- Conversation context — what you and Devin have been working on in
  the current session.
- Uncommitted changes — your work-in-progress diff carries over.
  Commit or stash anything you don't want sent.

Note: "Not using the Devin CLI? You can hand off from Claude Code,
Codex, Cursor, or any coding agent — and from plain shell scripts —
with the open-source Devin Handoff plugin." (github.com/club-cog/devin-handoff)
```

### Custom subagent `AGENT.md` example, verbatim (docs.devin.ai/cli/subagents)
```
Directory convention: .devin/agents/reviewer/AGENT.md
(also: .agents/agents/reviewer/AGENT.md; or globally at
~/.config/devin/agents/reviewer/AGENT.md on Linux/macOS,
%APPDATA%\devin\agents\reviewer\AGENT.md on Windows)

---
name: reviewer
description: Reviews code changes for correctness and style
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - exec
permissions:
  allow:
    - Exec(git diff)
    - Exec(git log)
  deny:
    - write
    - edit
---

You are a code review subagent. Your job is to review code changes
thoroughly and report findings back to the parent agent.

Focus on:
1. Correctness — logic errors, edge cases, off-by-one mistakes
2. Security — potential vulnerabilities
3. Style — consistency with the rest of the codebase
4. Performance — obvious inefficiencies

Always cite specific file paths and line numbers in your findings.

Frontmatter fields: name, description, model (default: default subagent
model, SWE-1.6 by default — not the parent's model), allowed-tools
(default: all tools; cannot grant ask_user_question, which is always
withheld from subagents), permissions (default: inherit), max-nesting
(default: none — overrides the maximum nesting depth).

Import compatibility: "Custom subagents are also imported from Claude
Code's agent format: .claude/agents/*.md — Each .md file becomes a
subagent profile." "Claude Code agent files use tools instead of
allowed-tools in their frontmatter. Both formats are supported
automatically."
```

### Subagent nesting-depth example, verbatim (docs.devin.ai/cli/subagents)
```
"By default, subagents cannot spawn their own subagents — only the
root agent can."

max-nesting: 3 allows the following chain:

Root agent (depth 0)
└── Custom subagent (depth 1) — can spawn children
    └── Child subagent (depth 2) — can spawn children
        └── Grandchild subagent (depth 3) — cannot spawn (depth limit
            reached)
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claim 1
    (GitHub enterprise admins can set `disableBypassPermissionsMode` to
    prevent Copilot CLI and VS Code from auto-skipping permission
    prompts) — this note's Claim 8 (Devin CLI's Bypass mode "never
    overrides organization-level permissions configured by your admin
    via Team Settings; admin-enforced deny and ask rules always take
    priority") is the same governance shape from a second, independent
    vendor: an individual user's "skip all prompts" mode exists, but an
    org admin can constrain or override it centrally. Neither source
    discloses comparable configuration-file detail for the other
    vendor's mechanism.
  - `blog-anthropic-how-contain-claude.md` Claim 3 (environmental
    containment should be the primary design priority because
    model-layer defenses will never reach 100% effectiveness) and
    Claim 7 (Claude Code's OS-level sandboxes, Seatbelt/bubblewrap,
    reduced permission prompts by 84% while catching 83% of overeager
    behaviors) — this note's Claim 7 (Devin CLI's Autonomous mode
    requires `--sandbox` and contains shell/network access via OS-level
    sandbox scopes rather than removing prompts outright, unlike Bypass)
    is a concrete, shipped instance of the same design principle from a
    second vendor: reducing approval friction without removing
    environmental containment. Devin's docs give no equivalent
    quantified before/after figure (e.g. no stated percentage reduction
    in prompts or overeager-behavior catch rate for Autonomous mode).
  - `blog-cognition-auto-triage.md` Claim 3 ("spin up sub-Devins to
    investigate in parallel") — this note's Claim 11 (subagents run
    independent conversation chains, spawned foreground or background)
    gives the general mechanism behind that specific triage-time
    behavior; the two sources describe the same underlying capability
    at different points in this corpus's timeline, with this note
    supplying the mechanics that source's claim named but did not
    explain.
  - `blog-sankalp-claude-code-20.md` Claim 4 (Claude Code's custom
    sub-agents live at `.claude/agents/your-agent-name.md`) — this
    note's Claim 13 directly corroborates the existence and shape of
    that file format from the far side: Devin CLI's own docs describe
    reading `.claude/agents/*.md` files as an automatic custom-subagent
    import path, confirming both the file location and its
    frontmatter-plus-system-prompt structure independently of the
    Claude Code practitioner source.

- **Contradicts**: None identified. No claim in this source conflicts
  with an existing source note's claim under matching conditions. One
  candidate was considered and rejected: the Devin CLI docs'
  `/handoff` command and a Claude Code practitioner's own custom
  `/handoff` command (`blog-sankalp-claude-code-20.md` Claim 3) share
  an identical command name but describe unrelated mechanisms — Devin's
  is a built-in feature that moves a session to a different execution
  environment (local to cloud VM); the Claude Code practitioner's is a
  self-authored slash command that writes a session summary before
  `/clear` within the same environment. Same name, different vendors,
  different mechanisms, no shared claim to disagree over — this is a
  naming coincidence, not a contradiction, and does not meet the
  MINER.md §4a filing bar.

- **Extends**:
  - `blog-cognition-devin-in-windsurf.md` — that source's Claim 5 (local
    for planning/prototyping/iteration, cloud for
    implementation/testing/QA/deployment) and Claim 7 (single-click
    handoff of a locally-produced plan to a cloud Devin session) are
    extended here from an IDE-specific, plan-as-artifact handoff into a
    terminal-native, session-as-artifact handoff (Claim 1, Claim 9) with
    a named command (`/handoff`) and an explicit list of exactly what
    state transfers (repo/branch, conversation context, uncommitted
    diff) — detail that source's Windsurf-based description did not
    specify.
  - `blog-cognition-devin-desktop.md` — that source's Claim 8 names
    "Devin CLI: The intelligence of Devin in your terminal" as one of
    four unified product surfaces without further detail; this note
    supplies the terminal surface's actual mechanics (permission modes,
    handoff command, subagent system) that the Desktop announcement
    only named in passing. That source's Claim 4 (ACP support letting
    Codex, Claude Agent, and OpenCode run inside Devin Desktop) is a
    protocol-level interoperability claim for the Desktop IDE surface;
    this note's Claim 13 (importing Claude Code's `.claude/agents/*.md`
    files as custom Devin CLI subagent profiles) is a second, distinct
    interoperability claim for the CLI surface, at the level of
    configuration file format rather than a runtime agent protocol.
  - `blog-cognition-auto-triage.md` — see Corroborates above.

- **Novel**: The four-mode permission taxonomy (Normal, Accept Edits,
  Bypass, Autonomous) with Autonomous specifically bound to and
  auto-selected within `--sandbox` sessions (Claims 6-7) is new to this
  corpus's Cognition cluster — prior sources describe local vs. cloud
  execution but not a graduated in-product permission-mode spectrum at
  this granularity. The exact `/handoff` payload (repo/branch,
  conversation context, uncommitted diff) and the cross-agent "Devin
  Handoff" open-source plugin enabling handoff *from* Claude Code,
  Codex, or Cursor to cloud Devin (Claims 9-10) are both new — no prior
  source in this corpus documents Devin as an interop target for rival
  agents' delegated work. The full subagent system — profile-based
  model selection with an explicit cost warning for `subagent_general`,
  `AGENT.md`-defined custom profiles with Claude-Code-format import
  compatibility, and a default no-nesting rule overridable via
  `max-nesting` (Claims 11-14) — is the most mechanically detailed
  subagent/sub-workflow specification in this corpus for any vendor,
  surpassing the format-level detail available for GitHub Agentic
  Workflows' inline sub-agents (`docs-ghaw-inline-sub-agents.md`) on
  the specific dimensions of cost model and nesting-depth control.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claims 6-8 (the four-mode
  permission taxonomy; Bypass vs. Autonomous as "remove containment
  entirely" vs. "reduce prompts but keep sandbox containment"; and
  admin-enforced Team Settings overriding Bypass) as the most granular,
  concrete permission-mode reference in this corpus's coding-agent CLI
  coverage. Pair with `blog-anthropic-how-contain-claude.md` Claims 3
  and 7 to show two independent vendors converging on
  "sandbox-first, prompts-second" as the design answer to approval
  fatigue, and with `docs-github-copilot-enterprise-bypass-permissions.md`
  Claim 1 to show admin-override-of-bypass as a second, independently
  shipped enterprise control shape.

- **Chapter 02 (Harness Engineering) / Chapter 04 (Context Engineering)**:
  Add Claim 9 (the `/handoff` command's exact payload: repo/branch,
  conversation context, uncommitted diff) as a concrete, citable answer
  to "what does a local-to-cloud agent handoff actually need to carry,"
  updating the guide's existing Cognition local/cloud coverage
  (`blog-cognition-devin-in-windsurf.md`) with mechanical specifics that
  source lacked. Flag the explicit warning that uncommitted changes
  transfer unless stashed — an actionable operational detail for anyone
  building or using a similar handoff mechanism.

- **Chapter 02 (Harness Engineering)**: Add Claims 11-14 (subagent
  execution model, profile-based cost/model selection, `AGENT.md`
  custom-subagent format, Claude-Code-format import, and default
  no-nesting rule) as the most mechanically detailed subagent reference
  in this corpus. Specifically flag Claim 12's cost warning
  (`subagent_general` inherits the parent's — possibly premium — model,
  multiplying spend on fan-out) as actionable guidance for readers
  designing multi-agent workflows with any vendor's tooling, and
  Claim 13's Claude Code interoperability as evidence that agent
  configuration formats (not just runtime protocols like ACP, per
  `blog-cognition-devin-desktop.md` Claim 4) are becoming a
  cross-vendor de facto standard.

- **Chapter 01 (Daily Workflows)**: Add Claim 10 (the open-source
  "Devin Handoff" plugin letting Claude Code, Codex, Cursor, or shell
  scripts hand work to cloud Devin) as a concrete example of a vendor
  positioning its cloud execution backend as usable independently of
  its own local agent — relevant if the guide discusses mixing agent
  vendors within one workflow rather than committing to a single tool's
  full stack.

## Extraction Notes

- Five pages were read in full beyond the primary blog post, within
  MINER.md §1's "follow up to 5 linked pages" budget: the CLI marketing
  landing page (`devin.ai/terminal`, reached via the blog post's "Watch
  the film here" link, which itself redirects from
  `www.devin.ai/terminal`), and four official docs pages reached from
  that landing page's "Read Docs" link and the docs site's own
  navigation and `llms.txt` index: CLI Quickstart
  (`docs.devin.ai/cli/quickstart`), Essential Commands
  (`docs.devin.ai/cli/essential-commands`), Hand off to cloud Devins
  (`docs.devin.ai/cli/handoff`), and Subagents
  (`docs.devin.ai/cli/subagents`). The docs pages were fetched as raw
  Markdown source (`.md` suffix on the docs URL) where available
  (handoff, subagents) or as tag-stripped raw HTML via `curl` with a
  browser user-agent (quickstart, essential-commands, and the blog post
  and landing page themselves) — the same verbatim-verification
  approach used in `blog-cognition-devin-desktop.md`'s Extraction Notes
  — specifically to avoid relying on WebFetch's small-model summarizer
  for anything quoted directly. Every quote above was cross-checked
  against this raw text.
- A sixth candidate link ("Devin can now Manage Devins" and "Devin can
  now Schedule Devins," surfaced only via the cognition.com/blog index
  while searching for a possible companion post, not linked directly
  from the primary source) was deliberately not followed — it is not a
  linked page from this source, and pulling it in would exceed the
  scope of this extraction; it remains a candidate for a future,
  separate source note if queued.
- The model list in Claim 2 (Opus 4.7, GPT-5.5, SWE-1.6) is dated to
  the blog post's 04.27.26 publish date; the CLI landing page, fetched
  fresh on 2026-07-20, already lists a newer set (Opus 4.8, Fable 5,
  GPT-5.5, SWE-1.6). This is flagged in Claim 2's assessment as ordinary
  drift on a continuously-updated marketing page, not treated as a
  claim conflict.
- No contradiction meeting the MINER.md §4a filing bar was identified.
  One candidate — the shared `/handoff` command name between this
  source and a Claude Code practitioner's self-authored command in
  `blog-sankalp-claude-code-20.md` Claim 3 — was considered and
  rejected as a naming coincidence between unrelated mechanisms, not a
  disagreement about the same claim; see Cross-References → Contradicts.
- Cross-references verified before writing: re-read
  `blog-cognition-devin-in-windsurf.md` in full and confirmed Claims 5
  and 7 by number and content; re-read `blog-cognition-devin-desktop.md`
  in full and confirmed Claims 4 and 8 by number and content; re-read
  `blog-cognition-auto-triage.md` in full and confirmed Claim 3 by
  number and content; re-read
  `docs-github-copilot-enterprise-bypass-permissions.md` in full and
  confirmed Claim 1 by number and content; re-read
  `blog-anthropic-how-contain-claude.md` in full and confirmed Claims 3
  and 7 by number and content; re-read `blog-sankalp-claude-code-20.md`
  in full and confirmed Claims 3 and 4 by number and content; re-read
  `docs-ghaw-inline-sub-agents.md` in full and confirmed it does not
  describe a nesting-depth limit or cost model, supporting the Novel
  section's comparison. No claim number was guessed or approximated.
