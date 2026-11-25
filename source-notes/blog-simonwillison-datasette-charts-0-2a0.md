---
source_url: https://simonwillison.net/2026/Nov/24/datasette-charts/
source_type: blog-post
title: "datasette-charts 0.2a0"
author: Simon Willison
date_published: 2026-11-24
date_extracted: 2026-11-25
last_checked: 2026-11-25
status: current
confidence_overall: emerging
issue: "#4936"
---

# datasette-charts 0.2a0

> A short release beat showing that datasette-charts now exposes `suggest_charts` and `chart` tools to Datasette Agent, with the chat chart and the human chart-builder panel linked by a page address that the agent is told about after the user acts.

## Source Context

- **Type**: blog-post (a "beat" linking to the GitHub release 0.2a0 and a demo video). Read: the post, the GitHub release page, the repo README (Agent integration section), and the linked chat-export gist. Via WebFetch summaries, so exact wording was only available in short fragments.
- **Author credibility**: Simon Willison is the creator of Datasette and the plugin's author; the README and release notes are first-party.
- **Scope**: Covers the agent integration, a `decade` time unit and a line-chart fix. Does not cover production use, evaluation of chart quality, or the video content beyond what the gist shows. The post gives no code or metrics itself.
- **Relationship to prior note**: The triage comments suggested this might be the successor to `datasette-agent-charts`. The post links to `datasette/datasette-charts`, a separate repo from `datasette/datasette-agent-charts`. I did not verify a rename; the 0.2a0 agent integration is exposed via different tool names (`chart`, `suggest_charts`, not `render_chart`), so treat them as distinct packages.

## Extracted Claims

### Claim 1: datasette-charts 0.2a0 integrates with Datasette Agent, giving the agent a tool to draw a chart and a tool to suggest charts
- **Evidence**: GitHub release notes and README Agent integration section.
- **Confidence**: settled (first-party release notes)
- **Quote**: "Now integrates with Datasette Agent."
- **Our assessment**: Capability is opt-in and appears only when both plugins are installed, matching the composable plugin pattern already in the corpus.

### Claim 2: The agent has two tools: `suggest_charts` (column roles plus ranked suggestions) and `chart` (draws a chart from a spec and returns the plotted rows)
- **Evidence**: README Agent integration section; gist transcript shows `suggest_charts` then `chart` calls.
- **Confidence**: emerging (README description plus one transcript)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: A "suggest, then draw" two-step lets the model ground its spec in computed column roles instead of guessing. Returning the plotted rows to the model is the key detail: the model cannot see pixels, so it gets the data behind the chart. This differs from `render_chart` in the earlier note, which took raw SQL and a chart-type enum with no suggestion step.

### Claim 3: The model writes chart specs in the plugin's JSON format, not JavaScript, and gets validation errors back to correct
- **Evidence**: README (per fetch summary): if a spec doesn't fit the data the model receives a list of errors.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Declarative spec plus validate-and-retry feedback is a sound agent-tool pattern; it limits the attack surface (no model-written JS) and gives self-correction.

### Claim 4: The agent learns about the user's panel edits only after the user acts, via the address of the page being sent with the next message
- **Evidence**: README; the demo shows the agent describing a different chart after the user switched tables in the panel.
- **Confidence**: emerging (single demo)
- **Quote**: "the agent is told the address of the page, which holds the chart you are looking at."
- **Our assessment**: The shared state is a URL (page address with chart spec in the fragment), not a live sync channel. The agent is told on the next user message. This is cheap and stateless, but the agent only knows what it can re-derive from the URL.

### Claim 5: Tools run with the chatting user's permissions; charting a table needs `view-table` but not `execute-sql`
- **Evidence**: README Agent integration section.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Contrasts with the `execute-sql` gate on column discovery in the earlier note. Here table charting uses a spec/filter model rather than model-written SQL, so a lower permission suffices; SQL is only written when charting a query.

