---
source_url: https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night
source_type: blog-post
title: "Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night"
author: Anthropic (case study featuring Silas Alberti, SVP of Research, Cognition)
date_published: 2026-07-10
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1753"
---

# Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night

> Anthropic case study, built around quotes from Cognition's SVP of Research
> Silas Alberti, arguing that Claude Fable 5 is the first model Cognition has
> trusted for unattended multi-hour Devin runs — evidenced by an internal
> "Frontier Code" benchmark jump (prior Opus ~10% → Fable 5 ~30% on the
> hardest subset) and named failure modes of prior models (session drift,
> confident-first-guess triage, shallow log reading) that Fable 5 avoids.

## Source Context

- **Type**: blog-post (Anthropic/Claude blog, claude.com, published
  2026-07-10; corporate case study with named practitioner quotes, no
  individual Anthropic byline)
- **Author credibility**: Published by Anthropic on claude.com — marketing
  framing, hosted to position Claude favorably — but the substantive claims
  are attributed throughout to Silas Alberti, SVP of Research at Cognition
  (maker of Devin, an autonomous AI software engineer product with customers
  "ranging from high-growth startups to Fortune 500 companies"). Alberti's
  team "trains and tests the models behind Devin and has run nearly every
  Claude generation since the start," giving him direct, comparative
  exposure to prior Claude model generations in the same production harness.
  No independent/non-Anthropic-hosted account of these claims exists in this
  source; treat as a single-practitioner account amplified by a vendor
  channel. No code, benchmark methodology detail, architecture diagram, or
  third-party verification is included.
- **Scope**: Covers Cognition's internal evaluation philosophy ("we trust no
  eval"), a historical claim about Claude 3.6 Sonnet as an earlier step
  change, named failure modes of "earlier models" (unspecified exact
  version(s), described only as "prior Opus" for the benchmark comparison),
  the Frontier Code benchmark score jump, a first-person eight-hour
  unattended session anecdote, and forward-looking product claims about
  proactive agent monitoring. Does NOT cover: benchmark methodology or task
  composition for Frontier Code, exact model version(s) behind "earlier
  models" language (only one comparison, prior Opus vs. Fable 5, is
  version-specific), pricing, session cost, harness/tooling architecture
  details beyond "internal debugging tools" and "the browser," or any
  quantified proactive-monitoring outcome data (the 90% figure is a
  forecast, not a measurement).

## Extracted Claims

### Claim 1: Cognition explicitly distrusts benchmarks in isolation and gates model adoption on its own engineers' subjective judgment of a "real day of work"
- **Evidence**: Direct quotes from Alberti describing a repeated pattern of
  models acing benchmarks and failing in practice, and Cognition's
  countermeasure (highest-taste developers testing each new model).
