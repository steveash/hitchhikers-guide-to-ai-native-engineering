---
source_url: https://github.blog/changelog/2026-06-02-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input
source_type: docs
title: "Copilot CLI: Improved UI, rubber duck, prompt scheduling, and voice input"
author: GitHub (official changelog)
date_published: 2026-06-02
date_extracted: 2026-06-05
last_checked: 2026-06-05
status: current
confidence_overall: settled
issue: "#1067"
---

# Copilot CLI: Improved UI, Rubber Duck, Prompt Scheduling, and Voice Input

> GitHub's June 2026 Copilot CLI changelog introduces four capabilities — rubber duck peer-review agent, prompt scheduling, voice input, and experimental terminal — that expand the CLI interaction model from synchronous text sessions to include async deferred execution, multi-agent critique, and voice modality.

## Source Context

- **Type**: docs (GitHub official product changelog, June 2, 2026; ~350 words)
- **Author credibility**: GitHub engineering team official product changelog. Authoritative for the existence of these features, their availability status (GA vs. experimental), exact slash commands, and behavioral descriptions. Not a credible source for: real-world effectiveness of rubber duck review, voice accuracy under various conditions, prompt scheduling behavior on failure or machine sleep, or how these features interact with remote control sessions.
- **Scope**: Four Copilot CLI features announced June 2, 2026 — (1) rubber duck agent (GA), (2) voice input (GA), (3) prompt scheduling via `/every` and `/after` (experimental), and (4) experimental terminal redesign with tabs and accessibility modes. Does NOT cover: rubber duck's model selection or context window, prompt scheduling recovery on failure, voice input language support, administrative policy requirements for Business/Enterprise users, or how these features interact with auto model selection (see `docs-github-copilot-cli-auto-model-selection.md`) or remote control (see `docs-github-copilot-cli-remote-control-ga.md`).

## Extracted Claims

### Claim 1: Rubber duck is a GA built-in CLI agent that acts as a constructive critic, reviewing plans, designs, implementations, or tests for potential issues

- **Evidence**: Official GitHub product changelog announcing GA status. Explicitly invokable via `/rubber-duck`.
- **Confidence**: settled (product fact — GA stated in official changelog)
- **Quote**: "Rubber duck is a built-in CLI agent that acts as a constructive critic."
- **Our assessment**: This introduces a peer-review pattern within a single CLI session — the main agent does the work, the rubber duck agent critiques it. For practitioners: adding a rubber duck pass before accepting an agent's output provides a second-opinion from a different agent context, potentially catching issues the primary agent's self-assessment misses. The `/rubber-duck` manual invocation means practitioners control when the second pass runs — it is not automatic, preserving throughput for low-risk tasks.

### Claim 2: The main agent can pass work to the rubber duck secondary agent for review, covering four artifact types: plans, designs, implementations, and tests

- **Evidence**: Official changelog states that the main agent can pass work for review across four specific artifact types.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: (no direct quote for the delegation mechanism; see Claim 1 for the agent description)
- **Our assessment**: The four supported review targets (plans, designs, implementations, tests) map to distinct phases of a development cycle. This suggests rubber duck is tuned to offer phase-appropriate critique. For harness engineering: integrating `/rubber-duck` after each major output creates a multi-agent verification pipeline using only built-in CLI primitives — no additional API calls or external agents required. This is the CLI-native equivalent of the "verify before execute" pattern the guide recommends.

### Claim 3: Prompt scheduling introduces `/every` for recurring execution and `/after` for one-shot deferred execution — currently experimental

- **Evidence**: Official changelog documents both commands with concrete usage examples. A schedule manager tracks active schedules. Available via `/experimental on`.
- **Confidence**: emerging (product fact; experimental designation means behavior may change before GA)
- **Quote**: (no single verbatim sentence covering both commands; see Concrete Artifacts for documented examples)
- **Our assessment**: These are the first asynchronous temporal execution primitives documented in the Copilot CLI in our corpus. `/every` enables recurring task automation — running tests periodically, polling a build, checking a condition — without requiring external cron infrastructure. `/after` enables deferred execution — schedule a summary after a long task, trigger a follow-up after a delay. For practitioners running long CLI sessions, the CLI can execute scheduled work autonomously without manual queuing of each follow-up. The experimental status means teams should not rely on scheduling for critical workflows until GA.