### Claim 6: Charts in chat are not stored with the conversation; they are redrawn from current data when the conversation is opened
- **Evidence**: README.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Avoids stale or leaked data in saved transcripts and respects current permissions on reopen. Tradeoff: an old conversation may show a different chart than the one the model described.

### Claim 7: The agent noticed a different chart in the panel and described it when asked "what does the chart show?"
- **Evidence**: Blog post demo (video, not text). The gist transcript, however, shows the follow-up `sql_query` filtered on `package = 'datasette'`, not `sqlite-utils`.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Per the gist, the model answered by re-querying with SQL rather than reading the rendered chart. In that part of the transcript it did not read the chart the same way it drew it. Worth noting for anyone designing UI-state awareness: telling the model a URL is not the same as the model seeing the artifact. We could not watch the video, so this reading rests on the gist only.

### Claim 8: Smaller changes: a `decade` time unit for columns spanning centuries, and line charts of data that skips buckets now connect points
- **Evidence**: GitHub release notes.
- **Confidence**: settled
- **Quote**: "New `decade` time unit, suggested for columns spanning centuries where yearly buckets would be too many."
- **Our assessment**: Minor; not guide-relevant except as a chart-rendering fix.

## Concrete Artifacts

```
Tools (datasette-charts 0.2a0 README, Agent integration, via fetch summary):
  suggest_charts  — column roles + ranked chart suggestions
  chart           — draws chart in chat from a spec; returns plotted rows
Both take: database, and one of table | sql | query_name
  table  -> optional filters, e.g. {"state": "CA", "price__gt": "5"}
  query  -> optional params
```

```
Demo prompt (post): Use #stats to show sqlite-utils downloads over time as a chart.
Transcript order (gist 12646fcc...): suggest_charts -> chart (weekly line, downloads summed)
  -> user switches panel -> "what does the chart show?" -> sql_query
State handoff: chart spec URL-encoded in chart_path after "#chart="; widget is a
<datasette-chart> element with a config attribute (source + spec + chart_url).
```

## Cross-References

- **Corroborates**: `blog-simonwillison-datasette-agent-charts.md` (overall): same composable "charting as an optional plugin to datasette-agent" model, with the structured-spec-not-free-text design (its Claims 1, 2, 7).
- **Contradicts**: None identified. The permission difference (`view-table` here vs `execute-sql` in that note's Claim 3) is a conditioning difference: different plugin and different tool design (spec/filters vs SQL), not an opposing claim.
- **Extends**: `blog-simonwillison-datasette-agent-charts.md`: adds suggestion tool, returned-rows feedback, validation errors and human/agent shared chart panel. `blog-simonwillison-datasette-agent-0-5a0-panel.md` for the agent side panel concept (not re-read in depth for this note; see that note for panel details).
- **Novel**: Page-address-as-shared-state between a human UI panel and the agent; stateless chart redraw instead of stored charts; tool returning data rows to the model alongside a visual.

## Guide Impact

- **Chapter 03 (agent tool design)**: Add `suggest_charts` + `chart` as an example of a "suggest, then act" pair where the action tool returns the underlying data to the model and returns validation errors for retry. Anecdotal/emerging; single alpha project.
- **Chapter 04 (permissions / plugins)**: Note that scoping a tool to a declarative spec lets it need a lower permission (`view-table`) than a SQL-writing path (`execute-sql`), alongside the existing note's discovery-query gating.
- **Human/agent shared state (Ch03 or Ch04, if a section exists)**: Cite the URL-on-next-message mechanism as a lightweight option, with the caveat from Claim 7 that the model may not "see" the artifact.

## Extraction Notes

- Thin source: the post is a beat; detail comes from the release, README and gist. All were fetched through a summarizing tool, so quotes are limited to short fragments that the tool returned in quotation marks; the long README sentences are paraphrased in Our assessment rather than quoted.
- The demo video was not watched. The post's "agent noticed the change" claim is from the post's text; the gist suggests the answer came via a fresh SQL query (Claim 7).
- No contradiction issue filed.
- Alpha (0.2a0): tool names and behaviors may change.