- **Confidence**: anecdotal (single practitioner's stated policy, no
  external corroboration of the policy's track record)
- **Quote**: "We've been burned like this a bunch of times, Alberti says. So the team trusts its own engineers over any score. Its highest-taste developers put each new model through a real day of work, and the bar is whether the code is something they'd actually keep."
- **Our assessment**: This is a credibility-establishing claim more than an
  actionable pattern — it frames every subsequent claim in the post as
  coming from a source that (per its own telling) applies unusual scrutiny
  before trusting a model. Worth citing precisely because it raises the
  bar for what the rest of the post's claims mean if taken at face value,
  though the framing itself is unverifiable from this source alone (no
  benchmark-vs-practice failure examples are named).

### Claim 2: Cognition traces the first major capability step change for Devin to Claude 3.6 Sonnet (late 2024), specifically its reliable multi-step tool chaining, which tripled internal usage
- **Evidence**: Direct attribution to Alberti's team history running "nearly
  every Claude generation since the start."
- **Confidence**: anecdotal (single team's retrospective attribution, no
  usage data beyond "tripled," no definition of the measured usage metric)
- **Quote**: "He traces the first real jump to Claude 3.6 Sonnet in late 2024. It was the first model that could reliably chain tools and hold a multi-step task. When the team plugged it into Devin, internal usage tripled."
- **Our assessment**: A specific, dated historical claim rather than a
  vague "models have improved" statement, which gives it citability — but
  "internal usage tripled" has no baseline, timeframe, or unit given, so it
  should be treated as directional evidence of a step change, not a
  measured effect size.

### Claim 3: Before Fable 5, delegated agents in Cognition's harness could stay on-task reliably for only minutes to about an hour, after which sessions "drifted"
- **Evidence**: Direct quote establishing the prior capability ceiling that
  the rest of the post argues Fable 5 broke.
- **Confidence**: anecdotal (single practitioner's characterization, no
  named model version(s) for "before Fable," no quantified drift metric)
- **Quote**: "Before Fable, you could delegate agents that could stay on-task for a couple of minutes, maybe an hour, Alberti says."
- **Our assessment**: This is the load-bearing baseline for the post's
  central "horizon" claim (Claim 6) — establishes minutes-to-~1hr as
  Cognition's pre-Fable-5 ceiling for unattended delegation, a substantially
  shorter ceiling than the 2+ hour figure from Anthropic Labs' own
  Opus 4.6 harness post (see Cross-References → Extends). The two figures
  are not directly comparable: this claim describes plain delegation
  without a scaffolded harness, while the Anthropic Labs figure describes a
  purpose-built generator/evaluator harness on the SDK.

### Claim 4: Earlier models lost coherence when given multiple concurrent ideas to weigh, and on one database migration a prior Opus model technically completed the task but introduced subtle bugs
- **Evidence**: Direct quote naming a concrete failure category (concurrent
  idea overload) and a specific anecdote (a migration task with a
  technically-complete-but-buggy outcome).
- **Confidence**: anecdotal (single anecdote, no reproduction count, exact
  prior-Opus version unspecified)
- **Quote**: "Give an earlier model five ideas to weigh at once, and it would lose track and get confused. On one database migration, a prior Opus model technically finished the job but introduced a series of subtle bugs along the way."
- **Our assessment**: "Technically finished but introduced subtle bugs" is a
  specific and useful failure-mode description — it names a false-negative
  risk in completion-based evaluation (the task shows as "done" while
  quality silently regressed), which is a sharper framing than a generic
  "earlier models made mistakes" claim. No detail on what the bugs were or
  how they were caught.

### Claim 5: In incident triage, earlier models stayed at the surface of logs rather than digging for the relevant line, and were biased toward confidently asserting the first plausible answer rather than admitting uncertainty
- **Evidence**: Direct quote describing the triage failure pattern and its
  behavioral cause (models "trained to give an answer no matter what").
- **Confidence**: anecdotal (practitioner characterization, no incident
  count or before/after comparison)
- **Quote**: "Earlier models tended to stay at the surface of the logs instead of digging for the relevant line, and they were trained to give an answer no matter what—so they'd 'confidently claim the first plausible thing they discover and then stop.' Engineers learned to tune them out."
- **Our assessment**: "Engineers learned to tune them out" is a strong
  practitioner-trust signal distinct from a capability score — it describes
  organizational behavior change (ignoring the tool) in response to
  unreliable output, which benchmark scores would not capture. This
  corroborates a broader theme in this corpus that overconfident,
  surface-level answers erode practitioner trust faster than outright
  failures do (see Cross-References → Corroborates).

### Claim 6: On Cognition's internal "Frontier Code" benchmark's hardest subset, the prior Opus model scored ~10% and Claude Fable 5 scored ~30%
- **Evidence**: Specific before/after percentage figures attributed to a
  named internal benchmark, explicitly designed to counter benchmark gaming
  ("anti-slop").
- **Confidence**: emerging (specific numeric comparison from a credible,
  comparatively experienced source, but methodology, task count, and task
  composition of Frontier Code are not disclosed, and "prior Opus" does not
  name an exact version)
- **Quote**: "Cognition grades models on Frontier Code, a benchmark it built because existing ones kept rewarding code that passed tests but wouldn't survive a real codebase. Alberti calls it an 'anti-slop' standard. On its hardest subset, the prior Opus model scored around 10%. Claude Fable 5 scored about 30%."
- **Our assessment**: A 3x jump on a self-designed, non-public benchmark is
  suggestive but not independently verifiable — Frontier Code's task
  composition, scoring rubric, and sample size are not disclosed in this
  source, so the figure should be cited as Cognition's internal claim, not
  as a peer-reviewed or reproducible result. Notable that Cognition's own
  initial reaction was suspicion of a bug, which is itself evidence the
  team did not expect or want an inflated number (see Claim 7).

### Claim 7: The Frontier Code benchmark jump initially triggered suspicion of measurement error, but dogfooding (practical use) confirmed the result — a departure from the team's usual multi-week internal debate over whether a benchmark jump reflects real capability
- **Evidence**: Direct quotes describing the team's skeptical first reaction
  and the unusually fast alignment between benchmark and practical
  experience.
- **Confidence**: anecdotal (single team's account of its own internal
  process, no external observer)
- **Quote**: "The team's first reaction was suspicion. 'Is there a bug? This can't be true.' Usually a benchmark jump comes with engineers arguing for weeks over whether the model is actually better in practice. This time the dogfooding agreed with the numbers. 'It was kind of a shocker, honestly,' Alberti says."
- **Our assessment**: This is a process claim, not a capability claim — it
  argues Cognition's normal skepticism protocol (weeks of internal
  argument) was short-circuited, which functions as second-order evidence
  strengthening Claim 6, given Claim 1 establishes that this team
  specifically distrusts benchmark numbers by default.