### Claim 4: Voice input is GA, runs entirely on the user's machine, and supports two input methods — spacebar hold and Ctrl+X+V

- **Evidence**: Official changelog documents both input methods and explicitly confirms local-only audio processing.
- **Confidence**: settled (GA product fact in official changelog)
- **Quote**: "Hold the space bar on your keyboard and talk to input a prompt. Alternatively, press Ctrl+X followed by V to start recording"
- **Our assessment**: Local processing is the key differentiator — audio never leaves the machine. This addresses a common enterprise privacy concern about cloud-processed voice input. The two input methods (push-to-talk spacebar vs. Ctrl+X+V toggle) suit different interaction styles: push-to-talk for quick dictation vs. toggle mode for longer inputs. For practitioners: voice input enables hands-free CLI interaction, reducing friction when narrating complex instructions or reviewing output while hands are occupied.

### Claim 5: Voice input runs locally — all recorded audio stays on the user's machine

- **Evidence**: Official changelog explicitly states local processing as a design property.
- **Confidence**: settled (stated definitively in official changelog)
- **Quote**: "Voice input runs locally, so all audio you record stays on your machine."
- **Our assessment**: The on-device processing guarantee is a significant enterprise adoption enabler. Teams with strict data-residency requirements for developer tooling can now evaluate voice input without the usual concern about audio being transmitted to third-party servers. Note: the runtime download requirement (Claim 6) means teams with network restrictions must provision access to the runtime download before users can enable voice input.

### Claim 6: Voice input requires a one-time runtime download on first use, guided by the CLI

- **Evidence**: Official changelog states the CLI guides users through this download when first enabling voice input.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "The first time you enable voice input, the CLI guides you through downloading the runtime."
- **Our assessment**: Teams should include the runtime download step in their Copilot CLI onboarding documentation. Practitioners in air-gapped or restricted-network environments may not be able to complete the download without special provisions. Since voice input is GA (not experimental), this download is a production dependency, not an experimental preview step.

### Claim 7: The experimental terminal redesign introduces tab navigation across Session, Issues, Pull requests, and Gists — with theme-aware semantic colors and accessibility improvements

- **Evidence**: Official changelog describes the new terminal layout and tab targets. Color modes are explicitly named; screen reader detection is listed as an accessibility feature.
- **Confidence**: emerging (experimental feature; may change before GA)
- **Quote**: (no single verbatim quote; tab names listed in changelog as Session view, Issues, Pull requests, and personal Gists)
- **Our assessment**: Tab navigation turns the CLI into a multi-pane workspace — practitioners can switch between their agent session and GitHub entities without opening a browser. The Gists tab is an unexpected inclusion, suggesting practitioners who store session context or snippets in Gists can access them mid-session. For harness engineering: referencing Issues and PRs from within the CLI session may reduce manual copy-paste of issue descriptions into prompts.

### Claim 8: The experimental terminal adds five color modes — default, github, dim, high-contrast, and colorblind — plus automatic screen reader detection

- **Evidence**: Official changelog names the color modes. Screen reader detection is described as automatic (no manual configuration required).
- **Confidence**: emerging (experimental; color mode names may change before GA)
- **Quote**: "default, github, dim, high-contrast, and colorblind"
- **Our assessment**: The `colorblind` and `high-contrast` modes signal accessibility-first design intent. The `github` mode offers brand-consistent theming for practitioners who work primarily in GitHub's web UI. Automatic screen reader detection is the most significant accessibility improvement — accommodations activate without user configuration. For enterprise deployments: the high-contrast and colorblind modes may meet accessibility compliance requirements that currently prevent some practitioners from using the CLI.

### Claim 9: Rubber duck and voice input are generally available; experimental terminal and prompt scheduling require `/experimental on`

- **Evidence**: Official changelog explicitly states availability status for each feature.
- **Confidence**: settled (availability status stated definitively in official changelog)
- **Quote**: (rubber duck and voice input are "generally available today"; prompt scheduling and experimental terminal are "available to try via `/experimental`")
- **Our assessment**: The two-tier availability (GA vs. experimental) is operationally important for team deployments. Rubber duck and voice input can be rolled out to all Copilot CLI users without additional friction. Experimental features require each user to opt in via `/experimental on` — teams cannot enable these centrally for all users. This bifurcation also signals that rubber duck and voice input are production-stable, while prompt scheduling and the terminal redesign may still have rough edges. For guide advice: recommend rubber duck as a reliable default pattern; treat prompt scheduling as emerging but worth piloting.

