---
source_url: https://vercel.com/changelog/claude-managed-agents-with-chat-sdk
source_type: blog-post
title: "Run Claude Managed Agents with Chat SDK"
author: Ben Sabic (Vercel, Content Engineer); contributor Amelia Charles
date_published: 2026-07-27
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: settled
issue: "#2915"
---

# Run Claude Managed Agents with Chat SDK

> A one-minute Vercel changelog entry announcing that Claude Managed Agents
> can be operated through Chat SDK's adapter layer, backed by two much
> deeper first-party artifacts followed as sub-pages: an official Anthropic
> quickstart (`claude-quickstarts/managed-agents/chat-sdk`, a web-only demo)
> and a full Vercel knowledge-base guide that deploys a production Slack
> research bot on Next.js + Upstash Redis + Vercel Connect. Together they
> document the concrete session-event-streaming bridge code, a tool-policy
> pattern that disables Bash specifically because the agent reads untrusted
> web pages, and operational details (agent-version pinning, session
> revalidation, fast webhook acknowledgement) not documented anywhere else
> in the corpus.

## Source Context

- **Type**: blog-post (Vercel changelog) as the filed source, but the
  changelog itself is only a ~1-minute-read announcement. Per MINER.md §1
  ("follow up to 5 linked pages that seem substantive"), two linked
  first-party pages were fetched and extracted alongside it, because the
  changelog's own content is too thin to support a useful source note on
  its own:
  1. **Anthropic's quickstart repo README** —
     `https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/chat-sdk`
     (verified against the raw `README.md` at
     `raw.githubusercontent.com/anthropics/claude-quickstarts/main/managed-agents/chat-sdk/README.md`).
     A minimal, web-adapter-only demo: no chat platform to register with,
     just an Anthropic credential.
  2. **Vercel's knowledge-base guide** —
     `https://vercel.com/kb/guide/claude-managed-agents-chat-sdk`, titled
     "Build Claude Managed Agents with Chat SDK." A full walkthrough of
     `vercel-labs/cma-chat-sdk`, a production-shaped Slack bot deployed on
     Vercel with Upstash Redis and Vercel Connect. This is where nearly all
     of the concrete, novel technical content in this note comes from.
  Two further linked pages (`chat-sdk.dev/` marketing home,
  `chat-sdk.dev/docs/getting-started`) were not fetched as separate
  sources — they are the general Chat SDK product/docs entry points already
  covered structurally by the two Chat SDK adapter notes already in the
  corpus (see Cross-References), not integration-specific content.
- **Author credibility**: The changelog is credited to Ben Sabic (Content
  Engineer), the same byline as `blog-vercel-chat-sdk-slack-agent-support.md`,
  with Amelia Charles as a listed contributor. The quickstart repo is
  published under Anthropic's own `anthropics/claude-quickstarts` GitHub
  organization — first-party, and (per its own README) built to be walked
  through by Claude Code itself (`claude "walk me through setting up..."`
  reads `skill.md` and drives setup). The KB guide is unsigned Vercel
  documentation (no byline), presented as first-party product documentation
  rather than a blog post, with concrete file paths, environment variable
  tables, and multiple full TypeScript code blocks — the most
  implementation-detailed of the three pages.
- **Scope**: Covers how to wire Claude Managed Agents' session/event API to
  a chat surface via Chat SDK, in two shapes: a minimal local web demo and a
  production Slack deployment with persistent state, webhook handling, and
  agent-version lifecycle management. Does **not** cover: pricing beyond
  what's already documented in `blog-anthropic-claude-managed-agents.md`
  (session-hour rate), non-Slack platform specifics (Teams, Discord,
  WhatsApp are named as also-supported but not walked through), how
  `event_deltas` token-preview gating is rolled out per-organization beyond
  the one sentence noting it exists, or independent production-scale
  evidence (the KB guide's troubleshooting section implies real usage
  patterns but names no customer).

## Extracted Claims

### Claim 1: Chat SDK exposes Claude Managed Agents through the same single type-safe handler and multi-platform adapter model it uses for any other chat backend — "swapping a few lines" moves the same agent from a local web demo to Slack, Teams, Discord, WhatsApp, or 30+ other platforms
- **Evidence**: The changelog's own "What you get" bullet list (raw HTML,
  not a fetch-tool paraphrase — verified via `curl` against the page's raw
  markup) plus the quickstart README's line "Swapping a few lines in the
  handler moves your agent to Slack, Teams, Discord, WhatsApp, and 30+
  other platforms."