### Claim 8: Fable 5 sustained an unattended, self-sufficient coding session for approximately eight hours overnight and made real progress, a duration Alberti says he had not seen from a Claude model before
- **Evidence**: First-person anecdote from Alberti describing a specific
  overnight session, framed as the post's central "horizon" finding.
- **Confidence**: anecdotal (single named anecdote, no session count, no
  task description, no verification of what "real progress" meant
  concretely)
- **Quote**: "The biggest thing we noticed was the horizon, how long it can be self-sufficient, he says. There have been tasks where I was about to go to bed and I was like, 'Okay, just please keep working on this and don't stop until I wake up.' And then I wake up, and it's been working for eight hours straight and actually making real progress. I hadn't seen that before."
- **Our assessment**: This is the post's headline claim and the one most
  likely to be cited or over-cited elsewhere — it is a single anecdote
  (one session, one night, unspecified task) presented as representative,
  with no data on frequency (does this happen every night, or was this the
  best of many attempts?), no cost figure, and no description of what
  "real progress" looked like on inspection. The guide should cite this as
  an existence proof of extended unattended operation, not as a claim that
  8-hour unattended runs are now routine or reliable at that duration.

### Claim 9: The sustained horizon was enabled by Fable 5 staying "clear-headed" in messy context — properly using Cognition's internal debugging tools (including paging through browser logs), stating explicit invariants before executing a migration, and pinpointing root cause on triage while stating what it didn't know
- **Evidence**: Direct quotes describing three specific behavioral changes
  from Fable 5 relative to the failure modes named in Claims 4-5.
- **Confidence**: anecdotal (practitioner characterization, mirrors
  claimed prior failure modes point-for-point but with no comparative
  measurement)
- **Quote**: "It was the first model to properly use Cognition's internal debugging tools, paging through logs in the browser and drawing conclusions despite the noise. On a migration that had tripped up earlier models, it stated the invariants it would hold itself to, then executed against them. On triage, it pinned down the root cause and said what it didn't know, which Alberti says is what actually rebuilds trust."
- **Our assessment**: "Said what it didn't know... is what actually rebuilds trust" is the most citable single sentence in the post for a
  guide chapter on verification/trust — it explicitly frames calibrated
  uncertainty disclosure (not raw accuracy) as the trust-restoring
  behavior, directly answering Claim 5's failure mode ("confidently claim
  the first plausible thing... Engineers learned to tune them out"). The
  "stated the invariants it would hold itself to, then executed against
  them" detail is a specific, transferable pattern (self-declared
  constraints before autonomous execution) distinct from the trust framing.

