---
source_url: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
source_type: blog-post
title: "Code w/ Claude London 2026: Rethinking how we build"
author: Anthropic (Boris Cherny, Head of Claude Code; Lisa Crofoot, Research Product Manager)
date_published: 2026-05-26
date_extracted: 2026-05-27
last_checked: 2026-05-27
status: current
confidence_overall: emerging
issue: "#960"
---

# Code w/ Claude London 2026: Rethinking how we build

> Official Anthropic event recap documenting the first European Code w/ Claude conference
> (London, May 2026), featuring Boris Cherny's keynote thesis that agents collapse the
> historical gap between idea and execution, two new Claude Managed Agents capability
> announcements (self-hosted sandboxes and MCP tunnels), and customer sessions from Spotify,
> Base44, and Legora.

## Source Context

- **Type**: blog-post (official Anthropic event recap, claude.com/blog, May 26, 2026; covers
  a two-day event held the same week in London)
- **Author credibility**: First-party Anthropic event recap. Boris Cherny is Head of Claude
  Code — authoritative on product direction and philosophy. Lisa Crofoot is a Research Product
  Manager at Anthropic. The post is primarily a product/event marketing piece; it does not
  contain the technical depth of Anthropic's engineering blog posts. Customer sessions
  (Spotify, Base44, Legora) are named but not described in detail. The feature announcements
  (self-hosted sandboxes, MCP tunnels) repeat content from the May 19, 2026 announcement
  post in compressed form — full detail is in blog-anthropic-claude-managed-agents-selfhosted.md.
- **Scope**: Covers Boris Cherny's keynote framing, two Managed Agents feature announcements,
  named customer sessions, workshop topics, and the Code w/ Claude event series expansion
  to Europe and Japan. Does NOT cover session recording content, specific details from the
  Spotify/Base44/Legora presentations, workshop instructional content, or technical
  implementation details of the announced features. The source is short (~5 min read) — this
  is a thin event recap rather than a deep-dive article. Session recordings (if any) are
  not available as text through the blog post.

## Extracted Claims

### Claim 1: Programming historically accumulated layers of complexity (compilers, typecheckers, build systems) that pushed the distance between having an idea and executing it progressively further out

- **Evidence**: Boris Cherny's keynote framing, presented as a historical narrative of how
  software development evolved. The concrete examples (TI-83 homework programs, eBay Pokémon
  card HTML) ground the abstraction in personal experience — immediacy of execution as the
  original "magic" of programming.
- **Confidence**: anecdotal (keynote narrative; the "growing complexity" observation is widely
  recognizable to practitioners but not a controlled measurement)
- **Quote**: "Somewhere along the way, he suggested, programming got complicated. Compilers,
  typecheckers, build systems, and each layer pushed the distance between 'I have an idea'
  and 'it runs' a little further out."
- **Our assessment**: The "idea-to-execution distance" framing is not an empirical claim but
  a practitioner-legible narrative about why modern software development feels friction-heavy.
  It provides a conceptual structure for the guide's "why now" argument: the accumulation of
  toolchain layers is measurable as friction experienced by practitioners, and agents reduce
  that friction. The observation that each added layer (compiler, typechecker, build system)
  contributes its own delay to the feedback cycle is consistent with everything the corpus
  documents about practitioner adoption of agentic workflows — they adopt agents where the
  feedback cycle is longest.

### Claim 2: Agents collapse the idea-to-execution gap, returning programming to the immediacy of early computing — describe a problem and the program appears

- **Evidence**: Boris Cherny's keynote thesis, framed as the direct consequence of Claim 1.
  The TI-83 and eBay HTML anecdotes establish the baseline ideal (code that ran immediately,
  experiments with direct feedback). Agents restore that baseline.
- **Confidence**: anecdotal (first-party vendor keynote; no measured evidence; the framing is
  philosophically coherent)
- **Quote**: "With agents, that distance is collapsing again: you describe a problem, and the
  program shows up."
