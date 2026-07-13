---
source_url: https://www.latent.space/p/software-factories
source_type: blog-post
title: "Warp CEO Zach Lloyd on why software factories are the next phase of coding"
author: Richard MacManus (interviewer, Latent Space) / Zach Lloyd (interviewee, CEO, Warp)
date_published: 2026-07-01
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: anecdotal
issue: "#1819"
---

# Warp CEO Zach Lloyd on why software factories are the next phase of coding

> A written Q&A interview (Latent Space, 2026-07-01) with Warp CEO Zach Lloyd,
> conducted immediately after his AI Engineer World's Fair (AIEWF) keynote on
> software factories. Lloyd traces Warp's product arc — Rust terminal (2021) →
> terminal-with-agents (open-sourced April 2026) → Oz, a cloud agent
> orchestration platform for "software factories" — and describes factories as
> automating the full engineering loop (triage, spec, implementation, review,
> verification, shipping, monitoring) while integrating into existing tools
> (Jira/Linear, Slack/Teams, GitHub) rather than replacing them. He predicts
> gradual, per-repo adoption (20% → 30-60% automated PRs) and that within a
> year every significant software project will run "something resembling a
> factory," comparable to GitHub or CI/CD becoming standard practice.

## Source Context

- **Type**: blog-post (written Q&A interview, not a podcast transcript or
  conference dispatch)
- **Author credibility**: Richard MacManus is the interviewer/writer for this
  Latent Space piece, and states in his framing that he has "been covering
  Warp for a couple of years now" and interviewed Lloyd previously. The
  substantive claims come from Zach Lloyd, Warp's CEO, speaking about his own
  company's product strategy and pivot — first-person practitioner/founder
  testimony, not third-party analysis. This is a single-company, single-
  executive account with an obvious commercial interest in the "software
  factory" thesis Warp has built its product around.
- **Scope**: Covers Warp's product history and rationale for the Oz pivot, the
  definition and origin of the "software factory" term as Lloyd uses it, how
  Oz integrates with existing developer tools, the framing of "factory
  engineering" as a new discipline, forward-deployed-engineering-style
  transformation work, Warp's own use of Oz to manage its open-sourced CLI,
  and Lloyd's 12-month adoption prediction. Does not cover: Oz's technical
  architecture in implementation detail (no model names, latency numbers, or
  system diagrams), customer names or adoption metrics beyond Warp's own
  usage, or a full transcript/recording of the AIEWF keynote itself (the
  interview references the keynote as available on YouTube but does not quote
  it directly).

## Extracted Claims

