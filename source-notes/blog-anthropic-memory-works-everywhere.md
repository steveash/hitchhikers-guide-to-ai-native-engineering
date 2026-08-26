---
source_url: https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it
source_type: blog-post
title: "Claude's memory works everywhere, and you decide what's in it"
author: Anthropic (product announcement)
date_published: 2026-08-25
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: settled
issue: "#2963"
---

# Claude's memory works everywhere, and you decide what's in it

> The August 25, 2026 announcement that Claude's consumer memory (chat on
> web/desktop/mobile) and Claude Cowork now share a single memory store,
> plus the mechanics of topic-file storage, live-during-chat updates, and
> sensitive-topic opt-in controls. The linked Help Center article supplies
> the implementation detail the blog post itself omits: RAG-based past-chat
> search, per-project memory isolation, pause vs. reset semantics, and
> enterprise/org-level controls.

## Source Context

- **Type**: blog-post (official Anthropic/Claude product announcement,
  claude.com/blog, August 25, 2026), cross-read with the linked Help Center
  article "Use Claude's chat search and memory to build on previous context"
  (support.claude.com, marked "Updated today" at time of extraction) that the
  blog post links to for "learn more."
- **Author credibility**: First-party Anthropic product announcement —
  authoritative on what the feature does and which access tiers get it. No
  named individual author; standard house style for claude.com/blog product
  posts. No customer testimonials or third-party validation are included —
  this is a self-described feature description, not an efficacy claim, so the
  lack of independent verification matters less here than it would for a
  performance benchmark.
- **Scope**: Covers unification of memory between Claude chat (claude.ai web,
  desktop, mobile) and Claude Cowork running in the cloud; the shift from
  end-of-conversation summarization to live topic updates during chat; the
  Settings > Memory topic-file UI for reading/editing/deleting memories;
  default exclusion of sensitive topics (health, race, ethnicity, religion,
  politics, gender identity) with an opt-in toggle; hard exclusions that
  survive even the sensitive-topics opt-in (government ID numbers, criminal
  history, immigration status, AUP-violating content); and default-on
  availability for Free/Pro/Max vs. admin-gated for Team/Enterprise. The blog
  post does **not** mention Claude Code, Claude in Chrome, or the API/SDK at
  all — despite the Prospector's triage comment framing this as spanning
  "claude.ai, Claude Code, Cowork, extensions," the post's own scope is
  narrower: chat (claude.ai/desktop/mobile) and Cowork only. It also does not
  cover pricing, the underlying storage/retrieval architecture (vector store
  vs. filesystem vs. other), or how memory interacts with the Claude API.
  The cross-read Help Center article fills some of these gaps (RAG-based past
  chat search, encryption at rest, legacy-vs-new migration) but likewise never
  mentions Claude Code.

## Extracted Claims

### Claim 1: Claude Cowork (when run in the cloud) and Claude chat now share one memory store instead of two separate ones
- **Evidence**: Direct first-party statement of the launch's core change, restated in the section "One memory across Claude Cowork and chat" with three worked examples (manager-update drafting, conference budget/logistics doc, quarterly metrics deck).
- **Confidence**: settled (explicit product launch statement)
- **Quote**: "Starting today, the memory you use in chat is the same as in Claude Cowork. Now, wherever you work with Claude, it starts from what it already knows about you."
- **Our assessment**: This closes a gap that was implicit in earlier Managed-Agents-memory coverage (blog-anthropic-claude-managed-agents-memory.md), which described a *separate*, filesystem-based, enterprise-agent memory product. This announcement is about the *consumer* chat/Cowork product line, not Managed Agents — the two memory systems are architecturally distinct products that happen to share the word "memory." Guide text should not conflate them.