### Claim 10: Alberti places the Fable 5 jump in "a small class of true step changes, the kind that come roughly once a year"
- **Evidence**: Direct paraphrase/summary attributed to Alberti near the
  end of the "Claude Fable 5 clears Cognition's own bar" section.
- **Confidence**: anecdotal (subjective ranking by a single practitioner, no
  criteria given for what qualifies as a "true step change")
- **Quote**: (no direct quote for this claim in the fetched text; the
  article states this as reported narration — "He puts the jump in a small
  class of true step changes, the kind that come roughly once a year" —
  rather than as a quoted first-person sentence from Alberti)
- **Our assessment**: Treat as the article's editorial framing of Alberti's
  view rather than his verbatim words, since it is not inside quotation
  marks in the source. Consistent with Claim 2 (3.6 Sonnet as the prior
  step change, late 2024) which implies roughly a 1.5-year gap to Fable 5
  (mid-2026) — close to but not exactly "once a year," so the framing
  should be read as approximate, not as a precise cadence claim.

### Claim 11: Cognition's founding product bet — that agents should run in the cloud for hours at a time — was not viable with the models available during the company's first year, and Alberti says Fable 5 makes the full version of that bet viable
- **Evidence**: Direct quote connecting the historical capability gap to
  Cognition's original product thesis and Fable 5's role in closing it.
- **Confidence**: anecdotal (single practitioner's assessment of product
  viability, not a measured outcome)
- **Quote**: "Cognition's founding bet was that agents should run in the cloud for hours at a time. For the company's first year, the models weren't there yet." / "Alberti says Claude Fable 5 makes the full version of that bet viable, and some of it is already in the product."
- **Our assessment**: This connects the capability claim (Claim 8) directly
  to a business narrative — the article is explicit that the founding
  product thesis predates the model capability that would fulfill it,
  which is a useful frame for the guide's discussion of how agent
  reliability ceilings gate product design, not just individual session
  outcomes.

### Claim 12: Devin already performs some proactive, un-tagged intervention in production — watching a Slack channel and jumping into an issue without being tagged, or monitoring production and triaging a spike on its own
- **Evidence**: Direct quote naming two concrete current product behaviors,
  with Alberti's qualitative reaction when the agent gets it right.
- **Confidence**: anecdotal (two named behaviors, no frequency, accuracy
  rate, or false-positive rate given)
- **Quote**: "Devin can watch a Slack channel and jump into an issue without being tagged, or monitor production and triage a spike on its own. When it gets one of those right, he says, it feels 'like a real engineer on the team.'"
- **Our assessment**: "When it gets one of those right" is a notable
  hedge — it implicitly concedes the behavior is not always right, without
  quantifying how often. The guide should not cite this as "Devin reliably
  self-triages production spikes"; it is evidence that self-triggered
  proactive intervention exists as a shipped capability, with an
  unspecified success rate.

### Claim 13: Alberti forecasts that within one to two years, 90% of agent sessions will be proactive — the agent finding a problem, scanning the codebase, and messaging the human with a fix, rather than being invoked
- **Evidence**: Direct quote, explicitly framed as an expectation/forecast,
  not a current measurement.
- **Confidence**: anecdotal (single practitioner's forward-looking
  prediction, not a measured trend)
- **Quote**: "He expects this to become the default for engineering teams. In a year or two, he says, 90% of agent sessions will be proactive ones that find a problem, scan the codebase, and message you with the fix."
- **Our assessment**: This is a prediction, not a data point, and should be
  clearly labeled as such if cited — the specific "90%" figure has no
  stated basis (no current proactive-session percentage is given as a
  baseline trendline). Directly relevant to, and extends, this corpus's
  existing coverage of proactive/self-triggered agent behavior (see
  Cross-References → Extends).

