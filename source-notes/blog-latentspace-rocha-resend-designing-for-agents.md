---
source_url: https://latent.space/p/resend/
source_type: blog-post
title: "Designing for Agents — Zeno Rocha, Resend"
author: Zeno Rocha (Resend CEO), interviewed by swyx (Latent Space); show notes by Latent Space
date_published: 2026-11-10
date_extracted: 2026-11-24
last_checked: 2026-11-24
status: current
confidence_overall: anecdotal
issue: "#4927"
---

# Designing for Agents — Zeno Rocha, Resend

> Show notes for an 86-minute podcast give three small, concrete agent-facing practices (a `.md` pricing page, a check on what MCP tool results return, a very large MCP tool surface) plus a vendor-run AEO recommendation figure. The notes have no code, config or methodology.

## Source Context

- **Type**: blog-post (podcast episode page: show notes, chapter list, link to a transcript attachment). The extraction below covers the show-notes prose only.
- **Author credibility**: Zeno Rocha is Resend's co-founder and CEO, so he is first-party on Resend's product but also promotes it. The show notes are written by the Latent Space host, so Rocha's views reach us secondhand. The AEO study is not Rocha's own independent work, and the page does not describe its methodology.
- **Scope**: It covers AEO (answer engine optimization) as distribution, writing docs for machines, MCP tool-count growth and tool-result size, and email-deliverability trade-offs. It gives no code, schemas, SDK or CLI detail, despite chapters titled "CLI, SDKs and craft" and "Writing for machines".

## Extracted Claims

### Claim 1: One AEO study found Claude Code recommending Resend first for email far more often than any alternative, but a later, broader study was more competitive
- **Evidence**: A single study cited in the show notes (figures: 64 of 102 extractable recommendations; SendGrid first 7 times and an alternative 55 times). A later "comprehensive AEO study" is said to show Postmark on top for most models. No methodology, prompts or sample design are given on the page.
- **Confidence**: anecdotal
- **Quote**: "In a recent AEO study, Claude Code picked Resend first in 64 of the 102 email recommendations the researchers could extract."
- **Our assessment**: The figure is a vendor-adjacent, single-study data point and shouldn't be cited as adoption evidence. Of the two studies, the page says the later one "was a bit more competitive, with Postmark coming up top for most models", which shows how unstable the result is across studies and model versions. The useful point is the mechanism: if a user accepts the agent's first pick, the first recommendation captures most of the choice.

### Claim 2: If a developer accepts the agent's patch, the second-choice provider rarely gets tried
- **Evidence**: A rhetorical question from the host, with no data.
- **Confidence**: anecdotal
- **Quote**: "If the developer asks an agent to implement email and accepts the patch, how often does anyone get around to trying the second choice?"
- **Our assessment**: Plausible but unmeasured. It is a hypothesis about agent-mediated selection, not a result.

