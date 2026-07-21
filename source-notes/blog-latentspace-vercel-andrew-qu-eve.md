---
source_url: https://www.latent.space/p/vercel-agents-new-software
source_type: blog-post
title: "Vercel's Andrew Qu on why agents are a new kind of software"
author: Richard MacManus (Latent Space), interviewing Andrew Qu (Chief of Software, Vercel)
date_published: 2026-07-03
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2098"
---

# Vercel's Andrew Qu on why agents are a new kind of software

> A first-person Q&A with Vercel's Chief of Software on why "agents are a new type
> of software" needing different primitives than web applications, how Vercel's
> internal pain points building its own agent (v0) grew into the `eve` framework,
> why skills exist to forward-correct outdated model knowledge, and why Vercel now
> serves agent requests Markdown instead of HTML.

## Source Context

- **Type**: blog-post (Q&A interview transcript, published on Latent Space's
  Substack under the "AINews: Weekday Roundups" section, July 3, 2026). Format is
  a direct interview transcript (question/answer pairs), not narrative reporting —
  every substantive claim below is Andrew Qu's own words as transcribed by the
  interviewer, Richard MacManus.
- **Author credibility**: Andrew Qu is Chief of Software at Vercel, working
  directly with the CTO "across internal engineering, product experimentation and
  emerging technologies." Per his own stated bio in the article, he "built
  libraries for MCP, created skills.sh and led the development of eve, Vercel's
  framework for building agents" — i.e., he is the named engineering lead for the
  specific framework (`eve`) the interview is about, not a marketing or PR
  spokesperson. This is first-party, practitioner-level authority on Vercel's own
  agent-framework design decisions. Richard MacManus is the interviewer
  (Latent Space); no independent editorial framing or fact-checking of Qu's claims
  is present beyond the direct Q&A structure. No metrics, benchmark numbers, or
  named customer case studies are given anywhere in the piece — every claim is
  qualitative, first-person practitioner narrative.
