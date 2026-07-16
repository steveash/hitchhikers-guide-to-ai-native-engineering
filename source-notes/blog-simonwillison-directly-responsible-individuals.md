---
source_url: https://simonwillison.net/2026/Jul/12/directly-responsible-individuals/
source_type: blog-post
title: "Directly Responsible Individuals (DRI)"
author: Simon Willison
date_published: 2026-07-12
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1916"
---

# Directly Responsible Individuals (DRI)

> Willison argues that LLM-powered agents should never be designated the
> "Directly Responsible Individual" (DRI) for a project because accountability
> is uniquely human — grounding the claim in Apple/GitLab's DRI role
> definition and IBM's 1979 "a computer can never be held accountable"
> training slide.

## Source Context

- **Type**: blog-post (link-blog entry on simonwillison.net, a "Link Blog"
  post — Willison's short-form commentary format that quotes/links a primary
  source and adds his own reaction, rather than a long-form essay)
- **Author credibility**: Simon Willison is a high-signal, widely-cited
  independent commentator on LLM tooling and engineering practice (co-creator
  of Django, creator of Datasette, prolific writer on applied LLM use). This
  post is opinion/commentary, not empirical research — the credibility here
  is "worth listening to," not "peer reviewed." Willison explicitly frames
  the claim as his own view ("I don't think..."), not as settled doctrine.
- **Scope**: The post is three short paragraphs. It (1) surfaces a definition
  of "Directly Responsible Individual" from the GitLab handbook, noting the
  term originated at Apple; (2) states Willison's position that an agent
  should never be considered a project's DRI; (3) cites IBM's 1979 training
  slide as supporting precedent. It does not cover implementation mechanics
  (how to structure agent oversight, what a human DRI should actually do
  with agents reporting to them, escalation design) — those are covered by
  other corpus sources (see Cross-References). To fill in definitional and
  provenance context that the post links to but doesn't restate, I followed
  the two links in the post: the GitLab handbook DRI page, and Willison's own
  earlier (Feb 2025) post about the IBM slide's origin.

## Extracted Claims