- **Confidence**: settled (first-party feature description; the mechanism —
  a `create<Platform>Adapter()` factory per platform — is independently
  confirmed by two other adapter-specific changelogs already in the corpus)
- **Quote**: "Portability by design: Swapping a few lines in the handler
  moves your agent to Slack, Teams, Discord, WhatsApp, and 30+ other
  platforms."
- **Our assessment**: This is the integration's core value proposition, and
  it is credible given the corpus already documents the same
  `create<Platform>Adapter()` shape independently for Slack and Discord
  (see Cross-References). What's new here is that the *backend* being
  adapted is Managed Agents specifically, not a hand-rolled LLM call — the
  adapter boundary sits between Chat SDK's chat surface and Managed Agents'
  session/event API rather than between Chat SDK and an arbitrary model
  call.

### Claim 2: The chat server keeps no database of its own — the Managed Agents session is the single source of truth, and the `useChat` conversation ID is literally the Managed Agents session ID
- **Evidence**: Changelog bullet plus the quickstart README's architecture
  description ("One persistent Managed Agents session per conversation
  owns the research... The server stores nothing: the `useChat`
  conversation ID is a Managed Agents session ID. The sidebar is the
  sessions API. Transcripts replay from the session's event log.
  Compaction and prompt caching happen inside the session.")
- **Confidence**: settled (first-party architecture statement, consistent
  across both the changelog and the quickstart README)
- **Quote**: "No database to run: The Managed Agents session stores the
  conversation, so the sidebar, transcript, and replay read from it, no
  server-side state of your own."
- **Our assessment**: This only holds for the *conversation* state — the
  production Slack deployment (Claim 8 below) still needs Redis for
  cross-cutting state (subscriptions, thread→session mapping, webhook
  dedup) that isn't part of any one session. So "no database" is true for
  the minimal web demo specifically, and the KB guide is explicit that a
  production multi-channel deployment still needs external state for
  everything that isn't a single conversation's content. This is a useful
  nuance the changelog's own bullet elides.

### Claim 3: The event-stream bridge must subscribe to a Managed Agents session's event stream *before* sending the user's message, then use the returned message event's ID as an anchor to discard any stale events left over from a previous turn
- **Evidence**: The KB guide's "The event-stream bridge" section, with a
  full code example (see Concrete Artifacts) showing
  `client.beta.sessions.events.stream()` called first, then
  `client.beta.sessions.events.send()`, with the anchor ID extracted from
  the send response.
- **Confidence**: settled (concrete, runnable first-party code with an
  explained failure mode it prevents)
- **Quote**: "The stream only emits events produced after attachment, so
  `streamTurn` subscribes first and then sends the `user.message` event...
  The returned event ID acts as an anchor. The loop discards everything on
  the stream until it sees its own `user.message` echo back, so events left
  over from a previous turn never produce a stale reply."
- **Our assessment**: This is the single most concrete, previously
  undocumented technical detail in this source for our corpus — no other
  source note describes the Managed Agents session/event streaming API's
  subscribe-then-send ordering requirement or the anchor-based
  stale-event-rejection pattern. Anyone building a custom (non-Chat-SDK)
  bridge to Managed Agents' event stream needs to replicate this ordering
  or risk a race where a turn's reply is contaminated by leftover events
  from the previous turn.

### Claim 4: The reference agent's tool policy auto-approves every tool except Bash, which is disabled outright — specifically because the agent reads untrusted web pages, and an auto-approved shell with network access would let a malicious page trick it into leaking conversation data
- **Evidence**: The KB guide's "The agent definition" section, with the
  full `agentTools()` TypeScript function (see Concrete Artifacts) and an
  explicit prose justification for the Bash exclusion.
- **Confidence**: settled (first-party code plus an explicit, specific
  threat-model justification — not a generic "be careful" caveat)
- **Quote**: "Every tool in the toolset is auto-approved except Bash, which
  is disabled outright. Auto-approval is what makes a headless Slack bot
  workable, since there's no UI to click approve in. Bash comes out
  entirely because the agent reads untrusted web pages, and an
  auto-approved shell with network access would let a malicious page trick
  it into leaking conversation data. Don't re-enable Bash without a real
  human-approval flow and restricted egress."
- **Our assessment**: This is a specific, checkable prompt-injection threat
  model applied to a concrete deployment: any agent that (a) fetches
  untrusted content and (b) runs unattended (no human in the loop to click
  "approve") should not also have an auto-approved shell with network
  egress, because the untrusted content becomes an injection vector for
  data exfiltration via that shell. The guide's own troubleshooting section
  reinforces this is a hard rule, not a default to relax: when a turn
  fails because the agent requested an unapproved tool, the fix is
  explicitly "keep Bash disabled," not "approve it."

### Claim 5: A stored session ID pulled from external state (Redis) is treated as untrusted input and re-validated before reuse — it must exist, belong to the current agent, and not be archived or terminated; only genuine invalidity triggers a fresh session, while transient API errors are re-thrown so a network blip doesn't discard a thread's research context
- **Evidence**: The KB guide's "Participant policy and session state"
  section, describing an `ownedSession()` validation function.
- **Confidence**: settled (specific, named validation function with an
  explicit error-handling distinction between "genuinely invalid" and
  "transient failure")
- **Quote**: "Session resolution is validate-or-recreate. The stored
  session ID is untrusted input from Redis, so `ownedSession()` checks it
  before use: the session must exist, belong to this agent, and not be
  archived or terminated. Transient API errors are re-thrown, so a network
  blip doesn't discard a thread's research context."
- **Our assessment**: This is a small but easy-to-miss correctness detail
  for anyone building persistent, externally-keyed sessions against a
  hosted agent platform: naively treating any lookup failure as "session
  gone, start fresh" would silently discard conversation history on every
  transient network error. The explicit re-throw-on-transient-error
  behavior is the kind of detail that's obvious once stated and easy to
  get wrong by default.

### Claim 6: Because Anthropic pins each Managed Agents session to the agent version active when the session was created, updating the agent's prompt/model/tools does not retroactively change already-open conversations — only new sessions see the new behavior
- **Evidence**: The KB guide's "Customize the analyst" section.
- **Confidence**: settled (specific, first-party platform behavior
  statement with a direct operational consequence spelled out)
- **Quote**: "Anthropic pins each session to the agent version that created
  it, so existing Slack threads keep the old behavior even after an
  update. Start a new thread to see your changes."
- **Our assessment**: This is a real operational gotcha for iterating on a
  deployed Managed Agents bot: a prompt fix pushed via `cma:update` (which
  publishes a new agent version) will not retroactively fix a
  currently-open thread that's misbehaving — the fix only takes effect on
  the next new thread. Anyone debugging "I fixed the prompt but the bot in
  this thread is still doing the old thing" needs to know this is expected
  platform behavior, not a deployment failure. This is not stated or
  implied anywhere else in the corpus's existing Managed Agents notes.

### Claim 7: A single-human Slack thread gets automatic replies to every message, but the moment a second human joins, the bot unsubscribes from ambient messages and responds only to explicit @mentions — implemented as a four-line participant-count check
- **Evidence**: Both the changelog-adjacent KB guide prose and a short,
  fully-quoted TypeScript snippet (see Concrete Artifacts).
- **Confidence**: settled (first-party code plus explicit rationale in the
  guide's own troubleshooting section)
- **Quote**: "An unmentioned message counts as a follow-up only when the
  bot is talking to one person. When a second human joins, the bot
  unsubscribes and stays quiet until someone mentions it again."
- **Our assessment**: This is a concrete, minimal implementation of a
  pattern that matters for any chat-resident agent operating in
  multi-person threads: distinguishing "a DM-like one-on-one conversation
  where every message is implicitly addressed to the bot" from "a group
  conversation where the bot should not interject unless named." The
  four-line implementation (`participants.length !== 1` gates
  `unsubscribe()`) is cheap enough that it's a reasonable default pattern
  to recommend rather than a bespoke solution requiring heavier
  infrastructure.

### Claim 8: The production Slack deployment (`vercel-labs/cma-chat-sdk`) is a four-layer stack — Slack surfaced via Chat SDK + Vercel Connect, Claude Managed Agents running Claude Sonnet 5 as the agent, Upstash Redis for cross-request state, and Next.js 16 on Vercel for the runtime — with the custom code reduced to about six source files plus a small provisioning CLI
- **Evidence**: The KB guide's "The stack" section (a table plus four
  one-line layer descriptions) and "Code walkthrough" section.
- **Confidence**: settled (first-party architecture description, and the
  file-count claim is directly checkable against the file list given
  elsewhere in the same guide)
- **Quote**: "Managed Agents: Runs the model loop, the sandbox, and the web
  tools. Chat SDK: Handles the Slack surface, including mentions, threads,
  typing indicators, and streamed posts. Vercel Connect: Manages the Slack
  app and its credentials. Redis: Keeps the state that has to survive
  redeploys. That leaves your code as a thin bridge between them, about six
  source files."
- **Our assessment**: This is a useful concrete data point on how thin the
  custom "glue" code can be when the heavy infrastructure (sandboxed
  execution, credential brokering, chat-platform protocol handling, cross-
  deploy state) is delegated to three separate hosted services (Managed
  Agents, Vercel Connect, Upstash) plus one SDK (Chat SDK). It corroborates
  the broader "managed platforms shrink the custom-code surface area"
  narrative already present in `blog-anthropic-claude-managed-agents.md`
  and extends it with an actual file count for one concrete deployment.

### Claim 9: Slack's webhook acknowledgement deadline (seconds) is bridged to a multi-minute research turn using Next.js's `after()` primitive — the webhook responds immediately while the actual agent turn runs in the background with a 300-second budget, and Redis-backed deduplication prevents Slack's automatic webhook redelivery from double-running a turn
- **Evidence**: The KB guide's "Fast webhook acknowledgement" section, with
  a short code excerpt showing `after()` wired into the `waitUntil` hook of
  Chat SDK's webhook handler.
- **Confidence**: settled (specific, named mechanism with an explicit
  numeric budget and a stated failure mode it prevents)
- **Quote**: "Slack expects webhook acknowledgements within seconds, but a
  research turn takes minutes... Chat SDK's webhook handler acknowledges
  Slack right away and runs the turn in the background, where `maxDuration
  = 300` gives it up to five minutes to finish streaming. If Slack
  redelivers a webhook, Redis-backed deduplication stops the turn from
  running twice."
- **Our assessment**: This is a specific, reusable pattern for any
  webhook-driven agent whose actual work exceeds the calling platform's
  ack deadline — separate the fast synchronous ack from the slow
  asynchronous work, and independently guard against the calling
  platform's own retry/redelivery behavior turning one logical event into
  duplicate work. The "route takes the platform as a parameter" detail
  (`/api/webhooks/[platform]/route.ts`) also shows this is designed to be
  reused unmodified when a second Chat SDK adapter (e.g., Teams) is added
  later.

### Claim 10: A debug mode (`CLAUDE_DEBUG_MODE=true`) posts a per-turn diagnostics card into the chat itself — duration, model request count, token and prompt-cache usage, web search/fetch counts, and a direct link to that turn's trace in the Claude Console
- **Evidence**: The KB guide's "Debug mode" section.
- **Confidence**: settled (specific, named environment variable with an
  enumerated content list)
- **Quote**: "Set `CLAUDE_DEBUG_MODE=true` to post a compact diagnostics
  card after every completed turn: duration, model requests, token and
  prompt-cache usage, web search and fetch counts, and a link to the
  session trace in the Claude Console."
- **Our assessment**: Surfacing per-turn cost/performance diagnostics
  directly in the chat surface (rather than requiring a separate
  dashboard visit) is a low-friction way to keep prompt/cost tuning
  in-context during development. This complements, rather than duplicates,
  `blog-anthropic-claude-managed-agents.md`'s Claim 7 (Claude Console
  tracing) — that note documents the platform-level tracing surface; this
  note documents an application-level convenience that surfaces a subset
  of the same data inline in Slack.