### Claim 2: Cowork-chat memory sharing only applies when Cowork runs in the cloud — local Cowork sessions do not use memory at all
- **Evidence**: Explicit note in the Help Center article, stated twice (once in "One memory across chat and Claude Cowork," once flagged again as a callout box).
- **Confidence**: settled (explicit product constraint, stated with a "Note:" callout — the kind of caveat vendors are usually careful to get right since it affects user expectations)
- **Quote**: "Memory across Cowork and chat only works when Cowork runs in the cloud. It isn't available in Cowork sessions that run locally on your computer."
- **Our assessment**: This is the single most guide-relevant mechanical detail in the whole source, and it does not appear anywhere in the blog post itself — only in the linked Help Center article. Anyone building a workflow that depends on "Cowork already knows what I told chat" needs to know this fails silently for local Cowork sessions. This is exactly the kind of caveat that gets lost when only the announcement post is read.

### Claim 3: Memory is now built as topic-based files, saved live during the conversation, rather than as an end-of-conversation summary
- **Evidence**: Direct statement of a mechanism change plus a worked example (deadline-change scenario). Corroborated independently by the Help Center article's "How Claude stores memory" section.
- **Confidence**: settled (explicit mechanism description, and consistent across both the blog post and the Help Center article)
- **Quote**: "Claude now adds topics to memory as you chat, instead of summarizing conversations after they end. Mention that your project deadline moved to September, and your next conversation already knows without you having to say 'remember this.'"
- **Our assessment**: This is a meaningful architecture shift from "memory = periodic summary of chat history" to "memory = a maintained set of discrete topic files," and it directly parallels the "manual `#`-hotkey to auto-save" shift already documented for Claude Code in blog-anthropic-context-engineering-claude-5.md (Claim 10). The Help Center article independently confirms the topic-file model is not exclusive to this announcement — the *legacy* memory experience (described later in the same Help Center article, under "Information for legacy memory users") explicitly used a different mechanism: a single memory synthesis regenerated every 24 hours. So the "topic files, updated live" design is itself a replacement for an older "24-hour summary synthesis" design, not merely a description of how memory has always worked at Anthropic — a distinction the blog post's celebratory framing elides entirely.

### Claim 4: Each memory item lives in a separate, individually readable/editable/deletable file listed under Settings > Memory > Topics, and editing one file propagates the correction to all future conversations
- **Evidence**: Direct statement in "See and edit your saved memories," corroborated by the Help Center's "View and manage your memory" section.
- **Confidence**: settled (consistent UI/mechanism description across both first-party sources)
- **Quote**: "Everything Claude remembers is in a list of files under Topics in Memory settings, where you can read, edit, or delete each one. The files are short, and a fix pays off everywhere: correct your company's old name in one file and every conversation from then on gets it right."
- **Our assessment**: This is a concrete, user-facing correction mechanism worth citing directly for any guide section on managing agent/assistant memory drift — a wrong fact only needs to be fixed once, at the topic-file level, rather than re-explained per conversation. Structurally this resembles the "memories are files" design in blog-anthropic-claude-managed-agents-memory.md (Claim 2: "Memory on Managed Agents mounts directly onto a filesystem"), though that source is about developer/API-level filesystem mounting for agents and this one is about a consumer settings UI — different implementations converging on the same "memory as inspectable, editable files" pattern.

