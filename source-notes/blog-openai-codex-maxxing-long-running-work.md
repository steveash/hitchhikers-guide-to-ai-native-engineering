---
source_url: https://openai.com/index/codex-maxxing-long-running-work
source_type: blog-post
title: "Codex-maxxing for long-running work"
author: "OpenAI (whitepaper), featuring practitioner Jason Liu"
date_published: 2026-06-22
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1919"
---

# Codex-maxxing for long-running work

> An OpenAI whitepaper — linked from a short landing-page blog post — that packages
> ten named UX patterns (durable threads, voice input, steering, memory/vault, computer
> and browser use, remote control, thread automations, three worked "loop" examples,
> goal-setting, and the side panel) around a single featured practitioner, Jason Liu,
> to argue Codex is becoming a persistent workspace for long-running work rather than
> a single-prompt coding tool.

## Source Context

- **Type**: blog-post landing page (`openai.com/index/codex-maxxing-long-running-work`,
  published June 22, 2026, ~250 words) that exists mainly to link to an 11-page PDF
  whitepaper (`cdn.openai.com/pdf/8a9f00cf-d379-4e20-b06f-dd7ba5196a11/OAI_WhitePaper_Codex-maxxing26.pdf`).
  Nearly all substantive content is in the PDF; the landing page itself contains only the
  headline, a one-line summary, and a "Read the full guide" link. Both were read in full.
- **Author credibility**: Published by OpenAI (whitepaper credits "Author: OpenAI" on its
  closing page) and structured around a single named external practitioner, Jason Liu,
  quoted throughout in pull-quotes ("source: Jason Liu"). This is promotional/product
  content, not an engineering retrospective — it reads as a curated tour of ten Codex
  product surfaces, illustrated with one practitioner's workflow, rather than a controlled
  study or a first-party engineering account of internal architecture (contrast with
  `blog-anthropic-harness-long-running.md`, which is an Anthropic engineering retrospective
  with cost/iteration data). No usage metrics, no comparison to other agents, and no detail
  on Jason Liu's role or affiliation beyond "Creator" is given anywhere in the document.
- **Scope**: Covers ten named Codex features/patterns for long-running, multi-surface work:
  durable threads, voice input, steering, memory (the "vault"), computer/browser use,
  remote control, thread automations, three worked example "loops," goal-setting for
  verifiable success criteria, and the side panel as an artifact-review surface. Does NOT
  cover: pricing, model version/configuration, adoption metrics, comparison to Claude Code
  or GitHub Copilot, or any account from a second named user. The whitepaper is illustrated
  entirely through one practitioner's stated preferences and a small number of UI
  screenshots; no benchmark or quantified outcome is given for any pattern.

## Extracted Claims

### Claim 1: A "durable thread" — a pinned conversation dedicated to a recurring workstream — accumulates context, preferences, and open loops over time, at the cost of higher per-turn spend than a fresh short thread
- **Evidence**: Product feature description with five named example use cases (Chief of
  Staff, OpenAI CLI, Social feedback monitoring, Agents SDK, Codex for open source) and an
  explicit cost tradeoff statement.
- **Confidence**: emerging (first-party feature description; the cost tradeoff is stated
  as fact but not quantified)
- **Quote**: "Durable threads keep history available as the conversation grows and stores them in the memory vault. But there's a tradeoff: long-running threads carry context and may cost more to run than a fresh short thread. For important workstreams, continuity can be worth it and easier to manage."
- **Our assessment**: This names, as a first-class UX pattern, the tradeoff practitioners already navigate ad hoc: one long thread that remembers everything vs. many short threads that are cheaper but stateless. OpenAI's guidance ("use a durable thread for work you expect to revisit") gives a concrete selection rule — recurring workstreams get a pinned thread; one-off tasks don't — but no threshold (token count, calendar duration, dollar cost) is given for when the cost crosses over into "worth it."