### Claim 11: The web-only quickstart requires no chat-platform registration at all — no Slack/WhatsApp app, no webhook verification, no tunnel — because it runs on Chat SDK's web adapter, and the whole setup can be driven by Claude Code itself reading a `skill.md` file in the repo
- **Evidence**: The changelog's "Getting Started" framing plus the
  quickstart README's own Quickstart section, which shows both a
  Claude-Code-driven path (`claude "walk me through setting up the Chat SDK
  and Claude Managed Agents"`) and a manual `npm install && npm run
  setup && npm run dev` path.
- **Confidence**: settled (directly reproducible from the published README)
- **Quote**: "To see it work, a new Anthropic quickstart builds a working
  research analyst you chat with in the browser. It runs on Chat SDK's web
  adapter, so there's no platform registration, webhook verification, or
  tunnel, just your Anthropic credentials."
- **Our assessment**: This is a deliberate on-ramp design choice worth
  naming for the guide: the web adapter is used specifically to strip away
  every piece of chat-platform ceremony (app registration, OAuth scopes,
  webhook signing, tunneling a local dev server) so a developer's first
  contact with Managed Agents + Chat SDK is unblocked by platform setup.
  The production path (Slack, via the KB guide) is presented as a second,
  separate step once the core session/event bridge is understood in
  isolation.