- **Our assessment**: This is the most quotable claim in the source. The "describe a problem,
  and the program shows up" formulation captures the shift from imperative (how) to declarative
  (what) programming as the dominant interface paradigm. This is consistent with the agentic
  workflows documented throughout the corpus but this source is the first to package it as a
  historical-narrative argument rather than a technical recommendation. It is useful for the
  guide's introduction as a practitioner-facing motivation: agents are not a new layer of
  complexity but a reduction of accumulated complexity.

### Claim 3: Self-hosted sandboxes (public beta) split Claude Managed Agents into an Anthropic-managed orchestration layer and a customer-controlled execution layer

- **Evidence**: Feature announcement at the London event. The blog post provides the most
  concise single-sentence architectural description. Full technical detail — provider
  comparison, credential security, sandbox interface specification, customer deployments —
  is in blog-anthropic-claude-managed-agents-selfhosted.md (Claim 1).
- **Confidence**: settled (first-party product announcement; feature is in public beta as of
  May 19, 2026)
- **Quote**: "Tool execution moves to an environment you configure—your own infrastructure or
  a managed provider like Cloudflare, Daytona, Modal, or Vercel—while the agent loop that
  handles orchestration, context management, and error recovery stays on Anthropic's
  infrastructure."
- **Our assessment**: The quote here is the most succinct architectural description of the
  split available in any corpus source. The distinction between "agent loop" (Anthropic-managed,
  unchanged) and "tool execution" (customer-pluggable, new) is precise and complete in one
  sentence. Early adopters named at this event: Amplitude, Clay, Rogo (see
  blog-anthropic-claude-managed-agents-selfhosted.md Claim 11 for their implementation
  details). The London event is the in-person launch vehicle for this feature, which was
  published May 19 (one week earlier).

### Claim 4: MCP tunnels (research preview) enable agents to reach private-network MCP servers via a single outbound connection with no inbound firewall rules and end-to-end encryption

- **Evidence**: Feature announcement at the London event. Full technical detail in
  blog-anthropic-claude-managed-agents-selfhosted.md (Claims 9–10).
- **Confidence**: settled (first-party product announcement; feature is in research preview as
  of May 19, 2026)
- **Quote**: "Your agents reach MCP servers inside your private network without exposing them
  to the public internet. A lightweight gateway you deploy makes a single outbound connection:
  no inbound firewall rules, no public endpoints, and traffic encrypted end to end."
- **Our assessment**: The quote is the clearest single-passage description of MCP tunnels
  architecture anywhere in the corpus — it is architecturally complete: private network access,
  outbound-only connection model, zero public exposure, end-to-end encryption. The London
  recap uses this language; blog-anthropic-claude-managed-agents-selfhosted.md Claim 9 uses
  nearly identical language with the addition of management surface (Claude Console, org
  admin) and API scope (Messages API in addition to Managed Agents). Research preview
  access requires a separate request.

### Claim 5: Spotify, Base44, and Legora presented customer sessions at the London event on scaling engineering with Claude Code

- **Evidence**: Named in the event recap as customer case study sessions. No session content
  details are provided in the blog post itself.
- **Confidence**: anecdotal (event session listing; no content extractable from this source)
- **Quote**: (no direct quote; companies named in session listing without accompanying
  description)
- **Our assessment**: The three named customers suggest Claude Code adoption across distinct
  domains: Spotify (developer experience at scale for a large engineering org), Base44
  (hypergrowth product engineering scaling), Legora (legal AI — the only legal-domain
  customer to appear in the corpus as a Code w/ Claude presenter). Legora's presence
  is novel to the corpus — no existing source note mentions Legora. No extractable patterns
  from this source; session recordings are not available as text through the blog post. If
  individual session recaps or recordings become available, they should be mined separately.

### Claim 6: Code w/ Claude is expanding as an international practitioner event series — the London event is the first European edition; Tokyo (June 5–6, 2026) follows with livestreamed Day 1 content