### Claim 2: Voice input's benefit is not speed but that spoken input captures the "unedited version" of a person's thinking — half-remembered names, loose direction, uncertainty — which text input tends to filter out
- **Evidence**: Product description plus a worked example transcript ("I think there is some guy named Ben in Slack who mentioned this, I do not remember exactly what, just go look.") and a Jason Liu pull-quote.
- **Confidence**: anecdotal (single-practitioner framing of why voice input is useful; not a controlled comparison of voice vs. text prompt quality)
- **Quote**: "The benefit isn't only speed. It's that spoken input often includes the unedited version of the work: the half-remembered name, the loose direction, the uncertainty, the thing that would be awkward to type but natural to say."
- **Our assessment**: This is a specific, non-obvious claim about *why* voice input helps, distinct from the generic "voice is faster than typing" framing. The companion Jason Liu quote — "A lot of plans get better when the model has access to the messy version of what you think" — extends it: voice is framed as a context-quality lever (more of the messy reasoning reaches the model), not merely a convenience feature. No evidence is given beyond the practitioner's own account that plans actually get better; this is asserted, not measured.

### Claim 3: "Steering" — issuing the next instruction while Codex is already working, mid-task — lets a user correct direction, add context, approve the next step, or queue an action after a tool call, without waiting for the current step to finish
- **Evidence**: Product description with six example steering utterances ("Make this smaller," "Once this is done, open a PR," "Wait for the preview deployment," etc.) and a UI screenshot showing a queued instruction ("Once this is done, open a PR.") submitted while Codex is mid-run.
- **Confidence**: settled (concrete, demonstrated product mechanic — queuing an instruction while an agent is actively executing — not a subjective framing claim)
- **Quote**: "Steering means adding the next instruction while Codex is already working. You can correct direction, add context, approve the next step, or queue up the next action after a tool call."
- **Our assessment**: This is a specific interaction mechanic (queue an instruction mid-execution rather than only at turn boundaries) that is worth distinguishing from the term "steering" as used elsewhere in the corpus. `blog-anthropic-steering-claude-code-mechanisms.md` uses "steering" as an umbrella term for *pre-session* instruction mechanisms (CLAUDE.md, skills, hooks, rules, subagents) — i.e., how you configure Claude's behavior before or between sessions. This source uses "steering" for something narrower and different: *live, mid-execution* message queuing during a single active run. Both are legitimate uses of the word but describe different mechanisms at different points in the agent lifecycle; a reader of both notes should not conflate them. This is a terminology collision, not a substantive contradiction — no contradiction issue filed (see Cross-References).