### Claim 12: Token-preview streaming (`event_deltas`) is gated per-organization while a 2026-07-01 Managed Agents update rolls out; without the gate, the integration still works correctly but replies arrive whole instead of streaming token-by-token
- **Evidence**: A single explicit caveat sentence in the quickstart
  README's Quickstart section (not present in the changelog itself, which
  presents streaming as unconditional).
- **Confidence**: emerging (stated as a rollout-in-progress caveat, with no
  detail on rollout timeline, how an organization checks its own gate
  status, or what "whole" replies look like in the UI compared to streamed
  ones)
- **Quote**: "Token previews (`event_deltas`) are gated per organization
  while the 2026-07-01 Managed Agents update rolls out. Without the gate,
  everything still works and replies arrive whole instead of streaming."
- **Our assessment**: This directly qualifies Claim 1's "token-by-token
  streaming" framing from the changelog: streaming is not universally
  available at time of writing, it is a rollout-gated feature with a
  documented graceful degradation (correctness preserved, UX degraded to
  non-streaming). A reader relying only on the changelog's bullet list
  would not know this caveat exists — it is only stated in the quickstart
  README, one of the sub-pages this note followed per MINER.md §1. This is
  a concrete example of why following linked sub-pages matters: the
  headline feature list overstates what's uniformly available today.