- **Scope**: Covers Vercel's shift from web-application hosting to agent-building,
  the origin story of the `eve` framework (born from building v0's own agent),
  Qu's framing of "agents as a new type of software" requiring different
  primitives (context, tools, resumability, long-running work), a rule of thumb
  for autonomous-vs-human-in-the-loop task design, why skills matter (forward-
  correcting outdated model knowledge), Vercel's practice of serving Markdown to
  agent requests instead of HTML, and Vercel's stated ambition to make "Vercel
  itself" an agent embedded across its website, Slack, and dashboard. Does NOT
  cover: `eve`'s API or configuration syntax, specific sandbox implementation
  details, pricing, or any quantitative before/after metrics for any of the
  practices described. No linked sub-pages were present in the article to follow
  (MINER.md §1) — the piece is a single self-contained transcript with no inline
  links to other Vercel documentation or blog posts.

## Extracted Claims

### Claim 1: Andrew Qu, as Vercel's Chief of Software, personally built Vercel's early MCP library and `skills.sh`, and led development of `eve`, Vercel's agent framework
- **Evidence**: First-party biographical statement in the article's introduction.
- **Confidence**: settled (biographical fact about the interview subject, stated directly)
- **Quote**: "He has built libraries for MCP, created skills.sh and led the development of eve, Vercel's framework for building agents."
- **Our assessment**: Establishes Qu's direct authorship credibility for the framework-design claims that follow — he is not describing someone else's engineering decisions. Worth noting for the guide as an example of a single practitioner's fingerprints spanning three separate infrastructure layers (protocol tooling, skill discovery, and the agent framework itself), suggesting these three pieces were designed as a connected system rather than independently.

### Claim 2: Vercel's agent framework `eve` originated from reusable libraries built to solve internal "paper cuts" — switching models/providers, adding fallbacks, and making runs resumable — encountered while building v0's own agent
- **Evidence**: First-party origin narrative describing the specific problems that motivated the framework's creation.
- **Confidence**: anecdotal (single-company origin story, no external verification, but told in specific and falsifiable terms)
- **Quote**: "While building our own agent in v0, our vibe-coding product, we ran into a lot of paper cuts that existing tooling did not solve: switching models or providers, adding fallbacks and making runs resumable. We turned those solutions into reusable libraries that could support v0 and also help customers build their own agents. Over time, we accumulated a set of primitives and decided to assemble them more cohesively. That became eve."
- **Our assessment**: This is a concrete "dogfooding produced the framework" narrative, structurally similar to how internal tool-building often precedes a productized framework. The three named paper cuts (model/provider switching, fallbacks, resumability) are a specific, checkable list of what existing agent tooling was missing at the time `eve` was conceived — useful as a concrete "what a production agent framework must handle" checklist distinct from generic "agents need good infrastructure" framing.

### Claim 3: `eve` became a dedicated, prescriptive framework after an internal "agent on every desk" initiative surfaced recurring best practices — filesystem agents, skills, compaction, and subagents — that Qu wished had come "out of the box"
- **Evidence**: First-party account of an internal initiative and the specific practices it surfaced.
- **Confidence**: anecdotal (single-team internal initiative, no external verification)
- **Quote**: "About a year ago, I started working toward putting an agent on every desk inside Vercel. That led me to build a successful data agent, and along the way a number of best practices emerged: filesystem agents, skills, compaction and subagents. These were all things I wished had come out of the box. Eventually, we asked: what if there were a prescriptive way to do this, so other developers did not have to go through the same exploration? That is where eve came from."
- **Our assessment**: This names the same four harness building blocks (filesystem agents, skills, compaction, subagents) that recur across the corpus's harness-engineering sources (`blog-humanlayer-skill-issue-harness-engineering.md`, `blog-anthropic-large-codebase-best-practices.md`) as independently rediscovered, not externally copied — Qu frames them as "things I wished had come out of the box," i.e., emergent lessons from one team's internal build-out rather than adoption of an existing published taxonomy. This is corroborating evidence that these four primitives are converging as a de facto standard harness toolkit across independent organizations (see Cross-References).

### Claim 4: Agents are "a new type of software," less predictable than web applications, requiring different primitives for context, tools, resumability, and long-running work
- **Evidence**: Direct framing statement in response to being asked whether agents are simply another kind of application or genuinely new.
- **Confidence**: emerging (a conceptual framing claim from a framework's lead engineer, not an empirically measured distinction)
- **Quote**: "I think agents are a new type of software. They are not as predictable as web applications. The infrastructure can look similar, but the interaction, interface and outputs are much more dynamic. That changes how you build them. You need different primitives for context, tools, resumability and long-running work."
- **Our assessment**: This is the article's title claim and organizing thesis. The specific list of "different primitives" needed (context, tools, resumability, long-running work) is a compact four-item spec that overlaps substantially with, but is phrased independently of, the harness-configuration-surface taxonomies already in the corpus (CLAUDE.md/AGENTS.md, MCP, skills, sub-agents, hooks, back-pressure per `blog-humanlayer-skill-issue-harness-engineering.md`; the seven-extension-point taxonomy per `blog-anthropic-large-codebase-best-practices.md` Claim 5). Notable omission from Qu's four-item list relative to those taxonomies: no explicit mention of hooks or deterministic control flow — Qu's framing emphasizes infrastructure primitives (resumability, long-running work) over configuration/instruction surfaces.

### Claim 5: A good agent use case is "a repetitive task that still requires some reasoning" — not fixed automation, because the system must interpret the situation and decide what to do
- **Evidence**: Direct answer with three named internal Vercel examples of agent use cases.
- **Confidence**: emerging (a design heuristic from practitioner experience, not independently tested against a broader use-case dataset)
- **Quote**: "A good candidate is often a repetitive task that still requires some reasoning. It is not just fixed automation, because the system has to interpret the situation and decide what to do."
- **Our assessment**: This is a reusable selection heuristic for "should this be an agent, a script, or a human task?" decisions — a task that is repetitive (favoring automation) but requires situational interpretation (disfavoring fixed/deterministic scripting) sits in the agent-appropriate zone. The three named internal examples — "a first pass at legal contract redlining, to marketing retrospectives and identifying people to contact, to writing queries against our data stores" — ground the heuristic in specific, business-process (not developer-tooling) use cases, distinct from most of the corpus's coding-agent-centric examples.

### Claim 6: Whether an agent should work autonomously or keep a human in the loop depends on the task's feedback cycle — well-defined tasks with a known target output can run autonomously to completion, while careful or surgical engineering work needs the human checking back in
- **Evidence**: Direct answer to a question about autonomy vs. human-in-the-loop design, framed as a task-dependent choice rather than a universal rule.
- **Confidence**: emerging (a design principle stated as practitioner judgment, without a decision framework or worked examples beyond the general categories given)
- **Quote**: "I don’t think the future is all autonomous loops, and I don’t think it is all human-in-the-loop. It is about choosing a feedback cycle that fits the task. If the task is well defined and you know what the final output should look like, it can be reasonable to let a loop continue until it is done. For more careful or surgical engineering work, you should check back in and make sure you are steering the model correctly."
- **Our assessment**: This explicitly rejects both autonomy-maximalist and human-in-the-loop-maximalist framings in favor of a task-shape-dependent rule: known/well-defined output → autonomous loop; surgical/careful engineering → frequent check-ins. This is a clean, reusable framing for the guide's autonomy-calibration discussion, though it stops short of giving concrete criteria for what counts as "well defined" versus "surgical" beyond the two illustrative categories named.

### Claim 7: A year before this interview, Vercel did not anticipate how important sandboxes, secure code execution, and long-running job support would become — these needs emerged only from production experience
- **Evidence**: First-party retrospective statement about which primitives were not anticipated in advance.
- **Confidence**: anecdotal (single-company retrospective claim, illustrative rather than quantified)
- **Quote**: "A year ago, we did not know sandboxes would become so important, or how much demand there would be for secure code execution and long-running jobs. As we learn more from production, there will be much more to build."
- **Our assessment**: This is a specific, named instance of "harness requirements emerge from production usage rather than being fully specified upfront" — sandboxes and long-running-job support are singled out as the two primitives whose importance Vercel underestimated a year prior. This corroborates the broader corpus finding that sandbox/secure-execution infrastructure has become a load-bearing, previously-underestimated primitive across multiple vendors (see Cross-References).

### Claim 8: Vercel is not trying to own every part of the agent lifecycle — it wants to make it easy to integrate with specialized partners, while still shipping observability and evaluations "out of the box" for anything deployed to Vercel via `eve`
- **Evidence**: Direct answer to a question about whether Vercel is building an end-to-end agent platform.
- **Confidence**: emerging (a stated platform strategy, not independently verified against actual partner-integration breadth or evaluation feature completeness)
- **Quote**: "Yes and no. We value partners that provide specialized parts of the agent lifecycle, but we also want it to be very easy for developers to get started. If you deploy eve to Vercel, you get observability and evaluations out of the box. We want to make that experience more comprehensive while making it easy to integrate with partners rather than owning every component."
- **Our assessment**: This positions Vercel's agent strategy as "batteries-included default, but not a walled garden" — deploying `eve` to Vercel gets you baseline observability/evals for free, but Vercel is explicitly not trying to displace specialized sandbox, evaluation, or tooling partners. This is a strategic/business claim more than a technical one, useful mainly for readers evaluating `eve` against a build-vs-buy-vs-integrate decision.

### Claim 9: Skills exist because models often contain outdated information about a company's own product, and a skill can forward-correct that — publishing skills for the current product version is recommended alongside auditing and updating existing outdated content
- **Evidence**: Direct answer with a concrete, named example of the specific outdated information skills are meant to correct.
- **Confidence**: emerging (a design rationale for skills grounded in one concrete named example, not a systematic study of model knowledge staleness)
- **Quote**: "Models often contain outdated information. For example, they still sometimes recommend Vercel Postgres, even though we deprecated it years ago in favor of our marketplace. A skill can tell the agent that Vercel Postgres is deprecated and steer it toward the current approach. Until companies can audit and update every old piece of content, skills provide a way to forward-correct the model. I would recommend publishing skills for the latest version of your product. But companies should also audit their existing content, identify what is outdated and update it or add clear notes."
- **Our assessment**: This frames skills specifically as a fix for training-data staleness about a company's own product — a narrower and more concrete rationale than the general "skills are portable, on-demand knowledge" framing found elsewhere in the corpus. The Vercel Postgres example is a specific, checkable case of a real deprecated product a model might still recommend. This is a distinct angle from `blog-anthropic-claude-code-skills-lessons.md` Claim 7 ("skills should not restate capabilities Claude already knows — only information Claude cannot infer adds value"): that source's principle is about avoiding redundant content; Qu's claim is about actively counteracting stale/wrong content the model already "knows." Both are compatible but describe different skill-writing motivations — the Anthropic source addresses volume/noise, this source addresses correctness.

### Claim 10: Bot/agent traffic to websites is rising while human traffic is flat or declining even as impressions increase, and Vercel now detects agent requests and serves Markdown directly instead of HTML
- **Evidence**: Reference to Vercel-published traffic reports plus a direct description of a shipping practice.
- **Confidence**: emerging (the traffic-trend claim references unnamed "reports" without figures given in this piece; the Markdown-serving practice is a direct first-party description of a current, shipping behavior)
- **Quote**: "We have published reports showing bot traffic rising while human traffic is stagnant or declining, even as impressions increase, because agents and bots are hitting websites more frequently. The future of the web is therefore to be as accessible to bots and agents as possible, so they can learn about your product and use it successfully. At Vercel, we already detect when an agent makes a request and serve Markdown directly. Instead of forcing it to process HTML designed for a visual browser, we provide a format that is easier to read."
- **Our assessment**: The traffic-trend claim references external Vercel reports not named or linked in this piece, so it should be treated as an unverified pointer rather than a self-contained data point — if this becomes load-bearing for the guide, the underlying Vercel traffic report should be separately mined. The Markdown-serving practice itself, however, is a concrete, verifiable architectural claim: user-agent or request-header-based content negotiation that serves a different representation (Markdown) to agent/bot requests than to browser requests. This is the most novel technical claim in the source (see Cross-References → Novel).

### Claim 11: Websites will increasingly serve two distinct experiences — a visual site for humans and a structured, machine-readable representation for agents — and Vercel states it is "already doing that today"
- **Evidence**: Direct follow-up confirmation, restating and affirming the practice described in Claim 10.
- **Confidence**: emerging (first-party confirmation of a current, shipping practice, though still a single-company data point)
- **Quote**: "I think so. Humans may continue to receive the visual site, while agents receive a more structured, machine-readable representation. We are already doing that today."
- **Our assessment**: This confirms Claim 10's Markdown-serving practice is not a future roadmap item but a present-tense, already-implemented behavior at Vercel ("already doing that today"). For the guide, this is a concrete example of dual-representation web architecture — deliberately maintaining two content representations gated on requester type — as opposed to a single representation that both humans and agents must parse.

### Claim 12: Vercel's next area of interest is "multiplayer agent development" — solving how teammates share context and techniques for agent-assisted work (e.g., getting a front-end interface right) rather than each person rediscovering it independently
- **Evidence**: Direct answer about what problems Qu is most interested in solving next.
- **Confidence**: anecdotal (a stated personal/team priority and forward-looking interest, not a shipped feature or measured problem)
- **Quote**: "One of the things at the top of my agenda is multiplayer agent development. Whenever a team collaborates, people struggle to share context. I may have techniques for getting a front-end interface right on the first attempt, but another person may not know them. I am interested in how we can share that context between teammates and allow them to contribute to it."
- **Our assessment**: This names a specific, underexplored problem — context and technique-sharing between teammates who each use agents individually — distinct from the more commonly discussed "context engineering" problem of the human-to-agent context handoff. This is a team-to-team (not human-to-agent) context-sharing gap. No mechanism or product is described; this is a stated open problem, not a solution, and should be treated as a forward-looking direction rather than an established practice.

### Claim 13: Rather than shipping agents primarily as standalone products, Vercel is positioning "Vercel itself" as becoming an agent — embedded in its website, Slack, and dashboard to act on the user's behalf
- **Evidence**: Direct answer to whether agents will become a separate application category or a built-in capability, framed as Vercel's own specific strategic choice (with an explicit caveat that other companies may choose differently).
- **Confidence**: emerging (a stated strategic direction, not a fully shipped, independently verifiable product survey — "we have an agent on the website, in Slack and in the dashboard" is asserted as current, but with no description of what these agents can do)
- **Quote**: "For Vercel, Vercel itself is becoming an agent. We have an agent on the website, in Slack and in the dashboard that can do things on your behalf. Other companies will ship agents as standalone products. For us, agents are tightly coupled to everything we build. We want the entire platform to be agent-friendly — and, in many ways, to make the platform itself an agent."
- **Our assessment**: This is the article's closing thesis and the second half of its title framing (agents as "embedded platform capabilities rather than separate applications" per the WebFetch summary framing). Qu explicitly frames this as Vercel's specific strategic choice, not a universal prediction — "it depends on who you are and what you are building" precedes this quote in the transcript. Useful for the guide as a named example of the "agent as pervasive platform capability" strategy, contrasted with the "agent as standalone product" strategy other companies pursue.

## Concrete Artifacts

### Full Q&A transcript structure (article section order, for navigation)

```
Source: https://www.latent.space/p/vercel-agents-new-software

1. From web applications to agents
   - What does a Chief of Software do at Vercel?
   - How did Vercel evolve from web development to agents?
2. Why eve became necessary
   - How did Vercel reach the point of needing a dedicated agent framework?
   - Are agents simply another kind of application, or a genuinely new form
     of software?
   - What kinds of problems are particularly well suited to agents?
3. Building effective agents
   - When should an agent work autonomously, vs. keep a human in the loop?
   - What was the main lesson from prompting → bespoke tools → coding-agent
     harnesses → filesystem agents → skills?
   - Is Vercel building an end-to-end agent platform?
4. Skills and current knowledge
   - Why have skills become so important?
5. An agent-readable web
   - How will websites evolve as more traffic comes from agents?
   - Does that mean one experience for humans and another for agents?
6. What comes next
   - What problems are you most interested in solving next?
   - Will agents become a separate application category, or a standard
     capability built into most software?
```

### Named internal Vercel agent use cases (verbatim list, from the "well suited to agents" answer)

```
Source: https://www.latent.space/p/vercel-agents-new-software

"We see a lot of business agents. Internally at Vercel, we use them for
repetitive work ranging from a first pass at legal contract redlining, to
marketing retrospectives and identifying people to contact, to writing
queries against our data stores."
```

### Four best-practice primitives named as the origin of `eve` (verbatim list)

```
Source: https://www.latent.space/p/vercel-agents-new-software

"a number of best practices emerged: filesystem agents, skills, compaction
and subagents. These were all things I wished had come out of the box."
```

## Cross-References

### Cross-reference verification notes
`blog-humanlayer-skill-issue-harness-engineering.md`, `blog-anthropic-large-codebase-best-practices.md`,
`blog-anthropic-claude-code-skills-lessons.md`, `blog-anthropic-claude-managed-agents-selfhosted.md`,
and `blog-anthropic-harness-long-running.md` were re-read (in full or via their
`### Claim N:` heading list) during this extraction per MINER.md §4b, and every
claim number cited below was located and confirmed against that note's own
numbered claims in document order before writing this section.

- **Corroborates**:
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 1 ("coding agent
    = AI model(s) + harness") and Claim 11 (harness engineering as a distinct,
    named engineering discipline): this source's Claim 4 ("agents are a new
    type of software... you need different primitives for context, tools,
    resumability and long-running work") is an independent, differently-worded
    articulation of the same core idea from a second, unrelated company — that
    agent quality is a function of infrastructure/harness design, not just
    model choice.
  - `blog-anthropic-large-codebase-best-practices.md` Claim 5 (seven-extension-point
    harness taxonomy: CLAUDE.md, hooks, skills, plugins, MCP servers, LSP
    integrations, subagents) and `blog-humanlayer-skill-issue-harness-engineering.md`'s
    six-surface list: this source's Claim 3 independently names filesystem
    agents, skills, compaction, and subagents as the primitives that emerged
    from Vercel's own internal build-out — a third, independent organization
    converging on largely the same toolkit (skills and subagents overlap
    directly across all three; "filesystem agents" and "compaction" are named
    with different terminology but describe adjacent concerns to context
    management). This is meaningful corroboration that these are becoming an
    industry-standard toolkit rather than one vendor's idiosyncratic choices.
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 3 ("customers
    control compute resources... enabling agents to handle compute-heavy
    workloads like long builds") and the sandbox-provider claims generally
    (Claims 5-8): this source's Claim 7 ("we did not know sandboxes would
    become so important, or how much demand there would be for secure code
    execution and long-running jobs") corroborates, from the demand side, why
    sandbox infrastructure has become a load-bearing feature that multiple
    vendors (Anthropic's Managed Agents sandbox partners, Vercel's own `eve`)
    have independently invested in.
  - `blog-anthropic-harness-long-running.md`'s general framing that harness
    design should track evolving production needs rather than converge on a
    fixed structure: this source's Claim 7 (sandboxes and long-running jobs
    were unanticipated a year prior, "as we learn more from production, there
    will be much more to build") is an independent articulation of the same
    principle — harness/framework requirements are discovered through
    production use, not fully specified in advance.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No claim in
  this source directly opposes a claim in an existing corpus note.

- **Extends**:
  - `blog-anthropic-claude-code-skills-lessons.md`: that note documents
    Anthropic's own internal skills taxonomy and design best practices,
    including Claim 7's "don't restate what Claude already knows" principle.
    This source's Claim 9 extends the *rationale* for skills in a direction
    that note does not cover: skills as an active countermeasure to stale/wrong
    training-data knowledge about a company's own deprecated products (the
    Vercel Postgres example), not merely as a way to avoid padding with
    redundant content.
  - `blog-vercel-enterprise-apps-and-agents.md`: that note documents Vercel's
    enterprise governance/access-control products (Passport, Connect,
    Enterprise Managed Users, BYOC) built on top of `eve` and the "Agent
    Stack," explicitly noting that its own opening sentence references `eve`
    and `/blog/agent-stack` only as unelaborated context. This source is the
    first in the corpus to document `eve`'s own design philosophy and origin
    story directly, filling the gap that note's Extraction Notes flagged as
    "outside this issue's triage scope" at the time.
  - `docs-ghaw-sandbox-reference.md`: that note documents GitHub Agentic
    Workflows' sandbox/firewall configuration mechanics in technical detail
    (AWF, MCP Gateway, filesystem access tiers). This source's Claim 7 supplies
    the demand-side narrative (why sandboxes became necessary in production)
    for a different vendor's/framework's sandbox investment — corroborating,
    from an independent company, that sandbox infrastructure is a common,
    convergent need rather than one platform's idiosyncratic design choice.

- **Novel**:
  - **Skills as a countermeasure to stale training data about a company's own
    deprecated products** (Claim 9): no prior corpus source frames skills'
    purpose this specifically — as forward-correcting a model's persistent,
    wrong recommendations about a company's own product line (the named
    Vercel Postgres deprecation example) — as distinct from the more general
    "skills are portable knowledge" or "skills avoid restating the obvious"
    framings already documented.
  - **Content negotiation serving Markdown to agent requests, HTML to human
    requests, at the same URL** (Claims 10-11): no prior corpus source
    documents a production website practicing agent-vs-human request
    detection and serving a structurally different (Markdown vs. HTML)
    representation as a result. This is architecturally distinct from
    `blog-simonwillison-html-effectiveness.md`'s topic (requesting HTML
    *output from* Claude for richer presentation) — that source is about what
    format an agent should ask a model to produce; this source is about what
    format a *website* should serve *to* an agent making a request.
  - **"Multiplayer agent development" as a named, distinct open problem**
    (Claim 12): team-to-team sharing of agent-use techniques and context (as
    opposed to human-to-agent context engineering) is not framed this way by
    any other corpus source — it names a collaboration gap specifically
    between people who each use agents, not between a person and their agent.
  - **A named practitioner (Andrew Qu) whose personal work spans MCP tooling,
    skill-discovery infrastructure (skills.sh), and the agent framework itself**
    (Claim 1): no prior corpus source documents one individual's fingerprints
    across all three of these infrastructure layers at a single company.

