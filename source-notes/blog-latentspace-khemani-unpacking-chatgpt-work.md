---
source_url: https://www.latent.space/p/unpacking-chatgpt-work
source_type: blog-post
title: "Unpacking ChatGPT Work: the Agent for a Billion Users"
author: Shlok Khemani (Latent Space)
date_published: 2026-08-04
date_extracted: 2026-08-21
last_checked: 2026-08-21
status: current
confidence_overall: emerging
issue: "#2841"
---

# Unpacking ChatGPT Work: the Agent for a Billion Users

> An outsider's reverse-engineered feature analysis of ChatGPT Work —
> Memory, Proactivity, Scheduled Tasks, Browser Use, and the
> Plugins/Skills/Tools architecture — reported through hands-on testing
> rather than insider access, naming specific mechanisms (a
> `/workspace/scratch` directory, a browser "permission ledger," a
> standalone-vs-heartbeat scheduled-task split) not documented elsewhere
> in the corpus.

## Source Context

- **Type**: blog-post (Latent Space / Substack feature analysis, published
  2026-08-04, single long-form article with named section headings).
- **Author credibility**: Shlok Khemani, writing for Latent Space (a
  trusted, high-signal AI-engineering publication already well
  represented in this corpus). This is an external analyst's
  reconstruction based on hands-on product use and public reporting
  (linked tweets), not an OpenAI insider interview — several claims
  (e.g. the "10 million users" figure) are explicitly sourced to
  third-party social-media posts rather than official OpenAI
  announcements, and the author flags this distinction himself
  ("reportedly crossed"). Treat as a credible but externally-sourced
  reconstruction, one step removed from primary-source status.
- **Scope**: Covers ChatGPT Work's persistent storage and memory system,
  proactivity/suggestion behavior, scheduled tasks, browser-use
  architecture and its current failure modes, the plugins/skills/tools
  architecture, local vs. cloud operating modes, and three open design
  questions the author identifies going forward. Does NOT cover: harness
  internals shared with Codex (covered by
  `blog-latentspace-nathan-chatgpt-work-harness.md`), pricing, enterprise
  admin/compliance features, or quantified task-success/error-rate data
  for any feature — all feature descriptions are qualitative/behavioral,
  not benchmarked.

## Extracted Claims