## Concrete Artifacts

### Quickstart repo file structure (`claude-quickstarts/managed-agents/chat-sdk/README.md`)

```
Source: https://raw.githubusercontent.com/anthropics/claude-quickstarts/main/managed-agents/chat-sdk/README.md

setup/agent-config.ts   - Model + system prompt: the agent's entire behavior
setup/create-agent.ts   - One-time provisioning: the analyst agent and its environment
setup/update-agent.ts   - Pushes the edited config onto the existing agent as a new version
src/app.ts              - Platform-neutral API core: /api/chat, /api/sessions, /api/history, /api/activity
src/main.ts             - The local Node host: the chat page plus the API core, served by one process
src/bot.ts              - Chat SDK instance, web adapter, getUser (the auth boundary), message handler
src/managed-agents.ts   - The bridge: the turn loop, token previews, the session ownership check
src/sessions.ts         - The sidebar's data source: list, create, and replay sessions
src/card.tsx            - The "brief ready" JSX card and its web fallback
src/brief.ts            - Shared card and trace formats: what the server writes and the page renders
src/activity.ts         - In-process fan-out of turn activity to live subscribers
web/                     - The chat page: React + useChat, the sidebar, the activity feed, bundled by esbuild
skill.md                - Setup walkthrough, gotchas, debugging
CLAUDE.md               - Design notes
```

### Quickstart environment variables and npm scripts (`claude-quickstarts/managed-agents/chat-sdk/README.md`)

```
Environment variables:
ANTHROPIC_API_KEY    | no  | API key from platform.claude.com. Skip after `ant auth login`
CLAUDE_AGENT_ID       | yes | The analyst agent, printed by `npm run setup`
CLAUDE_ENVIRONMENT_ID | yes | The agent's sandbox environment, printed by `npm run setup`
PORT                  | no  | Where the server listens (default 3000)
HOST                  | no  | Bind address (default 127.0.0.1). Set 0.0.0.0 only after replacing the demo getUser
QUICKSTART_MODEL      | no  | Overrides the agent's model, applied by `npm run setup` and `npm run update-agent`

npm scripts:
npm run setup         - One-time provisioning: creates the agent and its environment, prints their IDs
npm run update-agent  - Pushes an edited setup/agent-config.ts onto the existing agent as a new version
npm run dev           - Runs the server, restarting on change; web/ edits apply on browser reload
npm start             - Runs the server once, no watcher
```

### Chat SDK web-adapter server (`src/bot.ts`, production Slack deployment) — Slack surface

