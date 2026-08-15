---
source_url: https://vercel.com/changelog/chat-sdk-adds-native-slack-agent-support
source_type: blog-post
title: "Chat SDK adds native Slack agent support"
author: Ben Sabic (Vercel, Content Engineer)
date_published: 2026-07-17
date_extracted: 2026-08-15
last_checked: 2026-08-15
status: current
confidence_overall: emerging
issue: "#2721"
---

# Chat SDK adds native Slack agent support

> Vercel's Chat SDK ships a native Slack adapter (`createSlackAdapter()`)
> bundling Slack's agent-messaging surface — Messages-tab conversations,
> thread-aware suggested prompts, rotating status messages, token-by-token
> streaming with a Post+Edit fallback for non-streaming workspaces (e.g.
> GovSlack), and native feedback buttons — behind one declarative config
> object, plus a documented gotcha: under `agentView`, Slack's own channel
> history only captures the user's half of the conversation.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  short, single-feature release note with one embedded TypeScript code
  example and a three-item feature list). Confirmed by inspecting the raw
  page HTML/RSC payload (not just the rendered summary) that the extracted
  text below is the actual page content, not a fetch-tool paraphrase.
- **Author credibility**: First-party Vercel changelog entry, credited to a
  single named author, Ben Sabic, whose byline on the page carries the title
  "Content Engineer" (confirmed via the page's author-byline markup, not
  stated in the article body itself). This differs from the sibling Discord
  Components V2 changelog (`blog-vercel-chat-sdk-discord-components-v2.md`),
  which is credited to two named individuals (Josh Singh, Ben Sabic) whose
  bylines are not further titled on that page, and where Josh Singh is also
  a credited co-author on the much longer, engineering-heavy AI SDK 7
  release note. That pattern suggests the Discord entry had direct
  engineering co-authorship, while this Slack entry may be more purely a
  documentation/content-team writeup of an already-shipped adapter — a
  slightly lower-signal authorship profile, though still first-party and
  technically precise (concrete config keys, method names, and a specific
  workspace example are named). No customer quotes, adoption metrics, or
  production-deployment evidence are given.
- **Scope**: Covers exactly one feature: Chat SDK's new Slack adapter and
  the four capabilities bundled into the same release note (suggested
  prompts, streaming with fallback, feedback buttons, and the `agentView`
  threading caveat). Does **not** cover: pricing, a rollout/GA timeline,
  independent benchmarks, named production users of the Slack adapter, the
  adapter's OAuth/bot-token setup or required Slack app scopes/permissions,
  or how this adapter compares to Chat SDK's other platform adapters beyond
  what can be inferred by comparing to the Discord note.

## Extracted Claims

### Claim 1: Chat SDK's new Slack adapter bundles Slack's full "agent messaging experience" — Messages-tab conversations, suggested prompts, rotating status messages, token-by-token streaming, and native feedback buttons — behind a single adapter
- **Evidence**: The changelog's lead description sentence, which frames the
  adapter as covering the complete set of Slack-native agent UI surfaces
  rather than a subset.
- **Confidence**: settled (first-party feature description, unambiguous as
  a statement of what shipped)
- **Quote**: "The adapter supports the full Slack agent messaging
  experience, from agent conversations in the Messages tab to suggested
  prompts, rotating status messages, token-by-token streamed replies, and
  native feedback buttons."
- **Our assessment**: Like the Discord Components V2 entry, this positions
  a Chat SDK adapter as a platform-native feature pass-through: the adapter
  is following Slack's own product surface (the linked Slack "agent
  messaging experience" changelog at docs.slack.dev) rather than defining
  its own abstraction over chat. That's a meaningful distinction for the
  guide — Chat SDK's value proposition here is less "a portable chat
  abstraction" and more "wire up Slack's newest agent-native UI primitives
  without hand-rolling the Slack API calls."

### Claim 2: Suggested prompts accept either a static payload or an async resolver that receives thread context (including what the user is currently viewing under `agentView`), and pin automatically whenever an agent thread opens
- **Evidence**: A dedicated "Suggested prompts, per thread" bullet in the
  adapter's feature list, plus the code example's `suggestedPrompts` config
  block showing a static `title` + `prompts` array shape.
- **Confidence**: settled (first-party API description with a runnable code
  example for the static case; the async-resolver case is described in
  prose only — no code example of that variant is given)