## Concrete Artifacts

No code, config, benchmark methodology, or terminal transcripts are included
in this source — it is a prose case study with no reproduced technical
artifacts. The only quantitative artifacts are the benchmark percentages
(Claim 6) and the session duration (Claim 8), both captured above as claims
rather than as separable code/config blocks.

## Cross-References

- **Corroborates**: `blog-simonwillison-fable-relentlessly-proactive.md`
  Claim 1 (Willison: "After two days of experience with Claude Fable 5 I
  think the best way to describe it is relentlessly proactive") and Claim 3
  (Fable autonomously wrote its own Python CORS web server — creating
  infrastructure it was never asked to create — during that debugging
  session). This source's Claim 12 (Devin
  self-triaging Slack/production issues without being tagged) and Claim 13
  (90% proactive-session forecast) describe the same "acts without being
  asked" behavioral shift from an independent practitioner and company,
  strengthening the case that unprompted proactive intervention is an
  emerging, cross-practitioner-observed Fable 5 characteristic rather than
  a single anecdote.
- **Corroborates**: `blog-anthropic-fable-finding-unknowns.md` Claim 11
  (Thariq Shihipar: "Claude Fable is the first model where I find the
  quality of the work is bottlenecked by my ability to clarify its
  unknowns" — i.e., the model's raw capability stopped being the limiting
  factor). This source's Claim 9 (Fable 5 stating invariants before
  executing, and stating what it doesn't know on triage) describes a
  complementary shift: the model surfacing its own reasoning/certainty
  boundaries more legibly, which is part of what would make a
  practitioner's own clarification effort the new bottleneck.