- **Evidence**: Blog post opening explicitly frames London as bringing "Code w/ Claude to
  Europe"; Tokyo announcement with specific dates. The related posts section lists
  "Code w/ Claude SF 2026 recap: Building on the AI exponential" (May 12, 2026) as the
  prior event — establishing the series pattern: SF → London → Tokyo.
- **Confidence**: settled (explicit event announcement with dates; the SF event already
  occurred and is referenced)
- **Quote** (opening): "This week in London, we brought Code w/ Claude to Europe. The event
  brought together builders, developers, and founders for two days of keynotes, breakout
  sessions, and workshops with the teams building Claude."
- **Quote** (Tokyo): "Code w/ Claude heads to Tokyo next (June 5–6). All Day 1 keynotes and
  breakout sessions will be streamed live."
- **Our assessment**: The SF → London → Tokyo cadence within a six-week window (May 12 →
  May 26 → June 5) signals that Anthropic is treating Code w/ Claude as an aggressive
  global practitioner community-building series, not a periodic product-launch event.
  The livestreaming of Tokyo's Day 1 is notable: it converts an in-person event into a
  global broadcast, extending the practitioner community reach. The international expansion
  is a team adoption signal: Anthropic is investing in seeding practitioner communities
  globally through structured in-person knowledge transfer.

### Claim 7: Workshop sessions at London addressed advanced Claude Code usage and optimizing thinking budgets and effort levels across models as practitioner-level concerns

- **Evidence**: Event program description in the recap. No workshop content details are
  provided in the blog post.
- **Confidence**: anecdotal (event program listing; no workshop content extractable from
  this source)