### Claim 1: Lloyd traces the "software factory" concept to roughly the last six months, as an evolution from one-off cloud agent runs, to scheduled cloud agents, to automating the full software engineering loop
- **Evidence**: Direct answer to the interviewer's question about when Lloyd first encountered the term "software factory."
- **Confidence**: anecdotal (single founder's recollection of his own product-thinking evolution, not a dated timeline with artifacts)
- **Quote**: "We started with more one-off automation: run an agent in the cloud. A lot of platforms began there. Then it became: run an agent in the cloud on a timer. The next question was, what is the most valuable loop to automate? The answer is basically the main loop of software engineering: triage, specification, implementation, review, verification, shipping and monitoring."
- **Our assessment**: This gives a concrete three-stage progression (ad hoc cloud run → scheduled cloud run → full-lifecycle loop) for how one vendor arrived at the "factory" framing, which is more specific than a bare assertion that "loops" are the current industry vocabulary. It corroborates the broader "chat → tools → goals → automations" periodization already in the corpus (see Cross-References).

### Claim 2: Lloyd states he doesn't care whether the "factory" term itself sticks — the essential and lasting shift is from interactive development to automated development, with "factory" as a useful metaphor for that shift
- **Evidence**: Direct answer, offered as a closing qualifier after describing Oz's roadmap.
- **Confidence**: anecdotal (single executive's stated framing preference)
- **Quote**: "But I don’t care that much whether the term sticks. The essential shift is from interactive development to automated development. “Factory” is a useful metaphor for that."
- **Our assessment**: This is a useful hedge for the guide to preserve when citing Lloyd's "factory" vocabulary elsewhere in the corpus (see Cross-References, dispatch Claim 7): Lloyd himself frames "factory" as a metaphor for an underlying interactive-to-automated transition, not as a load-bearing technical term. The guide should cite the underlying claim (automation replacing interactive agent use) rather than treating "factory" naming itself as the substance.

### Claim 3: The next version of Oz will include a factory setup flow and a "factory floor" management view, and this is explicitly what Warp is building its product around
- **Evidence**: Direct answer describing Oz's product roadmap.
- **Confidence**: anecdotal (single founder's stated roadmap, not yet shipped/verifiable at time of publication)
- **Quote**: "It is literally what we are gearing our product around. In the next version of Oz, you will set up your factory, see what it looks like and manage the factory floor."
- **Our assessment**: This is the most concrete, checkable product claim in the interview — a specific named UI concept ("factory floor") for a not-yet-shipped release. It should be flagged in the guide as a stated roadmap intention rather than a shipped, verified capability, and would be worth a future Miner follow-up once Oz's next version ships.

### Claim 4: Setting up an Oz factory means choosing repositories, which parts of the software lifecycle to automate, and where humans are brought into the loop — a decision that varies by organization and codebase
- **Evidence**: Direct answer describing the Oz onboarding flow.
- **Confidence**: anecdotal (single founder's description of his own product's UX)
- **Quote**: "You choose your repositories, the parts of the software lifecycle you want to automate, and the points where humans should be brought into the loop. Different organizations and codebases will have different preferences. Do you fully automate code review? Do you have humans review certain high-risk changes?"
- **Our assessment**: This restates, in near-identical substance, the "pick your repos, pick the parts of the lifecycle... pick the ways... humans [are] brought into the loop" configurability framing Lloyd gave in his AIEWF booth interview (see Cross-References — dispatch Claim 8), confirming it as a consistent, repeated framing across two separate interviews on the same day rather than an offhand remark in just one.

### Claim 5: Most of what a "software factory" adds is not a new interface but an integration into existing workflows — pulling issues from Jira/Linear, accepting submissions via Slack/Teams, and letting developers redirect agents from GitHub
- **Evidence**: Direct answer describing how the factory loop is assembled operationally.
- **Confidence**: anecdotal (single founder's product description, no named customer example)
- **Quote**: "The system then starts creating the loop. It might pull issues from Jira or Linear, let people submit them through Slack or Teams, and allow developers to redirect an agent from GitHub. What is interesting from a product perspective is that most of the factory is not necessarily a new interface. It is an integration into people’s existing workflows."
- **Our assessment**: This is a specific, actionable integration list (Jira/Linear, Slack/Teams, GitHub) rather than a vague "integrates with your tools" claim, and it reinforces the guide's likely framing that factory/loop adoption rides on top of existing tool surfaces rather than requiring a new dedicated UI — directly useful for Ch02 operational guidance on what standing up a factory actually touches.

### Claim 6: Warp's underlying mission (help developers ship better software faster) has stayed constant since 2021, but the product form has changed twice — modern terminal, then terminal-with-agents — because "the underlying AI improves so quickly"
- **Evidence**: Direct answer connecting Warp's founding mission to its two prior product pivots and the coming third one.
- **Confidence**: anecdotal (single founder's account of his own company's strategy)
- **Quote**: "The underlying AI improves so quickly that my view of the future is what I described in the talk: the interactive component is going to become less important." / "As the underlying technology gets better, companies that do not adapt are going to be left behind."
- **Our assessment**: The second half of this quote is a pointed competitive claim (adapt or be left behind) rather than a neutral description, consistent with Lloyd having a direct commercial stake in developers accepting the automated-factory framing — the guide should present this as founder conviction/thesis, not as disinterested market analysis, mirroring the caveat the corpus already applies to Lloyd's other "factory" claims (see Cross-References, dispatch Claim 9's assessment).

### Claim 7: Lloyd reframes "factory engineering" as meta-engineering — building the system that builds the product — using the same problem-solving skills applied to why an agent succeeds or fails, how to adjust its feedback, and how to change the workflow
- **Evidence**: Direct answer to the interviewer's question about developers finding the "factory" term mechanized or uncreative.
- **Confidence**: anecdotal (single founder's reframing of an objection to his own product thesis)
- **Quote**: "I think it can be extremely interesting if you view the job as meta-engineering: building the system that builds the product. It uses many of the same problem-solving skills. You are asking why an agent performs one task well and another poorly. How should you adjust its feedback? What context does it need? How should the workflow change?"
- **Our assessment**: This is a more granular, skills-level elaboration of the "you'll be building the thing that builds the product" framing already in the corpus from Lloyd's AIEWF booth interview (see Cross-References, dispatch Claim 7) — it names three concrete meta-engineering activities (diagnosing agent success/failure, adjusting feedback, adjusting workflow shape) rather than only asserting the role shift exists.

### Claim 8: Standing up a software factory is often a forward-deployed-engineering-style "transformation project" requiring real engineering to configure and deploy the system, and Warp positions itself as a platform business rather than a services business even though transformation-style work exists in the market today
- **Evidence**: Direct answer to a question about how forward-deployed engineering fits the software-factory model.
- **Confidence**: anecdotal (single founder's characterization of his own company's business-model positioning)
- **Quote**: "A lot of forward-deployed engineering work in this area is effectively a transformation project. It requires real engineering from someone who understands how to configure and deploy one of these systems. We do some of that, and some of our competitors do as well. I don’t know what the final state will look like. Warp is approaching it more as a platform business than a services business. But there is certainly a business today in sending smart people into a company to transform its workflow using these products."
- **Our assessment**: This directly answers the Prospector's key question about FDE/transformation-service framing (see Prospector triage comment). It is a more explicit platform-vs-services positioning statement than the corpus's existing FDE coverage offers for Warp specifically — useful for Ch05 to show a second named vendor (alongside Sierra and Cursor) explicitly locating "transformation" work within, but distinct from, its core product.

### Claim 9: Warp open-sourced its own CLI in April 2026 and placed the resulting project under Oz's control, using Warp's own factory platform (plus community contributions and agents) to develop it, while still employing internal engineers and serving nearly one million developers
- **Evidence**: Direct answer describing what happened to the original Warp CLI product after the Oz pivot, plus MacManus's framing note about Warp's user base.
- **Confidence**: anecdotal (single founder's account of an internal dogfooding decision; the "almost one million users" figure is unsourced/unattributed within the piece)
- **Quote**: "When we open-sourced Warp, we put the repository under the control of Oz. We built a software factory around the open-source project, using our own factory platform. We are still trying to improve Warp as much as possible. We are doing it with the community, and we are doing a lot of it with agents. In that sense, Warp is a test bed for the factory concept."
- **Our assessment**: This is the interview's most concrete, verifiable-in-principle artifact — a named, dated (April 2026) product decision (open-sourcing the CLI) tied to a specific operational claim (the resulting repo is managed by Oz as a live factory). It substantiates Lloyd's factory thesis with an internal example rather than only a forward-looking prediction, though it remains a single vendor's self-reported account of its own dogfooding, not independently verified usage data.

### Claim 10: Adoption of software factories will be gradual — companies start with specific low-risk repositories or issue types, then progressively increase the percentage of automatically-merged pull requests (e.g. from 20% toward 30-60%), with a persistent remainder of work too ambiguous or greenfield to automate
- **Evidence**: Direct answer to a question about the next year's adoption trajectory.
- **Confidence**: anecdotal (single founder's prediction, no company names or measured adoption data cited)
- **Quote**: "Companies will start with specific use cases, certain types of issues or lower-risk repositories. Those are places where they may be comfortable not having a human review every single line of code. They will see how it performs. Then the engineering challenge becomes: instead of merging 20% of pull requests automatically, can we get to 30%, 40%, 50% or 60%? There will still be a remaining percentage of work done by people because it is too difficult, ambiguous or dependent on greenfield thinking."
- **Our assessment**: This is the interview's most operationally specific adoption claim, giving concrete percentage anchors (20% → 30/40/50/60%) rather than a vague "gradual adoption" statement. It directly answers the Prospector's question about adoption metrics, though these numbers are Lloyd's illustrative framing, not a cited customer benchmark — the guide should present them as an example trajectory, not a measured industry average.

### Claim 11: Lloyd predicts that within the next year, every significant software project will run "something resembling a factory," becoming a standard part of serious software projects comparable to GitHub or CI/CD
- **Evidence**: Direct answer to the same adoption-trajectory question, as a closing prediction.
- **Confidence**: anecdotal (single founder's 12-month industry-wide prediction, unhedged in its "would be surprised if that did not happen" phrasing)
- **Quote**: "But I think this shift will happen over the next year. My prediction is that every significant software project will have some engine of code — something resembling a factory — continuously driving it forward. It will become similar to GitHub or CI/CD: a standard part of how serious software projects operate. I would be surprised if that did not happen."
- **Our assessment**: This is the interview's clearest, most falsifiable timeline claim and directly answers the Prospector's key question about Lloyd's adoption timeline. The GitHub/CI-CD comparison is a strong, checkable analogy (both became near-universal within a multi-year, not one-year, adoption curve), which is worth flagging in the guide as an aggressive compression of that historical adoption timeline — a one-year prediction for factory-style automation to reach GitHub/CI-CD-level ubiquity is a much shorter window than either of those two comparators actually took.

### Claim 12: Lloyd advises AI engineers to prepare for the shift by building automation around one annoying part of their own workflow rather than the product directly, since problems like code-review bottlenecks or unclear agent changes only surface once you attempt to build the loop
- **Evidence**: Direct answer to a question about what conference attendees should do to prepare.
- **Confidence**: anecdotal (single founder's practical recommendation, framed as general advice rather than a case study)
- **Quote**: "Instead of only building the product directly, try building some automation toward a factory and see what it feels like. Suppose you want an agent to implement incoming user issues automatically. What is involved in making that work? What prevents you from adopting it? Perhaps code review is the bottleneck. Perhaps the agent is making changes, but you cannot clearly see what it did. You only discover those problems by trying to build the loop. Get out of the mindset of building everything by hand. Find an annoying part of your job and try to create a loop that handles it for you using a factory approach."
- **Our assessment**: This is directly actionable practitioner advice (start with one annoying workflow, expect code-review-bottleneck and change-visibility problems to surface) rather than a slogan-level exhortation to "adopt factories" — worth citing in the guide as a concrete first-step recommendation for individual engineers, distinct from the organization-level adoption claims in Claims 4 and 10.

### Claim 13: MacManus's own framing attributes Warp's decision to open-source its core CLI in April 2026 to increased competition from Claude Code, Codex CLI, and Gemini CLI
- **Evidence**: The interviewer's introductory framing, not a statement attributed to Lloyd himself.
- **Confidence**: anecdotal (a single journalist's inference about causation, not confirmed by Lloyd in the interview text itself)
- **Quote**: "But the competition among CLI tools has dramatically increased in recent years, including from Claude Code, Codex CLI, and Gemini CLI — three products backed by massive tech companies. This likely led to Warp’s decision to open-source its core CLI tool in April this year."
- **Our assessment**: This claim should be clearly attributed to MacManus's own editorial inference ("likely led to") rather than presented as Lloyd's stated reasoning — Lloyd's own answers in this interview describe the open-source decision only in terms of it becoming a factory test bed (Claim 9), not competitive pressure. Useful for the guide's competitive-landscape framing, but the causal claim and the founder's own stated rationale should not be conflated.

## Concrete Artifacts

### Warp's product evolution timeline (as stated by Lloyd and framed by MacManus)
```
Source: Latent Space, "Warp CEO Zach Lloyd on why software factories are the
next phase of coding" (Richard MacManus interviewing Zach Lloyd, 2026-07-01)

- Mid-2021: Warp founded as a Rust-based terminal (pre-ChatGPT)
- Post-ChatGPT: terminal gains integrated coding agents
- April 2026: Warp open-sources its core CLI tool
- 2026 (Oz): Warp launches Oz, a cloud agent orchestration platform for
  "software factories"; the open-sourced CLI repo is placed under Oz's
  control as an internal test bed
- Next version of Oz (unshipped at publication): adds a factory setup flow
  and "factory floor" management view
```

### The "main loop of software engineering" per Lloyd
```
Source: same interview, Claim 1

triage → specification → implementation → review → verification → shipping
→ monitoring
```

### Factory integration surface (per Lloyd)
```
Source: same interview, Claim 5

- Issue intake: Jira, Linear
- Human submission: Slack, Teams
- Agent redirection: GitHub
```

### Adoption trajectory example (per Lloyd)
```
Source: same interview, Claim 10

Automated PR merge rate: 20% (starting point) → 30% → 40% → 50% → 60%
(progressive target), applied first to low-risk repos / specific issue
types before wider rollout
```

## Cross-References

- **Corroborates**:
  - `blog-latentspace-aiewf-loops-software-factories-dispatch.md` (Claim 8 —
    Lloyd's AIEWF booth interview: "pick your repos, pick the parts of the
    lifecycle that you want to automate, pick the ways in which you want
    humans to be brought into the loop"): this note's Claim 4 restates the
    same configurability framing almost verbatim in a separate interview
    conducted the same day, confirming it is Lloyd's consistent description
    of Oz's setup flow rather than a one-off phrasing. That dispatch's
    Claim 7 ("software engineering will become factory engineering," "you'll
    be building the thing that builds the product") is extended by this
    note's Claim 7, which adds the specific meta-engineering activities
    (diagnosing agent success/failure, adjusting feedback, adjusting
    workflow) behind that framing.
  - `blog-cursor-continual-harness-improvement.md` (Claim 13 — Cursor's own
    production "software factory": weekly LLM log scanning that creates
    Linear tickets and can trigger Cloud Agents): this note's Claim 9 (Warp
    placing its own open-sourced CLI under Oz's control as a factory test
    bed) is a second, independently-documented vendor example of a company
    running its own product development through the "software factory"
    pattern it sells — corroborating that this is not purely aspirational
    vendor messaging but something at least two named companies (Cursor,
    Warp) report doing to their own codebases.
  - `blog-ghaw-pelis-agent-factory-intro.md` (Claim 1 — GitHub's gh-aw team
    operating over 100 agentic workflows in production; Claim 2 — deliberate
    heterogeneous specialization over one "perfect" agent): a third
    independent "factory" implementation, this time GitHub's own internal
    one. Lloyd's Claim 4/5 (factory setup = choosing repos/lifecycle
    stages/human checkpoints, integrated into existing tools rather than a
    new interface) is a compatible, higher-level description of the same
    kind of heterogeneous, tool-integrated automation GitHub's factory note
    documents in operational detail.

- **Contradicts**: None identified. No claim in this interview materially
  opposes an existing corpus note in a way that would change guide advice.
  (Claim 13's attribution note above is a scoping caveat about who is making
  which claim, not a substantive contradiction between sources.)

- **Extends**:
  - `blog-latentspace-aiewf-loops-software-factories-dispatch.md` (Claims
    6-9, covering Lloyd's main-stage talk and booth interview): that note
    explicitly flagged Lloyd's booth interview as thin — a single
    configurability quote with no roadmap, adoption metrics, or business-
    model detail. This note supplies exactly that missing depth: Oz's
    roadmap (Claim 3), the Jira/Linear/Slack/Teams/GitHub integration list
    (Claim 5), the FDE/transformation-service business-model split (Claim
    8), the open-source-CLI-as-test-bed example (Claim 9), and concrete
    adoption percentages and a 12-month timeline (Claims 10-11) — none of
    which appear in the dispatch.
  - `blog-latentspace-meurer-agent-engineer-fde.md` (Claim 4 — "most
    customer-specific work takes place at the orchestration layer rather
    than in the models themselves"; Claim 7 — product engineering and FDE
    converging): this note's Claim 8 adds a second named vendor's (Warp's)
    account of the FDE/transformation-work split, explicitly framing it as
    a "platform business" with adjacent "transformation project" services
    work — a business-model angle Meurer's interview does not address (her
    interview covers what the work involves, not how Sierra frames its
    revenue model relative to it).

- **Novel**:
  - **Oz's roadmapped "factory floor" management UI** (Claim 3): not
    previously documented in the corpus; a specific, checkable near-term
    product claim.
  - **The specific tool-integration list for a "software factory"** (Claim
    5 — Jira/Linear for issue intake, Slack/Teams for human submission,
    GitHub for agent redirection): more operationally specific than any
    prior corpus mention of factory/loop tool integration.
  - **Warp's own open-sourced CLI run as a live factory under Oz** (Claim
    9): a concrete, dated (April 2026) dogfooding example, new to the
    corpus's "factory" coverage.
  - **Concrete adoption-percentage trajectory (20% → 30-60% automated PRs)**
    (Claim 10): the corpus's prior "factory" adoption claims (e.g. the
    dispatch's Claim 8) describe configurability in the abstract; this is
    the first source in the corpus's factory coverage to attach specific
    illustrative percentages to the adoption curve.
  - **A named 12-month industry-adoption prediction compared explicitly to
    GitHub/CI-CD's path to ubiquity** (Claim 11): new to the corpus at this
    level of specificity (a comparator technology and an explicit timeframe).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Lloyd's adoption-percentage
  trajectory (Claim 10 — starting with low-risk repos/issue types, then
  progressing from 20% toward 30-60% automatically-merged PRs) alongside the
  existing Cursor production example (`blog-cursor-continual-harness-improvement.md`
  Claim 13) to show a second vendor's account of dialing in automation
  incrementally with concrete percentage anchors rather than an all-or-
  nothing switch. Add the specific tool-integration list (Claim 5 — Jira/
  Linear, Slack/Teams, GitHub) as a concrete answer to "what does standing up
  a factory actually touch." Add Lloyd's 12-month adoption prediction and
  GitHub/CI-CD comparison (Claim 11) as a named industry benchmark, flagged
  per Claim 11's assessment as a notably compressed timeline relative to how
  long GitHub and CI/CD themselves took to become standard practice.

- **Chapter 05 (Team Adoption)**: Add Warp's platform-vs-services framing
  (Claim 8 — "Warp is approaching it more as a platform business than a
  services business," while acknowledging "there is certainly a business
  today in sending smart people into a company to transform its workflow")
  as a second named vendor's (alongside Sierra's, per
  `blog-latentspace-meurer-agent-engineer-fde.md`) explicit statement on how
  FDE-style transformation work relates to, but is distinct from, its core
  product. Add Lloyd's individual-engineer starting advice (Claim 12 — pick
  one annoying workflow, expect code-review-bottleneck and change-visibility
  problems to surface) as a concrete first-step recommendation for engineers
  beginning factory-style automation.

- **Chapter 02 or 05 — framing caveat**: Per Claim 6's and Claim 9's
  assessments, the guide should present Lloyd's predictions and Warp's own
  dogfooding example as one vendor's founder-level conviction and self-
  reported internal usage, not independently verified industry data — this
  interview carries the same self-interest caveat the corpus already applies
  to Lloyd's AIEWF booth quotes (see
  `blog-latentspace-aiewf-loops-software-factories-dispatch.md`, Claim 9's
  assessment).

## Extraction Notes

- **Fetch method**: The Substack page was fetched directly via `curl` (not
  the WebFetch summarizer, which returned a paraphrased/summarized version on
  first attempt) and the article body was extracted from the
  `available-content` div, tag-stripped and HTML-entity-decoded in Python.
  All `Quote` fields above were copied verbatim from that plain-text
  extraction (Q&A format preserved: "Latent Space: [question]" / "Lloyd:
  [answer]"), then cross-checked against the extracted text before being
  placed in this note. The article was not paywalled — the full interview
  (approximately 1,900 words) was present in the served HTML with no "keep
  reading" gate encountered.
- **Full source read**: The entire interview was read in full, start to
  finish, including MacManus's framing paragraphs before and after the Q&A.
  The piece references Lloyd's AIEWF keynote as available on YouTube but does
  not embed a transcript or link directly within the fetched HTML; that video
  was not separately fetched/watched, so no claims are drawn from the keynote
  itself beyond what Lloyd restates in this written interview.
- **Confidence rationale**: Rated `anecdotal` overall — this is a single
  founder/CEO's account of his own company's product strategy, roadmap, and
  predictions, given to one interviewer, with no customer names, adoption
  data, or independently verifiable metrics beyond Warp's own self-reported
  dogfooding (Claim 9) and one unsourced user-count figure ("almost one
  million users," stated by MacManus, not Lloyd). Several claims (2, 6, 11)
  are explicitly forward-looking predictions or an executive's stated
  personal framing preference, which compounds the anecdotal rating.
- Cross-references verified: `blog-latentspace-aiewf-loops-software-factories-dispatch.md`,
  `blog-cursor-continual-harness-improvement.md`,
  `blog-ghaw-pelis-agent-factory-intro.md`, and
  `blog-latentspace-meurer-agent-engineer-fde.md` were each re-read in full
  (or, for the longer notes, the specifically cited claims) before citing;
  no claim numbers were guessed.
- No contradiction found/filed: no claim in this interview materially
  opposes an existing corpus note in a way that would change guide advice,
  per MINER.md §4a's "when NOT to file" guidance. Note that three separate
  Prospector triage comments appear on the source issue (apparently from
  repeated/duplicate triage runs); their guidance is consistent (Ch02/Ch05
  relevance, Oz product detail, adoption timeline), and this note follows
  the most specific and most recent of the three.