### Claim 4: Memory should be an external, reviewable artifact — something you can "open, edit, diff, and reuse" — rather than left implicit in conversation history, because message history alone is insufficient once threads run long
- **Evidence**: Product framing plus a concrete directory-tree screenshot of a memory "vault" (`vault/AGENTS.md`, `TODO.md`, `projects/`, `agent/USER_CONTEXT.md`, `people/`, etc.) and an explicit repositories-vs-vault distinction.
- **Confidence**: settled (the reviewability principle and the repos/vault distinction are stated as explicit, non-hedged design guidance)
- **Quote**: "Memory acts as a notebook to provide context for actions. As threads last longer, they need memory outside the conversation. While message history helps, it's not always enough. Useful context should become something you can open, edit, diff, and reuse."
- **Our assessment**: The explicit "Repositories hold code. The vault holds rolling context around the work." distinction is the most transferable idea in this claim: it argues for a dedicated, versioned, human-reviewable memory store (people notes, decisions, open loops, daily notes, project state) that is architecturally separate from the codebase, and — when the vault itself lives in GitHub — reviewable via diffs the same way code changes are. This corroborates and extends the CLAUDE.md-as-persistent-context pattern documented elsewhere in the corpus, but is explicitly framed as *runtime, accumulating* memory (what happened, what's still open) rather than *static* project instructions (build commands, conventions) — a different content type than CLAUDE.md, even though both are markdown-in-a-repo.

### Claim 5: Memory should record discrete facts as they occur ("this decision was made," "this loop is closed") rather than accumulate vague impressions passively — treated as an explicit instruction to give the agent, not an automatic background process
- **Evidence**: A worked "memory instruction" example block: "As people are mentioned, update the relevant people notes. As projects move forward, update the project page. As loops close, mark them closed. As decisions are made, write down the decision and why it matters."
- **Confidence**: emerging (prescriptive design guidance from the whitepaper; not demonstrated with a before/after example of vague-vs-discrete memory)
- **Quote**: "That review step matters. Long-running threads should not quietly accumulate vague impressions in conversation history. They should record what changed."
- **Our assessment**: This is a concrete, actionable instruction template distinct from the more abstract Claim 4 (memory-as-notebook). It gives four specific event-to-write-action mappings (person mentioned → update people notes; project moves → update project page; loop closes → mark closed; decision made → record decision + rationale) that a practitioner could paste directly into a memory-maintenance system prompt. The explicit call-out that this needs a human review step ("you can see what Codex thought was important enough to write down") acknowledges the same risk documented elsewhere in the corpus around agents over- or under-recording context — but offers no mechanism to detect when the agent's judgment about what to record is wrong, only that diffs make it checkable after the fact.

### Claim 6: Surface choice for computer/browser tasks should follow a specific decision rule: local browser preview for iterating on a local app, Chrome for tasks needing logged-in/multi-tab state, and full computer use (with review) only when a desktop app is the sole path
- **Evidence**: Explicit conditional guidance following a four-surface taxonomy ($browser, @chrome, @computer, Connectors) plus Skills as a fifth, packaging mechanism.
- **Confidence**: settled (explicit, unhedged decision rule from a first-party product source)
- **Quote**: "If you are iterating on a local app, use the browser surface. If the task depends on logged-in state or multiple authenticated tabs, use Chrome. If the only way to complete the task is through a desktop app, use computer use with clear permissions and review."
- **Our assessment**: This is a clean, minimal decision tree for a problem (which execution surface should an agent use for a given task) that most agent-tooling guidance leaves implicit. The ordering is notably risk-graded: it recommends the narrowest-scope surface (local browser preview) first and only escalates to the broadest-scope, highest-risk surface (full computer use) as a last resort, explicitly paired with "clear permissions and review" rather than treated as equivalent to the other options. Skills are framed separately, as a way to avoid "retaught every time" — packaging a successful workflow's instructions, references, and scripts for reuse — which is the same instinct behind reusable Claude Code skills, applied here to browser/computer-use workflows specifically.

### Claim 7: Remote control (mobile check-in on a desktop-initiated session) is explicitly framed as *not* a license to skip review — it exists to keep enough attention on a long-running loop to unblock the next decision point, not to let tasks run unsupervised
- **Evidence**: Product description plus a Jason Liu pull-quote describing the intended workflow (start at desk, walk away, review from phone, approve/redirect).
- **Confidence**: emerging (design intent stated explicitly by OpenAI; the practitioner quote describes intended use, not a measured outcome)
- **Quote**: "Remote control is not a reason to skip reviews. It is a way to keep enough attention on the loop to unblock the next move." / (Jason Liu) "Start the task at your desk. Walk away. Review the next decision point from your phone. Approve, redirect, or ask for a different pass."
- **Our assessment**: The explicit "not a reason to skip reviews" framing is notable as a vendor pre-empting a foreseeable misuse of its own feature (treat remote control as "fire and forget" rather than "stay in the loop from elsewhere"). This corroborates `docs-github-copilot-cli-remote-control-ga.md`, which shipped the equivalent capability (start on desktop, monitor/approve/steer from mobile, web, or another IDE) as a GA feature on the same general timeline — OpenAI's framing here is the normative complement to GitHub's mechanical description: both vendors converge on "remote control extends supervision across devices," not "remote control removes the need for supervision."

### Claim 8: "Thread automations" are heartbeat-style recurring wake-ups scoped to a single existing conversation thread — Codex returns to that same thread on a schedule, preserving its accumulated context, rather than starting a fresh session each time
- **Evidence**: Explicit contrast diagram ("normal prompt: do this now" vs. "thread automation: keep checking this and move it forward when something changes") plus a worked example creating a 30-minute Slack/Gmail-monitoring automation, with the product's own confirmation text shown in a screenshot.
- **Confidence**: settled (a specific, demonstrated mechanic: automation is attached to and preserves one thread's context, rather than being a stateless recurring job)
- **Quote**: "Thread automations are heartbeat-style recurring wake-up calls attached to the current thread. They tell Codex to return to the same conversation on a cadence, preserving the context instead of starting from scratch each time. A thread can have multiple schedules. It can run until a condition is met. It can adjust cadence as the task changes."
- **Our assessment**: The key differentiator from generic cron scheduling is context preservation within a single thread — this is closer to Claude's Managed Agents "scheduled deployments" (`blog-anthropic-managed-agents-scheduled-vaults.md`, Claim 1–2) and GitHub Copilot CLI's `/every`/`/after` prompt scheduling (`docs-github-copilot-cli-rubber-duck-scheduling-voice.md`, Claim 3) in mechanism, but distinct in scope: this note's automation explicitly reattaches to the *same* durable thread (so a Chief-of-Staff thread's automation shares all prior context with manually-issued messages in that thread), whereas Managed Agents' scheduled deployments are described as scheduling agent *sessions* generally, and GitHub's `/every`/`/after` schedule follow-up actions *within* a single CLI session's lifetime rather than reattaching a scheduled job to a specific persistent conversation across sessions. Three vendors now document three variants of the same underlying need (recurring unattended agent work); practitioners should treat "scheduling" as a spectrum from stateless cron-like triggers to fully context-preserving thread reattachment, not a single undifferentiated feature.

### Claim 9: Worked example — a 30-minute Slack/Gmail-monitoring automation is explicitly bounded to drafting only ("do not send anything without approval"), keeping the human as the final gate on tone, timing, and approval even though research and drafting run unattended
- **Evidence**: The "Loop 1 [Chief of Staff]" worked example, with an explicit "[What Codex prepares]" vs. "[You decide]" split shown in the whitepaper's own diagram.
- **Confidence**: settled (a specific, demonstrated prompt and its stated behavioral boundary, not an inferred pattern)
- **Quote**: "Every 30 minutes, check Slack and Gmail for unanswered messages that may need attention. Research the context and draft replies, but do not send anything without approval." / "[What Codex prepares] Open messages, Relevant context, Draft replies, Questions that need judgment. [You decide] Approval, Tone, Timing, Final decision."
- **Our assessment**: This is a concrete instance of the produce/approve split that recurs across all three worked "loop" examples in the whitepaper (this one; a Slack-feedback-driven Remotion re-render loop; and a customer-support refund-negotiation loop that explicitly reserves "any irreversible action" for human consent). None of the three loops in this whitepaper is fully autonomous end-to-end — each pairs unattended research/drafting/monitoring with an explicit, named human decision point before anything externally visible (a send, a publish, a refund) happens. This is a useful, OpenAI-first-party-documented instance of the "bounded autonomy" pattern that appears throughout the corpus under different names.

### Claim 10: A "strong" goal for an agent gives it something to verify against (a test suite, review criteria, or a clear definition of done) rather than only a plan to execute — illustrated with a library port that used the original codebase's own unit test suite as the pass/fail bar for the new implementation
- **Evidence**: An explicit weak-goal/strong-goal contrast pair, plus a named worked example (porting the Python "Rich" terminal-formatting library to Rust, keeping the public API compatible and passing the original Python test suite).
- **Confidence**: emerging (the general principle is asserted directly; the single example is presented without measured outcomes — no pass rate, timeline, or cost is given for the Rich-to-Rust port)
- **Quote**: "A weak goal asks Codex to implement a plan. A stronger goal gives Codex something to test against: expected behavior, review criteria, constraints, or a clear definition of done." / "Port this library, keep the public API compatible, and use the original unit tests as the success check. The work is ready for review when the same tests pass and the differences are documented."
- **Our assessment**: This is the same underlying principle as the "sprint contracts" pattern in `blog-anthropic-harness-long-running.md` (Claim 4) — negotiating and fixing what "done" means, in checkable terms, before generation starts — independently arrived at by a different vendor for a different product surface (a single-agent goal statement here, vs. a pre-sprint generator/evaluator negotiation there). The convergence across two vendors on "give the agent a checkable definition of done, not just a plan" strengthens this as a durable, vendor-independent practice rather than an idiosyncrasy of either product. Unlike the Anthropic post, this source gives no data (cost, iteration count, pass rate) for its own worked example — the Rich-to-Rust port is illustrated with a screenshot of the GitHub repository, not with results.

### Claim 11: The side panel is framed as more than a preview pane — it is where a shared artifact (markdown, spreadsheet, CSV, PDF, slides, or a small local web app) becomes the object both the user and Codex act on jointly, with review comments treated as instructions
- **Evidence**: Product description across three named sub-capabilities (Inspect artifacts, Operate web surfaces, Review changes), including the specific claim that a single `index.html` file with JavaScript/CSS is "often enough" to become a full interactive review surface, plus a Jason Liu pull-quote.
- **Confidence**: emerging (feature description plus a practitioner endorsement quote; no measurement of how often this pattern is used or how it compares to reviewing artifacts outside the panel)
- **Quote**: "The side panel is where Codex stops being only a chat app and starts becoming the place the work happens." (Jason Liu) / "You and Codex can look at the same object while the work is still moving. Comments become instructions. The artifact becomes context."
- **Our assessment**: "Comments become instructions, the artifact becomes context" is a specific and useful framing for how review feedback should flow back into an agent loop: rather than translating a visual/formatting critique into a prose instruction, the artifact itself (with inline comments) is the context the next turn operates on. The claim that a minimal `index.html` is "often enough" as a live interactive surface (rather than requiring a full dev server or deployed preview) is a concrete, checkable claim about minimum viable review infrastructure, though no example of a specific minimal artifact's fidelity limits is given.

## Concrete Artifacts

### Memory vault directory structure (whitepaper, Section 04 — Memory)

```
vault/
├── AGENTS.md              # How the vault operates
├── TODO.md                # Cross-project priorities and follow-ups
│
├── projects/
│   ├── README.md          # Active-project index
│   ├── agents-sdk/
│   ├── codex-for-open-source/
│   ├── early-access-program/
│   ├── rust-migration-blog/
│   └── ...                # Other active and archived workstreams
│
├── agent/
│   ├── USER_CONTEXT.md     # Working preferences and context
│   ├── daily-summary-*.md  # Daily decisions and follow-ups
│   └── ...                 # Research, synthesis, and learning
│
├── people/
```
*(directory tree as shown in whitepaper screenshot; truncated at "people/" where the
source image itself is cropped)*

### Memory instruction template (whitepaper, Section 04 — Memory)

```
As people are mentioned, update the relevant people notes.
As projects move forward, update the project page.
As loops close, mark them closed.
As decisions are made, write down the decision and why it matters.
```

### Durable-thread example workstreams (whitepaper, Section 01 — Durable threads)

```
Pinned threads (example, from whitepaper UI screenshot):
  • Chief of Staff
  • Workstream: Hiring
  • Workstream: Finding Office Space
  • Monitor: X / LinkedIn
  • Project: Codex for OSS
  • Workstream: Sponsoring Hackathons
```

### Three worked "loop" examples (whitepaper, Section 08)

```
Loop 1 [Chief of Staff]
  Trigger:  Every 30 minutes, check Slack and Gmail for unanswered messages
  Prepares: Open messages, relevant context, draft replies, judgment questions
  Human decides: Approval, tone, timing, final decision

Loop 2 [Monitor for feedback]
  Trigger:  Every weekday morning, check a Slack feedback thread
  Prepares: Feedback summary, updated render (Remotion), revision notes, review link
  Human decides: Creative judgment, final approval, publishing decision

Loop 3 [Get a refund]
  Trigger:  Every 5 minutes, check whether a support agent joined the thread;
            switch to every 1 minute once they reply
  Prepares: Status checks, draft responses, evidence, recommended next step
  Human decides: Consent, approval, any irreversible action
```

### Weak goal vs. strong goal (whitepaper, Section 09 — Goals)

```
[Weak goal]
"Implement the plan in this Markdown file."

[Strong goal]
"Port this library, keep the public API compatible, and use the original
unit tests as the success check. The work is ready for review when the
same tests pass and the differences are documented."

Worked example: porting the Python "Rich" terminal-formatting library to Rust,
using Rich's own existing unit test suite as the pass/fail bar for the port.
```

### Five-surface decision guide for computer/browser work (whitepaper, Section 05)

```
$browser     — local web surfaces, previews, and annotations (iterating on a local app)
@chrome      — signed-in browser sessions and authenticated tabs (logged-in state, multi-tab)
@computer    — GUI-only work that requires clicking (desktop apps; only when no other path exists)
Connectors   — Slack, Gmail, Calendar, GitHub, and other work surfaces
Skills       — reusable, packaged workflows so Codex doesn't need to be retaught every time
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-cli-remote-control-ga.md` (Claim 1, Claim 2): GitHub shipped GA
    remote control for Copilot CLI sessions (mobile/web/VS Code/JetBrains) on a similar
    timeline. This source's Claim 7 ("remote control is not a reason to skip reviews... a
    way to keep enough attention on the loop to unblock the next move") is the normative
    framing that matches GitHub's mechanical description of the same capability set (track
    progress, steer, approve/deny permissions remotely). Two vendors independently converging
    on "extend supervision across devices, don't remove it" strengthens this as the intended
    design pattern for remote agent control generally, not an OpenAI-specific philosophy.
  - `blog-anthropic-harness-long-running.md` (Claim 4, "sprint contracts"): This source's
    Claim 10 ("strong goals" — give the agent a test suite or review criteria as the
    definition of done, illustrated with the Rich-to-Rust port using the original unit
    tests as the pass bar) is the same underlying principle as Anthropic's sprint contracts
    (pre-agreeing on what "done" means before code is written), independently documented by
    a second vendor for a single-agent goal statement rather than a generator/evaluator
    negotiation. This cross-vendor convergence is the strongest corroboration in this note.
  - `blog-anthropic-managed-agents-scheduled-vaults.md` (Claim 1, Claim 2) and
    `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 3): This source's
    "thread automations" (Claim 8) is a third vendor's variant of scheduled/recurring
    unattended agent work, alongside Anthropic's Managed Agents scheduled deployments and
    GitHub Copilot CLI's `/every`/`/after`. See Claim 8's assessment for the mechanism-level
    distinctions between the three.
  - `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 4, Claim 5): Both
    sources document voice input as a first-class CLI/agent-workspace feature shipped around
    the same period (GitHub's is GA and explicitly local-only; this source does not state
    whether Codex's voice input processes on-device or in the cloud — an open gap, see
    Extraction Notes).
  - `blog-openai-codex-knowledge-work.md` (Claim 6): That source's aggregate usage claim
    ("~50% of Codex users now run more than one task simultaneously") is the quantitative,
    aggregate-adoption counterpart to this note's qualitative, single-practitioner
    illustration of the same underlying shift — a user managing multiple durable threads
    and automations as parallel workstreams rather than one task at a time.