```typescript
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("The Slack surface" section)
Filename in guide: src/lib/bot.ts

import { createSlackAdapter } from "@chat-adapter/slack";
import { createRedisState } from "@chat-adapter/state-redis";
import { connectSlackAdapter } from "@vercel/connect/chat";
import { Chat } from "chat";
import { config } from "./config";
import { handleResearchMessage, type ThreadState } from "./research-handler";

const adapters = {
  slack: createSlackAdapter({
    ...connectSlackAdapter(config.slackConnector),
  }),
};

export const bot = new Chat<typeof adapters, ThreadState>({
  adapters,
  concurrency: "concurrent",
  state: createRedisState({ url: config.redisUrl }),
  userName: config.botUsername,
});

bot.onNewMention(async (thread, message) => {
  await thread.subscribe();
  await handleResearchMessage(thread, message, "new-mention");
});

bot.onSubscribedMessage(async (thread, message) => {
  await handleResearchMessage(thread, message, "subscribed");
});

bot.onDirectMessage(async (thread, message) => {
  await handleResearchMessage(thread, message, "direct");
});
```

### Participant policy (`src/lib/research-handler.ts`)

```typescript
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("Participant policy and session state" section)

if (mode === "subscribed" && !message.isMention) {
  const participants = await thread.getParticipants();
  if (participants.length !== 1) {
    await thread.unsubscribe();
    return;
  }
}
```

### Session event-stream bridge (`src/lib/managed-agents.ts`)

```typescript
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("The event-stream bridge" section)

const stream = await client.beta.sessions.events.stream(sessionId, {
  event_deltas: ["agent.message"],
});

const sent = await client.beta.sessions.events.send(sessionId, {
  events: [
    {
      content: [{ text, type: "text" }],
      type: "user.message",
    },
  ],
});

anchorId = sent.data?.find((event) => event.type === "user.message")?.id;
```

### Agent tool policy (`scripts/cma/lib/agent.ts`)

```typescript
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("The agent definition" section)

export function agentTools(): NonNullable<AgentCreateParams["tools"]> {
  return [
    {
      configs: [{ enabled: false, name: "bash" }],
      default_config: {
        enabled: true,
        permission_policy: { type: "always_allow" },
      },
      type: "agent_toolset_20260401",
    },
  ];
}
```

### Fast webhook acknowledgement (`src/app/api/webhooks/[platform]/route.ts`)

```typescript
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("Fast webhook acknowledgement" section)

return handler(request, {
  waitUntil: (task) => after(() => task),
});
```

### Manual production setup commands (`vercel-labs/cma-chat-sdk`)

```bash
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("Set up from a clone" section)

git clone https://github.com/vercel-labs/cma-chat-sdk
cd cma-chat-sdk
pnpm install

vercel link
vercel connect create slack --name claude-research-analyst --triggers
vercel connect attach slack/claude-research-analyst \
  --project your_vercel_project_here \
  --environment production \
  --triggers \
  --trigger-path /api/webhooks/slack

vercel integration add upstash/upstash-kv

# after adding ANTHROPIC_API_KEY to .env.local:
pnpm cma:setup --vercel
vercel deploy --prod
```

### Production environment variables (`vercel-labs/cma-chat-sdk`)

```
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("Environment variables" section)

ANTHROPIC_API_KEY     | Yes | None                  | Authenticates Claude Managed Agents
CLAUDE_AGENT_ID        | Yes | None                  | Persistent analyst created by `pnpm cma:setup`
CLAUDE_ENVIRONMENT_ID  | Yes | None                  | Anthropic-managed sandbox created by setup
REDIS_URL              | Yes | None                  | Stores subscriptions, deduplication, thread/session mappings
SLACK_CONNECTOR        | Yes | None                  | Vercel Connect Slack connector UID
BOT_USERNAME           | No  | claude-research-bot   | Chat SDK bot name
CLAUDE_DEBUG_MODE       | No  | false                 | Posts per-turn diagnostics and a Claude Console link
```

### Troubleshooting table (`vercel-labs/cma-chat-sdk` guide)