### Claim 3: A pricing page with a slider is hard for an agent to read, and appending `.md` gives it a table in one request
- **Evidence**: A single example from Resend's pricing page, described by the host. It isn't a spec, and no test of agent accuracy is reported.
- **Confidence**: anecdotal
- **Quote**: "Add \n.md\n to the URL and the agent gets a table it can read in one request."
- **Our assessment**: A cheap, concrete practice: give interactive or visual pages a plain-markdown variant. It matches the content-negotiation idea in `blog-simonwillison-mcp-constrained-agent-value.md` (Claim 12). The page itself says nothing about how well agents read the result. (Quote text collapses the page's inline-code formatting around `.md`; the passage reads "Add `.md` to the URL and the agent gets a table it can read in one request.")

### Claim 4: Check whether a model knows your product, and whether it can answer a customer's question from your pricing table
- **Evidence**: The host's suggestion, tied to a mention of a previous Supabase interview. No procedure or data.
- **Confidence**: anecdotal
- **Quote**: "You can ask whether a model has heard of your product."
- **Our assessment**: A cheap smoke test for agent-readability of docs. Treat it as a practice to try, not a validated one.

### Claim 5: Resend's MCP server grew from roughly 20 tools or fewer at launch to more than 80, aiming at parity with the dashboard
- **Evidence**: Self-reported by the show notes; no tool list on the page.
- **Confidence**: anecdotal
- **Quote**: "When we recorded, Resend’s MCP server had grown from roughly 20 tools or fewer at launch to more than 80."
- **Our assessment**: A real-world data point that a vendor chose a large tool surface for dashboard parity, in contrast with the "two tools" Code Mode design. The page doesn't report any effect on model tool-selection quality, so it is evidence of what was built, not of whether it works well.

### Claim 6: The goal of the large MCP surface is to let a chat-client user do whatever they can do in the dashboard
- **Evidence**: Rocha's stated intent as relayed by the host.
- **Confidence**: anecdotal
- **Quote**: "Sending an email gets the demo working. Inviting a teammate, checking usage and managing billing account for some of the long tail."
- **Our assessment**: Useful framing: the demo path is the few core tools, and the long tail drives tool count. It is a product choice, not an engineering result.

### Claim 7: Tool count is not necessarily the real context cost; an oversized tool result can be the problem, and cutting tools wouldn't shrink it
- **Evidence**: An anecdote of Rocha opening collapsed tool calls in his own sessions and finding one result too large to fit in context.
- **Confidence**: anecdotal
- **Quote**: "Reducing the tool count wouldn’t by itself make that response any smaller."
- **Our assessment**: The most reusable claim here. It gives a cheap diagnostic: expand the result of a call you make every day and see how much the model uses. It stands next to the guide's tool-count concerns (see `blog-anthropic-seeing-like-an-agent.md`, Claim 11) as a second axis, result size, which tool-count debates tend to ignore. It is a single anecdote with no measurement.

### Claim 8: Cloudflare's Code Mode exposes a whole API through two tools, `search()` and `execute()`, as a contrast to an 80-tool design
- **Evidence**: A host reference to Cloudflare's Code Mode server; not analysed on the page.
- **Confidence**: emerging (the pattern is documented elsewhere in the corpus; this page only mentions it)
- **Quote**: "The design looks especially interesting alongside \nCloudflare’s Code Mode server\n, which exposes its API through two tools, \nsearch()\n and \nexecute()\n."
- **Our assessment**: A pointer only. The substance lives in `blog-ronacher-what-is-codemode.md`. The page doesn't say which design Rocha prefers.

### Claim 9: Shared click-tracking domains let one tenant's abuse (phishing, blocklisting) harm other tenants' legitimate email, so Resend introduced custom tracking domains
- **Evidence**: The host's explanation of Rocha's reasoning; no deliverability data.
- **Confidence**: anecdotal
- **Quote**: "If one customer uses that domain for phishing and it gets blocklisted, links in another customer’s perfectly legitimate emails can suffer too."
- **Our assessment**: A general multi-tenant-isolation lesson, only loosely related to AI-native engineering. Include only if a chapter covers operational trade-offs.

### Claim 10: A developer-first wedge (React Email) put the vendor's code in the repo before the buying decision, ahead of any agent
- **Evidence**: Resend's own history as told by the host.
- **Confidence**: anecdotal
- **Quote**: "By the time a developer needed a different provider, some of Resend’s code was already in the repo."
- **Our assessment**: An illustration of pre-agent distribution, probably out of scope for the guide. It suggests the agent's recommendation is influenced by what's already in the codebase, but the page doesn't test that.

## Concrete Artifacts

```
Artifacts available on the page (no code, config or schema is shown):
- AEO figures (Latent Space show notes, 2026-11-10): Claude Code picked Resend
  first in 64 of 102 extractable email recommendations; SendGrid first 7 times,
  present 55 times as an alternative. Later study: Postmark top for most models.
- Resend MCP tool count: ~20 or fewer at launch -> more than 80 (as of recording).
- Practice: append `.md` to a pricing-page URL to get an agent-readable table.
- Diagnostic: expand the result of a tool call you make every day; check how
  much of it the model actually uses.
- Show-note link: "Anthropic on writing tools for agents" (returning less data
  when a result fills the context window).
```

## Cross-References

- **Corroborates**: `blog-anthropic-seeing-like-an-agent.md` (Claim 11: the tool surface is a cost; this page adds that result size is a separate cost). `blog-simonwillison-mcp-constrained-agent-value.md` (Claim 12: machine-readable docs served over plain HTTP, here a `.md` URL suffix).
- **Contradicts**: None filed. The 80-tool MCP surface is a different design choice from Claude Code's roughly 20 tools (`blog-anthropic-seeing-like-an-agent.md`, Claim 11) and from Code Mode's two tools, but the page makes no claim that opposes either. This is context (dashboard parity vs coding-agent tools), so I did not file a contradiction.
- **Extends**: `blog-ronacher-what-is-codemode.md` (Claims 4 and 8, on keeping tool results and discovery out of the model's context) with a vendor example of the large-surface alternative. `blog-latentspace-modal-agent-experience.md` (Claim 3, the agent-experience framing) with a second vendor's AX practices.
- **Novel**: Agent-recommendation share (AEO) as a distribution concern, and the "inspect result size before cutting tool count" diagnostic. Neither appears in the notes I checked.

## Guide Impact

- **Chapter 02 (harness / tool design)**: When discussing MCP tool count, add a caveat that tool count and result size are separate context costs, and suggest inspecting actual tool results first. Cite this note as a single-anecdote, vendor-sourced data point and pair it with `blog-anthropic-seeing-like-an-agent.md`.
- **Chapter 04 (context engineering)**: Optionally mention oversized tool results as a context-budget failure that fewer tools won't fix. Evidence is anecdotal; hedge accordingly.
- **Agent-facing docs (whichever chapter covers it)**: A markdown variant of interactive pages (`.md` on a pricing page) is a low-cost practice; label it unvalidated.
- **Do not cite** the 64/102 AEO figure as adoption evidence in the guide.

## Extraction Notes

- The page is show notes (about 900 words) plus a chapter list. The full transcript is a separate attachment (`Resend - Zeno Rocha - Transcript.txt`), and I could not fetch it: the host's transcript link returned a Cloudflare challenge. The chapters "Designing the MCP" (37:55), "Writing for machines" (58:28) and "Winning recommendations" (1:06:00) likely hold more detail and are not covered here. A re-mine with transcript access would be worthwhile.
- Claims describe what the host wrote about Rocha, not Rocha's own words, so the quotes are the host's text. Two quotes (Claims 3 and 8) cross inline-code or link markup in the page, which is why the text is split across lines; the plain-text meaning is as stated.
- The Prospector flagged the AEO figures as vendor-sourced and unverified; I kept them as anecdotal.