- **Quote**: "Pass a static payload or an async resolver that receives the
  thread context, including what the user is currently viewing under
  `agent_view`. Prompts are pinned automatically whenever an agent thread
  opens."
- **Our assessment**: The context-aware resolver option (as opposed to the
  static example actually shown in the code block) is the more interesting
  half of this claim for agent design — it lets suggested prompts adapt to
  what the user is currently looking at in Slack, not just what channel/DM
  they're in. The source gives no example of that resolver's function
  signature or what "thread context" concretely contains beyond "what the
  user is currently viewing," which limits how directly this can be
  reproduced without consulting the linked adapter documentation.

### Claim 3: Streamed replies render token-by-token via Slack's native streaming API, including task and plan cards, and the adapter automatically falls back to a Post+Edit rendering mode for workspaces that don't support streaming (Slack names GovSlack as an example)
- **Evidence**: The "Native streaming with a fallback" bullet in the
  adapter's feature list.
- **Confidence**: settled (first-party statement of a specific,
  automatically-triggered fallback mechanism, with a named example
  workspace type)
- **Quote**: "Streamed replies render token-by-token via Slack's streaming
  API, including task and plan cards. If a workspace doesn't support
  streaming (e.g., GovSlack), the adapter switches to Post+Edit."
- **Our assessment**: This is a concrete, checkable capability boundary:
  an agent's response-rendering code doesn't need to branch on workspace
  type itself — the adapter absorbs that variance. "Task and plan cards"
  streaming token-by-token also implies the adapter treats structured
  agent-status UI (not just chat text) as a first-class streaming target,
  which is a step beyond plain-text token streaming. The source does not
  say what Post+Edit's update cadence or latency profile looks like
  compared to true streaming, which matters for anyone evaluating UX
  parity across workspace types.

### Claim 4: Feedback collection is a single boolean flag (`feedbackButtons: true`) that appends thumbs-up/down buttons to every streamed reply, with click handling routed through the same `bot.onAction` flow used elsewhere in Chat SDK
- **Evidence**: The "Built-in feedback" bullet in the adapter's feature
  list, plus the `feedbackButtons: true` line in the code example.
- **Confidence**: settled (first-party API description naming the exact
  config key and the exact handler entry point)
- **Quote**: "Set `feedbackButtons: true` to append thumbs-up/down buttons
  to every streamed reply, and clicks dispatch via the `bot.onAction`
  flow."
- **Our assessment**: Reusing `bot.onAction` (rather than introducing a
  Slack-specific feedback callback) suggests Chat SDK treats feedback-button
  clicks as just another instance of its general action-dispatch mechanism,
  the same one presumably used for Discord's `Button`/`LinkButton`
  components documented in the Discord note's code example. That's a
  reasonable inference from naming alone, but the source does not confirm
  `bot.onAction` is shared verbatim across adapters — it's not stated or
  shown side-by-side with the Discord adapter's action handling in either
  changelog.

### Claim 5: Under `agentView`, Slack threads each user message individually, so a bot's own Slack channel history only reflects the user's side of the conversation — Chat SDK's own transcript feature is the documented way to reconstruct full AI conversation history instead
- **Evidence**: A standalone "One thing to know" callout paragraph, placed
  immediately after the three-bullet feature list, distinct from the
  feature descriptions themselves.
- **Confidence**: settled (first-party statement of a specific, named
  limitation and its documented workaround)
- **Quote**: "One thing to know: under `agent_view`, Slack threads each user
  message individually, so channel history only returns the user's side of
  a DM. Use Chat SDK transcripts to build AI conversation history instead."
- **Our assessment**: This is the most operationally important claim in the
  source and the one most likely to bite an implementer who skims the
  feature list and goes straight to Slack's native history API for context.
  It's a platform-imposed data-model quirk (Slack's own message-threading
  behavior under `agent_view`, not a Chat SDK limitation), and the fix
  requires knowing Chat SDK maintains a separate transcript mechanism
  (linked to `chat-sdk.dev/docs/conversation-history` but not detailed
  further in this changelog) rather than relying on the chat platform's
  native history entirely. This generalizes past Slack: an agent-harness
  builder wiring any chat platform's native "agent view"/app-DM mode should
  not assume the platform's own history API returns a complete
  bidirectional transcript.