## Guide Impact

- **Chapter 02 (Harness Engineering / Agent Framework Design)**: Add this
  source's four-primitive framing (Claim 4: context, tools, resumability,
  long-running work) as a third, independent vendor's compact statement of
  what a production agent framework must provide beyond web-application
  infrastructure — cross-reference alongside the HumanLayer and Anthropic
  harness taxonomies (Claim 3's four best-practice primitives — filesystem
  agents, skills, compaction, subagents — as corroborating detail for why
  these specific building blocks recur across independently-built frameworks).

- **Chapter 02 (Harness Engineering) — agent use-case selection**: Add Claim 5's
  heuristic ("a repetitive task that still requires some reasoning... not just
  fixed automation, because the system has to interpret the situation and
  decide what to do") as a concrete decision rule for when a task is
  agent-appropriate versus better served by a deterministic script — this is a
  business-process-oriented complement to the corpus's mostly coding-agent-
  centric use-case guidance.

- **Chapter 02 (Harness Engineering) — autonomy calibration**: Add Claim 6's
  task-shape-dependent framing (well-defined output → autonomous loop;
  careful/surgical work → frequent human check-ins) as a named, reusable rule
  for deciding how tightly to keep a human in the loop, explicitly rejecting
  both "always autonomous" and "always human-in-the-loop" as universal
  answers.

- **Chapter 02 (Harness Engineering) — skills rationale**: Add Claim 9's
  "skills forward-correct stale training-data knowledge about your own
  deprecated products" framing (with the Vercel Postgres example) as a
  distinct, concrete motivation for publishing skills, alongside the existing
  "don't restate the obvious" design principle from
  `blog-anthropic-claude-code-skills-lessons.md`.

- **Chapter 04 (Context Engineering) or a new "agent-facing web" note**: Add
  Claims 10-11 (serving Markdown to agent requests, HTML to human requests, at
  the same URL) as a concrete, novel pattern for making a company's own website
  legible to agentic traffic — flag that the underlying traffic-trend numbers
  are referenced but not given in this source, so any guide claim about the
  *scale* of the bot-vs-human traffic shift should cite Vercel's original
  traffic report directly, not this interview.

- **Chapter 06 (Team Adoption) or wherever collaboration patterns are
  discussed**: Add Claim 12 ("multiplayer agent development") as a named,
  currently-unsolved problem — teammates who each use agents individually lack
  a mechanism to share discovered techniques/context with each other. Flag
  this as an open problem in the source, not a documented solution.

## Extraction Notes

1. **WebFetch produced only a five-bullet AI-generated summary, not verbatim
   text** — consistent with MINER.md §2a's warning that a summarizing pass can
   paraphrase quotes (its bracketed insertions like "task[s]" and "serve[s]"
   were themselves signs of paraphrase, not direct quotation). Per that same
   section's guidance, the raw page was instead fetched directly via `curl`
   and HTML-stripped to plain text; the site renders the full interview
   server-side with no paywall gate, so the complete transcript was recovered
   this way. Every `Quote` field in this note was located character-for-character
   in that raw-text capture before being used, not taken from the WebFetch
   summary pass.
2. **No linked sub-pages to follow.** Unlike some other Latent Space/Vercel
   sources in this corpus, this article contains no inline links to other
   Vercel blog posts, `eve` documentation, or the specification sites it
   discusses (skills.sh, the eve framework repo, or the "published reports" on
   bot traffic referenced in Claim 10) — nothing met MINER.md §1's "follow up
   to 5 linked pages that seem substantive" bar because no such links exist in
   the page content that was fetched.
3. **The bot-traffic-trend claim (part of Claim 10) is a reference, not a
   self-contained data point.** Qu refers to "reports" Vercel has "published"
   showing bot traffic rising and human traffic flat/declining, but no report
   is named, linked, or quantified in this interview. This is flagged
   explicitly in Claim 10's confidence rating and Our Assessment — if this
   traffic trend becomes load-bearing for the guide, the underlying Vercel
   report should be separately sourced and mined rather than cited through
   this secondhand mention.
4. **No contradictions identified; no contradiction issue filed.** This
   source's claims are novel extensions or corroborations of existing corpus
   material, not disagreements with any existing source note (see
   Cross-References → Contradicts).
5. **Confidence calibration: emerging.** Andrew Qu is a highly credible
   first-party source (named engineering lead for the exact framework
   discussed), and several individual claims are rated `settled` where they
   are unambiguous, checkable statements (Claim 1's biography). However, the
   overall confidence is `emerging` because: (a) this is a single Q&A
   interview transcript with no independent verification, benchmark data, or
   named third-party customer evidence anywhere in the piece; (b) most claims
   are qualitative design philosophy and origin narrative rather than
   measured outcomes; (c) at least one claim (Claim 10's traffic trend)
   references external evidence not included or linked in this source; and
   (d) two claims (Claim 12, Claim 13) are explicitly forward-looking
   priorities/strategy statements rather than descriptions of a fully shipped,
   independently verifiable state.