- **Contradicts**: None identified as a direct, same-claim conflict.
- **Extends**: `blog-anthropic-harness-long-running.md` Claim 8 (Opus 4.6
  "sustain[ed] coherent building for 2+ hours without intermediate
  checkpoints" in an Anthropic Labs generator/evaluator SDK harness, up
  from Opus 4.5's context-anxiety-driven need for sprint decomposition) and
  Claim 9 (harness components should be pruned as model capability grows).
  This source's Claim 8 (Fable 5, ~4-5 months later chronologically,
  sustaining ~8 hours unattended in Cognition's Devin harness) is a
  substantially larger duration figure from a different model, different
  harness (Devin/Claude Code-style vs. Agent SDK generator/evaluator), and
  different practitioner — consistent directionally with harness-long-running's
  thesis that sustained-autonomy ceilings expand with each model
  generation, but not a controlled comparison (different harness
  architecture, different task type, no shared benchmark). Also extends
  `failure-decker-4hr-session-loss.md` Lesson 5 ("Treat 3-4 hours as the
  practical session ceiling for complex work in Claude Code" — measured on
  Claude Code ~2.x in Feb 2026): this source's 8-hour figure is a
  different model generation and a different harness (Devin, not raw
  Claude Code), so it should not be read as overturning decker's Claude
  Code 2.x ceiling, but it does further corroborate the general trend
  (already noted in harness-long-running.md's Cross-References) that
  session-length ceilings are model-and-harness-dependent and have been
  moving upward across 2026, not a fixed property of "Claude Code."
- **Novel**: The Frontier Code benchmark and its ~10%→~30% (prior Opus →
  Fable 5) hardest-subset score jump (Claim 6) is new to this corpus — no
  existing source note documents this specific internal Cognition
  benchmark. The named failure-mode vocabulary "session drift" and
  "confidently claim the first plausible thing they discover and then
  stop" as Cognition's characterization of pre-Fable-5 incident-triage
  behavior (Claim 5) is also new, as is the ~8-hour unattended overnight
  session anecdote (Claim 8) as a concrete duration figure from a named
  production AI-coding company (as distinct from a single practitioner's
  personal-project session).

## Guide Impact

- **Chapter 03 (Agent Reliability / Verification)**: Add Claim 9's framing
  — "stating what it didn't know... is what actually rebuilds trust" — as
  a named practitioner-validated trust-restoration behavior, directly
  contrasting with Claim 5's named failure mode (confidently asserting the
  first plausible answer). Currently the guide lacks a direct quote tying
  calibrated uncertainty disclosure to practitioner trust recovery at this
  specificity; this source provides one, sourced from a company (Cognition)
  with a stated track record of skepticism toward vendor capability claims
  (Claim 1), which strengthens its citability relative to a purely
  vendor-authored claim.
- **Chapter 03/04 (Sustained Autonomy / Session Ceilings)**: Add Claim 8
  (an ~8-hour unattended Devin/Fable-5 session) as a data point in the
  session-ceiling discussion alongside `blog-anthropic-harness-long-running.md`
  (Opus 4.6, 2+ hours, SDK harness) and `failure-decker-4hr-session-loss.md`
  (Claude Code 2.x, ~3-4 hour practical ceiling). Explicitly flag it as a
  single anecdote from a different harness (Devin, not raw Claude Code or
  the Agent SDK generator/evaluator pattern), not a benchmarked or
  reproducible ceiling — the guide should not state "Fable 5 supports
  8-hour unattended sessions" as a general property without this caveat.
- **Chapter 04/05 (Proactive / Self-Triggered Agents)**: Add Claim 12
  (Devin watching Slack channels and monitoring production without being
  tagged) and Claim 13 (Alberti's 90%-proactive-sessions-in-1-2-years
  forecast) to the corpus's existing proactive-agent-behavior coverage
  (currently anchored by `blog-simonwillison-fable-relentlessly-proactive.md`).
  Label Claim 13 explicitly as a forecast, not a measurement, if cited.

## Extraction Notes

- The full article is short (~700 words across five sections: intro,
  "Where earlier models hit their limit," "Claude Fable 5 clears
  Cognition's own bar," "What's next," plus the closing paragraph). It was
  fetched in full via WebFetch in one pass requesting complete verbatim
  text, then verified in a second targeted pass confirming Silas Alberti's
  full name, his title (SVP of Research at Cognition), the absence of an
  individual Anthropic byline, and the publication date (July 10, 2026).
  No sub-pages or outbound links in the article warranted following — it
  is a single-page case study with no linked footnotes, benchmark
  methodology page, or related-post links surfaced in the fetched content.
- Claim 10 ("a small class of true step changes... roughly once a year")
  is reported narration in the source, not inside quotation marks — I did
  not fabricate a first-person quote for it; see the Claim's own "Quote"
  field, which explains this explicitly per MINER.md §2a Rule 5.
- No numbered claim in any other source note was cited by number in this
  note. All Cross-References either cite existing notes by claim number
  after re-reading the cited note to confirm the number and content
  (`blog-simonwillison-fable-relentlessly-proactive.md` Claim 1 and
  Claim 3; `blog-anthropic-fable-finding-unknowns.md` Claim 11;
  `blog-anthropic-harness-long-running.md` Claim 8 and Claim 9;
  `failure-decker-4hr-session-loss.md` Lesson 5, cited by its own "Lesson"
  numbering since that note uses Lessons rather than numbered Claims), or
  cite by section name for non-numbered material — no claim numbers were
  guessed.
- No contradiction was identified that met MINER.md §4a's filing bar: the
  session-duration figures across this source, `blog-anthropic-harness-long-running.md`,
  and `failure-decker-4hr-session-loss.md` differ, but each is scoped to a
  different model generation and a different harness architecture (a
  conditioning variable, not a same-conditions conflict), consistent with
  how `blog-anthropic-harness-long-running.md`'s own Cross-References
  section already treated its relationship to the decker note. No
  contradiction issue filed.
- This source makes no claim about pricing, exact model versions for
  "earlier models" (only the Frontier Code comparison names "prior Opus"
  specifically), or Frontier Code's benchmark methodology — these gaps are
  noted in Source Context and should not be filled by inference in the
  guide.