### Claim 6: The Slack adapter is configured as a single object passed to `createSlackAdapter()`, combining `agentView`, `suggestedPrompts`, `loadingMessages`, and `feedbackButtons` into one declarative call registered under `adapters.slack` on a `Chat` instance
- **Evidence**: The full worked TypeScript code example (see Concrete
  Artifacts), which is the only code in the source and shows all four
  config keys used together in one adapter instantiation.
- **Confidence**: settled (first-party runnable code example)
- **Quote**: (no direct quote; the artifact is code, reproduced verbatim in
  Concrete Artifacts below)
- **Our assessment**: This mirrors the exact configuration shape used by
  Chat SDK's Discord adapter (`createDiscordAdapter({ contentFormat: ... })`
  registered under a comparable adapters map, per the Discord note's code
  example) — a single factory function per platform, taking one config
  object, mounted into a shared `Chat` (or equivalent) instance. That's a
  consistent adapter-construction pattern across at least two platforms now
  documented in the corpus, which is worth naming explicitly for the guide
  as Chat SDK's general adapter shape rather than a Slack-specific
  convention.

### Claim 7: `loadingMessages` is configured as a plain array of literal strings that are shown while the agent is working, corresponding to the "rotating status messages" mentioned in the adapter's feature summary
- **Evidence**: The code example's `loadingMessages: ["Thinking...",
  "Digging through the archives..."]` line, read together with Claim 1's
  "rotating status messages" phrase from the lead description.
- **Confidence**: emerging (the config shape is shown directly in code, but
  the source never explains the rotation mechanics — timing interval,
  whether messages cycle in order or at random, or how many are shown
  before the final reply streams in)
- **Quote**: (no direct quote; the "rotating status messages" phrase from
  Claim 1's quote is the only prose description, and it does not describe
  the mechanism — see Concrete Artifacts for the literal array)
- **Our assessment**: This is a small but useful data point on Chat SDK's
  authoring ergonomics — a rotating-status UI feature is exposed as nothing
  more than a string array, no timing config exposed to the developer. That
  simplicity is worth noting, but it's also a gap: without knowing the
  rotation interval, a developer can't predict how "Thinking..." reads
  against actual agent latency (e.g., whether a slow tool call will exhaust
  the array and repeat, or hang on the last message).

## Concrete Artifacts

### Full adapter configuration example (from the changelog body, TypeScript)

```typescript
Source: https://vercel.com/changelog/chat-sdk-adds-native-slack-agent-support
Caption in source: "Configure your native Slack agent in Chat SDK"
Filename tag in source: lib/bot.ts

import { Chat } from "chat";
import { createSlackAdapter } from "@chat-adapter/slack";

const bot = new Chat({
  userName: "mybot",
  adapters: {
    slack: createSlackAdapter({
      agentView: true,
      suggestedPrompts: {
        title: "Welcome! What can I do for you?",
        prompts: [
          { title: "Catch me up", message: "What did I miss today?" },
          { title: "Draft a message", message: "Help me draft a message" },
        ],
      },
      loadingMessages: ["Thinking...", "Digging through the archives..."],
      feedbackButtons: true,
    }),
  },
});
```

### Full article body (reproduced in reading order, for reference)

```
Source: https://vercel.com/changelog/chat-sdk-adds-native-slack-agent-support
Title: "Chat SDK adds native Slack agent support"
Author byline: Ben Sabic, Content Engineer
Published: 17 Jul 2026 (datePublished 2026-07-17T00:00+00:00 per page metadata)