- **Quote**: (no direct quote; workshop topics described as "Go beyond the basics with Claude
  Code" and optimizing thinking budgets and effort levels across models)
- **Our assessment**: The workshop topics reveal two areas Anthropic considers worth structured
  in-person instruction for practitioners beyond introductory use: (1) advanced Claude Code
  patterns beyond the basics, and (2) cost/quality optimization via thinking budget and effort
  level controls. The second topic has no dedicated source note in the corpus yet — it signals
  an emerging practitioner concern about model effort calibration in production. If Anthropic
  publishes documentation or blog content on thinking budget optimization, that should be
  prioritized for mining.

## Concrete Artifacts

### Event Program Overview (from post)

```
Code w/ Claude London 2026 — May 2026 (exact dates not stated in blog post)
(Anthropic blog, 2026-05-26)

FORMAT: Two days of keynotes, breakout sessions, workshops

KEYNOTES:
  - Boris Cherny (Head of Claude Code): Agents collapse the idea-to-execution gap
  - Lisa Crofoot (Research Product Manager): Additional keynote content
    (details not provided in blog post)

WORKSHOPS:
  - "Go beyond the basics" with Claude Code
  - Optimizing thinking budgets and effort levels across models

CUSTOMER SESSIONS:
  - Spotify: [topic not described in blog post]
  - Base44: [topic not described in blog post]
  - Legora: [topic not described in blog post]

ANNOUNCEMENTS (see blog-anthropic-claude-managed-agents-selfhosted.md for full detail):
  - Self-hosted sandboxes (Public Beta): tool execution on customer infrastructure
    Providers: Cloudflare, Daytona, Modal, Vercel (or bring your own)
  - MCP tunnels (Research Preview): private-network MCP access via outbound gateway

EARLY ADOPTERS NAMED (for new features):
  - Amplitude, Clay, Rogo

EVENT SERIES TRAJECTORY:
  - Code w/ Claude SF 2026 (May 12, 2026)
  - Code w/ Claude London 2026 (May ~20-21, 2026) ← this event
  - Code w/ Claude Tokyo 2026 (June 5–6, 2026; Day 1 livestreamed)
```

### Boris Cherny Keynote Framing (verbatim from blog narration)

```
Boris Cherny (Head of Claude Code) — Code w/ Claude London 2026 Keynote
As narrated by the blog post (not a direct transcript):

Origin of programming's magic:
  "the first time he felt the 'magic' of coding. In secondary school, he wrote
  TI-83 programs that solved his math homework and tests, and taught himself HTML
  to make his eBay listings for Pokémon cards sell better."

Diagnosis of complexity growth:
  "Somewhere along the way, he suggested, programming got complicated. Compilers,
  typecheckers, build systems, and each layer pushed the distance between 'I have
  an idea' and 'it runs' a little further out."

Thesis about agents:
  "With agents, that distance is collapsing again: you describe a problem, and
  the program shows up."

Note: Phrases in single quotes ('magic', 'I have an idea', 'it runs') appear to be
Cherny's own words embedded in the blog's third-person narration. "He suggested" is
the blog's framing, not Cherny's words.

Source: Anthropic, claude.com/blog (2026-05-26)
```

### Feature Announcement Text (from London recap — compressed form)

```
Self-hosted sandboxes (Public Beta):
  "Tool execution moves to an environment you configure—your own infrastructure or
  a managed provider like Cloudflare, Daytona, Modal, or Vercel—while the agent
  loop that handles orchestration, context management, and error recovery stays on
  Anthropic's infrastructure."

MCP tunnels (Research Preview):
  "Your agents reach MCP servers inside your private network without exposing them
  to the public internet. A lightweight gateway you deploy makes a single outbound
  connection: no inbound firewall rules, no public endpoints, and traffic encrypted
  end to end."

Source: Anthropic, claude.com/blog (2026-05-26)
For full technical detail, provider comparison, and customer implementations:
  → blog-anthropic-claude-managed-agents-selfhosted.md
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-claude-managed-agents-selfhosted.md** (Claim 1): The London recap's
    self-hosted sandboxes quote ("the agent loop...stays on Anthropic's infrastructure, while
    tool execution moves to your own configured environment") expresses the same architectural
    split documented in Claim 1 of that note, in slightly different wording. Both sources are
    first-party Anthropic; the London recap is the event announcement form of the same content.
  - **blog-anthropic-claude-managed-agents-selfhosted.md** (Claim 9): The London recap's MCP
    tunnels quote ("A lightweight gateway you deploy makes a single outbound connection: no
    inbound firewall rules, no public endpoints, and traffic encrypted end to end") directly
    matches the architectural description in Claim 9 of that note.
  - **blog-anthropic-claude-managed-agents-selfhosted.md** (Claim 11): Amplitude, Clay, and
    Rogo are named at the London event as early adopters of the new features. Claim 11 of
    that note documents their specific implementations (Amplitude → Cloudflare, Clay →
    Daytona, Rogo → Vercel) with customer quotes.

- **Contradicts**: None identified. The London recap is consistent with all existing corpus
  notes on managed agents, MCP, and enterprise deployment. No contradictions filed.

- **Extends**:
  - **blog-anthropic-claude-managed-agents-selfhosted.md**: The London event is the in-person
    launch vehicle for the features announced May 19. The event context adds a dimension
    not in the feature post: practitioners were briefed on these capabilities live, with
    workshops and customer demonstrations alongside the technical announcement.
  - **blog-anthropic-legal-industry-deploy.md**: Legora appearing as a Code w/ Claude London
    customer session confirms legal AI practitioners are active in the Claude Code ecosystem,
    consistent with the legal deployment patterns documented in that note. Legora is the
    first legal-domain company to appear in the corpus as a Code w/ Claude event presenter.

- **Novel**:
  - **Boris Cherny's "idea-to-execution distance" as a design philosophy**: No existing
    source note frames the case for agents as a historical narrative — programming complexity
    as an accumulated gap that agents close, returning computing to its original immediacy.
    This is the first corpus source where a named Anthropic leader provides a philosophical
    argument for why agents matter, distinct from technical or business justifications.
  - **Code w/ Claude as a global practitioner event series**: The SF → London → Tokyo cadence
    within six weeks is the first documented evidence of Anthropic building Code w/ Claude as
    an aggressive international community-building series (not a periodic US-based event).
    The livestreaming of Tokyo Day 1 is the first documented mechanism for extending in-person
    practitioner knowledge transfer to remote practitioners.
  - **Legora as a named Code w/ Claude event presenter**: Legora does not appear in any other
    source note. Its presence at the London event confirms legal AI practitioners are building
    with Claude Code specifically (not just Claude for document analysis). The company may
    warrant a dedicated extraction if they publish practitioner content.
  - **"Thinking budgets and effort levels" as a structured practitioner workshop topic**:
    No existing source note addresses thinking budget and effort level optimization across
    models. This workshop topic signals an emerging gap in the corpus that may warrant a
    dedicated source note if Anthropic publishes technical guidance on it.

## Guide Impact

- **Chapter 01 (Introduction / Why Now)**: Boris Cherny's framing (Claims 1–2) provides the
  motivating narrative for the guide's existence. The "idea-to-execution distance" concept
  names the pain practitioners recognize, and "you describe a problem, and the program shows
  up" is a quotable summary of the agentic programming mode the guide teaches. Consider
  using it to frame why the shift to agentic workflows is a natural reduction of accumulated
  complexity, not a new complexity layer.

- **Chapter 02 (Harness Engineering)**: Cross-reference Claims 3–4 to
  blog-anthropic-claude-managed-agents-selfhosted.md for the full self-hosted sandboxes and
  MCP tunnels content. The London recap provides the most succinct one-sentence versions
  of each feature's architecture, which may be useful as inline definitions in the guide.

- **Chapter 05 (Team Adoption)**: Claim 6 (Code w/ Claude as international practitioner
  community-building series) is evidence that structured in-person knowledge transfer is
  a recognized adoption mechanism. The team adoption chapter should note that practitioner
  events — both live and livestreamed — are part of the ecosystem for building organizational
  competence with agents. The SF → London → Tokyo cadence demonstrates the pace at which
  the practitioner community is being actively built.

- **Chapter [planned: Model Usage / Cost Optimization]**: Claim 7 flags "thinking budgets
  and effort levels" as a practitioner concern prominent enough to merit a dedicated workshop
  at a flagship event. This chapter gap — how to optimize model effort and cost for production
  workloads — is identified as an extraction priority if Anthropic publishes guidance on it.

## Extraction Notes

- The source is a short event recap (~5 min read). The substantive technical content
  (self-hosted sandboxes, MCP tunnels) is documented far more deeply in
  blog-anthropic-claude-managed-agents-selfhosted.md (issue #820). This note captures what
  is unique to the London 2026 recap: the keynote framing, the event program, the customer
  sessions named (without content), and the event series expansion.
- Boris Cherny's keynote quotes are narrated by the blog post ("he suggested"), meaning the
  blog is paraphrasing his speech rather than providing a direct transcript. The phrases in
  single quotes ('magic', 'I have an idea', 'it runs') appear to be Cherny's own words
  within the blog's third-person narration. This distinction is noted in the Concrete
  Artifacts section.
- Three WebFetch passes were made with escalating verbatim-extraction instructions to maximize
  quote fidelity. The quotes in this note are from the most precise extraction pass.
- Session recordings from the London event (for Spotify, Base44, Legora, and the workshops)
  are not available as text through the blog post and were not accessible to extract. If
  those recordings become available as blog posts or transcripts, they should be mined
  separately.
- No session content details are available for Spotify, Base44, or Legora. Their presence
  at the event is confirmed; what they presented is not accessible from the blog post.
- The "Code w/ Claude SF 2026 recap: Building on the AI exponential" (May 12, 2026) is
  listed as a related post and appears to be an unmined event recap. If issued, it may
  contain patterns from the SF event that predate and inform the London event themes.
- Confidence is set to `emerging` overall: the feature announcements (Claims 3–4) are settled
  at the atomic level but are compressed repeats of content already in corpus; the keynote
  framing (Claims 1–2) is philosophically coherent but anecdotal; the event program details
  (Claims 5–7) are factual but thin on content.
