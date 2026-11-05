---
source_url: https://simonwillison.net/2026/Nov/3/datasette-agent/
source_type: blog-post
title: "datasette-agent 0.5a0"
author: Simon Willison
date_published: 2026-11-03
date_extracted: 2026-11-05
last_checked: 2026-11-05
status: current
confidence_overall: anecdotal
issue: "#4529"
---

# datasette-agent 0.5a0

> A short release post introducing a "panel" that docks the agent chat beside live Datasette pages, paired with datasette-apps so a database-backed app can be prompted into existence and then edited from the adjacent chat; the linked release notes add concrete mechanics (a `show_in_panel` tool, `#` references, a stop button, and a prompt that no longer lists the schema).

## Source Context

- **Type**: blog-post (short release "beat"; the substance is in the linked GitHub release notes, which were also read)
- **Author credibility**: Simon Willison is the creator of Datasette and the developer of datasette-agent and datasette-apps; this is first-party release documentation.
- **Scope**: Covers the panel feature and the datasette-apps pairing. The post itself has no code, config, or metrics. Release notes (https://github.com/datasette/datasette-agent/releases/tag/0.5a0) cover the surrounding changes. Does NOT cover architecture rationale or evaluation of the panel.

## Extracted Claims

### Claim 1: The agent chat can sit beside live Datasette pages in a panel
- **Evidence**: First-party release announcement with a screenshot; release notes state the agent opens pages in the panel via a `show_in_panel` tool and that same-site links open there too.
- **Confidence**: anecdotal
- **Quote**: "it lets the agent chat open and then sit next to pages from Datasette"
- **Our assessment**: Plausible and concrete. Notably the agent drives the panel (a tool call), so the visible artifact is part of the agent's action space rather than only a passive display. Alpha release; no usage evidence.

### Claim 2: With datasette-apps, a database-backed app can be prompted into existence and then modified from the adjacent chat
- **Evidence**: Single-sentence assertion plus screenshot; no transcript or failure data.
- **Confidence**: anecdotal
- **Quote**: "you can prompt a database-backed app into existence and then modify it from the chat"
- **Our assessment**: Describes a create-then-iterate loop with the artifact visible during editing. Whether it works reliably is unverified.

### Claim 3: Conversations are decoupled from the page and survive navigation (release notes)
- **Evidence**: Release notes list that conversations keep running when you navigate away, show progress on return, and allow only one running turn per conversation.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Relevant to the panel design: the agent session is a durable server-side object, with the UI a view onto it. Paraphrased from release notes.

### Claim 4: Interruption semantics: Stop keeps streamed text and lets a started tool finish (release notes)
- **Evidence**: Release notes describe a Stop button replacing Send; the message box remains editable while the agent works.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: A practical design choice (graceful cancel rather than abort mid-tool) that avoids half-completed tool effects. Worth noting for harness UX.

### Claim 5: `#` references run permission checks as the sending user, and plugins can add reference types (release notes)
- **Evidence**: Release notes: `#` autocompletes tables, databases, stored queries; a `register_agent_reference_types()` hook extends this.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Explicit user-directed context injection with per-user permission enforcement — a context-engineering pattern, and the hook shows the plugin-extensible design.

### Claim 6: System prompt no longer lists every database and table; discovery is via tools (release notes)
- **Evidence**: Release notes: prompt is now identical for all users and schemas; `list_tables`, `describe_query`, and count-bearing `list_databases_and_tables` provide discovery.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Move from eager schema-in-prompt to lazy tool-based discovery; a stable, user-independent prompt is also cache-friendly (our inference; the notes do not mention caching).

### Claim 7: Pages that refuse framing degrade gracefully, and cross-site links need confirmation (release notes)
- **Evidence**: Release notes: framing-refusal shows an error with open-in-new-tab link; external links ask for confirmation.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Shows the panel is an iframe-style embed with safety boundaries; consistent with the sandbox posture in the datasette-apps note.

## Concrete Artifacts

```
Source: release notes for datasette-agent 0.5a0 (paraphrased, not verbatim)
- panel beside chat; agent opens pages with `show_in_panel`
- "Chat | Panel" switch on narrow screens
- `#` autocomplete for tables/databases/stored queries
- hook: register_agent_reference_types()
- tools: list_tables, describe_query; sql_query now has query_ms
- Requires datasette>=1.0a41, datasette-llm>=0.1a9, llm>=0.37.1
- Try: https://agent.datasette.io/ (GitHub sign-in)
```

## Cross-References

- **Corroborates**: `blog-simonwillison-datasette-apps.md` (the apps plugin the panel pairs with, including its LLM-friendly design for generated apps).
- **Contradicts**: none found.
- **Extends**: `blog-simonwillison-datasette-agent.md` (platform and plugin model), `blog-simonwillison-datasette-agent-write-sql.md` (SQL tools whose parameter format changes here), `blog-simonwillison-datasette-agent-askuser.md` (earlier interaction-surface feature).
- **Novel**: The co-located panel UI, agent-controlled `show_in_panel`, and the prompt-to-app-then-edit loop; no existing note covers releases 0.4a0 or 0.5a0.

## Guide Impact

- **Chapter 02**: Optional example for agent UI surfaces: an agent chat docked beside the artifact it edits, with the agent able to navigate the panel by tool call. Low evidential weight (alpha release, no evaluation).
- **Chapter 04**: Optional example of replacing a schema-listing system prompt with on-demand discovery tools, plus user-initiated `#` references permission-checked as the user. Flag the cache benefit as inference.

## Extraction Notes

- The blog post is about three sentences; I also read the linked GitHub release notes. The web-fetch tool returned summaries rather than verbatim text, so only two short fragments are quoted (taken from fetch output); everything from the release notes is marked as paraphrase. The Assayer should verify the two quotes against the post.
- No contradictions found, so no contradiction issue was filed.