```
Source: https://vercel.com/kb/guide/claude-managed-agents-chat-sdk ("Troubleshooting" section)

Symptom: @mentions don't get a response
  Cause: bot not in channel, deployment not finished, or a required env var
         missing (fails server at startup)
  Fix: invite the bot, confirm deployment succeeded, check logs for a
       "must be set" configuration error

Symptom: "Earlier research context for this thread is no longer available"
  Cause: stored session no longer validates (Redis state expired, or the
         session was archived/terminated/belongs to a different agent,
         e.g. after re-running setup and creating a new agent ID)
  Fix: nothing broken — a fresh session was already created; restate
       context; if it recurs after re-provisioning, confirm the deployed
       CLAUDE_AGENT_ID matches the agent the thread was created against

Symptom: "The agent asked for an approval this bot can't handle"
  Cause: the agent's tool policy no longer auto-approves a tool it tried
         to use, and this Slack surface has no approve-button UI
  Fix: restore the always-allow default in agentTools(), run
       `pnpm cma:update`, start a new Slack thread; keep Bash disabled

Symptom: "I lost my connection mid-research, but the work continues on
          Anthropic's side"
  Cause: the HTTP event stream between the deployment and Anthropic
         dropped before the turn completed; the session itself keeps running
  Fix: wait and check the thread instead of resending (resending queues a
       duplicate turn behind the still-running one)

Symptom: bot stops responding to thread follow-ups after answering once
  Cause: a second human joined the thread; participant policy unsubscribed
         the bot from multi-human threads
  Fix: @mention the bot explicitly to get a response and re-subscribe it
```

## Cross-References

- **Corroborates**:
  - `blog-vercel-chat-sdk-slack-agent-support.md` — both notes now document
    the same `create<Platform>Adapter()` single-config-object adapter shape
    (that note's `createSlackAdapter({ agentView, suggestedPrompts,
    loadingMessages, feedbackButtons })` vs. this note's
    `createSlackAdapter({ ...connectSlackAdapter(config.slackConnector) })`).
    This note adds the missing other half of that note's picture: that
    prior note describes the *adapter's own* Slack-native UI features
    (suggested prompts, streaming with Post+Edit fallback, feedback
    buttons) but says nothing about what sits *behind* the adapter driving
    the actual agent logic. This note supplies that: a Managed Agents
    session, bridged via the event-stream pattern in Claim 3.
  - `blog-anthropic-claude-managed-agents.md` — this note's Claim 2 (no
    server-side conversation state; the session is the source of truth)
    and Claim 8 (sandboxed execution delegated to the platform) are
    concrete implementations of that announcement's Claims 1–3
    (infrastructure delegation, built-in orchestration harness,
    session persistence). Claim 4's Bash-disable tool policy is the first
    concrete, code-level example in the corpus of that announcement's
    Claim 7 ("scoped permissions... built in") — showing what a scoped
    permission policy actually looks like as JSON, not just as a marketing
    bullet.
- **Contradicts**: None identified.
- **Extends**: `blog-vercel-chat-sdk-slack-agent-support.md` — see
  Corroborates above; this is as much an extension (filling a documented
  gap in that note's Scope — "does not cover... the adapter's OAuth/
  bot-token setup") as a corroboration, since this note's Vercel Connect
  usage (`connectSlackAdapter`, `vercel connect create slack`) directly
  answers that gap for this specific integration.
- **Novel**: The Managed Agents session/event-streaming API surface itself
  (`client.beta.sessions.events.stream()` / `.send()`, the
  subscribe-before-send ordering requirement, and the anchor-ID pattern for
  rejecting stale events from a prior turn — Claim 3) is not documented
  anywhere else in the corpus. Same for the concrete tool-policy JSON shape
  (`agent_toolset_20260401`, per-tool `enabled: false` overrides against a
  default `always_allow` policy — Claim 4) and its specific prompt-
  injection-via-untrusted-web-content threat model for justifying a
  per-tool Bash exclusion. Agent-version pinning per session (Claim 6) and
  the untrusted-session-ID revalidation pattern (Claim 5) are also first
  appearances in the corpus of Managed Agents' session lifecycle
  semantics — prior Managed Agents notes describe capabilities and
  customer outcomes, not this level of session-state mechanics.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 4's tool-policy pattern
  (auto-approve everything except a named, explicitly disabled tool, with
  the disable justified by a specific threat model — untrusted content +
  network-capable shell = exfiltration risk) as a concrete, reusable
  template for scoping tool access in any unattended/headless agent that
  reads untrusted external content. Pair with Claim 3's event-stream
  subscribe-before-send/anchor pattern as implementation guidance for
  anyone bridging a hosted agent platform's event stream to a UI surface
  directly (i.e., not going through Chat SDK), since the ordering
  requirement and stale-event rejection logic are the platform's,
  not Chat SDK's.
- **Chapter 02 (Harness Engineering)**: Document Claim 6 (agent-version
  pinning per session) as an operational gotcha specific to hosted agent
  platforms with persistent sessions: unlike a stateless prompt-and-
  response call where every request picks up the latest prompt, a
  persistent session locks in the agent version active when it was
  created. Anyone iterating on a deployed agent's prompt needs to know
  existing conversations won't see the fix.
- **Chapter 05/06 (Integration Patterns / Production Deployment)**: Cite
  Claim 9's fast-ack/background-work split (Next.js `after()`, a numeric
  duration budget, Redis-backed dedup against platform-side webhook
  redelivery) as the general pattern for any webhook-driven agent whose
  real work exceeds the calling platform's synchronous-response deadline —
  this generalizes beyond Slack to any webhook-based chat or event
  integration. Claim 8's four-layer stack (chat surface / agent platform /
  cross-request state store / app runtime) is a reasonable reference
  architecture to name explicitly when the guide discusses what a
  "minimal production chat-agent deployment" looks like.
- **Chapter 01 (Daily Workflows)**: Claim 11 (the web-adapter quickstart
  strips out all chat-platform ceremony, and `claude "walk me through
  setting up..."` reading a repo's `skill.md` can drive the entire local
  setup) is a concrete example of using Claude Code itself as the
  onboarding mechanism for a new tool/SDK, worth citing alongside other
  corpus examples of skill-file-driven setup flows if the guide covers
  that pattern.

