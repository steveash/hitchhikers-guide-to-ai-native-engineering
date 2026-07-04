---
source_url: https://simonwillison.net/2026/Jun/28/jon-udell/
source_type: blog-post
title: "Quoting Jon Udell" (quoting "\"Doctor, it hurts when agents create unreviewable PRs.\" \"Don't do that.\"")
author: Jon Udell (quoted by Simon Willison)
date_published: 2026-06-28
date_extracted: 2026-07-04
last_checked: 2026-07-04
status: current
confidence_overall: anecdotal
issue: "#1503"
---

# Quoting Jon Udell: "Human Agent in the loop"

> Jon Udell reframes "human in the loop" — a phrase he argues cedes authority
> to machines — as "our loop, we recruit agents to join," and grounds the
> reframe in his own experience bootstrapping a 42,000-line desktop app
> (Bram) with Claude Code and Codex while staying "fully engaged" through a
> workflow that breaks tasks into small testable chunks and lifts shared
> context into a local worklist and GitHub repo. He connects the idea to
> Ward Cunningham and Brian Marick's 2008 "visible workings" concept —
> exposing the reasoning behind a system's behavior via an "Explore" button
> — as the model for what agent-assisted development should look like:
> not a black box, but a process whose workings remain visible.

## Source Context

- **Type**: blog-post. Simon Willison's "Quoting" format reproduces two
  paragraphs from Jon Udell's longer post at
  https://blog.jonudell.net/2026/06/28/doctor-it-hurts-when-agents-create-unreviewable-prs-dont-do-that/
  (published the same day, 2026-06-28), under the section heading "Human
  Agent in the loop." Both the Willison quotation post and Udell's full
  original article were read for this note. Udell's article in turn links
  to his own 2008 post,
  https://blog.jonudell.net/2008/03/04/ward-cunninghams-visible-workings/,
  which was also read in full since it supplies the concrete example behind
  the "visible workings" reference in the 2026 post.
- **Author credibility**: Jon Udell is a long-time technology writer and
  practitioner (former InfoWorld columnist, Microsoft Elm City/Hypothesis
  contributor) with a decades-long record of writing about software
  transparency and tooling — the 2008 post he links back to is his own
  first-hand account of a conversation with Ward Cunningham (creator of the
  wiki, co-signer of the Agile Manifesto). The 2026 post is first-person
  practitioner reporting: Udell is the author and sole user of Bram, a tool
  he is actively building with Claude Code and Codex. Simon Willison is a
  widely-read AI-tooling commentator whose "Quoting" posts curate
  high-signal passages; his selection of this specific paragraph signals it
  as the most quotable articulation of the reframe, not necessarily the most
  representative sentence of the full post.
