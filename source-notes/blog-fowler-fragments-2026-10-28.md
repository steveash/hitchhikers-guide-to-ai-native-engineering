---
source_url: https://martinfowler.com/fragments/2026-10-28.html
source_type: blog-post
title: "Fragments: October 28"
author: Martin Fowler (curator); primary linked sources — Annie Vella, "Supervisory Engineering Work"; Andy Nolan (Thoughtworks)
date_published: 2026-10-28
date_extracted: 2026-10-29
last_checked: 2026-10-29
status: current
confidence_overall: emerging
issue: "#4412"
---

# Fragments: October 28 (Fowler, relaying Annie Vella on supervisory control and automation levels)

> Fowler relays Annie Vella's mapping of Endsley & Kiris's five automation levels onto AI coding (None → Full automation), her caveat that an agent's account of its own actions may be inaccurate, and her call to redesign the job and the system together; he also observes Foocamp enterprise under-adoption.

## Source Context

- **Type**: blog-post (Fowler's "Fragments" link-blog, 28 October 2026; eight snowflake-separated sections). Only the Vella section, the Foocamp observations, and the token-sourcing item are extracted.
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks; `martinfowler.com` is a `trusted-feed` source. Annie Vella's post is grounded in her Masters research on AI's impact on software engineering and in the human-factors literature (Sheridan & Verplank 1978; Endsley & Kiris 1995; Bainbridge 1983). Andy Nolan is a Thoughtworks colleague writing about Thoughtworks' own strategy.
- **Scope**: Fowler's page reproduces the five-level table and two Vella quotes. I also read Vella's original post (https://annievella.com/posts/supervisory-engineering-work/, 23 Oct 2026) to confirm the table and obtain context (out-of-the-loop problem, four recommendations). Foocamp items are Fowler's own second-hand, Chatham-House-rule observations.
- **Not extracted**: Karpathy capability-gap quote, Foocamp social anecdotes, Laurie Voss/Torsten Slok "1997" bubble commentary, Adam Tornhill and Tim Bray opinion items (opinion, no evidence), and the Eric Evans DDD Europe video pointer (already covered in earlier Fragments notes per triage).
- **Not read**: Vella's slides/talk recording, and the Endsley & Kiris 1995 paper itself; the Vella claims about that paper are her reporting.

## Extracted Claims

### Claim 1: Coding is moving from direct control to supervisory control, because agents now close the loop (write code, run tests, fix mistakes) that humans used to close
- **Evidence**: Conceptual argument from supervisory-control research (Sheridan, MIT, late 1960s onward); no measurement in Fowler's page.
- **Confidence**: emerging
- **Quote**: "Now, coding agents can increasingly close that loop themselves - writing code, running tests and fixing their own mistakes - while we move towards supervisory control: telling the agent what we want, keeping an eye on how it’s going and taking over when we need to."
- **Our assessment**: Useful, decades-old vocabulary for what Ch00/Ch01 describe informally. It is a framing, not an empirical finding; it matches Gall's "middle loop" framing from a different tradition.

### Claim 2: Endsley & Kiris's five-level model gives a usable autonomy-level vocabulary for AI coding: None, Decision support, Consensual AI, Monitored AI, Full automation
- **Evidence**: Table in the post; each level specifies the human role (Decide/act; Concur; Veto; none) and system role (Suggest; Decide/act). Mapping to AI tools is Vella's, adapted from Endsley & Kiris (1995).
- **Confidence**: emerging
- **Quote**: "The five-level model developed by Endsley and Kiris seems apposite:" (Fowler); table rows include "3. Consensual AI … Concur … Decide, act … AI coding agents where you must approve the actions they take" and "4. Monitored AI … Veto … Decide, act … Auto-mode, with the ability to veto the coding agent’s actions".
- **Our assessment**: The levels are defined by *who decides and who acts*, which is cleaner than tool-brand or "agent vs. copilot" labels. The mapping is an analogy chosen by Vella, not validated for coding. Level 3 vs 4 maps to approve-each-action versus auto-mode-with-veto, which matches how current agent tools expose permission modes (see Cursor auto-review note).

### Claim 3: Both prior level models assume the computer's account of its own actions is honest, which does not hold for AI agents — so agents need more supervision, not less
- **Evidence**: Assertion by Vella ("As we all know by now"); no specific incident cited in this post.
- **Confidence**: emerging (widely corroborated elsewhere in the corpus, but unsupported here)
- **Quote**: "As we all know by now, what an AI agent says it did and what it actually did may not be the same thing. Still, it’s automation, and it still requires supervision - arguably more, since we can’t simply take its word for it."
- **Our assessment**: Strong implication for Ch03: verification must inspect artifacts and effects rather than rely on agent self-report. The classic levels are therefore a lower bound on needed oversight.

### Claim 4: The next step is to redesign the job and the system in tandem; the SDLC should be viewed as a control system we build and supervise
- **Evidence**: Argument; Fowler endorses it and notes "we don’t yet know what this new job design looks like".
- **Confidence**: anecdotal
- **Quote**: "What if we stopped thinking of the SDLC as a process we follow, and instead started thinking of it as a control system we build and supervise?"
- **Our assessment**: Directional, not actionable alone. Vella's original gives four concrete moves (below, Concrete Artifacts), which is where the actionable content lives.

### Claim 5: Higher automation reduces situation awareness (comprehension, not perception) and does not reduce workload — the "out-of-the-loop performance problem" (from Vella's original post, not in Fowler's page)
- **Evidence**: Vella's summary of Endsley & Kiris (1995) experiments using a simulated expert system; analogies to coding and cognitive-debt writing by Storey and Osmani.
- **Confidence**: emerging (lab experiments, non-coding task, second-hand)
- **Quote**: "They found evidence of what they expected to see: situation awareness dropped as the level of automation increased."
- **Our assessment**: Relevant to review practice: reviewing diffs alone gives passive understanding. Caveat: simulated task in 1995, not software engineering.

### Claim 6: The better automation gets, the more operator training it needs, because rare interventions are exactly where skills have atrophied (Bainbridge, via Vella's original)
- **Evidence**: Bainbridge, "Ironies of Automation" (1983), quoted by Vella.
- **Confidence**: settled (as human-factors theory); untested for coding agents
- **Quote**: "perhaps the final irony is that it is the most successful automated systems, with rare need for manual intervention, which may need the greatest investment in human operator training"
- **Our assessment**: Supports training/immersion arguments in Ch05; the guide's skill-atrophy discussion can cite a primary source rather than only practitioner anecdote.

### Claim 7: Agentic-engineering immersion courses with coaches are emerging, and the biggest impact is emotional/identity rather than technical
- **Evidence**: Fowler's report of Foocamp conversations (Chatham House rule, unattributed), with an analogy to Extreme Programming immersion classes.
- **Confidence**: anecdotal
- **Quote**: "Unsurprisingly the coaches observed that the biggest impact wasn’t technical, but emotional."
- **Our assessment**: Single second-hand anecdote from a self-selected bleeding-edge audience; no outcome data. Consistent with Vella's "it isn't the same job" argument.

### Claim 8: Large enterprises are using only a sliver of agent capability, constrained by slow-changing workflows, security (lethal trifecta), and poor data readiness
- **Evidence**: Fowler's observation from the <10% of Foocamp sessions he attended; a participant's metaphor.
- **Confidence**: anecdotal
- **Quote**: "corporations have acquired a Swiss-army knife, but are only using the toothpick."
- **Our assessment**: Fowler explicitly hedges ("I’m wary of talking about themes to an event where I attend less than one-tenth of the sessions"). Treat as a hypothesis for Ch05.

### Claim 9: Thoughtworks forecasts its 2028 token cost falling from $16-40M to "$6.8-1M" via a per-workload sourcing grid (rent frontier APIs vs. self-host open-weight)
- **Evidence**: Forecast by Andy Nolan, relayed by Fowler; the grid is two axes (domain differentiation, security & sovereignty), nine cells.
- **Confidence**: anecdotal (forecast, vendor-authored, not a measured result)
- **Quote**: "which we forecast will reduce our token costs in 2028 from $16-40M down to $6.8-1M."
- **Our assessment**: The "$6.8-1M" figure is evidently a typo; the primary note `blog-thoughtworks-nolan-renting-the-frontier.md` records $6.8M–$11M at 70–90% confidence. Do not re-extract the figure; no new evidence beyond the existing note. Not filed as a contradiction (transcription slip, not disagreement).

## Concrete Artifacts

```
Endsley & Kiris five levels, as mapped to AI coding by Annie Vella (reproduced in Fowler's page; adapted from Endsley & Kiris 1995)

Level               Human         System        In AI-assisted software development
1. None             Decide, act   -             No AI assistance
2. Decision support Decide, act   Suggest       The early days of AI coding assistants' autocomplete
3. Consensual AI    Concur        Decide, act   AI coding agents where you must approve the actions they take
4. Monitored AI     Veto          Decide, act   Auto-mode, with the ability to veto the coding agent's actions
5. Full automation  -             Decide, act   Full auto-mode, such as might be used in a dark software factory
```

```
Vella's four recommendations (from annievella.com/posts/supervisory-engineering-work/, not in Fowler's page; headings paraphrase-free from the post)
- Deliberately choose the level of automation to operate at, and for which types of work
- Design system signals to support situation awareness
- Describe intervention requirements and mechanisms
- Prepare people for the job
```

```
Sheridan & Verplank supervisor roles mapped to supervisory engineering work (Vella's post)
Plan and command -> Directing AI
Monitor          -> Evaluating its output
Intervene        -> Correcting it when it's wrong
Trust            -> Calibrating trust
```

## Cross-References

- **Corroborates**: `blog-thoughtworks-gall-supervisory-engineering.md` — its Claim 7 (directing, evaluating, correcting) is the same triad Vella cites as her research-derived definition of supervisory engineering work; this note ties it to the supervisory-control literature. `blog-cursor-agent-autonomy-auto-review.md` Claim 1 ("dial rather than a switch") parallels levels 3–4 as a graded choice.
- **Contradicts**: none. The token figure "$6.8-1M" differs from `blog-thoughtworks-nolan-renting-the-frontier.md` Claim 9 ($6.8M–$11M) but appears to be a typo; no contradiction issue filed.
- **Extends**: `blog-thoughtworks-nolan-renting-the-frontier.md` (Fowler's one-paragraph summary adds only the Fowler framing that token cost comes up in conversations "outside the Foocamp world"). `blog-addyosmani-software-factories-light-dark.md` (dark-factory concept) now has a named Level 5 in a formal taxonomy. Same series: `blog-fowler-fragments-2026-10-21.md`.
- **Novel**: The Endsley & Kiris level taxonomy applied to AI coding, the out-of-the-loop performance problem, Bainbridge's training irony, and the "agent self-report may not be accurate" caveat as a limit of classical automation models. None of the existing notes cite Vella, Endsley, Sheridan, or Bainbridge.

## Guide Impact

- **Chapter 00 / 01**: Consider adopting the five-level vocabulary (None / Decision support / Consensual / Monitored / Full automation) for describing autonomy and mapping tool permission modes to levels, citing this note (Claims 2, 4).
- **Chapter 03**: Add that classic automation models assume honest self-reporting, so agent claims of completion must be verified against artifacts (Claim 3); mention reduced comprehension when only reviewing diffs (Claim 5).
- **Chapter 05**: Cite the training irony (Claim 6) and Vella's four redesign moves, especially "deliberately choose the level of automation… for which types of work", as an adoption checklist; Foocamp items (Claims 7–8) only as flagged anecdote.
- **Chapter 06**: Level 4 "Monitored AI (veto)" is the human-in-the-loop posture assumed by monitored-autonomy security controls; the self-report caveat reinforces not trusting agent-reported actions in audit.

## Extraction Notes

- Read Fowler's page in full and Vella's original post in full. Claims 5 and 6 and the recommendations come from Vella's post, flagged as such; the Endsley & Kiris and Bainbridge papers were not read.
- Triage comments disagreed about scope (one said the Nolan grid was new, others said it is already covered). Verified: `blog-thoughtworks-nolan-renting-the-frontier.md` exists and covers the grid and figures, so Claim 9 is a cross-reference only.
- Fowler's page is a link-blog; the evidence base is mostly argument and anecdote, hence `emerging` overall.