- **Contradicts**: None filed. One notable terminology collision, not a substantive
  contradiction: this source's "steering" (Claim 3 — queuing a live instruction mid-execution
  during an active run) and `blog-anthropic-steering-claude-code-mechanisms.md`'s "steering"
  (an umbrella term for CLAUDE.md/rules/skills/hooks/subagents/output-styles as pre-session
  configuration mechanisms) use the identical word for two different points in the agent
  lifecycle — one is live/mid-task, the other is pre-session/configuration-time. Per MINER.md
  §4a this does not rise to a contradiction (neither source makes a claim that opposes the
  other; they simply reuse a common English word for different mechanisms), so no
  contradiction issue was filed. Flagged here so the Assayer/Smith do not conflate the two
  "steering" concepts if both sources are cited in the same guide section.

- **Extends**:
  - `blog-openai-codex-knowledge-work.md`: That source covered Codex's adoption metrics and
    usage-segment growth (developers vs. knowledge workers vs. personal users) with no
    concrete UX pattern detail. This source adds the concrete mechanics (durable threads,
    memory vault, thread automations, steering, remote control) that would produce the
    parallel-task and knowledge-work usage patterns that source measured in aggregate.
  - `blog-openai-notion-codex-case-study.md`: Both this note and the Notion case study are
    OpenAI-produced, single-practitioner customer-style narratives (Jason Liu here; Ryan
    Nystrom there) with the same epistemic profile — a named, credible practitioner, no
    aggregate metrics, no comparison to competing agents. This source is a step further
    removed from a specific company case study — it is framed as a general practice guide
    illustrated by one person's workflow rather than a company-attributed success story.
  - `blog-anthropic-session-management-1m-context.md`: That source addresses Claude Code's
    session/context-window mechanics (autocompact triggers, 1M context). This source's
    durable-threads tradeoff ("long-running threads carry context and may cost more to run
    than a fresh short thread") is the Codex-side analog of the same underlying context-cost
    problem, without the technical detail (token thresholds, compaction triggers) that the
    Claude Code source provides.

- **Novel**:
  - **Thread automations as context-preserving scheduled reattachment**: no prior corpus
    source documents a scheduling mechanism that explicitly reattaches to the *same* durable
    conversation thread (rather than starting a fresh session or firing a stateless job) —
    see Claim 8.
  - **"Comments become instructions, the artifact becomes context"**: this specific framing
    of how review feedback on a shared artifact should flow back into the next agent turn
    (Claim 11) is new phrasing not found elsewhere in the corpus, though the underlying
    idea of artifact-centric review is not entirely novel.
  - **Voice input as an "unedited version of your thinking" context-quality lever**
    (Claim 2): a specific, non-obvious argument for *why* voice input helps (captures messier,
    more honest reasoning) distinct from the "voice is faster" framing common elsewhere.
  - **Explicit produce/decide boundary formalized across three worked examples** (Claim 9):
    three parallel worked examples, each pairing unattended research/monitoring with a
    named, bounded human decision point (approval, creative judgment, consent for irreversible
    actions) — a concrete, repeated instance of the bounded-autonomy pattern.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add "durable threads" as a named pattern — dedicate a
  pinned, persistent thread to each recurring workstream (a project, a monitoring task, a
  chief-of-staff-style assistant) rather than starting fresh each time, with the explicit
  cost caveat (long threads cost more per turn than fresh ones) as the tradeoff to weigh.
  Add voice input's "unedited version of your thinking" framing (Claim 2) as a reason to
  recommend voice input beyond typing speed, next to GitHub Copilot CLI's local-only voice
  input entry (already in the corpus) — note the open gap that this source does not state
  whether Codex voice processing is local or cloud-based (see Extraction Notes).

- **Chapter 02 (Harness Engineering)**: Add the memory "vault" pattern (Claim 4, Claim 5) as
  a named alternative to relying on conversation history alone for long-running agent
  context: an external, versioned, diffable notebook (people, decisions, open loops, project
  state) that is explicitly *not* the same content type as static instruction files like
  CLAUDE.md. Add the concrete memory-instruction template (Concrete Artifacts) as an
  actionable pattern practitioners can adapt directly. Add the "strong goals" principle
  (Claim 10) alongside the sprint-contracts material already cited from
  `blog-anthropic-harness-long-running.md` — this is now a two-vendor-corroborated practice:
  give the agent a checkable, testable definition of done, not just a plan.

- **Chapter 02 or 06 (Scheduling / Production Deployment)**: Add "thread automations" to the
  scheduling taxonomy already assembling in the corpus (Claude Code Routines, Managed Agents
  scheduled deployments, GitHub Copilot CLI `/every`/`/after`) as a fourth variant — the one
  distinguished by reattaching to a specific durable thread's accumulated context rather
  than firing a stateless or session-fresh job. Note the four-vendor convergence on
  "recurring unattended agent work" as validation that this is now a load-bearing category
  of agent infrastructure, not a single vendor's experiment.

- **Chapter 03 (Verification) or wherever bounded-autonomy patterns are discussed**: Add the
  three worked "loop" examples (Concrete Artifacts) as concrete illustrations of the
  produce/decide split — each pairs unattended monitoring/drafting with an explicit, named
  human decision point before anything irreversible or externally visible happens. The refund
  loop's explicit reservation of "any irreversible action" for human consent is a clean,
  quotable instance of this boundary.

- **Chapter 04/05 (Remote Control / Team Adoption)**: Cite this source alongside
  `docs-github-copilot-cli-remote-control-ga.md` as two-vendor corroboration that "remote
  control extends supervision, it doesn't replace it" is the intended design philosophy for
  mobile/cross-device agent monitoring — not merely a GitHub-specific caveat.

## Extraction Notes

- The live URL (`https://openai.com/index/codex-maxxing-long-running-work`) returned HTTP 403
  to both WebFetch and direct `curl` with a browser user-agent. Retrieved via the Wayback
  Machine snapshot `http://web.archive.org/web/20260623104439/https://openai.com/index/codex-maxxing-long-running-work/`
  (crawled 2026-06-23, one day after publication), fetched with `curl` since WebFetch itself
  declines `web.archive.org` URLs directly. The archived landing page's text content was
  extracted by stripping HTML tags from the `<main>` element.
- Per MINER.md §1 ("follow up to 5 linked pages that seem substantive"), the landing page's
  one substantive outbound link — the 11-page PDF whitepaper — was fetched directly from
  `cdn.openai.com` (this URL was not blocked, unlike the landing page) and read in full via
  the PDF reader. All ten sections and every pull-quote, screenshot caption, and worked
  example in the claims above come from the PDF; the landing page alone would have supported
  none of the extracted claims beyond the one-sentence summary.
- All quotes above are copied verbatim from the PDF's rendered text (page-by-page, as
  returned by the PDF reader), including exact punctuation. Bracketed terms like "[Codex]"
  or "[durable thread]" reflect the whitepaper's own typographic convention of highlighting
  key terms in blue within body text — these bracket markers are the source's own styling,
  reproduced here only in Claim 3's quote where the bracketed term falls inside the quoted
  span; other quotes were selected to avoid mid-sentence bracket markers.
- Page-level image captions/UI screenshots (e.g., the vault directory tree, the pinned-thread
  list, the Slack/Gmail automation confirmation) are described in Concrete Artifacts as
  transcribed from the whitepaper's own screenshots, not independently verified against a
  live Codex session — this note cannot confirm the UI shown is current or unchanged since
  publication.
- Open gap: the whitepaper does not state whether Codex's voice input processes audio
  on-device or via a cloud service (contrast with GitHub Copilot CLI's explicit "runs
  locally" claim in `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`, Claim 5).
  Flagged for the Assayer/Smith rather than assumed either way.
- No contradiction issue was filed. The one notable overlap — two different corpus sources
  using the word "steering" for two different mechanisms — is a terminology collision, not a
  claim dispute, and is documented in Cross-References → Contradicts per MINER.md §4a.