### Claim 1: ChatGPT Work is defined as "an agent for knowledge work" that connects to a user's existing workplace tools (Slack, email, Drive, calendars, CRMs, project trackers, and "hundreds of other plugins") to gather cross-tool context and produce finished work, running on the Codex harness inside a cloud microVM
- **Evidence**: The article's own opening framing statement, under the "What is Work?" heading.
- **Confidence**: emerging (a specific, named product framing from a credible analyst, consistent with OpenAI's own marketing language but stated independently)
- **Quote**: "At its core: **An agent for knowledge work.** You connect it to the places you already work—Slack, email, Drive, calendars, CRMs, project trackers, and hundreds of other plugins—and it gathers context across all of them to produce finished work."
- **Our assessment**: This framing is consistent with `blog-openai-chatgpt-work-ambitious-partner.md` Claim 1 (ChatGPT Work "gathers information across a user's connected apps and workflows" and "stay[s] with complex, multi-hour projects"), so it corroborates rather than adds new architectural detail on its own — the value is in the more granular breakdowns that follow in this article.

### Claim 2: Each ChatGPT Work task gets a working directory at `/workspace/scratch` where the agent has ordinary-computer freedom (create folders, install dependencies, maintain databases), but continuity of context across tasks runs through ChatGPT's product layer rather than persisting on the computer itself, as a deliberate safety/control separation
- **Evidence**: The author's own technical description under "Persistence & Memory," presented as an architectural observation rather than an OpenAI statement.
- **Confidence**: emerging (a specific, named implementation detail from hands-on analysis, not confirmed by an OpenAI source in this article)
- **Quote**: "Every Work task (thread) gets a working directory under /workspace/scratch, where the agent has the freedom of a normal computer"
- **Our assessment**: This is a more mechanistic account of the same persistent-computer feature that `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 6 traces to OpenClaw as design inspiration (files that "stay around between sessions"). Neither source states whether `/workspace/scratch` itself is the persistent store or a per-task scratch space that gets wiped between tasks while continuity is reconstructed from the product-layer memory system (Claim 3 below) — this article's own wording ("continuity... runs through ChatGPT's product layer rather than the computer itself") suggests the latter, which is a meaningful architectural nuance not present in the Nathan interview.

### Claim 3: ChatGPT Work's memory relies on three elements — compressed summaries of recent tasks/files, a "Personal Context" tool that queries Chat/Work history through a separately managed service, and a ChatGPT-maintained user profile supplied at task start — and raw conversation transcripts are not stored on the computer for the agent to browse
- **Evidence**: The author's own description under "Persistence & Memory," including a named tool ("Personal Context") and its retrieval mechanism.
- **Confidence**: emerging (specific, named mechanism claims from hands-on analysis; not confirmed against OpenAI's own technical documentation in this article)
- **Quote**: "the agent calls Personal Context, a dedicated tool that queries Chat and Work history through a separately managed service and returns the relevant excerpts."
- **Quote (transcript access)**: "Raw conversation transcripts are not stored on the computer for the agent to browse"
- **Our assessment**: This extends `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 9 (bidirectional Memory V3, shared read/write across ChatGPT and ChatGPT Work) with retrieval mechanism detail Nathan's interview did not supply — specifically, that memory is accessed via a named tool call rather than by the agent browsing raw history directly, and that summarization/excerpting happens before context reaches the agent. Nathan's interview never names "Personal Context" as a distinct tool, so this is novel mechanism detail, not a restatement.

### Claim 4: ChatGPT Work generates personalized proactive task suggestions when users open new conversations (e.g., identifying an upcoming calendar event and pre-drafting a meeting-prep prompt), but these suggestions currently require the user to select and execute them — the agent does not yet complete suggested tasks autonomously
- **Evidence**: First-hand account of the author's own testing, under a section on proactivity.
- **Confidence**: anecdotal (a single tester's hands-on observation of a specific suggestion instance, not a systematic study of suggestion quality or frequency)
- **Quote**: "One suggestion offered to prepare me for an upcoming call. When I selected it, Work injected a pre-authored prompt."
- **Our assessment**: This is a useful, concrete boundary claim — proactivity here means surfacing suggestions a human must still trigger, not autonomous task completion — that sharpens the vaguer "proactive" language used elsewhere in the corpus. No existing note in this corpus draws this specific "suggests but does not execute" distinction for ChatGPT Work.

### Claim 5: ChatGPT Work supports two distinct scheduled-task mechanisms — standalone tasks that run from a saved prompt at a set time, and "heartbeat" tasks that reawaken an existing conversation with its prior context intact — with triggers settable to exact times, time windows (e.g. "morning"), or conditions the agent monitors
- **Evidence**: The author's own taxonomy of the scheduling feature, under "Scheduled Tasks."
- **Confidence**: emerging (a specific, named two-type taxonomy from hands-on analysis)
- **Quote**: "A **scheduled task inside an existing conversation**, triggered by a "heartbeat", reawakens that task with its context intact."
- **Our assessment**: This extends `blog-openai-chatgpt-work-ambitious-partner.md` Claim 11 (Scheduled Tasks can run once, repeat, or monitor-and-trigger on an event) by supplying a named implementation split — standalone vs. heartbeat — that OpenAI's own launch post does not distinguish. The "heartbeat" terminology is novel to this corpus and worth flagging as a specific mechanism name a guide chapter could cite.

### Claim 6: ChatGPT Work's browser use is handled by a separately hosted Chrome service the agent controls via tool calls (inspect, click, type, scroll, screenshot, manage tabs); the agent never has access to the browser's persistent profile or stored credentials, only a synchronized "permission ledger" recording which sites it may act on and whether it may move files to/from them — and this approach currently has concrete failure modes (Amazon US rejects the cloud browser as an unsupported session/client; some sites like Google Photos time out)
- **Evidence**: The author's own architectural description plus specific first-hand testing failures, under "Browser Use."
- **Confidence**: emerging for the architecture description, anecdotal for the specific site failures (single-tester observations, not a systematic compatibility survey)
- **Quote**: "a small permission ledger is synchronised into its computer alongside the workspace, recording, globally and per conversation, which sites it may act on and whether it may move files to or from them."
- **Quote (Amazon failure)**: "Amazon US rejected it as an unsupported "session or client""
- **Our assessment**: The credential-isolation design (agent acts on a permission ledger, never sees stored credentials/profile) is a specific, actionable security-architecture claim relevant to a guide chapter on agent computer-use safety — it names a concrete mechanism, not just a general "we're careful with credentials" assurance. The named failure modes (Amazon US, Google Photos) are useful as concrete, dated evidence that browser-use agents still hit real-world compatibility walls, worth citing as a counterweight to vendor launch-post framing that doesn't mention failures.

### Claim 7: ChatGPT Work's plugin architecture bundles three elements — apps (connecting to services via MCP servers), skills ("instructions with supporting material—references, templates, and sometimes scripts—to teach the agent a workflow"), and app templates for organization-specific configuration — with the Plugin Directory holding more than 1,000 entries, but discovery is a weak link: Work does not suggest a relevant installed plugin when one would outperform a generic web search
- **Evidence**: The author's own architectural breakdown plus a first-hand example of the discovery failure, under "Plugins, skills, and tools."
- **Confidence**: emerging for the architecture (specific, named three-part structure); anecdotal for the discovery-weakness claim (a single tester's observed instance, not a systematic audit of plugin-suggestion behavior)
- **Quote**: "**Skills**, which combine instructions with supporting material—references, templates, and sometimes scripts—to teach the agent a workflow."
- **Quote (tools)**: "Most use an MCP server to expose **tools**: discrete operations the agent can invoke, such as searching messages or sending an email."
- **Quote (directory size + discovery gap)**: "The Plugin Directory already holds more than 1,000 plugins covering most major apps and services, but discovery is a weak link."
- **Our assessment**: The apps/skills/app-templates three-part taxonomy is a specific, citable structure for a guide chapter on plugin/tool ecosystem design — more granular than the general "plugin" framing in `blog-openai-chatgpt-work-education-plugins.md` Claim 1 (which defines a plugin as "a package of apps, role-specific skills, instructions, and common workflows" — broadly consistent with this article's breakdown, corroborating the same three-part structure from an independent, external analysis). The discovery-weakness claim is a concrete, named UX gap (a working agent with 1,000+ installed capabilities that still defaults to web search over its own tools) worth flagging as a cautionary pattern for guide chapters on tool/plugin ecosystem design — more tools installed doesn't guarantee the agent reliably routes to the best one.

### Claim 8: ChatGPT Work has two operating modes with materially different sync behavior — Cloud Mode (default for web/mobile, tasks sync across devices with cloud-hosted storage) and Local Mode (desktop-only, the agent works directly on the user's machine with full computer use), and Local Mode tasks do not appear on web or mobile and currently cannot be moved to the cloud
- **Evidence**: The author's own description of the two modes, under "What is Work?"
- **Confidence**: emerging (a specific, named behavioral distinction from hands-on analysis)
- **Quote**: "In local mode, the agent works directly on your machine, across your files and apps, with full computer use. These tasks don't appear on web or mobile, and there's no way yet to move a local task to the cloud."
- **Our assessment**: This extends `blog-openai-chatgpt-work-ambitious-partner.md` Claim 12 (Computer Use lets ChatGPT Work operate the user's computer in the background) by naming the mode ("Local Mode") and its current sync limitation, a concrete gap that OpenAI's own launch-announcement framing does not mention. Useful as a caveat against overstating cross-device continuity when citing ChatGPT Work as an example of persistent-agent design.

### Claim 9: The article reports that ChatGPT Work (together with Codex) "reportedly crossed 10 million users" three weeks after its July 9, 2026 launch, sourcing this figure to a third-party X/Twitter post rather than an official OpenAI announcement, and separately notes that Greg Brockman has confirmed Chat and Work will merge into one product by the end of the year
- **Evidence**: The article's own opening framing, explicitly hedged as externally sourced ("reportedly").
- **Confidence**: anecdotal (the 10M figure is attributed to a single third-party social-media post, not an OpenAI-published statistic; the merger claim is the author's own paraphrase of Brockman's public statement, not a direct quote reproduced in the article)
- **Quote**: "Three weeks in, Work (along with Codex) has reportedly crossed 10 million users"
- **Our assessment**: This figure sits close in time to and is directionally consistent with `blog-latentspace-nathan-chatgpt-work-harness.md`'s Concrete Artifacts section, which records a "10 million" combined Codex + ChatGPT Work milestone announced around July 21, 2026 (per that note, sourced to a different tweet, from Tibo). Both this article (published Aug 4, "three weeks" post-launch) and that interview cite a "10 million" figure from third-party social posts within about two weeks of each other — this note treats them as likely referring to the same milestone rather than independent confirmation of two separate 10M events, since neither source ties the figure to an official, dated OpenAI announcement. The merger-by-year-end claim is not directly quotable from this article (the author paraphrases Brockman rather than quoting him), so it should be cited as this article's reporting, not as a verified Brockman quote.

### Claim 10: The article identifies three unresolved, ongoing design tensions for ChatGPT Work: (1) whether the cloud computer becomes users' primary AI workspace and how local/cloud syncing should feel seamless, (2) whether Work agents should gain more OpenClaw-like sovereignty over their computer environment, and (3) how Work becomes as familiar to users as base ChatGPT/Chat
- **Evidence**: The author's own closing analysis, under a "What's Next" section, framed as open questions rather than resolved answers.
- **Confidence**: anecdotal (these are the author's own editorial framing of open questions, not claims sourced to OpenAI)
- **Quote**: "1. Does the cloud computer become the user's primary AI computer? And how can syncing between it and the local machine feel seamless? 2. Do Work agents get more OpenClaw-like sovereignty over that computer? 3. How does Work come to feel as familiar to users as Chat?"
- **Our assessment**: Question 2 directly echoes the OpenClaw-inspiration lineage documented first-hand in `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 6, but frames it as an *unresolved* question ("more OpenClaw-like sovereignty") rather than a settled design choice — a useful tension for a guide chapter to hold open rather than resolve, since even the product's own team (per Nathan's interview) frames the current computer-use design as a "deliberate trade-off" that could shift. This is the clearest editorial (rather than reported) content in the article and should be cited as one analyst's framing of open questions, not as OpenAI's roadmap.

## Concrete Artifacts

```
Source: Latent Space, "Unpacking ChatGPT Work: the Agent for a Billion
Users," Shlok Khemani, https://www.latent.space/p/unpacking-chatgpt-work,
published 2026-08-04.

Memory system — three named inputs (Persistence & Memory section):
  1. Compressed summaries of recent tasks and files
  2. "Personal Context" tool — queries Chat/Work history via a
     separately managed service, returns relevant excerpts
  3. ChatGPT-maintained user profile, supplied at task start
  (Raw conversation transcripts are explicitly NOT browsable by the
  agent on the computer itself.)

Plugin architecture — three named components (Plugins, skills, and
tools section):
  1. Apps — connect to services, mostly via MCP servers, exposing
     discrete "tools" (e.g. searching messages, sending an email)
  2. Skills — instructions + supporting material (references,
     templates, scripts) teaching the agent a workflow
  3. App templates — organization-specific configuration
  Plugin Directory size: "more than 1,000 plugins"

Scheduled Tasks — two named types (Scheduled Tasks section):
  1. Standalone tasks — run from a saved prompt at a set time
  2. Heartbeat tasks — reawaken an existing conversation with prior
     context intact
  Trigger types: exact times, time windows ("morning"), or
  agent-monitored conditions

Operating modes (What is Work? section):
  - Cloud Mode (default, web/mobile) — cloud-hosted storage, syncs
    across devices
  - Local Mode (desktop only) — full computer use directly on the
    user's machine; does not sync to web/mobile; no path yet to move
    a local task to the cloud

Browser-use failure modes observed by the author (Browser Use section):
  - Amazon US: rejected the cloud browser session as an unsupported
    "session or client"
  - Google Photos: reported to time out

Three unresolved design tensions (What's Next section):
  1. Cloud computer as primary AI workspace + local/cloud sync
     seamlessness
  2. Whether Work agents gain more OpenClaw-like sovereignty
  3. How Work becomes as familiar to users as Chat
```

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly in
those notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 1 (ChatGPT
    Work gathers cross-app context to produce finished work) —
    corroborated by this source's Claim 1, the same core product
    framing from an independent external analyst.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 11 (Scheduled
    Tasks can run once, repeat, or monitor-and-trigger) — this source's
    Claim 5 corroborates the feature's existence and extends it with a
    named standalone-vs-heartbeat implementation split not present in
    the launch post.
  - `blog-openai-chatgpt-work-education-plugins.md` Claim 1 (a plugin
    defined as "a package of apps, role-specific skills, instructions,
    and common workflows") — corroborated and made more granular by
    this source's Claim 7 (apps / skills / app templates, with skills
    and apps individually defined).
  - `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 9
    (bidirectional Memory V3, shared read/write across ChatGPT and
    ChatGPT Work) — corroborated by this source's Claim 3, which adds
    retrieval-mechanism detail (the named "Personal Context" tool, and
    the explicit statement that raw transcripts are not agent-browsable)
    that Nathan's interview does not supply.
  - `blog-latentspace-nathan-chatgpt-work-harness.md` Concrete Artifacts
    (the "10 million" combined Codex + ChatGPT Work milestone, sourced
    there to a Tibo tweet around July 21, 2026) — this source's Claim 9
    reports the same approximate figure (sourced to a different tweet,
    from @thsottiaux, "three weeks in" from the July 9 launch, i.e.
    late July/early August). Cite cautiously as likely the same
    milestone circulating across two independent secondary sources,
    not as two separate confirmations of two different 10M events —
    neither source ties the number to an official, dated OpenAI
    announcement.
- **Contradicts**: None identified. No claim in this source was found to
  materially oppose an existing corpus source note on the same specific
  question; per MINER.md §4a, no contradiction issue was filed.
- **Extends**:
  - `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 6
    (OpenClaw-inspired persistent computer environment, files that
    "stay around between sessions") — this source's Claim 2 names the
    specific directory (`/workspace/scratch`) and adds the architectural
    nuance that cross-task continuity is reconstructed via the product
    layer/memory system rather than persisting on the computer itself.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 12 (Computer
    Use lets ChatGPT Work operate the user's computer in the background)
    — this source's Claim 8 names the specific mode ("Local Mode") and
    its current sync limitation (no path to move a local task to the
    cloud), a caveat the launch post omits.
- **Novel**:
  - The browser-use credential-isolation architecture — a synchronized
    "permission ledger" the agent consults instead of ever seeing stored
    credentials or the browser profile (Claim 6) — no prior corpus note
    documents this specific security mechanism for ChatGPT Work's
    browser use.
  - Concrete, dated browser-use failure modes: Amazon US session
    rejection and Google Photos timeouts (Claim 6) — the first corpus
    source to document specific real-world compatibility failures for
    ChatGPT Work's computer/browser-use feature, as a counterweight to
    launch-post framing that only lists successes.
  - The plugin-discovery weakness — Work does not proactively surface a
    relevant installed plugin over a generic web search (Claim 7) — new
    to the corpus; no existing note flags this as a current limitation.
  - The standalone-vs-heartbeat scheduled-task taxonomy and the
    "heartbeat" terminology itself (Claim 5) — novel naming/mechanism
    detail not present in the OpenAI launch post's more general
    description of Scheduled Tasks.
  - The "Personal Context" tool as a named memory-retrieval mechanism
    (Claim 3) — entirely new to the corpus.
  - The three explicitly framed open design tensions (Claim 10) — a
    named editorial framing of ChatGPT Work's unresolved product
    questions, not present elsewhere in the corpus.

## Guide Impact

- **Chapter 04 (Tool Use & Ecosystem / Plugin Architecture)**: Add
  Claim 7's apps/skills/app-templates taxonomy as a concrete, three-part
  reference structure for describing plugin ecosystems, alongside the
  discovery-weakness finding (a 1,000+-entry plugin directory that still
  defaults to web search over better-suited installed tools) as a named
  cautionary pattern — cite this as evidence that ecosystem *scale*
  (plugin count) does not by itself solve tool-selection reliability.
- **Chapter 03 (Multi-Agent Coordination / Computer Use & Browser Use)**:
  Add Claim 6's permission-ledger credential-isolation design as a
  concrete security pattern for agent browser-use (agent acts on a
  synced permission record, never sees stored credentials), paired with
  the named real-world failure modes (Amazon US, Google Photos) as
  evidence that browser-use agents still hit compatibility walls in
  production — useful as a grounding counterweight to more optimistic
  vendor framing already in the corpus.
- **Chapter 02 (AI-Native Patterns / Agentic Workflows)**: Add Claim 4's
  "suggests but does not execute" proactivity boundary and Claim 5's
  standalone-vs-heartbeat scheduled-task split as concrete examples of
  how a shipped product currently draws the line between autonomous and
  user-triggered agent action — useful for a guide discussion of what
  "proactive agent" currently means in practice versus in vendor
  marketing language.
- **Chapter 04 (Context Engineering / Memory)**: Add Claim 3's named
  three-part memory system and the "Personal Context" tool as a concrete
  worked example of retrieval-based (rather than full-transcript-browse)
  agent memory design, extending the Memory V3 architecture already
  documented via `blog-latentspace-nathan-chatgpt-work-harness.md`.

## Extraction Notes

- **Fetch method**: The first `WebFetch` pass against this URL returned a
  reasonably detailed but partially paraphrased summary (consistent with
  the known limitation, documented in several other Latent Space source
  notes in this corpus, that `WebFetch` processes pages through a small
  summarization model before returning). Two follow-up `WebFetch` calls
  were made with narrowly scoped prompts explicitly requesting
  character-for-character verbatim quotes for each claim area (Memory,
  Proactivity, Scheduled Tasks, Browser Use, Plugins/Skills/Tools, Local/
  Cloud modes, launch stats, and the closing "What's Next" section) before
  any `Quote` field in this note was finalized, per MINER.md §2a. Where a
  follow-up pass could not produce an exact quote (the Brockman
  merger-by-year-end claim), this note says so explicitly (Claim 9) rather
  than fabricating one.
- **Full article read**: The article was read in full via the fetch
  passes above, covering every named section (What is Work?, Persistence
  & Memory, Hints of useful proactivity, Scheduled Tasks, Browser Use,
  Plugins/skills/tools, What's Next). No linked sub-pages were followed —
  the article's outbound links are to tweets (used only as the sourcing
  basis for the 10M-users and merger claims, both already captured with
  appropriate hedging in Claim 9) and to OpenAI's own launch post, which
  is already extracted in full as `blog-openai-chatgpt-work-ambitious-partner.md`.
- **Cross-references verified**: `blog-openai-chatgpt-work-ambitious-partner.md`
  Claims 1, 11, 12; `blog-openai-chatgpt-work-education-plugins.md`
  Claim 1; and `blog-latentspace-nathan-chatgpt-work-harness.md` Claims 6
  and 9 (plus its Concrete Artifacts section) were each re-read in full
  before citing; no claim numbers were guessed.
- No contradiction with any existing source note was found during
  cross-referencing, so no contradiction issue was filed per MINER.md
  §4a.