## Concrete Artifacts

### Rubber Duck Invocation

```
# Manual rubber duck invocation
/rubber-duck

# Supported review targets:
# - Plans (before agent proceeds with implementation)
# - Designs (architectural or approach review)
# - Implementations (code review pass)
# - Tests (test coverage or quality review)
```

*Source: Copilot CLI changelog, June 2, 2026*

### Prompt Scheduling Commands

```
# Recurring execution (/every)
/every 30m run the frontend tests
/every 1h check for new issues

# One-shot deferred execution (/after)
/after 2h create summary

# A schedule manager tracks active schedules within the session

# Enable (experimental):
/experimental on
```

*Source: Copilot CLI changelog, June 2, 2026*

### Voice Input Methods

```
# Method 1: Push-to-talk
Hold spacebar → speak → release to submit

# Method 2: Toggle recording
Ctrl+X followed by V → speak → submit

# "Voice input runs locally, so all audio you record stays on your machine."
# First use: CLI guides through downloading the speech recognition runtime

# Availability: generally available (no /experimental required)
```

*Source: Copilot CLI changelog, June 2, 2026*

### Feature Availability Matrix

```
Feature                       Status         Enable
──────────────────────────────────────────────────────────
Rubber duck (/rubber-duck)    GA             (available by default)
Voice input                   GA             (available by default)
Prompt scheduling (/every,    Experimental   /experimental on
  /after)
Experimental terminal         Experimental   /experimental on

# CLI update: copilot update
# Share feedback: /feedback
```

*Source: Copilot CLI changelog, June 2, 2026*

### Experimental Terminal UI

```
Experimental Terminal (June 2026):

Tabs:
  - Session view       (current agent session)
  - Issues             (GitHub Issues)
  - Pull requests      (GitHub PRs)
  - Gists              (personal Gists)

Color modes: default, github, dim, high-contrast, colorblind
Accessibility: automatic screen reader detection
Colors: theme-aware semantic colors

Enable: /experimental on
```

*Source: Copilot CLI changelog, June 2, 2026*

## Cross-References

- **Corroborates** `docs-github-copilot-cli-remote-control-ga.md` (Claim 1): That source established Copilot CLI as a primary platform for new GitHub agent capabilities — remote control for async multi-platform oversight. This source adds four more CLI-first features (rubber duck, prompt scheduling, voice, terminal), reinforcing the pattern that the CLI is GitHub's primary agent development surface. The features are also complementary in practice: prompt scheduling creates deferred tasks that remote control can monitor asynchronously.

- **Corroborates** `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claim 5, Claim 6): That source documented a unified sessions view as an IDE-level observability primitive for concurrent sessions. This source shows the CLI gaining its own observability primitives — a schedule manager for active scheduled tasks and tab-based navigation. GitHub is developing parallel observability primitives in both the CLI and IDE surfaces.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` (Claim 5): That source documented routing transparency (which model was actually selected) as a practitioner affordance. This source adds rubber duck as another verification primitive — collectively, GitHub is building multiple layers of correctness-checking and observability into the CLI: model transparency (what ran), rubber duck (was the output good), schedule manager (what is queued).

- **Extends** `docs-github-copilot-agent-skills-cli.md` (Claim 1): That source established the Copilot CLI as the primary surface for new GitHub agent feature development. This source adds the latest cluster of CLI-only features (rubber duck, voice, scheduling, terminal), continuing the pattern documented across remote control, auto model selection, and JetBrains delegation.

- **Related** `blog-simonwillison-voice-mode-weaker.md`: That source covers ChatGPT's voice mode producing weaker outputs than text mode in consumer AI contexts. This source covers voice *input* (dictation into the CLI) rather than voice *output* (AI response via voice), and targets practitioner coding workflows rather than conversational AI. Not a contradiction — the features are distinct enough that the Karpathy model-stratification argument there does not directly apply to CLI dictation here.

