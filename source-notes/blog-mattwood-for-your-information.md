---
source_url: https://mattwood.blog/essays/2026/08/for-your-information/
source_type: blog-post
title: "For Your Information"
author: Matt Wood (Chief AI & Technology Officer, AWS)
date_published: 2026-08-01
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: emerging
issue: "#2647"
---

# For Your Information

> Matt Wood (AWS Chief AI & Technology Officer) announces FYI (mattwood.fyi), a
> personal knowledge graph built explicitly for dual human-and-agent consumption —
> a public, no-auth JSON Feed, Atom feed, `llms.txt`, and a REST query API over a
> typed item/edge graph — arguing that the valuable output of following a
> fast-moving field is curated judgment (a tacit, hard-to-write-down skill) rather
> than raw aggregation, and that exposing the *reasoning* and *connections* behind
> that judgment, not just conclusions, is what makes a personal feed useful to
> both readers and their agents.

## Source Context

- **Type**: blog-post (personal essay site, `mattwood.blog`, "essays" collection;
  short-form, single-author, no comments or citation infrastructure; ~700 words
  in the announcement essay itself). Unlike this author's four other essays
  already in the corpus (`blog-mattwood-how-this-was-made.md`,
  `blog-mattwood-barcode-bargain.md`, `blog-mattwood-field-and-frontier.md`,
  `blog-mattwood-half-life-assumption.md`), this essay announces and links to a
  live, independently verifiable artifact — the mattwood.fyi site itself — so
  this extraction followed that artifact directly (its homepage, `/agents/`,
  `/about/`, `/colophon/`, `/llms.txt`, and `/feed.json`) rather than relying
  solely on the essay's own description of it.
- **Author credibility**: Matt Wood is AWS's Chief AI & Technology Officer,
  having returned to AWS in 2026 after nearly 15 years there earlier in his
  career and, most recently, leading commercial technology and innovation at
  PwC (per `https://mattwood.blog/about/`, re-fetched for this extraction — bio
  text is byte-identical to the version quoted in all four sibling notes). He
  holds a PhD in machine learning and did a postdoctoral fellowship in
  NLP/bioinformatics at Weill Cornell Medicine. As with the sibling essays, this
  is a `trusted-feed` source that already passed an author-worth-listening-to
  bar. Unlike those essays (pure argument/analogy pieces with zero external
  citations), this source's central claims about *how the system is built* are
  independently checkable — this note fetched the live site and confirmed the
  JSON Feed schema, the query API's actual endpoints, and the site's build
  architecture directly, rather than relying on the essay's self-report alone.