- **Scope**: Covers one practitioner's experience keeping himself "fully
  engaged" while an agent writes code in a language (Rust) he had never used
  before the project; a language breakdown of the resulting codebase; a
  conceptual reframe of "human in the loop" language; and a concrete
  historical example (the Eclipse Foundation portal's "Explore" links) of
  what transparent agent-assisted workflows could look like. Does NOT cover:
  the industrial-scale "unreviewable PRs" problem in any depth beyond a
  one-paragraph anecdote about a talk Udell attended, benchmark data, harness
  configuration specifics (CLAUDE.md/AGENTS.md content), or any claim about
  how this generalizes beyond Udell's own one-person, one-tool project.

## Extracted Claims

### Claim 1: At an industry talk, an engineer described "unreviewable PRs" — thousands of lines of LLM-written changes that people can't make sense of — with "throw more agents at it" (reviewer agents that scan and triage) offered as the solution
- **Evidence**: Udell's first-hand account of attending a talk "by an engineer at a large software company."
- **Confidence**: anecdotal (single secondhand account of an unnamed talk, no company or speaker named)
- **Quote**: "I recently attended a talk, by an engineer at a large software company, on the topic of unreviewable PRs. The problem? When agents raise PRs with thousands of lines of LLM-written adds/deletes/edits, people can't make sense of them. The solution? Throw more agents at the problem: reviewer agents that scan what coding agents have produced, identify problems, and triage them."
- **Our assessment**: This is scene-setting rather than Udell's own claim — he does not name the company or engineer, and immediately positions his own experience as a counter-example rather than a rebuttal grounded in the same problem's scale. It is nonetheless the framing device for the whole post: "more reviewer agents" vs. "stay engaged via workflow" as two different responses to the same underlying volume problem. It corroborates, with an anecdote, the industry-wide review-bottleneck data already in the corpus (see Cross-References).

### Claim 2: Udell reports staying "fully engaged" while building Bram because of the workflow the tool embodies, not despite using agents heavily
- **Evidence**: Udell's direct first-person claim, offered as his answer to the "unreviewable PRs" framing in Claim 1 — he explicitly declines to evaluate the industrial-scale tradeoff ("I don't make software at industrial scale") and instead reports his own experience.
- **Confidence**: anecdotal (single practitioner, one project, self-reported)
- **Quote**: "I don't make software at industrial scale, so I can't evaluate the claim that throughput gain justifies the absence of end-to-end human engagement. What I can say is that as I use Bram to bootstrap itself, I am fully engaged thanks to the workflow embodied in the tool."
- **Our assessment**: Udell is careful to scope his claim — he explicitly refuses to generalize to the industrial-scale review problem from Claim 1. This is a meaningful hedge the guide should preserve: the post is not evidence that workflow design solves the "thousands of lines, can't make sense of them" problem at scale; it is evidence that a specific workflow kept one practitioner engaged on one project.

### Claim 3: Udell reads and understands Rust code that Claude Code and Codex write for him, despite never having written a line of Rust himself, and pushes back "when things don't smell right"
- **Evidence**: Direct first-person claim, grounded in the fact that Bram is a Tauri desktop app (Tauri's native language is Rust) and the language breakdown showing Rust as 24,630 of 42,805 total lines.
- **Confidence**: anecdotal (single practitioner, one project)
- **Quote**: "I have yet to write a single line of Rust! But I read the Rust code that Claude Code and Codex write for me, as they write it. I understand the nature and purpose of that code, and I push back when things don't smell right."
- **Our assessment**: This is a specific, checkable claim about the nature of engagement: reading-for-comprehension-and-pushback in an unfamiliar language, done *as the code is written* rather than after the fact on a finished diff. This is the same "real-time engagement vs. after-the-fact review" distinction that matters for reconciling this post with the corpus's PR-review-bottleneck literature (see Cross-References — Osmani's "human on the loop" framing describes exactly the after-the-fact posture Udell is contrasting himself with).

### Claim 4: Bram's workflow keeps the human engaged by breaking problems into small testable chunks and processing them in an orderly way — a deliberate application of "old best practices" under new pressure
- **Evidence**: Udell's own architectural description of why the workflow works, tied explicitly to the "documentation as part of the product" analogy.
- **Confidence**: anecdotal (design rationale from the tool's sole builder/user)
- **Quote**: "Bram's workflow helps do that by breaking problems into small testable chunks and processing them in an orderly way. That's hardly a novel idea. In the LLM era we are finding new reasons to honor old best practices. We've always said that documentation is an essential part of the product, for example, but we haven't always made it so. Now that readers include both people and machines we invest more effort in the docs. Why not also invite LLMs to join us in conventional agile practices?"
- **Our assessment**: The "small testable chunks" claim is the mechanism underneath Claim 2's "fully engaged" result — it names small-batch, testable decomposition as the specific practice that prevents the "unreviewable PR" outcome from Claim 1 in the first place, rather than trying to review large PRs after the fact. The documentation-as-product-for-machines-too framing directly corroborates existing corpus claims (see Cross-References).

### Claim 5: Bram lifts context that would otherwise be private to individual chat sessions into two shared spaces — a local worklist and the GitHub repository — so both humans and multiple agents (Claude Code, Codex) share the same context
- **Evidence**: Udell's direct architectural description of Bram's context-sharing mechanism.
- **Confidence**: anecdotal (first-person description of one tool's design)
- **Quote**: "Chat sessions build context that's private to LLMs, not shared with a team of people and agents. Bram lifts that context into two kinds of shared spaces: the local worklist and the GitHub repository. On the local worklist you define a task or feature, iterate on its spec, do the task or build the feature, and iterate on outcomes."
- **Our assessment**: This directly names the failure mode of chat-based agent use (context trapped in an ephemeral, single-agent, single-session conversation) and proposes a specific structural fix: externalize the task/spec/outcome cycle into artifacts that live in the repo, not the chat log. This is architecturally close to — but independently arrived at from — the corpus's existing "agents build understanding entirely from searchable text" claim (see Cross-References).

### Claim 6: Bram makes it a one-click operation to switch which agent (Claude Code or Codex) is working on a given worklist item, so one agent's plan or implementation can be weighed in on by the other
- **Evidence**: Udell's direct description, illustrated with an example of "about to bring in Claude as a relief pitcher."
- **Confidence**: anecdotal (single-tool feature description)
- **Quote**: "As shown here, it's a one-click operation to switch between agents so one can weigh in on a plan or implementation written by the other. Here I'm about to bring in Claude as a relief pitcher."
- **Our assessment**: This is a concrete cross-agent-review mechanism distinct from a dedicated "reviewer agent" (the approach criticized implicitly via Claim 1's "throw more agents at the problem") — instead of a specialized reviewer role, the *same class* of general-purpose coding agent is swapped in to critique the other's work on the same shared worklist item. It is a lightweight, tool-level implementation of a generator/critic pattern using interchangeable general agents rather than a dedicated verifier agent.

### Claim 7: Agents produce evocative, serviceable names for worklist items that Udell would not want to spend his own cognitive effort inventing
- **Evidence**: Udell's direct observation, with a specific example name he says he could have conjured himself but didn't need to.
- **Confidence**: anecdotal (single observation)
- **Quote**: "One of the delightful emergent properties of this system has been the evocative names that agents create for worklist items. Naming is famously hard. I could conjure a name like startup-freeze-tail-fanout-diagnostics on my own but these names aren't public-facing, they are perfectly serviceable, there is no reason for me to bear the cognitive load of creating them."
- **Our assessment**: A small but concrete example of task delegation that isn't about code generation — offloading a genuinely tedious, low-stakes naming task to the agent because the names are internal/searchable rather than public-facing, so quality bar is "serviceable" rather than "excellent."

### Claim 8: Udell prunes his worklist to roughly five to seven active items because human context windows can only handle that many things at once, using the tool's history/search to resurrect dropped items later
- **Evidence**: Udell's direct statement of his own working-memory constraint and the tool mechanism (Drop button, History page, search) that accommodates it.
- **Confidence**: anecdotal (single practitioner's self-reported working style)
- **Quote**: "Our human context windows can handle about five to seven things at a time, so I prune the worklist accordingly. If other things come up that bump the priority of startup-freeze-tail-fanout-diagnostics I can use the Drop button to clear it from the worklist. Then I can refind it on the History page, perhaps by searching for fanout, and ask the active agent to resurrect it as a new worklist item."
- **Our assessment**: This is a specific, actionable pattern for managing human attention (not agent context) alongside agent work: bound the active worklist to human working-memory capacity (~5-7 items) and rely on a searchable history rather than trying to keep everything active.

### Claim 9: The phrase "human in the loop" is objectionable because it cedes authority to the machines; the correct framing is that it is the human's loop, worked the same way as always, into which agents are recruited
- **Evidence**: Udell's direct, explicitly stated opinion, presented as the section's thesis.
- **Confidence**: anecdotal (opinion/framing claim, not an empirical one)
- **Quote**: "I dislike the phrase \"human in the loop\" because it cedes authority to the machines. Let's flip the narrative. It's our loop, we work the same way we always have, now we recruit agents to join the team. An agent-assisted process need not be a black box that takes in prompts and emits features."
- **Our assessment**: This is the post's central, most quotable claim and the reason it was triaged as high-novelty. It is a terminology/framing argument, not an empirical one — its value is normative and rhetorical: it names an implicit assumption in common usage ("in the loop" implies the loop belongs to something/someone else) and proposes a replacement framing that keeps authority explicitly with the human team. This directly complements — while operating at a different level from — the corpus's existing "human on the loop" framing (see Cross-References for the distinction between Udell's "our loop we invite agents into" and Osmani's "human on the loop: sampling, spot-checking, auditing").

### Claim 10: Ward Cunningham once implemented and demoed a concept Brian Marick called "visible workings" — making an Eclipse Foundation business-process workflow visible to end users via an "Explore" button next to the ordinary form UI, letting anyone inspect the business rule that motivated the form, before the user commits an action
- **Evidence**: Udell's account of a personal conversation with Ward Cunningham, corroborated by his own 2008 blog post on the same topic (https://blog.jonudell.net/2008/03/04/ward-cunninghams-visible-workings/), which describes the mechanism in more detail: a "swim" visualization laying out workflow steps and results in a table with a column per actor, reachable both by developers testing the system and by end users mid-form via the Explore link.
- **Confidence**: anecdotal (single historical anecdote, corroborated by the author's own contemporaneous 2008 account)
- **Quote**: "I'm reminded of a beautiful idea of Brian Marick's that Ward Cunningham once implemented and demoed to me. Brian called it visible workings. Ward's implementation made an Eclipse Foundation workflow visible. When the UI presented a form, it added an Explore button that you could use to inspect the business rule that motivated the form."
- **Additional quote** (from the linked 2008 post, corroborating detail): "This isn't just an innovative approach to software testing and workflow visualization. It's also a radical statement about business process transparency. For most of us, most of the time, business systems are black boxes whose internal workings we can only discern in the outcomes of our (often painful) interactions with them. But what if you could find out, before pressing the Save button, what's going on in that black box?"
- **Our assessment**: This is the most novel and concrete idea in the source: a 2008 pre-LLM precedent for exposing "why does the system behave this way" directly in the interface, rather than requiring a separate investigation. Udell explicitly repurposes it as the model for agent-assisted development: not "trust the diff," but "surface the reasoning" as a first-class, always-available interface element — the direct opposite of the "black box that takes in prompts and emits features" framing from Claim 9. No existing corpus source discusses Ward Cunningham, Brian Marick, or "visible workings"; this is a genuinely new concept for the corpus (see Cross-References — Novel).

### Claim 11: Udell's proposed practice for agentic software development is to treat it as a loop humans invite agents into, not one humans have been excluded from
- **Evidence**: Udell's closing sentence, the direct payoff of Claims 9-10 combined.
- **Confidence**: anecdotal (normative conclusion, not empirically tested)
- **Quote**: "Let's do agentic software development like that. Not as a loop we've been excluded from, instead as one we invite agents into."
- **Our assessment**: This is the post's thesis restated as a call to action, tying the terminology reframe (Claim 9) to the visible-workings model (Claim 10) as the concrete mechanism for making the reframe real rather than just rhetorical — an "our loop" claim is only credible if the workings actually stay visible (Claim 10), which is what Bram's shared worklist/repo context (Claims 5-6) attempts to deliver in practice.

## Concrete Artifacts

### Bram language breakdown (from Udell's post)
```
Source: Jon Udell, "'Doctor, it hurts when agents create unreviewable PRs.'
'Don't do that.'", blog.jonudell.net, 2026-06-28

Language      | Lines of code
--------------|---------------
Rust          | 24,630
JavaScript    | 7,542
XMLUI         | 4,149
Python        | 3,152
Markdown      | 1,419
XS (XMLUI)    | 742
Total         | 42,805

Context: Bram is a Tauri desktop app; Tauri's native language is Rust,
which is why Rust dominates despite Udell never having written Rust
before this project (github.com/judell/bram).
```

### The "visible workings" mechanism (from Udell's 2008 post, referenced in the 2026 post)
```
Source: Jon Udell, "Ward Cunningham's implementation of Brian Marick's
'Visible Workings'", blog.jonudell.net, 2008-03-04

- Portal: Eclipse Foundation member portal (member-only workflows:
  electing committers, scheduling project reviews)
- Public artifact: anyone (not just members) could explore the portal's
  own test scripts for these workflows
- Example workflow: "Change Personal Address"
  - "see" a test script that exercises the workflow
  - "run" the test script and inspect results (interleaved script lines +
    screenshots/emails)
  - "swim" the test: steps and results laid out in a table, time advancing
    down the rows, one column per actor in the workflow
- End-user-facing surface: next to the ordinary "Save" button on the
  address-change form, an "Explore" link let any user pop open the same
  swim visualization the developers used to test the feature — before
  committing the action
- Ward Cunningham's own framing (quoted in the 2008 post, from Ward's
  blog): "The MyFoundation portal, once again, respects the curiosity and
  intellect of its users by exposing all aspects of the processes it
  supports. Who asked for this? No one. No one thought to. That doesn't
  mean it isn't needed."
- Brian Marick's framing (quoted in the 2008 post): "Can we make filling
  out a form more like a conversation than an interrogation? ... These
  links let you ask a question every now and then. You get to ask, 'why
  do you ask?'"
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-agentic-code-review.md` Claim 2 (Faros AI: PRs merging
    with zero review up 31.3%, median review duration up 441.5%) — Udell's
    Claim 1 anecdote (an unnamed engineer describing "unreviewable PRs" and
    reviewer-agent triage as the industry response) is a first-person
    conference-talk corroboration of the same review-capacity crunch Osmani's
    post documents with quantified 2026 datasets. Udell offers no numbers of
    his own; the value is a second, independent anecdotal sighting of the
    same phenomenon Osmani's post quantifies.
  - `blog-anthropic-human-agent-teams.md` Claim 3 ("Agents build their
    understanding entirely from the text a team makes searchable... if it's
    not written down and accessible, it doesn't exist") — Udell's Claim 5
    (chat-session context is private to LLMs; Bram lifts it into a shared
    worklist and the GitHub repo) independently describes the same
    text-only-visibility constraint from the tool-builder's side: the fix
    for "agents only see what's written down" is to make the worklist/spec
    itself a written, repo-resident artifact rather than leaving it in an
    ephemeral chat transcript.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 2 ("the human
    engineer evaluates whether the agent actually solved the right
    problem") — Udell's Claim 3 (reading and understanding Rust code he
    never wrote himself, pushing back when it "doesn't smell right") is a
    concrete, first-person instance of exactly this supervisory-evaluation
    posture, grounded in a specific project rather than stated as an
    abstract principle.

- **Contradicts**: None filed. There is a real tension worth flagging for
  the Smith without escalating to a contradiction issue: `blog-addyosmani-
  agentic-code-review.md` Claim 11 argues the effective posture under
  agent-generated volume is "human on the loop" — sampling, spot-checking,
  auditing rather than reading every diff — while Udell's Claim 3 describes
  reading every line of Rust "as they write it." Per MINER.md §4a, this
  reads as a conditioning-variable difference rather than a material
  contradiction: Osmani's claim is about after-the-fact review of merged/
  proposed PRs at team/organizational scale under high volume; Udell's claim
  is about real-time engagement on a single-developer, single-project
  bootstrap effort where volume is not the constraint. Both sources could be
  correct simultaneously depending on team size and PR volume — this is a
  scale-conditioning variable, not two claims about the same situation
  reaching opposite conclusions.

- **Extends**: `blog-ronacher-clanker-terminology.md` Claim 3 ("If my coding
  tool opens a pull request, I opened that pull request, not the machine.")
  — Ronacher's claim establishes human responsibility-attribution for
  agent-authored changes; Udell's Claim 9 extends the same underlying idea
  from responsibility to authority and vocabulary specifically — arguing not
  just that humans are accountable for agent output, but that the very
  phrase used to describe human-agent collaboration ("in the loop") should
  be replaced because it implies humans are subordinate participants in a
  process the machine runs, rather than the reverse.

- **Novel**:
  - **The "human in the loop" → "our loop, agents invited in" terminology
    critique**: no existing corpus source directly critiques the phrase
    "human in the loop" itself as ceding authority; this is a new framing
    argument, distinct from (though complementary to) Osmani's "human on the
    loop" posture-shift framing, which does not challenge the "in the loop"
    phrase's implied authority structure at all.
  - **Ward Cunningham / Brian Marick's "visible workings" (2008) as a
    pre-LLM precedent for agent transparency**: no existing corpus source
    mentions Ward Cunningham, Brian Marick, or "visible workings." This is
    a genuinely new historical reference point — a concrete, seventeen-plus-
    year-old example of exposing the reasoning behind system behavior
    directly in a production UI, offered as the model for what agent-
    assisted development's transparency should look like.
  - **One-click agent-swap for self-review** (Claim 6): using a second
    general-purpose coding agent (not a dedicated reviewer/verifier agent)
    to critique the first agent's plan or implementation on the same shared
    worklist item is a lightweight cross-review mechanism not previously
    documented in the corpus's generator/verifier pattern discussions, which
    typically assume a distinct verifier role rather than an interchangeable
    peer agent.
  - **Human working-memory-bounded worklist pruning** (Claim 8): bounding
    the *human's* active attention to ~5-7 worklist items (as opposed to
    managing the *agent's* context window) with a searchable history for
    resurrection is a specific human-attention-management pattern not found
    elsewhere in the corpus, which more often discusses agent context
    management than human working-memory constraints.

## Guide Impact

- **Chapter 00 (Principles)**: Add the "our loop, not their loop" reframe
  (Claim 9) as a stated principle for how the guide talks about human-agent
  collaboration generally — the guide should prefer language that keeps
  human authority explicit (e.g., "agents join the team's existing process")
  over language that implies agents run the process and humans intervene
  from outside it (e.g., "human in the loop" used as a gate/checkpoint
  metaphor). Cite this source for the specific critique of "in the loop"
  phrasing.

- **Chapter 01 (Daily Workflows)**: Add Claim 4 (breaking work into small,
  testable chunks processed in order) and Claim 8 (bounding the active
  worklist to ~5-7 items, matching human working-memory capacity, with
  searchable history for resurrection) as concrete daily-workflow practices
  for staying engaged with agent output without being overwhelmed by it —
  this is a distinct, tool-agnostic practice from context-window management
  for the agent itself.

- **Chapter 03 (Verification)**: Add the "visible workings" concept (Claim
  10) as an aspirational design goal for how agent-produced changes should
  be reviewable: not just a diff, but an accessible "why" — the business
  rule or reasoning behind a change, inspectable on demand, analogous to the
  Eclipse Foundation portal's "Explore" button. Pair this with Claim 1 (the
  "unreviewable PRs" problem) as the concrete failure mode this design goal
  addresses, and with `blog-addyosmani-agentic-code-review.md` Claims 8-9
  (decision logs capturing agent's stated goal and rejected alternatives) as
  a more immediately implementable version of the same idea using today's
  PR tooling rather than a custom "Explore" UI.

- **Chapter 05 (Team Adoption)**: Cite Claim 9 (the "human in the loop"
  terminology critique) alongside `blog-addyosmani-agentic-code-review.md`
  Claim 11 ("human on the loop") as two related but distinct framings teams
  can choose between depending on context: Udell's "our loop, agents
  invited in" fits small teams/individual builders staying engaged in
  real time; Osmani's "human on the loop" (sampling/auditing) fits
  higher-volume team settings where reading every diff is not feasible. The
  guide should present these as complementary postures for different scales
  rather than picking one as universally correct (see Cross-References —
  Contradicts, for why this is a conditioning variable, not a contradiction).

## Extraction Notes

- The Simon Willison page (https://simonwillison.net/2026/Jun/28/jon-udell/)
  is a minimal "Quoting" post: it reproduces two paragraphs from Udell's
  "Human Agent in the loop" section (with a "[...]" mid-paragraph ellipsis
  marking Willison's own trim) and links to the full original. All claims
  beyond Claims 9 and 11 derive from the full article at
  blog.jonudell.net, which was fetched and read in its entirety.
- WebFetch declined to reproduce Udell's full article verbatim in one pass
  and offered summaries instead ("I can't reproduce the entire blog post
  verbatim... That would constitute reproducing substantial copyrighted
  content in full"). To satisfy the verbatim-quote requirement, the
  underlying HTML for both the Simon Willison page and both Jon Udell pages
  (the 2026 post and its linked 2008 "visible workings" post) was fetched
  directly via `curl` and parsed with a local script (tags stripped,
  entities unescaped, links preserved as inline markers) rather than routed
  through WebFetch's summarizing model. Every quote in this note is copied
  character-for-character from that directly-fetched, unprocessed HTML
  text — not reconstructed from a WebFetch summary. This is a more reliable
  provenance path than the WebFetch-targeted-refetch pattern used in several
  other corpus notes (see their Extraction Notes), and the Assayer can
  re-verify by fetching the same three URLs directly.
- The three Prospector triage comments on issue #1503 (there are three,
  apparently from repeated auto-triage runs) converged on different but
  compatible chapter sets (Ch00/01/05; Ch03/05; Ch01/02-03/04). This note's
  Guide Impact section covers Ch00, Ch01, Ch03, and Ch05, which is the union
  of chapters actually supported by specific claims in the source; Ch02 and
  Ch04 relevance mentioned in the third triage comment was considered but
  not included, since no claim in this source speaks to harness-configuration
  mechanics (CLAUDE.md/AGENTS.md content) or context-engineering techniques
  specifically — Claims 5-6 (shared worklist/repo context, agent-swapping)
  are closer to a workflow/tool description than a context-engineering
  technique, and are covered under Ch01 instead.
- No contradiction issue was filed. The one tension identified (Udell's
  "read every line as it's written" vs. Osmani's "human on the loop"
  sampling posture) was assessed against MINER.md §4a's criteria and judged
  to be a scale/context conditioning variable (single-developer real-time
  engagement vs. team-scale after-the-fact review under volume), not a
  material contradiction — both sources are cited together in Guide Impact
  above with that distinction made explicit.
- Cross-references verified: `blog-addyosmani-agentic-code-review.md`
  Claims 2 and 11, `blog-anthropic-human-agent-teams.md` Claim 3,
  `blog-thoughtworks-gall-supervisory-engineering.md` Claim 2, and
  `blog-ronacher-clanker-terminology.md` Claim 3 were each re-read in the
  cited note before this note was written, and the quoted text above for
  each is copied verbatim from those notes rather than reconstructed from
  memory.
- Confidence rated **anecdotal** overall: every claim in this source is
  first-person, single-practitioner, single-project observation (Udell
  building one tool for himself) or a single secondhand anecdote (the
  unnamed conference talk in Claim 1) or a decades-old personal recollection
  (Claim 10). Nothing here is empirically measured or independently
  corroborated by a second first-party account of the same tool. The value
  of the source is conceptual/framing (the terminology critique, the
  visible-workings precedent), not evidentiary weight.