- **Novel**:
  - **Rubber duck as a built-in peer-review agent pattern**: No prior source in corpus documents a CLI-native secondary agent serving as a constructive critic. Prior sources discuss self-critique via prompting or human review gates; this is the first automated peer-review agent as a first-class GA CLI command.
  - **Prompt scheduling (`/every`, `/after`) as temporal orchestration primitives**: No prior corpus source documents deferred or recurring CLI task execution as a built-in feature. Prior work requires external cron jobs, shell scripts, or GitHub Actions for time-based triggers.
  - **Local on-device voice input for a coding CLI assistant**: First documentation in corpus of voice modality for a coding CLI tool with a confirmed on-device processing guarantee and explicit privacy design.
  - **Multi-tab terminal UI with embedded GitHub entity navigation (Issues, PRs, Gists)**: No prior source documents a CLI that embeds GitHub entity browsing as first-class tabs. The CLI is evolving from a text-input-only interface toward a multi-pane workspace.
  - **Accessibility color modes in a coding CLI**: First corpus source to document named color modes (`default`, `github`, `dim`, `high-contrast`, `colorblind`) and automatic screen reader detection in a coding assistant CLI.

## Guide Impact

### Chapter 01: Daily Workflows

- **Rubber duck as a daily verification habit**: Add the rubber duck pattern as a recommended step after an agent produces a plan, implementation, or test — invoke `/rubber-duck` for a second-agent critique before accepting the output. Frame as a "cheap second opinion" that adds marginal time but increases output quality. Distinguish from human code review: rubber duck is fast and available at any hour, not a replacement for human judgment on critical changes.
- **Voice input for complex instructions**: Note voice input as useful for dictating long or nuanced prompts where typing is slower. Local processing removes the key enterprise objection (audio privacy). Highlight the one-time runtime download as the only adoption friction.
- **Prompt scheduling for background work**: Add `/every` and `/after` as patterns for practitioners who want the CLI to continue working during context switches. Example: `/every 30m run the frontend tests` enables the CLI to monitor build health autonomously during a long agent session.

### Chapter 02: Harness Engineering

- **Rubber duck in multi-agent pipelines**: Document rubber duck as a built-in verification layer available in any CLI session with no external infrastructure. A `produce → rubber-duck → review → apply` loop is achievable entirely within native CLI commands. This is the CLI-native equivalent of the guide's "verify before merge" pattern.
- **Prompt scheduling for async harnesses**: Note `/every` and `/after` as experimental primitives for deferred task orchestration. Teams currently using external schedulers for time-based triggers could pilot prompt scheduling for development-time workflows. Caveat: experimental status — not suitable for production harnesses until GA.
- **Experimental terminal for context switching**: The Issues/PRs/Gists tabs enable practitioners to reference GitHub context without leaving the CLI session. Document as a workflow pattern: review issues in the Issues tab, pull context into the Session directly.

### Chapter 04: Agent Behaviors and Patterns

- **Rubber duck as multi-agent peer review**: This is a concrete GA production instance of multi-agent critique — a second agent with a critic role reviewing the first agent's output. Add as the simplest possible multi-agent setup in the guide's coverage of multi-agent patterns: two agents, one produces, one critiques, available out-of-box in a GA CLI feature.
- **Temporal orchestration with prompt scheduling**: `/every` and `/after` introduce time as a first-class dimension in CLI agent workflows. Document the pattern: use `/every` for monitoring tasks (run tests, check conditions) and `/after` for completion triggers (generate summaries, create PRs after a task settles). Distinguish from GitHub Actions-based scheduling (more powerful, more infrastructure) and from remote control's manual steering (human-in-the-loop vs. autonomous).

## Extraction Notes

1. **Source is a short changelog (~350 words)**: Two WebFetch calls were made to the source URL. All substantive claims are exhausted in the nine claims above.
2. **Issue #561 (miner-blocked)**: The Prospector triage comments reference issue #561 (rubber duck supporting more models, May 7, 2026) which was miner-blocked and has no source note. This source (June 2, 2026) is therefore the first corpus note extracting rubber duck as a feature. The May 7 update is referenced only via issue, not in an extracted source note.
3. **Experimental features caveat**: Prompt scheduling and experimental terminal carry the caveat that behavior may change before GA. Claims 3, 7, and 8 are marked emerging accordingly; Claims 1, 4, 5, 6, and 9 are GA-backed and marked settled.
4. **No deep-linked documentation**: The changelog does not link to detailed docs for rubber duck invocation patterns, scheduling syntax, or terminal configuration. The extracted commands (`/every`, `/after`, `/rubber-duck`) come from examples in the changelog body.
5. **No contradictions identified**: Rubber duck peer-review, prompt scheduling, voice input, and the terminal redesign are all novel features with no prior corpus coverage that would generate a contradictory claim. No contradiction issue filed.