## Extraction Notes

1. **The filed changelog is too thin to stand alone as a source note.**
   At ~1 minute read time (three short intro paragraphs, a four-item
   bullet list, two closing paragraphs), it does not meet the "5–15
   claims" bar on its own. Per MINER.md §1, two linked first-party pages
   were fetched as sub-pages and form the bulk of this note's extracted
   claims (Claims 3–10, 12 all come from the KB guide or quickstart
   README, not the changelog itself). The changelog is retained as the
   `source_url` because it is the URL filed in the triggering issue and
   is the entry point that led to the other two pages.
2. **All quotes were verified against raw page HTML/Markdown fetched via
   `curl`, not against a WebFetch-tool summary.** An initial WebFetch pass
   on the changelog and the KB guide returned plausible-looking prose that,
   on verification, included invented section headings not present in the
   source (e.g., a "Getting Started" h3 that doesn't exist in the
   changelog's actual markup — the "To see it work..." paragraph follows
   the feature list directly with no heading between them; and a
   restructured "Technology Stack" table / "How It Works" numbered list /
   "Prerequisites for Deployment" heading in the KB-guide summary that do
   not match that page's real heading IDs, which are "The stack,"
   "What you need before deploying," and "How the research analyst
   works"). Every quote and code block in this note was cross-checked
   against the raw HTML (`data-kb-copy-code` attributes for the KB guide's
   code blocks, and direct `<p>`/`<li>` text for prose) or the raw
   `README.md` (for the GitHub quickstart, fetched via
   `raw.githubusercontent.com`) before being included here. One WebFetch-
   summary "quote" attributed to the KB guide's overview ("run a research
   analyst in Slack without building agent infrastructure") did not appear
   verbatim in the raw HTML at all; the real opening sentence ("Run a
   research analyst in Slack without building agent infrastructure. You
   @mention the bot with a question, and it searches and fetches sources
   inside an Anthropic-managed sandbox, then streams a sourced brief back
   into the thread.") was used instead, confirmed byte-for-byte against
   the page's raw markup.
3. **Not followed further**: `chat-sdk.dev/` and
   `chat-sdk.dev/docs/getting-started` (Chat SDK's own marketing/docs
   entry points, not integration-specific — already indirectly represented
   in the corpus via the Slack and Discord adapter notes) and
   `platform.claude.com/docs/en/managed-agents/overview` (the Managed
   Agents platform docs home, which is a general reference page rather
   than content specific to this Chat SDK integration).
4. **Confidence set to `settled` overall**, a step above the `emerging`
   rating given to the sibling Slack-adapter-only changelog
   (`blog-vercel-chat-sdk-slack-agent-support.md`), because most of this
   note's substantive claims are drawn from runnable, verifiable code in
   published repositories (the quickstart and `cma-chat-sdk` template)
   rather than from a marketing-style feature-list changelog alone. The
   one claim rated `emerging` individually (Claim 12, the per-organization
   streaming rollout gate) is flagged as such because it is a single,
   underspecified caveat sentence with no rollout timeline or detection
   mechanism given.
