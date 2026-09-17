---
source_url: https://claude.com/blog/cowork-is-now-claude
source_type: blog-post
title: "Claude Cowork and chat are now one Claude"
author: Anthropic (Claude.com blog)
date_published: 2026-09-16
date_extracted: 2026-09-17
last_checked: 2026-09-17
status: current
confidence_overall: emerging
issue: "#3502"
---

# Claude Cowork and chat are now one Claude

> Anthropic's announcement that Claude Cowork and Claude chat are merging into a single
> conversation surface — removing the mode-selection decision that prior Cowork
> onboarding guidance was built around — and adding Claude Docs/Slides plus an
> Auto/Manual permission toggle that mirrors Claude Code's auto mode, while shipping
> with a documented list of capability regressions (no GitHub import, no conversation
> branching, Dispatch closed to new users).

## Source Context

- **Type**: blog-post (first-party Anthropic product announcement, claude.com/blog,
  published September 16, 2026). Cross-read against the companion Help Center article
  "Claude Cowork and chat are one Claude" (support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude),
  linked from the blog post as "The full list of capabilities is in the Help Center,"
  which contains the technical detail (rollout mechanics, permission model, current
  limitations, prompting guidance) that the ~600-word blog post only gestures at.
- **Author credibility**: First-party Anthropic vendor announcement — authoritative on
  what the merged product does and how it is rolling out, since these are direct
  descriptions of a shipping (if staged) change to Anthropic's own product. The single
  named customer quote (Andrew Keller, Senior Economist) is a brief testimonial, not
  independently verified. The stated rationale for the merger ("people told us the
  frustrating part was deciding where a task belonged") is Anthropic's own
  characterization of user feedback, with no data cited — treat as anecdotal narrative,
  not a validated finding.
- **Scope**: Covers the product/UI mechanics of the Cowork+chat merger, the new
  Auto/Manual permission model, new deliverable types (Claude Docs, Claude Slides),
  staged rollout details, and a "what's different / current limitations" list for users
  migrating from separate Chat and Cowork surfaces. Does NOT cover: pricing changes,
  the underlying agent/orchestration architecture, enterprise admin controls beyond the
  30-day notice commitment, or usage-limit specifics beyond a qualitative statement that
  measurement may be temporarily inconsistent during rollout.

## Extracted Claims

### Claim 1: Claude Cowork and Claude chat are merging into a single conversation interface, removing the need to choose a product surface before starting a task
- **Evidence**: First-party product announcement plus companion Help Center technical article, both published the same day.
- **Confidence**: settled
- **Quote**: "Starting today, Claude Cowork and chat are merging into one Claude." (blog post)
- **Our assessment**: This is the headline architectural change and the reason the Prospector flagged this source as high-novelty — it invalidates the "separate product" model that multiple existing Cowork source notes describe as the status quo. See Cross-References.

### Claim 2: The stated rationale for the merger is that users didn't know which surface (Cowork vs. Design) a task belonged in, and work didn't carry over between the two
- **Evidence**: Anthropic's own narrative framing, no usage data or survey cited.
- **Confidence**: anecdotal
- **Quote**: "We built Cowork as a separate place for bigger work, and Design for visual work. People used both, and told us the frustrating part was deciding where a task belonged. What they'd started in one also didn't carry into the other." (blog post)
- **Our assessment**: Plausible and consistent with the friction pattern already documented in `blog-anthropic-cowork-getting-started.md` (a whole practitioner post exists to teach people how to make that Chat/Cowork decision), but it is Anthropic's self-reported justification for a product change, not independently measured.

### Claim 3: The merged experience is rolling out in stages — Pro/Max plans first, then Team/Free, with Enterprise admins guaranteed 30 days' notice before any change to their organization
- **Evidence**: First-party rollout commitment, stated in both blog post and Help Center article.
- **Confidence**: settled
- **Quote**: "This is rolling out to Pro and Max plans first, in the Claude app on web, desktop, and mobile over the coming weeks to existing and new users on these plans. There's nothing to turn on. Team and Free plans will follow soon, and Enterprise admins will hear from us at least 30 days before anything changes for their organizations." (blog post)
- **Our assessment**: Standard staged-rollout commitment; the 30-day Enterprise notice is a concrete, checkable claim worth tracking if a follow-up announcement is mined later.

### Claim 4: The rollout is per-account and one-way — even accounts on the same plan see the change at different times, and once migrated an account cannot switch back to separate Chat/Cowork
- **Evidence**: Help Center technical detail, more specific than the blog post.
- **Confidence**: settled
- **Quote**: "We're rolling this new experience out in stages, so even accounts on the same plan will see the changes at different times. You don't need to do anything to enable the new experience. If you're on a Pro or Max plan and your message box still shows \"Chat\" and \"Cowork\" options, you don't have it yet... Once your account has the new experience, you can't switch back to separate \"Chat\" and \"Cowork\" options." (Help Center)
- **Our assessment**: Practical implication for teams standardizing workflows: two teammates on the identical plan can be on different UI paradigms simultaneously, and there's no opt-out once migrated. Worth flagging for any guide advice that assumes a uniform Cowork/Chat experience across an org.

### Claim 5: Claude Docs and Claude Slides launch as new deliverable types, and Claude Design now works inside ordinary conversations instead of only as a standalone surface
- **Evidence**: First-party feature announcement.
- **Confidence**: emerging (explicitly beta)
- **Quote**: "Claude Docs and Claude Slides are new today, and Claude Design now works inside your conversations too... All three are in beta on paid plans, and Enterprise admins choose when to turn them on. If you use Claude Design on its own, it keeps working as before." (blog post)
- **Our assessment**: Extends the existing Claude Design corpus (`blog-anthropic-claude-design-product-designer-workflow.md` et al.) rather than replacing it — Design-as-standalone is explicitly preserved.

### Claim 6: A permission setting in the message box — "Auto" or "Manual" (default) — now controls how independently Claude acts across the whole conversation, replacing the separate Cowork/Chat mode choice as the locus of control
- **Evidence**: Help Center technical description of the control's two states and their behavior.
- **Confidence**: settled
- **Quote**: "A permission setting in the message box controls how independently Claude works: Auto: Claude keeps working without stopping to ask about each step, and automated safety checks run before it takes an action. Manual (default): Claude asks before it takes actions, and you choose whether to allow each one." (Help Center)
- **Our assessment**: This directly parallels the two-stage classifier architecture described in `blog-anthropic-claude-code-auto-mode.md` ("automated safety checks run before it takes an action" is nearly the same phrasing as that source's classifier-gated auto mode) — strong evidence Anthropic is standardizing one permission-gating pattern across Claude Code and the consumer chat/Cowork surface rather than maintaining separate safety models per product.

### Claim 7: Longer tasks continue running in the cloud after the user closes their laptop or leaves the page, except tasks that touch local files or apps, which require Claude Desktop to stay open
- **Evidence**: Help Center capability description.
- **Confidence**: settled
- **Quote**: "More involved tasks keep running in the cloud even if you close your laptop or leave the page. Come back when the task is done, and the result is waiting in the conversation. Tasks that use files or apps on your computer need Claude Desktop open." (Help Center)
- **Our assessment**: Consistent with prior Cowork background-execution claims; the local-file/Desktop-open caveat is a specific constraint worth carrying into any guide section on background task reliability.

### Claim 8: Scheduling recurring tasks (e.g., a weekly inbox summary) continues as a first-class capability in the merged product and can run in the cloud independent of the user's device being on
- **Evidence**: Help Center capability description, linking to a dedicated "Schedule recurring tasks in Claude Cowork" article.
- **Confidence**: settled
- **Quote**: "Ask Claude to run a task on a schedule, like a summary of your inbox every Monday morning. Scheduled tasks can run in the cloud, so they keep going when your computer is off." (Help Center)
- **Our assessment**: Corroborates the "set it and forget it" recurring-task pattern already documented in `blog-anthropic-cowork-marketing-ops.md`.

### Claim 9: The Dispatch feature (async multi-device task assignment) is closed to new users in the merged experience, though existing Dispatch users retain access
- **Evidence**: Help Center "Current limitations" list.
- **Confidence**: settled
- **Quote**: "Dispatch isn't available to new users. If you already use Dispatch, you can keep using it for now." (Help Center)
- **Our assessment**: A concrete feature-consolidation signal — Dispatch, previously announced as its own named capability in `blog-anthropic-dispatch-computer-use.md`, appears to be getting folded into (or superseded by) the unified conversation model rather than continuing as a standalone entry point for new users. Worth watching for a formal deprecation announcement.

### Claim 10: The merged experience ships with several documented capability regressions relative to standalone Cowork: no GitHub import, no conversation branching, degraded Incognito chats, and Search that excludes older Cowork tasks
- **Evidence**: Help Center "Current limitations" list, itemized by Anthropic itself (not third-party bug reports).
- **Confidence**: settled
- **Quote**: "Add from GitHub isn't supported. Branching a conversation from an earlier point isn't available. Incognito chats still work, but they open in the previous experience, so Claude can't create files or run code in them. Search doesn't include older Cowork tasks. It covers your chats and new conversations, and you can still find older tasks by name in Recents." (Help Center)
- **Our assessment**: High practical value — this is Anthropic voluntarily disclosing real capability gaps at launch, not a third-party failure report. Practitioners currently relying on GitHub-sourced Cowork tasks, conversation branching, or Incognito+file-creation should expect friction on migration, not a strict superset of prior functionality.

### Claim 11: Connected apps (Google Drive, Gmail, Microsoft 365, Slack) are used dynamically mid-task without requiring the user to pre-select a mode, pulling resources as the task needs them
- **Evidence**: Help Center capability description.
- **Confidence**: settled
- **Quote**: "Apps you've connected to Claude (like Google Drive, Gmail, Microsoft 365, or Slack) work while Claude carries out a task, so it can pull what it needs as it goes." (Help Center)
- **Our assessment**: Consistent with the connector-first design already described in `blog-anthropic-dispatch-computer-use.md`; this source extends it by removing the mode-selection step that previously gated when connectors were "in scope."

### Claim 12: All usage counts toward the same plan limit, agentic tasks (web search, code execution, file creation) consume more than a quick question, and usage measurement may be temporarily inconsistent for accounts mid-rollout
- **Evidence**: Help Center statement on usage accounting during the transition.
- **Confidence**: emerging
- **Quote**: "Everything you do with Claude counts toward your plan's usage limits. Longer agentic tasks that search the web, run code, or create files generally use more than a quick question. While the new experience rolls out, usage may be measured slightly differently for accounts that have it and accounts that don't." (Help Center)
- **Our assessment**: A direct, if vague, admission that usage accounting is in flux during rollout — practitioners tracking usage/cost budgets should expect temporary inconsistency rather than a clean cutover.

### Claim 13: Recommended prompting for the merged experience follows a three-part brief — desired outcome, delivery format, and required inputs — rather than a mode choice
- **Evidence**: Help Center "Get started" guidance.
- **Confidence**: emerging
- **Quote**: "You'll get better results when you include: Your desired outcome: what you want to end up with, like \"a one-page summary\" or \"a spreadsheet with a tab for each region.\" The format: how you want the result delivered, like a Word document, a slide deck, or a message you can paste into Slack. Inputs Claude will need: the files, links, or apps Claude should work from." (Help Center)
- **Our assessment**: This is a narrower, three-part restatement of the five-ingredient checklist in `blog-anthropic-cowork-getting-started.md` (Claim 3) — the newer guidance drops the older checklist's explicit "is this Cowork-shaped?" framing entirely, consistent with Claim 1 above (there is no longer a Cowork-shaped-task decision to make).

### Claim 14: A named practitioner testimonial describes delegating a multi-step, cross-database legal research task end-to-end from within a single conversation
- **Evidence**: Single named customer quote in the blog post; no independent verification.
- **Confidence**: anecdotal
- **Quote**: "I could have Claude pull up [my legal research database], and it would pull all the cases, read them, figure out which other cases I might need, download them, and store them in a folder for my personal review." - Andrew Keller, Senior Economist (blog post)
- **Our assessment**: Illustrative but thin evidence — one quote, and the speaker's title ("Senior Economist") doesn't obviously match the described task (legal case research), which is either a role mismatch in Anthropic's editing or evidence the speaker's actual work spans both domains. Treat as anecdotal color, not a validated capability benchmark.

## Concrete Artifacts

Capability list, verbatim from the Help Center article's "What Claude can do" section
(each is a named sub-heading followed by description; headings marked with `**`):

```
**Hand Claude a whole task**
Describe the outcome you want, and Claude works through the steps on its own:
searching the web, reading your files, running code, and putting the results
together. You don't need to break the work into steps or pick a mode first.
A quick question still gets a quick answer, and you can have several tasks
running at the same time.
Try: "Go through these five interview notes and pull out the top themes,
with a quote for each."

**Step away while Claude works**
More involved tasks keep running in the cloud even if you close your laptop
or leave the page. Come back when the task is done, and the result is
waiting in the conversation. Tasks that use files or apps on your computer
need Claude Desktop open.
Try: "Research the top project management tools for small teams and write
up a comparison. I'll check back later."

**Get finished files back**
Claude can create documents, spreadsheets with working formulas, and
presentations you can open in PowerPoint. Download them and use them
anywhere, or ask Claude to keep refining them.
Try: "Turn this analysis into a 10-slide deck I can present on Monday."

**Create designs, decks, and docs**
Claude can build charts, diagrams, and interactive visuals right in the
conversation... Claude Design makes on-brand visuals and mockups, Claude
Slides makes presentations, and Claude Docs makes living documents you
write with Claude and your team (Claude Design, Claude Slides, and Claude
Docs are in beta.)
Try: "Make a one-page visual summary of this launch plan."

**Use the apps you've connected**
Apps you've connected to Claude (like Google Drive, Gmail, Microsoft 365,
or Slack) work while Claude carries out a task, so it can pull what it
needs as it goes.
Try: "Find last quarter's board deck in my Drive and summarize what
changed since."

**Schedule recurring work**
Ask Claude to run a task on a schedule, like a summary of your inbox every
Monday morning. Scheduled tasks can run in the cloud, so they keep going
when your computer is off.
Try: "Every weekday at 8 AM, summarize new messages in my team's Slack
channels."
```
— Source: Help Center, "Claude Cowork and chat are one Claude"
(support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)

Permission model, verbatim:

```
A permission setting in the message box controls how independently Claude works:
Auto: Claude keeps working without stopping to ask about each step, and
automated safety checks run before it takes an action.
Manual (default): Claude asks before it takes actions, and you choose
whether to allow each one.
You can change the setting at any time, and you can stop or redirect Claude
while it works. The setting applies to the whole conversation. For work
with real consequences, like sending messages or changing important files,
stay close and review what Claude does.
```
— Source: Help Center, same article

Current limitations list, verbatim:

```
Add from GitHub isn't supported.
Branching a conversation from an earlier point isn't available.
Incognito chats still work, but they open in the previous experience, so
Claude can't create files or run code in them.
Search doesn't include older Cowork tasks. It covers your chats and new
conversations, and you can still find older tasks by name in Recents.
Dispatch isn't available to new users. If you already use Dispatch, you
can keep using it for now.
```
— Source: Help Center, same article

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-auto-mode.md` — the new Auto/Manual permission setting
    (Claim 6) uses near-identical framing ("automated safety checks run before it takes
    an action") to that source's classifier-gated Claude Code auto mode, suggesting one
    permission-gating design is being propagated across products.
  - `blog-anthropic-dispatch-computer-use.md` — connector-first, dynamic-resource-pull
    design (Claim 11) matches that source's connector-first hierarchy, now generalized
    to any conversation instead of a dedicated Dispatch/Cowork mode.
  - `blog-anthropic-cowork-marketing-ops.md` — scheduled recurring tasks (Claim 8)
    corroborate the "set it and forget it" pattern already documented there.

- **Contradicts**: No formal contradiction filed. `blog-anthropic-cowork-getting-started.md`
  Claim 1 ("The key decision boundary between Chat and Cowork is output type") describes
  a product paradigm that this source announces the removal of (Claim 1 here). This is
  not treated as a live contradiction under MINER.md §4a — the two sources describe the
  product at different points in time (pre- and post-merger), not two contemporaneous
  claims in tension. Recommend the Smith mark `blog-anthropic-cowork-getting-started.md`
  Claim 1 (and its Claim 2, "Cowork inverts the Chat usage model") as superseded-by-date
  rather than filing a contradiction issue, since there is no genuine disagreement to
  adjudicate — the underlying product simply changed.

- **Extends**:
  - `blog-anthropic-cowork-getting-started.md` — Claim 13 here (three-part prompting
    brief) is a narrower restatement of that source's five-ingredient checklist (Claim 3),
    with the Cowork-shaped-task decision step removed.
  - `blog-anthropic-cowork-deploy-guide.md` — its Chat/Cowork/Code decision framework is
    the enterprise-scale version of the same decision boundary this source removes.
  - `blog-anthropic-cowork-usage-taxonomy.md` and `blog-anthropic-cowork-enterprise.md` —
    both describe Cowork as a distinct surface with its own usage patterns and governance
    controls; this source doesn't contradict their data but changes the surface those
    patterns will occur on going forward.

- **Novel**: The Auto/Manual permission toggle's specific naming and default (Manual) in
  the consumer chat/Cowork context (Claim 6); the one-way, per-account staged migration
  mechanics with no opt-out (Claim 4); the voluntarily-disclosed capability-regression
  list (Claim 10); and Dispatch's closure to new users (Claim 9) are all new to the
  corpus.

## Guide Impact

- **Chapter covering interaction-pattern selection / mode choice** (Ch02 per Prospector
  triage): Any guide text instructing readers to decide "Chat vs. Cowork" based on output
  type (sourced from `blog-anthropic-cowork-getting-started.md` Claim 1) should be
  qualified as describing the pre-September-2026 Cowork architecture. Add a note that
  Anthropic has since merged the two surfaces, that the decision point is now a
  per-message Auto/Manual permission toggle rather than a product choice, and that the
  migration is staged and one-way per account (Claim 3, 4) — so guide readers on
  different plans/timelines may see either UI.
- **Chapters covering multi-agent/task-delegation patterns** (Ch04 per Prospector):
  Update any Dispatch coverage sourced from `blog-anthropic-dispatch-computer-use.md` to
  note that Dispatch is closed to new users as of this merger (Claim 9) — readers
  starting fresh should not expect to find it.
- **Any chapter citing Claude Design as a standalone deliverable surface**: note that
  Claude Docs and Claude Slides now exist alongside Design, all usable inline within
  ordinary conversations, while Design also continues to work standalone (Claim 5).
- **Any chapter advising on migration or capability parity when a vendor merges/changes
  product surfaces**: the documented regression list (Claim 10 — no GitHub import, no
  conversation branching, degraded Incognito, Search gaps) is a useful concrete example
  of "read the fine print before treating a UI merger as a strict superset."

## Extraction Notes

- The blog post itself is short (~600 words); the substantive technical detail (rollout
  mechanics, the Auto/Manual permission model, the current-limitations list, and
  prompting guidance) lives in the linked Help Center article
  (support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude), which
  the blog post itself points to as "The full list of capabilities is in the Help
  Center." Both pages were fetched and read in full (raw HTML extracted to plain text,
  not summarized by an intermediary model) to source verbatim quotes.
  No other linked sub-pages (e.g., "Schedule recurring tasks in Claude Cowork," "Use
  Claude Cowork safely") were followed, since the merger-specific claims were fully
  covered by the two primary pages; those linked articles cover pre-existing Cowork
  functionality already mined in other source notes.
- I considered filing a contradiction issue against `blog-anthropic-cowork-getting-started.md`
  Claim 1 but concluded it does not meet the bar in MINER.md §4a: both sources are
  accurate for the period they describe, and there is no live disagreement for a human
  to adjudicate. Flagged instead under Cross-References/Contradicts with a recommendation
  to mark the older claim superseded.