You can now build native Slack agents with Chat SDK's Slack adapter
[https://chat-sdk.dev/adapters/official/slack].

The adapter supports the full Slack agent messaging experience
[https://docs.slack.dev/changelog/2026/06/30/agent-messages-tab/], from
agent conversations in the Messages tab to suggested prompts, rotating
status messages, token-by-token streamed replies, and native feedback
buttons.

[code example — see above]

Here's what the adapter gives you:

- Suggested prompts, per thread: Pass a static payload or an async
  resolver that receives the thread context, including what the user is
  currently viewing under agent_view. Prompts are pinned automatically
  whenever an agent thread opens.
- Native streaming with a fallback: Streamed replies render token-by-token
  via Slack's streaming API, including task and plan cards. If a workspace
  doesn't support streaming (e.g., GovSlack), the adapter switches to
  Post+Edit.
- Built-in feedback: Set feedbackButtons: true to append thumbs-up/down
  buttons to every streamed reply, and clicks dispatch via the
  bot.onAction flow.

One thing to know: under agent_view, Slack threads each user message
individually, so channel history only returns the user's side of a DM.
Use Chat SDK transcripts [https://chat-sdk.dev/docs/conversation-history]
to build AI conversation history instead.

Read the documentation [https://chat-sdk.dev/adapters/official/slack] to
get started, or begin with one of our templates
[https://chat-sdk.dev/resources].
```

Note: the section breaks above ("Here's what the adapter gives you:" /
bullet list / "One thing to know" callout) are the source's own paragraph
and list structure, reproduced in order — the source has no subheadings
(no "Key Features" or similar heading text appears anywhere in the page's
HTML/RSC payload; any such heading in a summarized rendering of this page
is a fetch-tool artifact, not source content).

### Related resources (linked from the changelog)

- Slack adapter documentation: https://chat-sdk.dev/adapters/official/slack
- Slack's own "agent messaging experience" changelog (external, linked as
  the basis for what Chat SDK's adapter wraps):
  https://docs.slack.dev/changelog/2026/06/30/agent-messages-tab/
- Chat SDK conversation-history/transcripts docs:
  https://chat-sdk.dev/docs/conversation-history
- Adapter template gallery: https://chat-sdk.dev/resources

## Cross-References

- **Corroborates**: `blog-vercel-chat-sdk-discord-components-v2.md` — both
  notes now document the same Chat SDK adapter-construction pattern (a
  `create<Platform>Adapter()` factory taking one config object, registered
  under an `adapters` map on a shared `Chat`/bot instance: compare this
  note's `createSlackAdapter({...})` under `adapters: { slack: ... }` to
  the Discord note's `createDiscordAdapter({ contentFormat: ... })`
  example). Together they establish this as Chat SDK's general adapter
  shape across at least two platforms, not a one-off Discord convention.
  Both notes are also first-party Vercel changelog entries of comparable
  length and depth (one feature, one code example, a short bullet list),
  and Ben Sabic is a credited co-author on both.
- **Contradicts**: None identified.
- **Extends**: `blog-vercel-chat-sdk-discord-components-v2.md` — that note's
  Source Context stated it does not cover "how Components V2 interacts with
  Chat SDK's other supported chat platforms (Slack, etc. — this note is
  Discord-adapter-specific)." This note fills part of that gap by
  documenting Slack's adapter-level feature set directly, though it does
  not describe any UI-component/layout system comparable to Discord's
  Components V2 — Slack's adapter here covers conversational UI (suggested
  prompts, streaming, feedback buttons, status messages), not a
  freely-arrangeable component layout system. The two adapters therefore
  are not yet shown to be capability-equivalent; Discord's Components V2
  (containers/sections/media galleries/buttons/selects) has no documented
  Slack counterpart in either source.
- **Extends**: `blog-simonwillison-tobias-lutke-lehrwerkstatt.md` — that
  note documents Shopify's River coding agent operating exclusively in
  public Slack channels (refusing DMs) as a deliberate organizational
  design choice ("Lehrwerkstatt" / osmosis learning). Neither that source
  nor this one states or implies that River is built on Chat SDK — Lütke's
  tweet (as quoted by Willison) says nothing about the underlying chat
  integration technology, and this changelog does not mention River or
  Shopify. The link between the two notes is therefore purely thematic
  (both describe agents operating inside Slack), not a documented technical
  relationship: this note supplies a concrete example of what a
  Slack-native agent integration's *technical* capabilities can look like
  (suggested prompts, streaming, feedback buttons, the `agentView`
  threading caveat) that a River-like Slack-resident agent would need to
  navigate, regardless of whether River itself uses Chat SDK.
- **Novel**: This is the first source note in the corpus to document a
  chat-platform adapter's *conversational* feature set (suggested prompts,
  streaming with platform-capability fallback, inline feedback collection,
  and a documented history/transcript gotcha) as opposed to the Discord
  note's *layout/rendering* feature set (Components V2's arrangeable UI
  primitives). It's also the first source to document Chat SDK's `agentView`
  concept and the specific pitfall that a chat platform's native history API
  can silently return an incomplete (one-sided) conversation record under
  that mode — a concrete instance of "don't assume the platform's history
  API is the full picture" that isn't covered by any other adapter note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: If the guide covers building
  chat-integrated agent harnesses, cite Claim 5 (the `agentView` history
  gotcha) as a concrete, named example of a platform-specific data-model
  trap: a chat platform's own message/thread history API is not guaranteed
  to reconstruct a full bidirectional conversation, and harness builders
  need a separate, adapter-maintained transcript mechanism rather than
  reading the platform's native history as ground truth. Pair with Claim 6
  (the single-object `create<Platform>Adapter()` pattern, corroborated
  against the Discord note) as a documented example of a consistent,
  low-friction adapter-configuration convention worth recommending when the
  guide discusses multi-platform chat integration architecture.
- **Chapter 01 (Daily Workflows)**: If the guide discusses agents that
  interact with users via chat platforms (status updates, Q&A, feedback
  collection), cite Claims 2–4 (context-aware suggested prompts, streaming
  with automatic fallback, and one-flag feedback-button collection) as a
  concrete inventory of what a modern chat-native agent UI can offer beyond
  plain text — and note, per Claim 7, that the "rotating status message"
  feature is exposed as a bare string array with no documented timing
  control, a real ergonomics gap for anyone trying to match status-message
  cadence to actual agent latency.
- **Chapter 05/06 (Integration Patterns / Security)**: If the guide expands
  coverage of Shopify's River-in-Slack pattern
  (`blog-simonwillison-tobias-lutke-lehrwerkstatt.md`), this source can be
  cited as background on what a Slack-native agent's technical surface
  looks like in a comparable off-the-shelf toolkit (Chat SDK) — while
  being explicit, per the Cross-References entry above, that no source in
  the corpus confirms River itself is built on Chat SDK.

## Extraction Notes

1. **WebFetch paraphrase caught and corrected**: An initial WebFetch pass
   returned a summary with invented subheadings ("Key Features," "Important
   Implementation Note") and a fabricated intro quote ("The Chat SDK now
   offers native Slack integration through its Slack adapter, enabling
   developers to build agents with full messaging capabilities..."). A
   second WebFetch pass targeting verbatim reproduction of specific
   passages returned wording much closer to the source, and — critically —
   this was then cross-checked directly against the page's raw HTML/RSC
   JSON payload (fetched via `curl`, not through the fetch-tool's
   summarizing model) to confirm every quote used in this note character-
   for-character, including sentence boundaries that span an inline
   hyperlink (e.g. Claim 1's quote spans "The adapter supports the full "
   + linked text "Slack agent messaging experience" + ", from agent
   conversations..."). The invented subheadings do not appear anywhere in
   the raw payload and are not used in this note. This is a direct
   confirmation of MINER.md §2a's warning: a summarizing fetch can
   reconstruct or invent structure (headings) not present in the source,
   and only a fetch targeting or verifying verbatim text — checked against
   raw page content — is safe to quote from.
2. **Author title sourced from byline markup, not article text**: "Content
   Engineer" appears in the page's author-byline HTML (`<span
   class="...">Content Engineer</span>` adjacent to the Ben Sabic author
   link), not in the article body itself. It is reported in Source Context
   as page metadata, not quoted as if it were prose from the article.
3. **No sub-pages were followed as additional sources.** The article links
   to the Slack adapter documentation, Slack's own "agent messaging
   experience" changelog (an external, non-Vercel page), the Chat SDK
   conversation-history docs, and a template gallery. These are
   reference/index pages elaborating on a single already-fully-described
   feature rather than substantive independent prose about this release,
   consistent with how the Discord Components V2 note (same source
   pattern) treated its own linked reference pages — so per MINER.md §1
   they were not fetched as separate sources. Their URLs are preserved in
   Concrete Artifacts for anyone following up.
4. **Claim count (7) is proportionate to source depth**: this is a short,
   single-feature changelog entry (two intro sentences, one code example,
   a three-item bullet list, and one callout paragraph) — comparable in
   length to the sibling Discord Components V2 changelog, which likewise
   supported 7 claims rather than the template's suggested 5–15 upper
   range.
5. **No contradiction with any existing corpus note was found**; see
   Cross-References. No contradiction issue was filed.