- **Scope**: Covers the announcement's stated motivation (why volume alone
  doesn't help you follow AI; filtering/judgment as the scarce skill), the
  dual-audience design (human reader vs. agent), the specific machine-readable
  channels (JSON Feed, Atom feed, `llms.txt`, query API), the "attention feed
  vs. finished-thoughts feed" framing, the cross-feed-comparison idea, and (via
  direct verification of the linked site) the concrete API surface, item/edge
  graph data model, copy-paste agent-context block, and serverless build
  architecture. Does NOT cover: any usage data for the site (it launched
  2026-08-01, this extraction is eleven days later), any named user or agent
  that has actually queried it, or any comparison to other agent-readable
  content standards (e.g. `llms.txt`'s originating spec, MCP, or RSS) — the
  essay and site treat `llms.txt` and the JSON Feed format as given tools, not
  as choices being argued for over alternatives.

## Extracted Claims

### Claim 1: Following a fast-moving field well is primarily a filtering/judgment problem, not a coverage problem — and that judgment is a form of tacit knowledge that can't be fully written down but can be demonstrated through what it produces
- **Evidence**: Author's own first-person reflection on his AI-reading practice, generalized into the essay's motivating claim.
- **Confidence**: anecdotal (single practitioner's self-report on his own information-processing habits, no survey or measurement)
- **Quote**: "I read about AI constantly. It's the center of my work. Over time, I noticed something: the most useful thing I was doing wasn't cataloguing everything, it was filtering. Deciding what felt important, what felt surprising, what felt like it connected to something I'd seen three months ago. [...] That judgment is partly tacit knowledge: understanding built through experience. You can't simply write it all down, but you can show more of what it produces: the things you notice, the connections you make, and the evidence that changes your mind."
- **Our assessment**: This is the essay's foundational claim and the reason FYI is built as a feed of connections rather than a search index or a links-only digest. It reframes "personal knowledge graph" not as an information-storage problem but as an externalization-of-judgment problem — you can't transfer the tacit skill directly, so you expose its outputs (what got flagged, what got linked, what changed a prior view) as a proxy. This is a sharper, more specific claim than generic "curation beats volume" advice.

### Claim 2: A feed of someone's ongoing attention (what they notice, question, and revise) is more valuable than a feed of only their finished, polished conclusions
- **Evidence**: Author's own definitional argument for what FYI is trying to be, contrasted explicitly with the long-form essays on the same author's other site.
- **Confidence**: anecdotal (asserted design principle, not tested against reader/agent behavior)
- **Quote**: "That's what I'm trying to do with FYI: a curated, connected record of what I'm actually paying attention to and why. A feed of someone's attention is often more interesting than a feed of their finished thoughts. When I link two things together, or flag something as challenging an idea I'd previously found convincing, that relationship is part of the record too."
- **Our assessment**: This is the essay's clearest statement of *why* the graph's edges (not just its nodes) are the valuable artifact — a "challenges" link between two items is itself content, not metadata. It directly parallels this same author's `blog-mattwood-how-this-was-made.md` Claim 2/3 diagnosis that organizations share finished outputs but almost never share process (see Cross-References) — here applied to personal knowledge curation rather than organizational AI-adoption spreading, but making structurally the same "process/reasoning is the valuable, usually-hidden thing" argument.

### Claim 3: Connecting a curated feed to an agent lets that agent combine it with the reader's own notes and context to surface connections the reader wouldn't otherwise have had reason to look for
- **Evidence**: Author's own stated use case for the agent integration, with an illustrative example query.
- **Confidence**: anecdotal (illustrative use case, not a demonstrated or measured agent interaction)
- **Quote**: "Your agent can combine my feed with your own notes and context to surface connections you wouldn't otherwise have reason to look for: something I flagged last week that relates to what you're working on now, shifts in how I read a topic over time, or answers to questions like \"has anyone in my feeds changed their mind about agents recently, and why?\""
- **Our assessment**: This is the essay's positive case for *why* agent access matters beyond convenience — it's not "read my blog faster," it's cross-referencing the author's judgment against the reader's private context, which neither party could do alone without the other's data being both accessible and structured enough to query. The claim is aspirational (no worked example is given), but the site's actual query API (Concrete Artifacts, below) is built specifically to support exactly this kind of query.

### Claim 4: A knowledge feed intended for agent use must be public, require no authentication or API key, and expose its structure through multiple redundant machine-readable channels — because "the agent part only works if your agent can actually read the site"
- **Evidence**: Author's own design requirement, followed by the specific channel list (JSON feed, `llms.txt`, query API).
- **Confidence**: emerging (a stated design principle that this extraction independently verified against the live site — all listed endpoints returned HTTP 200 with no authentication)
- **Quote**: "The agent part only works if your agent can actually read the site, so FYI is built for agents as deliberately as it is for people. Everything is public and machine-readable, with no account or API key required. There’s a structured JSON feed, an llms.txt file, and a small query API over the graph itself: search it, pull what’s new, or follow the connections around any idea."
- **Our assessment**: This is the essay's most directly actionable design principle for anyone building agent-consumable content, and it is independently confirmed rather than merely asserted: this extraction fetched `mattwood.fyi/feed.json`, `mattwood.fyi/llms.txt`, and several `/api/fyi/q/*` endpoints directly and found all of them public and unauthenticated. It's a concrete counterpoint to "agent-readable" systems that gate access behind a portal, login wall, or rate-limited key — the design bet here is that removing every access-friction point is what makes "give your agent this URL" viable as a distribution mechanism at all.

### Claim 5: Some agent HTTP-fetch tools strip query-string parameters that look like IDs, so a public API meant for agent consumption should expose path-based endpoint variants as the preferred form, with query-string variants as fallback
- **Evidence**: Explicit operational note in the site's own agent-instructions document, addressed to the agents consuming the API, not to human readers.
- **Confidence**: emerging (a specific, checkable engineering claim about agent tool behavior, stated as the reason for a concrete API design choice — this extraction did not independently test which specific agent tools strip query strings, but the design response is directly verifiable in the API surface itself)
- **Quote**: "Note: some agent fetch tools strip query-string parameters that look like IDs. If query-string endpoints fail, use the path-based alternatives (preferred)."
- **Our assessment**: This is the single most concrete, novel-to-the-corpus engineering lesson in the source — a specific, named agent-tooling failure mode (query-string stripping) and a specific mitigation (offer both `GET /api/fyi/q/search/KEYWORD` and `GET /api/fyi/q/search?q=KEYWORD`, with the path form documented as preferred). This is a harness/API-design consideration that generalizes beyond this one site: any REST API intended for agent consumption should not assume query-string parameters survive the agent's fetch tool unmodified.

### Claim 6: The site's data model treats items as typed (riff / link / essay) and connects them via directional, typed, reasoned graph edges — not a flat chronological list
- **Evidence**: The site's own agent-instructions document and query-API documentation, describing item types and edge query parameters directly.
- **Confidence**: emerging (directly observed in the live API surface and JSON Feed schema, not merely asserted in prose)
- **Quote**: "Get all graph connections for a specific item. Returns edge type, direction (incoming/outgoing), confidence, and reason. Add ?type=challenges (or supports, develops_into, related_to) to filter."
- **Our assessment**: This is a concrete, inspectable data model (item types: riff/link/essay; edge types: challenges/supports/develops_into/related_to; edges carry direction, confidence, and a stated reason) rather than an abstract "knowledge graph" claim. It substantiates Claim 2's assertion that relationships are first-class content — the API literally exposes "why is this connected to that" as a queryable field, not just "these two things are related."

### Claim 7: Comparing multiple people's curated feeds side by side is presented as more valuable than reading any single feed alone, analogous to comparing notes with colleagues after reading the same source
- **Evidence**: Author's own closing argument for why he frames this as a multi-feed ecosystem rather than a single product.
- **Confidence**: anecdotal (aspirational framing, no second comparable feed exists yet in the essay's own account)
- **Quote**: "You can also set feeds like this alongside each other, comparing perspectives across people the way you might compare notes with colleagues after reading the same article. And that's the idea I'm most excited about. My perspective here is just one view, and it becomes more useful sitting next to yours, or next to someone else whose read on AI you've always found sharp."
- **Our assessment**: This extends Claim 3's single-feed-plus-your-context use case to a multi-feed comparison use case, but it's the essay's most speculative claim — it describes value that depends on other people publishing comparable feeds an agent can cross-reference, which does not yet exist per this essay's own account. Worth flagging in the guide as the aspirational, unproven half of the pitch, distinct from the already-working single-feed query API (Claims 4-6).

### Claim 8: FYI explicitly models itself on early-2000s personal/link-blogging practice (Swiss Miss, Daring Fireball, and others), treating that era's "short, associative, personal feeds of attention" as a precedent now being adapted for agent consumption
- **Evidence**: Author's own historical framing in the essay's postscript, naming specific blogs.
- **Confidence**: anecdotal (historical analogy, unsourced beyond the author's own characterization of those sites' style — consistent with how this author's other essays use unsourced historical analogies, e.g. the barcode and nautical-chart essays)
- **Quote**: "PS: The blogs of the early internet were doing something like this long before \"knowledge graph\" was a phrase anyone used. Microblogs from Swiss Miss, Daring Fireball, Marcel Molina, Jason Kottke, and others were onto exactly this twenty years ago: short, associative, personal feeds of attention rather than conclusions. That spirit is very much what FYI is trying to be, for the agentic age."
- **Our assessment**: This is a framing device, not a technical claim, but it's a useful positioning statement for the guide: FYI is explicitly *not* pitched as a novel content format, but as an old content format (the tumblelog/link-blog) re-plumbed with agent-readable channels. This is consistent with the site's own `/colophon` page, which independently states "Plain HTML, no JavaScript... No analytics, no tracking, no cookies" — deliberately low-tech on the human-facing side even as the agent-facing side gets a purpose-built API.

### Claim 9: FYI is explicitly framed as an unfinished experiment whose form is expected to change based on what people and their agents actually find useful, rather than a settled product
- **Evidence**: Author's own closing framing, repeated in two places in the essay.
- **Confidence**: anecdotal (stated intent, not yet tested against any usage data at the time of this extraction — the site launched 2026-08-01, eleven days before this extraction)
- **Quote**: "That's what I'm hoping to find out: whether connected perspectives can help people think better about a fast-moving field. The form will almost certainly change as I learn what people and their agents actually find useful. That is part of the experiment too."
- **Our assessment**: This directly bounds how much weight the guide should put on FYI as a finished pattern to imitate — the author himself frames it as provisional. The guide should cite the concrete, already-built mechanisms (Claims 4-6: public no-auth access, path-based endpoint robustness, typed item/edge model) as verifiable engineering choices worth reusing, while treating the higher-level claims about value (Claims 3, 7, 9) as an open, self-acknowledged experiment rather than a validated outcome.

## Concrete Artifacts

### Agent access channels (as stated in the essay and independently verified against the live site)

```
Source: Matt Wood, "For Your Information," mattwood.blog, 2026-08-01
(https://mattwood.blog/essays/2026/08/for-your-information/), cross-checked
against mattwood.fyi directly by this extraction (all fetched 2026-08-12,
all returned HTTP 200, no authentication required)

- JSON Feed (recommended for agents): https://mattwood.fyi/feed.json
  - Standard JSON Feed 1.1 with a `_fyi` extension object per item
- Atom Feed (full HTML content): https://mattwood.fyi/feed.xml
- Agent instructions: https://mattwood.fyi/agents/
- llms.txt: https://mattwood.fyi/llms.txt
- Individual item permalinks: https://mattwood.fyi/i/{id}
```

The full query API endpoint list (search, semantic search, items, edges,
summary) is reproduced verbatim below as part of the site's own
"Instructions for Your Agent" document — see the next artifact block — rather
than paraphrased here, to avoid any non-verbatim restatement of API syntax.

### The "Instructions for Your Agent" copy-paste context block (verbatim excerpt, fetched directly from `mattwood.fyi/agents/`)

```
Source: "Instructions for Your Agent," mattwood.fyi/agents/ (fetched 2026-08-12)
This is a live document the site generates for users to paste into their own
agent's context; the version below was current as of this extraction.

# Context: Matt Wood's FYI (mattwood.fyi)

[... "## Who is Matt Wood?" section omitted here — a short, differently-worded
bio paragraph than the mattwood.blog/about bio quoted in this note's Source
Context; it names his AWS CAIO role and customer-facing work but omits the
PhD/medical-school/Weill Cornell details the blog bio includes ...]

## What is this site?

mattwood.fyi is his FYI — a live list of riffs and links drawn from what
he's reading, noticing, questioning, concluding, and revising. It sits
between the long-form essays on mattwood.blog and the silence between them.

Three types of items:

- **riff**: A self-contained idea, distinction, analogy, reaction, or small
  argument. These are Matt's own thinking — not summaries of other people's
  work.
- **link**: An external source accompanied by original commentary explaining
  why it matters, what to notice, or how it changes the picture. Never a
  naked URL.
- **essay**: A pointer to a newly published mattwood.blog essay. The essay
  remains canonical on the blog; FYI carries the thesis, context, and
  relationship to recent items.

[... "## How to access this site" section omitted here — its channel list is
reproduced above in the "Agent access channels" artifact block ...]

## Query API (public, no auth required)

For structured queries against the knowledge graph, use these REST endpoints.
All are public, no authentication required. All return JSON.

Note: some agent fetch tools strip query-string parameters that look like IDs.
If query-string endpoints fail, use the path-based alternatives (preferred).

### Search
- GET https://mattwood.fyi/api/fyi/q/search/KEYWORD (preferred, path-based)
- GET https://mattwood.fyi/api/fyi/q/search?q=KEYWORD
  Search items by keyword in title and content. Returns matching items with permalinks.

### Semantic Search
- GET https://mattwood.fyi/api/fyi/q/semantic/NATURAL+LANGUAGE+QUERY (preferred, path-based)
- GET https://mattwood.fyi/api/fyi/q/semantic?q=QUERY
  Search by meaning, not keywords. Uses vector embeddings to find semantically similar items.
  Returns items ranked by similarity score (0-1). Use this for natural language questions.

### Items
- GET https://mattwood.fyi/api/fyi/q/items?since=YYYY-MM-DD&type=link|riff|essay&limit=N
  List items filtered by date and/or type. Defaults to most recent 25.

### Edges (connections)
- GET https://mattwood.fyi/api/fyi/q/edges/SHORT_ID (preferred, path-based)
- GET https://mattwood.fyi/api/fyi/q/edges?itemId=SHORT_ID
  Get all graph connections for a specific item. Returns edge type, direction (incoming/outgoing), confidence, and reason.
  Add ?type=challenges (or supports, develops_into, related_to) to filter.

- GET https://mattwood.fyi/api/fyi/q/edges?type=challenges
  Get ALL edges of a specific type across the whole graph.

### Graph summary (snapshot)
- GET https://mattwood.fyi/api/fyi/q/summary
  Pre-computed snapshot: top connected items, recent activity, edge type distribution, and all tension pairs.
  Includes a generated_at timestamp. This is a point-in-time snapshot computed at last site rebuild —
  if generated_at is stale, prefer the live endpoints above for current data.

## How to answer common questions
- "What is Matt reading about X?" → /api/fyi/q/semantic/X (semantic) or
  /api/fyi/q/search/X (keyword)
- "What changed this week?" → /api/fyi/q/items?since=YYYY-MM-DD (7 days ago)
- "What challenges idea Y?" → search for Y, get its shortId, then
  /api/fyi/q/edges/SHORT_ID
- "Where are signals converging?" → /api/fyi/q/summary gives top connected
  items
- "What are the tensions?" → /api/fyi/q/edges?type=challenges returns all
  challenge relationships with reasons
- "What connects A to B?" → get edges for both items and look for shared
  connections

[... "## Recent items" section omitted here — a ten-item list of the site's
most recent entries as of the fetch timestamp below, not reproduced since it
is simply the ten most recent items visible on the live homepage at fetch
time ...]

## What should you do with this?
- Answer questions about what Matt is currently thinking about
- Surface relevant items when a user asks about topics he's covered
- Quote and cite — every item has a stable permalink, use it
- Notice patterns across items (recurring themes, evolving positions)
- Go deeper — if a user asks about something adjacent, fetch the relevant
  item and read it rather than guessing
- Be honest about gaps — if he hasn't written about something, say so
  rather than extrapolating
- Fetch the JSON feed for the latest; don't rely solely on this static page

[... "## Canonical source" section omitted here — a short paragraph stating
mattwood.fyi is authoritative for short-form thinking and mattwood.blog for
long-form essays, both accessible without authentication ...]

## Updates
This context block was generated on 2026-08-12 at 15:49 UTC. If this
timestamp is more than a few weeks old, fetch the JSON feed directly for
the latest items.
```

### JSON Feed item schema (sample item, fetched directly from `mattwood.fyi/feed.json` by this extraction, 2026-08-12)

```json
{
  "id": "ef7de84c-15c3-4ab8-9b65-af6f0995b50c",
  "content_text": "> AI tools are accelerating development velocity without guardrails, causing projects with weak engineering practices to accumulate technical debt at unsustainable rates and collapse into unmaintainable systems that no one understands.",
  "date_published": "2026-08-12T15:49:01.412051+00:00",
  "_fyi": {
    "type": "link",
    "tags": []
  },
  "title": "AI is removing the middle class of software engineering",
  "url": "https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html",
  "external_url": "https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html"
}
```

### Site build architecture (verbatim from `mattwood.fyi/colophon/`, fetched directly by this extraction, 2026-08-12)

```
Source: "Colophon," mattwood.fyi/colophon/ (fetched 2026-08-12)

## How it's built
- Storage: DynamoDB for items, S3 for static hosting
- Compute: A single Python Lambda handles the API and regenerates the
  entire static site on every publish
- Editor: A bespoke single-page app for quick capture — optimized for
  riffs (ideas), links (sources + commentary), and essay pointers
- CDN: CloudFront
- Feeds: Atom (feed.xml) for humans, JSON Feed 1.1 (feed.json) for agents
- Agent context: /llms.txt provides structured instructions for AI agents
  to connect to the feed

## Design principles
- Plain HTML, no JavaScript (except the random page redirect)
- Dark mode via prefers-color-scheme
- Every item gets a stable permalink
- Dual audience: readable by humans, parseable by agents
- No analytics, no tracking, no cookies

## Tools
- Written and published using a custom editor built with Claude, Kiro,
  and AWS Lambda
- Site generation: Python, markdown library
- Infrastructure: AWS (Lambda, DynamoDB, S3, CloudFront, API Gateway)
```

## Cross-References

- **Corroborates**:
  - `blog-mattwood-how-this-was-made.md` (same author) Claim 2 ("Organizations
    share outputs constantly: decks, memos, reports, analysis. They almost
    never share process. The finished document moves from inbox to inbox. How
    it was made stays invisible.") and Claim 3 (invisible process has a
    specific cost — people don't update their sense of what's possible, or
    quiet use becomes the norm): this essay's Claim 2 ("A feed of someone's
    attention is often more interesting than a feed of their finished
    thoughts") makes the structurally identical argument — that the
    reasoning/process behind a conclusion is the valuable, usually-hidden
    artifact — applied to personal knowledge curation for readers and agents
    rather than to organizational AI-adoption spreading. Two applications of
    the same underlying design principle by the same author, three weeks
    apart, strengthens the case that "expose process, not just conclusions"
    is a load-bearing idea across this author's thinking generally, not a
    one-off essay device.
  - `blog-langchain-human-judgment-improvement-loop.md` Claim 1 ("The most
    critical organizational knowledge is tacit — it lives in employees' minds
    and is not documented, making explicit extraction from domain experts
    necessary to build reliable agents"): this essay's Claim 1 (personal
    curation judgment is "partly tacit knowledge: understanding built through
    experience. You can't simply write it all down, but you can show more of
    what it produces") makes a related but distinctly-scoped claim — LangChain's
    note is about extracting tacit knowledge *from* domain experts *into* an
    agent's workflow/tool/context design at build time; this essay is about a
    single person's ongoing curation practice, where the tacit judgment stays
    with the human and only its *outputs* (flags, links, revisions) are
    exposed for an agent to read at query time. Both independently identify
    "judgment/expertise resists direct transcription, so expose what it
    produces instead" as the workable move, from different domains (enterprise
    agent-building vs. personal information curation).
  - `blog-mattwood-half-life-assumption.md` (same author) Claim 8 (record
    *why* a decision was made, as testable conditions, not only *what* was
    decided): a parallel instance of this author's recurring argument that
    recording reasoning, not just outcomes, is the mechanism that makes
    knowledge reusable later — applied there to organizational decisions with
    testable trigger conditions, and here (Claim 6) to graph edges that carry
    an explicit stated `reason` field alongside their type and confidence.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  existing corpus note argues that agent-facing content systems should be
  gated behind authentication, or that raw aggregation without curation is
  preferable to filtered judgment, so this essay's central claims do not
  conflict with prior source notes. No contradiction issue filed.

- **Extends**:
  - `failure-htdt-godogen-game-generation.md` Lesson 2 ("Lazy-loading large
    API reference corpora is necessary for context-window-constrained code
    generation") and Recovery 1 ("Custom API Reference Corpus with
    Lazy-Loading" — a GDScript API/quirks corpus queried on demand via an
    isolated skill context rather than injected upfront), which is the source
    behind the guide's existing Chapter 04 "Pre-Session Corpus Loading for
    Low-Coverage Domains" section: this essay's query API (Claim 6, and the
    Concrete Artifacts endpoint list) is the same "external, queryable-on-demand
    corpus rather than upfront context injection" pattern, generalized from a
    static API/language reference to a continuously updated personal
    knowledge feed — an agent calls `/api/fyi/q/semantic/{query}` on demand
    rather than the whole feed being loaded into context upfront, which is
    exactly the lazy-load discipline Lesson 2 recommends, applied to a
    different kind of external reference material.
  - `practitioner-getsentry-sentry.md` (Chapter 02, "External Skill
    Repositories" / "Production Data as Agent Skills"): that note documents
    pulling structured, versioned skill content from external repositories
    into an agent's context. This essay's site is a different shape of
    external agent-consumable resource — not a skill/instruction repository
    but a continuously updated personal knowledge feed — but shares the same
    underlying design bet that machine-readable, purpose-built external
    endpoints (not a general-purpose webpage an agent has to scrape) are what
    make third-party content usable by an agent harness.

- **Novel**:
  - The specific, named agent-tooling failure mode and mitigation in Claim 5
    (some agent fetch tools strip query-string parameters that look like IDs;
    offer path-based endpoint variants as the preferred form) — new to the
    corpus. No existing source note documents this particular API-design
    consideration for agent-consumed REST endpoints.
  - The typed item / typed-and-reasoned graph edge data model (Claim 6: riff/
    link/essay item types; challenges/supports/develops_into/related_to edge
    types, each carrying direction, confidence, and a stated reason) — a new,
    concrete worked example of representing "why two things are connected" as
    first-class, queryable API data, distinct from the corpus's existing
    knowledge-graph or memory discussions.
  - "Filtering is the scarce skill, and it is tacit knowledge you demonstrate
    through its outputs rather than write down directly" (Claim 1) as an
    explicit framing for why a curated feed's *connections*, not just its
    *contents*, are the thing worth publishing — new vocabulary for the
    corpus's existing tacit-knowledge material (`blog-langchain-human-judgment-improvement-loop.md`,
    `blog-anthropic-human-agent-teams.md`).
  - The concrete no-auth, multi-channel (JSON Feed + Atom + `llms.txt` +
    REST API) redundant-access design for a single-person content source
    (Claim 4) — the corpus's first worked example of what "build this so an
    agent can actually read it" looks like end-to-end for a personal
    (non-enterprise, non-product) knowledge source.

## Guide Impact

- **Chapter 04 (Context Engineering) — "Pre-Session Corpus Loading for
  Low-Coverage Domains" section**: This section currently documents one
  case (a GDScript API/quirks corpus, lazy-loaded via an isolated skill
  context) of an external reference an agent queries on demand rather than
  loading upfront. Add this source's query API design (Claim 6 and the
  Concrete Artifacts endpoint list — semantic search, edge lookups, a
  pre-computed summary snapshot) as a second, independently-sourced example
  of the same on-demand-query-over-upfront-injection discipline, applied to
  a continuously updated personal knowledge feed rather than a static
  language reference. This broadens the pattern from "niche framework docs"
  to "any external, larger-than-context-budget knowledge source an agent
  needs to consult selectively."

- **Chapter 02 (Harness Engineering) — new subsection, or an addition to
  "Skills and External Config"**: Add Claim 5 (some agent HTTP-fetch tools
  strip query-string parameters that look like IDs; offer path-based REST
  endpoint variants as the preferred form, with query-string variants as
  fallback) as a specific, actionable API-design rule for anyone building a
  REST endpoint meant to be called by an agent's fetch/`curl`-style tool.
  This is a concrete, previously undocumented failure mode in the corpus and
  a cheap mitigation — worth stating explicitly rather than leaving teams to
  rediscover it independently.

- **Chapter 04 (Context Engineering) — "Tool Choice and Context Cost"
  section**: Add Claim 4 (public, no-auth, multi-channel machine-readable
  access — JSON Feed, Atom, `llms.txt`, REST API — as the precondition for
  "your agent can actually read this") as a design principle for teams
  publishing any external content source intended for agent consumption:
  authentication and API-key requirements are a hard blocker for casual
  agent access in a way they are not for a human clicking through a login
  flow once. Pair with Claim 6's typed-item/typed-edge data model as a
  concrete worked example of what "machine-readable" should mean beyond
  "returns JSON" — types, relationships, and stated reasons for those
  relationships, not just a flat content dump.

## Extraction Notes

1. **WebFetch's summarizing model paraphrased rather than quoted verbatim**
   on the first attempt (asked to "return the FULL text content... verbatim"
   of the essay, it returned a restructured, headed, and reworded summary —
   e.g. rendering "the most useful thing I was doing wasn't cataloguing
   everything, it was filtering" as a quoted fragment inside an otherwise
   paraphrased passage, and inventing section headings like "Key Concept" and
   "Design Philosophy" that do not exist in the source). Per MINER.md §2a,
   this note does not rely on that WebFetch output for any quote. The full
   essay HTML was instead retrieved directly via `curl` with a browser
   user-agent (HTTP 200) and quoted character-for-character from that raw
   text, consistent with the method documented in all four sibling
   `blog-mattwood-*` notes.
2. Unlike the sibling essays, this source describes and links to a live,
   independently checkable system. Per MINER.md §1's "follow up to 5 linked
   pages that seem substantive" guidance, this extraction followed the
   essay's link to `mattwood.fyi` and, from there, `/agents/` (the agent
   instructions and query-API documentation — the single most substantive
   page for this source's actual claims), the homepage (to observe real feed
   items and confirm the nav structure), `/about/`, `/colophon/` (build
   architecture), and directly fetched `/llms.txt` and `/feed.json` (not
   HTML pages, but the actual data artifacts the essay and `/agents/` page
   both name as primary access channels — fetching them was necessary to
   verify Claim 4 and Claim 6 rather than take the essay's description on
   faith). All fetches were direct `curl`/HTTP requests with a browser
   user-agent, made on 2026-08-12, and all returned HTTP 200 (or a 302 to a
   trailing-slash canonical URL, followed to 200) with no authentication.
3. The site's `/agents/` page states its "Instructions for Your Agent"
   context block "was generated on 2026-08-12 at 15:49 UTC" — the same day
   as this extraction — and explicitly warns that if that timestamp is more
   than a few weeks old, the JSON feed should be fetched directly instead.
   The Concrete Artifacts excerpt of that block above should be understood
   as a snapshot as of this extraction date, not a permanently stable
   document; the site's own design intent (per Claim 9) is that its content
   and even its instructions-to-agents will keep changing.
4. This note did not attempt to verify Claim 5's premise (that some
   unspecified agent fetch tools strip ID-like query-string parameters)
   against any specific tool's actual behavior — the claim is reported as
   the site operator's own stated engineering rationale for the API's
   path-based endpoint design, not independently reproduced by this
   extraction.
5. No contradiction issues filed. This essay's claims (agent-readable
   content should be public and unauthenticated; curated judgment beats raw
   aggregation; process/reasoning is more valuable than isolated conclusions)
   were checked against the corpus for any note arguing the opposite; none
   was found — see Cross-References → Contradicts.
6. `confidence_overall` is rated `emerging`, one step above this author's
   four sibling notes (all rated `anecdotal`). The higher rating reflects
   that several of this essay's central claims (Claims 4, 5, 6) describe a
   live, independently-fetchable system whose existence and structure this
   extraction directly confirmed, rather than resting solely on the author's
   unverified self-report — but the essay's higher-level value claims
   (Claims 1, 3, 7, 9) remain anecdotal, self-described as an unproven
   experiment with no usage data available at eleven days post-launch.