### Claim 1: The clearest available definition of "Directly Responsible Individual" (DRI) — a term Willison identifies as originating at Apple — is a person "ultimately accountable for the success or failure of a specific project, initiative, or activity," per the GitLab handbook
- **Evidence**: Willison's own research, citing the GitLab handbook's DRI
  page as the best definition he found after "going" looking for one (per
  the page's own meta description). The GitLab handbook page itself
  attributes the term's origin to Apple.
- **Confidence**: settled (definitional citation to a public, checkable
  source — the GitLab handbook page)
- **Quote**: "I went looking for a definition of \"Directly Responsible
  Individuals\" and the best I found was in the GitLab handbook. Apparently
  the term originated at Apple, where it's used to describe the person who
  is \"ultimately accountable for the success or failure of a specific
  project, initiative, or activity\"."
- **Our assessment**: This is a useful, precise definition to anchor
  organizational-accountability language in the guide. "Ultimately
  accountable for success or failure" is a stronger and more specific bar
  than generic phrases like "owns the project" — it implies a single named
  person bears the consequences, good or bad, which is exactly the property
  Willison argues agents cannot hold.

### Claim 2: Willison's core position — an agent should never be considered the DRI for a project, because accountability is a uniquely human capacity
- **Evidence**: Stated directly as personal opinion, with an explicit
  causal claim ("because humans can take accountability... where machines
  cannot").
- **Confidence**: emerging (this is a normative argument/opinion from a
  credible commentator, not an empirical finding — it is a position other
  sources in the corpus independently converge on, which raises its
  practical weight, but it remains an argued stance rather than measured
  data)
- **Quote**: "I don't think an agent should ever be considered the DRI for
  a project - that's something that feels uniquely human to me, because
  humans can take accountability for their actions where machines cannot."
- **Our assessment**: This is the load-bearing claim of the post and the
  most guide-relevant one. It's a clean, quotable governance principle:
  whatever authority an agent is delegated, final accountability for
  outcomes should route to a named human. This aligns with — and gives a
  named organizational-design term to — the "designated principal" and
  "chain of command" requirements independently argued in
  `blog-jetbrains-agentic-ai-governance.md` and
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` (see
  Cross-References). Willison doesn't address the harder edge cases (e.g.,
  can an agent be the DRI for a narrowly-scoped, low-stakes internal task?
  what happens when a human DRI is themselves mostly rubber-stamping agent
  decisions?) — those are left as open questions for the guide to address
  rather than answered by this source.

### Claim 3: Willison offers IBM's 1979 internal training slide — "A computer can never be held accountable, therefore a computer must never make a management decision" — as supporting precedent for the no-agent-DRI position
- **Evidence**: A direct link to, and quote of, an IBM internal training
  slide from 1979, framed as historical/institutional precedent for
  distrusting machine decision-making authority.
- **Confidence**: anecdotal (the slide is described by Willison himself, in
  the linked Feb 2025 post, as being of uncertain provenance — see
  Extraction Notes)
- **Quote**: "(See also IBM's legendary 1979 training slide that states
  \"A computer can never be held accountable, therefore a computer must
  never make a management decision.\")"
- **Our assessment**: The quote is rhetorically effective and worth citing
  for its historical framing, but its evidentiary weight is weaker than it
  first appears. Per Willison's own earlier investigation (linked from this
  post — see Extraction Notes), the original slide's physical copy was
  destroyed in a flood, IBM's own archives could not locate it, and its
  earliest confirmed public appearance is a 2017 tweet reporting it as
  found among a retiree's papers. That's "plausible period artifact with
  undocumented chain of custody," not "verified IBM corporate policy
  document." The guide should cite it as a rhetorical touchstone/aphorism,
  not as documented IBM history.

### Claim 4 (from linked GitLab handbook): A DRI has final decision-making power but is expected to consult stakeholders before deciding — DRI is not a synonym for unilateral authority
- **Evidence**: GitLab handbook's own description of the DRI role, fetched
  from the page Willison links to as his source definition.
- **Confidence**: settled (first-party organizational-policy description
  from GitLab's own public handbook)
- **Quote**: "The DRI has final decision-making power but should consult
  and collaborate with relevant stakeholders to gather input and divide
  tasks effectively."
- **Our assessment**: This nuance matters for the guide because it clarifies
  what "DRI" actually authorizes: final say, not solitary decision-making.
  If the guide adopts DRI language for human ownership of agent
  configuration/deployment (as `blog-anthropic-large-codebase-best-practices.md`
  already does for Claude Code configuration ownership), it should carry
  this consult-then-decide expectation forward, not just the "final
  decision-making power" half.

### Claim 5 (from linked GitLab handbook): DRIs are not required to justify every decision to avoid analysis paralysis, but the framework's value depends on there being exactly one such person per project/task, not a diffuse group
- **Evidence**: GitLab handbook's stated rationale for the DRI model.
- **Confidence**: settled (first-party organizational-policy rationale)
- **Quote**: "DRIs do not owe explanations for their decisions to avoid
  analysis paralysis"
- **Our assessment**: This is the practical mechanism by which DRI avoids
  becoming committee-by-another-name: a single named person can act without
  re-litigating the decision with every stakeholder. This is a direct
  argument against having an agent (or a diffuse "the team" / "the model")
  hold this role even loosely — if no single human owns the "no
  explanation owed" authority, the DRI model's core efficiency benefit is
  lost regardless of whether an agent is technically doing the work.

### Claim 6 (from Willison's linked Feb 2025 post): The IBM 1979 slide's chain of custody is itself unverified — the physical original was reportedly destroyed in a flood, and IBM's own archives could not locate a copy
- **Evidence**: Willison's own earlier investigation, in which he asked
  publicly for the original source and relayed the replies he received.
- **Confidence**: anecdotal (secondhand social-media-sourced account of an
  artifact's provenance, explicitly flagged by Willison as uncertain)
- **Quote**: "It was found by someone going through their father's work
  documents, and subsequently destroyed in a flood." / "I spent some time
  corresponding with the IBM archives but they can't locate it."
- **Our assessment**: Included specifically to caveat Claim 3 — see that
  claim's assessment. This is the kind of detail a careless extraction
  would drop (it isn't in the July 2026 post itself, only reachable via the
  link), which is exactly the sort of provenance-checking MINER.md's
  quote-verification step exists to catch.

## Concrete Artifacts

### GitLab handbook's DRI role structure (linked source, not restated in Willison's post)

```
Directly Responsible Individuals (DRI) — GitLab Handbook
(https://handbook.gitlab.com/handbook/people-group/directly-responsible-individuals/)

Definition:
  "Apple coined the term 'directly responsible individual' (DRI) to refer
  to the ultimately accountable for the success or failure of a specific
  project, initiative, or activity."

Empowering DRIs:
  - DRIs do not owe explanations for their decisions (avoids analysis
    paralysis)
  - Should welcome input from others but are not required to convince or
    justify their choices
  - Prevents projects "flying under the radar" from fear of endless
    explanation cycles

Collaboration expectation:
  - DRIs must consult with all relevant teams and stakeholders
  - Gather context, input, and feedback before deciding
  - While empowered to decide, should leverage team expertise and judgment

Characteristics of a Project DRI:
  - Most often assigned at the task level (example given: Product Manager
    is DRI for prioritization, Engineering Manager is DRI for delivery)
  - As managers of one, team members are most often the DRI for the tasks
    they personally accomplish
```

### IBM 1979 training slide — text and provenance

```
Text of the slide (as quoted by Willison, July 2026 and Feb 2025 posts):
  "A computer can never be held accountable
   Therefore a computer must never make a management decision"

Provenance (from Willison's Feb 2025 post, "A computer can never be
held accountable"):
  - Willison asked publicly (June 2024, on Twitter/X) for the original
    source
  - Reply from Jonty Wareing: found by someone going through their
    father's work documents; the physical original was "subsequently
    destroyed in a flood"
  - Willison: "I spent some time corresponding with the IBM archives but
    they can't locate it."
  - Earliest confirmed public appearance identified: a February 2017
    tweet from @bumblebike, which places it as from 1979 internal IBM
    training
```

## Cross-References

- **Corroborates**: `blog-anthropic-large-codebase-best-practices.md`
  (Claim 14: the minimum viable organizational structure for large-codebase
  Claude Code deployment is a human DRI with authority over the
  configuration stack). That note establishes DRI as the practical
  ownership model for Claude Code configuration but doesn't argue *why* the
  DRI must be human rather than an agent. This source supplies that
  governance rationale directly: accountability is a human-only property,
  so the DRI role — by definition the party who is "ultimately
  accountable" — cannot be assigned to an agent even where the agent does
  most of the operational work.
- **Corroborates**: `blog-jetbrains-agentic-ai-governance.md` (Claim 3:
  agentic systems need a defined chain of command — a specific person or
  function with authority over the outcome who monitors behavior and
  intervenes when the system drifts). Willison's DRI framing gives that
  requirement a concrete, named organizational-design term ("DRI") rather
  than the more generic "chain of command."
- **Corroborates**: `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`
  (Claim 1: the Andon Labs autonomous retail agent's governance failure was
  structural — "no governance document, no designated principal, no clear
  liability chain"; Claim 5: the framework's manual-oversight tier requires
  a "designated principal + human-written core mandate"). "No designated
  principal" is precisely the gap Willison's post argues against — Andon
  Labs is a concrete real-world case of what happens when nobody holds the
  DRI role for an autonomous agent's actions.
- **Corroborates**: `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`
  (Claim 4: governance cannot be retrofitted onto an agent platform after
  deployment — it must be built into the operating environment's "original
  DNA," including human escalation). Consistent with Willison's argument
  that human accountability has to be structurally assigned, not assumed.
- **Extends**: `blog-simonwillison-udell-human-agent-loop.md` (Claim 9: the
  phrase "human in the loop" is objectionable because it cedes authority to
  the machines; the correct framing is that it is the human's loop, into
  which agents are recruited). Same author, same underlying philosophy —
  human agency/accountability as the organizing frame for agentic work —
  but a different post and a different angle: Udell/Willison's other post
  is about day-to-day engagement in a workflow, this post is about formal
  organizational accountability for a project's outcome. Together they
  argue for human centrality at both the workflow level and the governance
  level.
- **Novel**: No existing corpus note applies the specific "DRI" (Directly
  Responsible Individual) organizational-design term to the question of
  agent accountability, or traces the IBM 1979 slide's actual (uncertain)
  provenance. This source is the first to name the Apple/GitLab DRI
  framework explicitly as the vocabulary for "who is accountable when an
  agent is involved."

## Guide Impact

- **Chapter 05 (Team Adoption) — Organizational Structure**: The existing
  DRI recommendation (from `blog-anthropic-large-codebase-best-practices.md`,
  currently framed narrowly around Claude Code configuration ownership)
  should be broadened using this source's definition and rationale: DRI
  means "ultimately accountable for success or failure," and the reason it
  must be a named human — not a role an agent can hold, even informally —
  is that accountability itself doesn't transfer to a machine. Recommend
  adding a short explicit statement to Ch05: "however much of the work an
  agent performs, assign a human DRI who is accountable for the outcome."
- **Chapter 06 (Security and Threat Model)**: The "no designated principal"
  failure mode from the Andon Labs case
  (`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`) and the
  chain-of-command requirement from
  `blog-jetbrains-agentic-ai-governance.md` are both about the same
  structural gap this source names. Recommend a "who is the DRI for this
  agent's actions?" checklist question in whatever threat-model /
  pre-deployment section exists, citing this source for the underlying
  accountability principle and the two Thoughtworks/JetBrains sources for
  concrete failure modes and control mechanisms.
- **Framing note for the guide's tone**: When citing the IBM 1979 slide (if
  the guide chooses to use it as a memorable aphorism), it should either
  omit the "IBM" institutional attribution or caveat it as an anecdote of
  uncertain provenance rather than documented IBM corporate policy — see
  Claim 6.

## Extraction Notes

- This is a very short link-blog post (three paragraphs). Per MINER.md
  guidance to follow substantive linked pages, I followed both links in
  the post: the GitLab handbook's DRI page and Willison's own earlier
  (Feb 2025) post about the IBM slide's provenance. Both add material,
  checkable context (Claims 4-6) that isn't restated in the July 2026 post
  itself but that the post relies on.
- The WebFetch tool's summarized output for the source URL produced
  inconsistent paraphrases of the GitLab quote across separate calls (one
  version read "ultimate accountability for a specific project, initiative,
  or activity's success or failure," another read "ultimately accountable
  for the success or failure of a specific project"). Because MINER.md
  treats fabricated/paraphrased quotes as a hard rejection criterion, I did
  not trust either WebFetch paraphrase and instead fetched the raw HTML of
  the source page directly via curl and extracted the verbatim text by
  hand. All quotes in this note (from the Willison post, the GitLab
  handbook, and Willison's Feb 2025 post) were taken from that raw-HTML
  extraction, not from a summarizer.
- No contradiction with any existing corpus note was found — this source
  strengthens and names a principle (human-only accountability /
  designated principal) that multiple governance-focused sources already
  converge on independently.
- Confidence is set to `emerging` for the note overall: Claims 1, 4, and 5
  (definitional citations to the public GitLab handbook) are settled as
  descriptions of what GitLab's policy says, but the note's central,
  guide-relevant claim (Claim 2 — agents should never be DRIs) is Willison's
  personal argued position, not an empirical or first-party product claim,
  and Claim 3's supporting evidence (the IBM slide) is explicitly
  anecdotal/uncertain per Claim 6.