### Claim 5: Claude does not store sensitive personal topics (health, race, ethnicity, religion, political affiliation, gender identity) to memory by default; users can opt in via a "include sensitive topics in memory" toggle
- **Evidence**: Stated in both the blog post and, in more detail, the Help Center article's "Sensitive topics in memory" section.
- **Confidence**: settled (explicit, consistent policy statement in two first-party sources, with mechanism detail — a one-time in-chat notice as an alternate opt-in path — that would be hard to fabricate)
- **Quote**: "By default, Claude does not store topics related to personal or sensitive subject matter, like your health, race, ethnicity, religious beliefs, politics, gender identity, and other similar areas."
- **Our assessment**: Reasonable default for a consumer product; the opt-in path (blog post's meal-prep/allergy example: "Claude will remember things like your gluten allergy when suggesting recipes for weekly meal prep") is a believable illustrative use case rather than a specific customer-reported outcome, so we treat it as product-marketing color rather than an independently verified claim.

### Claim 6: Turning on sensitive-topic memory is not retroactive — only sensitive information mentioned after the toggle is flipped gets saved, and each such save surfaces a one-time visible notice
- **Evidence**: Explicit mechanism statement in the blog post's "Decide if you want Claude to remember sensitive topics" section, matched almost verbatim by the Help Center article.
- **Confidence**: settled
- **Quote**: "Claude saves sensitive topics going forward. Anything from before you turned it on isn't saved retroactively."
- **Our assessment**: This non-retroactivity detail is the kind of privacy-relevant mechanic that's easy to get wrong when summarizing a memory feature secondhand — worth citing precisely rather than paraphrasing if the guide ever discusses opt-in memory of sensitive data.

### Claim 7: Even with sensitive-topic memory enabled, Claude will never store government ID numbers, criminal history, immigration status, or content that violates Anthropic's Acceptable Use Policy
- **Evidence**: Explicit hard-exclusion list, stated in both sources with near-identical wording; Help Center article adds "financial account numbers" to the list (blog post's list: "sensitive identification numbers (SSN, government ID numbers, etc), criminal history, immigration status" — the Help Center's list additionally names "financial account numbers" explicitly).
- **Confidence**: settled
- **Quote**: "This includes sensitive identification numbers (SSN, government ID numbers, etc), criminal history, immigration status, or anything that violates our Acceptable Use Policy (AUP) in its memory. Claude will inform you when it's unable to update memory to include any of this information."
- **Our assessment**: A hard floor beneath the user-configurable sensitive-topics toggle. Useful for any guide section that discusses what categories of data will *never* end up in Claude's persistent memory regardless of user settings — relevant to enterprises evaluating data-handling risk.

### Claim 8: Memory is on by default for Free, Pro, and Max plans across web, desktop, and mobile; Team and Enterprise plans require admin/owner approval and are off by default
- **Evidence**: Explicit availability statement in the blog post's "Getting started" section, corroborated by the Help Center article's "What is Claude's memory?" section with matching tier breakdown.
- **Confidence**: settled
- **Quote**: "Memory is on by default on Free, Pro and Max plans across web, desktop, and mobile. Note that saving sensitive topics in memory is off by default. On iOS and Android, update to the latest version of the mobile app to get the most recent updates. For Team and Enterprise, admins control availability for their organization, and memory is off for individual users until they turn it on."
- **Our assessment**: Two separate defaults are being conflated in casual reading and worth keeping distinct in the guide: (1) memory itself defaults on for individual consumer plans but off for org plans pending admin action; (2) *sensitive-topic* memory defaults off for everyone regardless of plan tier, requiring explicit per-user opt-in even after an org enables base memory. The Help Center's "Controls for Team and Enterprise plan owners" section adds a detail the blog post omits entirely: turning memory off at the org level "permanently deletes all memory data for everyone in your organization" immediately — a one-way door worth flagging for any guide content aimed at Enterprise admins.

### Claim 9: Past-chat search (a separate but related capability) uses Retrieval-Augmented Generation and surfaces as a visible tool call in the conversation
- **Evidence**: Explicit mechanism statement in the Help Center article's "Search past chats with Claude" section — this capability is not mentioned in the blog post at all.
- **Confidence**: settled (explicit architecture disclosure — vendors don't usually name "RAG" unless describing the actual retrieval mechanism)
- **Quote**: "These searches use Retrieval-Augmented Generation (RAG) and will appear as tool calls during your conversations."
- **Our assessment**: This is the most specific piece of retrieval-architecture detail in either source, and it clarifies that "memory" and "chat search" are two distinct capabilities in Claude's product surface: memory is the maintained topic-file store described in Claims 3-4, while chat search is a separate RAG-based retrieval layer over raw conversation history, visible to the user as an explicit tool call rather than an invisible context injection. Guide content that discusses "how Claude remembers things" should distinguish these two mechanisms rather than treating "memory" as a single monolithic system.

### Claim 10: Each project has its own isolated memory space and project summary, separate from account-level memory and other projects
- **Evidence**: Explicit statement in the Help Center article's "Project memory and summary" section (appears twice — once under the current memory experience, once under the legacy-memory section, both with matching wording).
- **Confidence**: settled
- **Quote**: "Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats."
- **Our assessment**: Relevant to any guide discussion of multi-project or multi-client usage patterns — a consultant or freelancer using Claude for multiple clients should not assume account-level memory bleeds into project-scoped work, and vice versa. Not mentioned at all in the blog post; only surfaced by following the linked Help Center article, which is exactly the kind of sub-page MINER.md's step 1 exists to catch.

### Claim 11: "Pause memory" and "reset memory" are distinct, irreversible-in-different-ways operations — pausing preserves existing memory but stops new saves, while reset permanently and irrecoverably deletes all memory including project memories
- **Evidence**: Explicit mechanism description in the Help Center article's "Turn memory on or off" section, with the reset operation explicitly flagged as non-undoable.
- **Confidence**: settled
- **Quote**: "Reset memory: Permanently deletes all memories including project memories. Once you select this option and click 'Reset memory,' this cannot be undone. Upon re-enabling the feature, you'll start from scratch and Claude will not have its previous memory."
- **Our assessment**: The blog post only says "You can pause memory or reset it at any time," collapsing this into what sounds like one reversible action. The Help Center article reveals reset is a destructive, non-reversible operation while pause is not — an important distinction to preserve if the guide ever instructs users on managing or clearing agent memory, since conflating the two could lead someone to reset when they meant to pause.

## Concrete Artifacts

```
Blog post section headers (claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it),
in document order:
1. "One memory across Claude Cowork and chat"
2. "Memory updates as you chat"
3. "See and edit your saved memories"
4. "Decide if you want Claude to remember sensitive topics"
5. "Getting started"
```

```
Help Center article structure (support.claude.com, "Use Claude's chat search and
memory to build on previous context"), current (non-legacy) memory experience sections:
- Search past chats with Claude
  - What Claude can search
  - Search and reference past chats
  - Can I prevent Claude from searching my past chats?
  - Can I exclude a specific past chat from searches?
- What is Claude's memory?
- How does Claude's memory work?
  - How Claude stores memory
  - Project memory and summary
  - One memory across chat and Claude Cowork
- Turn memory on or off
- What Claude remembers
- What Claude doesn't remember (incognito chats)
- Data retention and privacy
- User controls and visibility
- Controls for Team and Enterprise plan owners
- Information for legacy memory users (documents the OLD summary-based system this
  replaces, migration deadline: legacy memory export available "until September 9, 2026")
```

```
Migration notice from the Help Center article (verbatim), documenting a hard deadline
relevant to any guide content about memory continuity for existing users:

"We have introduced an improved experience for memory and migrated users off the
legacy experience. If you think Claude has forgotten something in that migration:
Navigate to Settings > Memory and until September 9, 2026, you will see the option
to export your legacy memory. Once you have exported your legacy memory, paste it
back into Claude, highlighting the portion that may have been forgotten."
```

```
Data retention/compliance details from the Help Center article (verbatim fragments),
"Data retention and privacy" section:

"All memory will be retained in accordance with existing chat data retention policies."
"When a conversation expires or is deleted, related memory entries generated from it
won't be removed, but you can delete individual memories at any time."
"All memory data is included in data exports."

"Data handling and compliance" section (Enterprise):
"Memory entries are stored with encryption at rest."
```

## Cross-References

- **Corroborates**: blog-anthropic-context-engineering-claude-5.md (Claim 10) — that
  note documents Claude Code's shift from a manual `#`-hotkey CLAUDE.md save to
  automatic memory-saving, and flags as an open gap that "what triggers a save, where
  memories are stored, how conflicts are resolved is given in this article" — i.e., no
  mechanism detail was available. This source does not resolve that gap for Claude
  Code specifically (it never mentions Claude Code), but it corroborates the broader
  industry-wide Anthropic pattern of moving from manual/periodic memory capture to
  live automatic capture, and supplies the kind of mechanism detail (topic files,
  live updates, edit/delete UI) that a future Claude Code-specific source could be
  checked against.
- **Contradicts**: None identified. No existing source note makes a claim about
  consumer chat/Cowork memory mechanics that this source disagrees with.
- **Extends**: blog-anthropic-claude-managed-agents-memory.md — that note documents a
  *different* memory product (Claude Managed Agents' filesystem-mounted, API-managed,
  enterprise-agent memory, announced April 23, 2026) built for autonomous agent
  deployments. This source's Claim 1 and Claim 4 describe a structurally similar
  "memory as inspectable/editable files" pattern but for the consumer chat/Cowork
  product line, with a settings-UI editing surface rather than a developer API. The
  guide should treat these as two distinct memory systems within Anthropic's product
  line that share a design philosophy (discrete, inspectable, editable memory units)
  rather than describing one as an evolution of the other.
- **Novel**: The Cowork/chat memory unification (Claim 1), the local-Cowork exclusion
  caveat (Claim 2), the RAG-based past-chat-search mechanism as distinct from memory
  (Claim 9), per-project memory isolation (Claim 10), the pause-vs-reset distinction
  (Claim 11), and the hard September 9, 2026 legacy-memory export deadline are all new
  to the corpus — no existing source note covers Claude's consumer memory feature at
  this level of mechanism detail.

## Guide Impact

- **Chapter 03 (Context Engineering — Memory)**: Add the consumer memory
  architecture (topic files, live updates, edit/delete via Settings > Memory) as a
  parallel example to the existing Claude Code auto-memory discussion sourced from
  blog-anthropic-context-engineering-claude-5.md, but keep them as separate systems —
  do not imply Claude Code shares this exact memory store, since neither source
  states that. Add Claim 9's RAG-vs-memory distinction: any guide language describing
  "how Claude remembers past conversations" should split this into two mechanisms
  (maintained topic-file memory, and separate on-demand RAG search over raw chat
  history) rather than one.
- **Chapter 04 (Agents & Multi-turn)**: Add Claim 2 (local Cowork sessions do not
  share memory with chat; only cloud-run Cowork does) as a concrete gotcha for anyone
  building multi-surface agent workflows that assume shared context — this is the
  single most actionable, non-obvious detail in the source and currently absent from
  the guide.
- **Chapter 05 (Building AI-Native Applications)**: If the guide discusses
  privacy/data-handling defaults for AI products as a design pattern, cite Claims 5-7
  (sensitive-topic opt-in with hard exclusions for IDs/criminal history/immigration
  status) as a concrete example of tiered consent design: default-safe, user-opt-in
  for a "sensitive but useful" band, and a non-negotiable exclusion band beneath that.

## Extraction Notes

- The claude.com blog post itself is short (~450 words of body text; the "5 min"
  reading-time estimate appears to include page chrome). Per MINER.md step 1, I
  followed the one substantive linked page from the post — the Help Center article
  "Use Claude's chat search and memory to build on previous context"
  (support.claude.com/en/articles/11817273), which is far more detailed and is the
  source of Claims 2, 9, 10, and 11, none of which appear in the blog post itself.
  I did not find 4 additional distinct substantive linked pages beyond this one to
  reach MINER.md's "up to 5" ceiling — the blog post's other outbound links are
  navigation chrome (nav menu, footer, related-posts teasers) rather than content
  links relevant to this topic.
- Both pages were fetched as raw HTML via `curl` and stripped of markup directly
  (rather than via the summarizing WebFetch tool) specifically so that every `Quote`
  field above could be copied character-for-character from the source rather than
  reconstructed from an LLM-generated summary, per MINER.md §2a.
- The Help Center article documents a "legacy memory" experience (24-hour periodic
  summary synthesis, `Settings > Capabilities` UI) as a still-partially-live fallback
  path for users not yet migrated, with an explicit export deadline of September 9,
  2026. This legacy system is described in the source as being superseded by the
  topic-file system this note focuses on; I did not write separate claims for the
  legacy mechanics since they describe a system being retired, but flagged the
  migration deadline in Concrete Artifacts since it is a fact with a currency window.
- I did not find a contradiction between this source and any existing note, so no
  contradiction issue was filed per MINER.md §4a.
