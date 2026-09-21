---
source_url: https://addyosmani.com/blog/audit-your-agent-files/
source_type: blog-post
title: "Audit your Agent files"
author: Addy Osmani
date_published: 2026-08-27
date_extracted: 2026-09-21
last_checked: 2026-09-21
status: current
confidence_overall: emerging
issue: "#3594"
---

# Addy Osmani: Audit your Agent files

> A configuration-hygiene synthesis arguing agent config has a "half-life":
> CLAUDE.md/AGENTS.md files and skills accumulate cruft as models and
> harnesses improve, and the fix is periodic auditing (`claude`'s `/doctor`)
> rather than one-time authoring discipline. Synthesizes four empirical
> papers (config-smell prevalence, personalized-skill effectiveness,
> context-file correctness impact, and prose-vs-code context value) that are
> new to this corpus, plus a first-party Anthropic data point already on file.

## Source Context

- **Type**: blog-post (addyosmani.com, published 2026-08-27; personal blog,
  cross-posted to the author's newsletter/social channels per the article's
  own framing as a synthesis of "developer discourse on Twitter" and Hacker
  News threads).
- **Author credibility**: Addy Osmani is a well-established, previously-cited
  corpus source (11 other `blog-addyosmani-*`/`blog-osmani-*` notes already
  on file) and a practicing maintainer of a public Agent Skills package
  (`github.com/addyosmani/agent-skills`), giving him direct first-hand
  exposure to the skill-authoring and audit problems he describes. He is
  transparent about the limits of his own evidence throughout (e.g., flags
  the personalization paper's simulator-based methodology as "promising
  rather than final" rather than presenting it as settled). This is
  practitioner synthesis of primary research, not primary research itself —
  the value here is the curation and framing, plus his own first-hand audit
  anecdotes.
- **Scope**: Covers why agent configuration (CLAUDE.md/AGENTS.md, skills)
  degrades over time, four external empirical studies bearing on
  config/skill/context-file value, the author's own audit of his personal
  setup using Claude Code's `/doctor` command, and a recommended audit
  cadence. Does NOT cover hooks-specific auditing in depth, MCP server
  auditing mechanics, or give a step-by-step audit checklist — the guidance
  stays at the level of principles and cadence, not a procedure.

## Extracted Claims

### Claim 1: Agent configuration has a "half-life" — instructions written for an older model/harness generation become stale and can actively hurt as models and harnesses improve
- **Evidence**: Author's synthesis thesis, stated as the article's TL;DR and elaborated throughout with supporting studies (Claims 2-6).
- **Confidence**: emerging
- **Quote**: "Your coding agent's configuration has a half-life. Models improve, harnesses add capabilities, codebases change, and the instructions we wrote for an older version stay behind. Recent research finds inconsistent value from personalized skills. I now run Claude's /doctor every few weeks, review memory separately, and ask each instruction to earn its place again."
- **Our assessment**: This is the organizing frame for the whole piece and directly extends the corpus's existing "instruction value can expire" thread (see Cross-References). It reframes CLAUDE.md/skill maintenance as a recurring cost of *improving* models/harnesses, not just a hygiene nice-to-have — the more the underlying agent improves, the more of your own instructions become dead weight. Worth adopting as the rationale for a periodic-audit recommendation in the guide, distinct from initial-authoring guidance already covered elsewhere.

### Claim 2: A 100-repository study found configuration smells (context bloat, skill leakage, lint leakage) in most real-world AGENTS.md/CLAUDE.md files
- **Evidence**: Cites a June 2026 empirical study (arXiv:2606.15828, "Configuration Smells in AGENTS.md Files: Common Mistakes in Configuring Coding Agents," dos Santos et al.) analyzing 100 popular open-source repositories with AGENTS.md or CLAUDE.md files. The paper's own abstract confirms the exact figures Osmani cites: Lint Leakage in 62% of files, Context Bloat in 42%, Skill Leakage in 35%, with several smells "frequently co-occur[ring]."
- **Confidence**: settled (peer-reviewed-style empirical study with a stated methodology — grey literature review plus repository mining — and precise, checkable percentages that match the paper's own abstract)
- **Quote**: "For the numbers: a June study of 100 popular repositories found lint-related leakage in 62%, context bloat in 42%, and skill leakage in 35%."
- **Our assessment**: This is the strongest empirical anchor in the piece — an independently verifiable statistic (confirmed directly against the cited paper's abstract) that most real AGENTS.md/CLAUDE.md files in the wild have identifiable, named defects, not just "could be tidier." This is new to the corpus (no existing source note cites this paper) and gives the guide a hard number to justify recommending a recurring audit rather than a one-time authoring pass.

### Claim 3: The author's own CLAUDE.md files exhibited the same failure modes he warns against — overly long examples, redundant content duplicated from READMEs/manifests, and reactive rule-accumulation ("add a rule every time the agent errors")
- **Evidence**: First-person admission and self-audit, not a study.
- **Confidence**: anecdotal
- **Quote**: "When I try looking at some of the CLAUDE.md files that I've put together in the past, not for sharing with people but just in my own setup, I've also gone past 200 lines. And I found that there were a few common failure modes that I've seen in my own files. Things like overly long examples. Redundant content that may have been present in readmes or package manifests or skill files. Add a rule every time the agent errors."
- **Our assessment**: Low evidential weight on its own (n=1, self-reported) but valuable because it names a specific *mechanism* of bloat — "add a rule every time the agent errors" — that is more actionable than a generic "files get bloated" observation. This mechanism (reactive rule accumulation) is the practical explanation for how a repo crosses the 62%/42%/35% smell thresholds in Claim 2.

### Claim 4: Personalized skills built from one developer's interaction history did not meaningfully outperform a generic skill pooled across many developers, across 206 real sessions from 13 developers
- **Evidence**: Cites arXiv:2608.10319 ("Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories," Huang, Du, Lan). The paper's abstract confirms the study used "206 real-world developer-agent sessions from 13 developers" comparing personalized skills against no-skill, generic-skill, and other-user-skill baselines, finding "personalized skills provide small and inconsistent improvements over the no-skill baseline, whereas generic skills pooled across developers achieve the largest and most consistent gains."
- **Confidence**: emerging (the underlying paper itself flags its evaluation as simulator-based — see Claim 5 — so treat the finding as directionally credible but not fully validated against real task outcomes)
- **Quote**: "The surprising result was that personalization didn't help very much. A skill based on one developer's history performed about as well as a skill borrowed from somebody else. A generic skill built from lots of developers was more useful overall."
- **Our assessment**: This directly contradicts a common intuition (and arguably the pitch behind several "learn my preferences" agent-memory features): that individualized skill personalization is worth the investment. It is new to the corpus. The practical implication for the guide is specific — invest in team/community-level generic skills first, and treat personal-preference accretion into permanent skill/memory files with more skepticism than is currently common practice.

### Claim 5: Personalization becomes more effective specifically when the same developer preference recurs across several similar tasks — but this finding rests on an LLM-based simulator, not real task outcomes
- **Evidence**: Same paper as Claim 4, author's own explicit caveat about methodology.
- **Confidence**: emerging (author explicitly downgrades this from "final" to "promising")
- **Quote**: "Personalization did look more promising when the same preference recurred across several similar tasks, though the experiments used an LLM-based developer simulator, so treat this as promising rather than final. My takeaway is to begin with a strong generic skill and add personal rules gradually. I wouldn't promote a preference into permanent agent memory because I mentioned it once."
- **Our assessment**: This is the load-bearing nuance on Claim 4 — it prevents an over-broad "personalization never helps" reading and gives a concrete threshold ("recurs across several tasks," not "mentioned once") for when a preference is worth promoting to a durable skill or memory entry. The "start generic, add personal rules gradually, don't promote on first mention" sequence is directly actionable guidance for anyone designing an agent-memory or skill-authoring workflow.

### Claim 6: Repository context files (AGENTS.md/CLAUDE.md) did not make a measurable difference to task correctness across 288 runs on 17 real tasks, but did change how efficiently the agent worked
- **Evidence**: Cites arXiv:2607.27250 ("Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories," Khatri). The paper's abstract confirms "288 evaluated runs" across "17 real tasks from 3 repositories," concluding "context strategy does not measurably move correctness on either agent (bounded to <=10-15pp via equivalence testing)" and that failures came from "implementation skill... not missing repository knowledge that a context file could supply." Osmani adds a concrete illustration not quantified in the abstract: a context file warning that a test suite was slow caused Claude to run more targeted tests, improving efficiency without improving correctness.
- **Confidence**: emerging (a single controlled ablation study, not yet independently replicated, but pre-registered/equivalence-tested methodology per the abstract, which is stronger than an observational study)
- **Quote**: "Across 288 runs on 17 real tasks, they didn't make a clear difference to correctness." / "Context files did change how the agents worked, though. In one repository, the guide warned that the full test suite was very slow. Claude responded by running more targeted tests and wasting less time. It didn't become better at implementing the feature, but it followed the repository's workflow more efficiently."
- **Our assessment**: This is a precise, falsifiable claim that sharpens (rather than contradicts) the corpus's existing "context files help workflow, not raw capability" thread — see Cross-References for the specific relationship to `paper-gloaguen-agentsmd-effectiveness.md`, which measures a related but distinct effect (generation method, not presence/absence). The test-suite anecdote is a concrete, reusable example of the correct scope for a context file: operational facts about the repo (what's slow, what's generated, what's off-limits), not implementation guidance.

### Claim 7: Context files are useful for operational facts the model can't infer from code (expensive commands, generated files, architectural boundaries, safety rules) but cannot teach subtle implementation judgment
- **Evidence**: Author's synthesis of Claim 6's findings, generalized into a design rule.
- **Confidence**: emerging
- **Quote**: "A context file can tell an agent about expensive commands, generated files, architectural boundaries, or project-specific safety rules. It can't necessarily teach the agent how to make a subtle design decision; the near misses usually came down to implementation judgment, and more repository prose wouldn't have solved those problems."
- **Our assessment**: This is a concrete scoping rule the guide can state directly: CLAUDE.md/AGENTS.md content should be restricted to facts, not judgment coaching. It is consistent with, and gives a research-backed rationale for, existing corpus guidance to keep CLAUDE.md lean and fact-focused rather than treating it as a design-philosophy document.

### Claim 8: Prose summaries of code answer far fewer behavioral questions than the source code itself (4 of 45 vs. 27 of 45), because summaries lose the small details that matter
- **Evidence**: Cites a related study (arXiv:2607.09691, "What Context Does a Coding Agent Actually Need to Act?," Sam-Bodden). The paper's abstract confirms the exact figures: natural-language summaries answer "$4/45$ vs. $27/45$" behavioral questions compared to source code, on held-out repositories with an independent judge, and states "the gap belongs to the representation, not the summarizer — a frontier model's summaries score exactly as poorly as a 3B model's."
- **Confidence**: settled (specific, pre-registered-style measurement with an independent judge; the paper explicitly rules out summarizer quality as a confound)
- **Quote**: "A related study points the same way: prose summaries answered 4 of 45 behavioral questions about code while the source itself answered 27 of 45, because summaries smooth over the small details that matter. Point the agent at real code, not descriptions of it."
- **Our assessment**: This is a strong, quantified argument against a specific common pattern — writing prose architecture/module summaries into CLAUDE.md or a skill instead of `@`-referencing the actual code. It generalizes Claim 6/7's "point at facts, not descriptions" framing with a much larger effect size (a ~7x gap in answerable questions) and independent methodology, making it one of the more citable statistics in this note.

### Claim 9: Anthropic removed more than 80% of Claude Code's system prompt for its Claude 5-generation models with no measurable loss on internal coding evaluations
- **Evidence**: Restates a first-party Anthropic claim from "The new rules of context engineering for Claude 5 generation models" (already mined in this corpus — see Cross-References).
- **Confidence**: emerging (first-party claim from the team that made the change; the underlying eval suite and numeric scores are not public, as this note's own hedge states)
- **Quote**: "And in The new rules of context engineering, Anthropic says it removed more than 80% of Claude Code's system prompt for its Claude 5 generation models with no measurable loss on internal coding evaluations. That result is not a target; the evaluations are not public, and it covers specific models in a specific harness."
- **Our assessment**: Osmani's own hedge here ("not a target," "evaluations are not public") is a useful editorial model for the guide: cite the figure as directionally supportive of "trim aggressively," but don't present an 80% cut as a target ratio for practitioners to hit on their own repos, since the original claim is scoped to Anthropic's own system prompt and models. This is a re-citation, not new evidence — see `blog-anthropic-context-engineering-claude-5.md` Claim 1 for the primary-source version of this same figure, independently confirmed against the Anthropic blog's own text during this extraction ("We removed over 80% of Claude Code's system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations.").

### Claim 10: Claude Code's `/doctor` command audits configuration hygiene — unused skills, MCP servers, and plugins relative to their context cost, over-specified CLAUDE.md files, and slow hooks
- **Evidence**: First-person account of running the command against the author's own setup.
- **Confidence**: emerging (product-behavior claim from direct usage, not vendor documentation)
- **Quote**: "I was really happy to see Claude put out the doctor command in Claude Code. It's a good hygiene command, and it basically runs a checkup covering unused skills and MCP servers and plugins relative to their context cost, whether you've got an over-specified CLAUDE.md file, slow hooks, or cruft, or things like that."
- **Our assessment**: This corroborates and adds detail to `blog-anthropic-context-engineering-claude-5.md` Claim 14, which documents the `claude doctor`/`/doctor` announcement but explicitly notes the announcement itself gave no detail on what the command checks. This source partially fills that gap from a user's actual experience (unused skills/MCP/plugins, over-specified CLAUDE.md, slow hooks), though it is still a practitioner's summary rather than a documented spec of the command's internal logic.

### Claim 11: `/doctor` inside a Claude Code session (the configuration audit) and `claude doctor` run from a shell (installation diagnostics only) are two different commands, a naming trap that causes some users to think `doctor` "only shows a status check"
- **Evidence**: Direct clarification of a naming collision the author has observed causing confusion.
- **Confidence**: emerging
- **Quote**: "One naming trap worth knowing: in Claude Code, /doctor inside a session is the configuration audit, while claude doctor in a shell only prints installation diagnostics, which is why some people report that doctor "only shows a status check.""
- **Our assessment**: This is a specific, actionable disambiguation that is easy to get wrong and not something a reader would infer from either command's name alone. Directly useful for the guide as a footnote/warning anywhere `/doctor` is recommended, to prevent readers from running the wrong command and concluding the audit feature is thin.

### Claim 12: An installed skill's full body is not loaded into every prompt — only names/descriptions load for discovery, within a listing budget that defaults to 1% of the context window, and the full body loads only on invocation
- **Evidence**: Author's claim, linked directly to Claude Code's own skills documentation. The linked docs page (code.claude.com/docs/en/skills) confirms this mechanism in its own words: "Claude Code loads a listing of skill names and descriptions into context... The budget scales at 1% of the model's context window."
- **Confidence**: settled (confirmed against the linked first-party documentation, which independently states the same 1% figure and discovery/invocation split)
- **Quote**: "And an installed skill does not dump its whole body into every prompt: names and descriptions load for discovery within a listing budget defaulting to 1% of the context window, and the body loads on invocation."
- **Our assessment**: This is a precise mechanical fact that corrects a plausible misconception (that having many installed skills directly bloats every prompt's token cost by their full body size). The actual cost is bounded by the 1% listing budget for discovery, with body cost paid only on invocation — this changes the framing of "should I delete unused skills" from "they're wasting tokens on every turn" to "they're wasting a small, bounded slice of the discovery budget, and crowding out the listing entries of skills you do use."

### Claim 13: Skill accumulation compounds quickly in practice — one developer reported going from 250 installed skills down to 25 after auditing — and installing a skill and keeping it indefinitely are separate decisions
- **Evidence**: Secondhand anecdote (a tweet the author recalls) plus the author's own generalization from it and from his own audit experience (Claim 3).
- **Confidence**: anecdotal
- **Quote**: "I remember recently seeing a tweet where somebody was saying, yeah, I started auditing my skills and I went down from 250 to 25. And I was just like, how do you end up with 250 skills? That's crazy. But experimenting with a lot of community skills, these can easily compound over time. And you don't want to confuse your agent, right? So you've got to periodically lint and clean up your agent environment. Installing a useful skill and keeping it forever are separate decisions."
- **Our assessment**: Weak evidence individually (secondhand, unverifiable, single data point) but the underlying mechanism — trying community skills for one-off tasks and never removing them — is plausible and consistent with the author's own first-person account (Claim 3) and the 35% skill-leakage figure (Claim 2). The closing aphorism ("installing... and keeping... forever are separate decisions") is a clean, quotable framing for the guide's audit-cadence recommendation.

## Concrete Artifacts

### The "archive first, encode hard rules elsewhere" audit principle
```
Source: addyosmani.com/blog/audit-your-agent-files/ (Addy Osmani, 2026-08-27)

"The lesson is that instruction value can expire, so archive first, and if
a rule must always hold, encode it in a test, hook, or permission rather
than leaving it as prose the model might lose."
```
This is the article's single most actionable prescriptive line: it gives a
two-part rule (1. default to archiving stale instructions rather than
editing them in place, 2. anything that must be unconditionally enforced
belongs in a test/hook/permission, not CLAUDE.md prose).

### Recommended audit cadence
```
Source: addyosmani.com/blog/audit-your-agent-files/ (Addy Osmani, 2026-08-27)

"I think there's high value personally in, like maybe every couple of
weeks, maybe at once a month even, just running doctor on your skills, on
your setup, and auditing what you're doing... And then if you have the
time, actually going and seeing, like, if you were to delete your skills,
or you were to instruct your agent, well, don't use any local skills at
all. Only try to complete this task using the raw model and harness. And
see, is it actually okay without using any of these skills?"
```
Concrete two-step audit procedure: (1) run `/doctor` every 2-4 weeks, (2)
periodically test with skills disabled entirely to check whether they are
still earning their keep, rather than assuming removal is unsafe by
default.

### Cited empirical papers (new to this corpus)
```
- arXiv:2606.15828 — "Configuration Smells in AGENTS.md Files: Common
  Mistakes in Configuring Coding Agents" (dos Santos, Costa, Montandon,
  Silva, Valente). 100-repo study; Lint Leakage 62%, Context Bloat 42%,
  Skill Leakage 35%.
- arXiv:2608.10319 — "Do Personalized Skills Help Coding Agents? An
  Empirical Study of Developer Interaction Histories" (Huang, Du, Lan).
  206 sessions, 13 developers; generic skills outperform personalized.
- arXiv:2607.27250 — "Do Context Files Help Coding Agents? A Two-Agent
  Ablation Study on Real Repositories" (Khatri). 288 runs, 17 tasks, 3
  repos, Claude Code + Codex; no measurable correctness effect.
- arXiv:2607.09691 — "What Context Does a Coding Agent Actually Need to
  Act?" (Sam-Bodden). SWE-bench Verified; prose summaries answer 4/45
  behavioral questions vs. 27/45 for source code.
```

## Cross-References

- **Corroborates**: `blog-anthropic-context-engineering-claude-5.md` Claim 1
  (Anthropic's own >80% Claude Code system-prompt reduction with no
  measurable loss) — this source's Claim 9 re-cites the identical figure
  from a practitioner's vantage point, and this extraction independently
  re-confirmed the primary-source wording directly against the Anthropic
  blog post's text.
- **Corroborates**: `blog-anthropic-context-engineering-claude-5.md` Claim 14
  (`claude doctor`/`/doctor` command announcement, which that note flags as
  having no detail on internal mechanism) — this source's Claims 10-11
  partially fill that gap with a user's first-hand account of what the
  command checks and the `/doctor`-vs-`claude doctor` naming trap, though
  still short of a documented spec.
- **Corroborates**: `blog-osmani-good-spec.md` Claim 5 (the "curse of
  instructions" — adherence drops as instruction count grows) — this
  source's Claim 3 ("the file balloons, adherence drops, you add more and
  more rules and quality can end up getting worse") is the same author
  restating the identical mechanism in a different post, giving internal
  consistency across two of his pieces.
- **Corroborates**: `blog-anthropic-claude-code-skills-lessons.md` Claim 7
  (skills should not restate capabilities Claude already has) and Claim 8
  (avoid railroading with overly specific instructions) — this source's
  Claim 3 (redundant content duplicated from READMEs/manifests) and Claim 7
  (context files can't teach subtle judgment) describe the same
  over-specification failure mode from the practitioner-audit side rather
  than the skill-authoring side.
- **Corroborates**: `failure-claudemd-ignored-compaction.md` Lesson 5
  (settings.json permissions are the only fully reliable enforcement
  mechanism, since prose rules are advisory) — this source's "archive
  first, encode hard rules in a test/hook/permission" principle (see
  Concrete Artifacts) reaches the same conclusion from a configuration-audit
  angle rather than a compaction-failure angle: two independent sources now
  agree that CLAUDE.md prose is not a reliable enforcement channel for
  hard constraints.
- **Extends, with a nuance (not a contradiction)**:
  `paper-gloaguen-agentsmd-effectiveness.md` (arXiv:2602.11988) Claim 1
  (LLM-generated AGENTS.md files reduce success rates) and Claim 2
  (developer-written context files improve success by ~4%). This source's
  Claim 6 (arXiv:2607.27250, Khatri) found context-file *presence* made no
  measurable difference to correctness at all, including implicitly for
  curated/developer-maintained files in the study's repos. This is not a
  direct contradiction of Gloaguen et al.'s ~4% developer-written
  improvement, because the two studies measure different independent
  variables — Gloaguen compares *generation method* (LLM-generated vs.
  developer-written vs. none) on SWE-bench/AGENTbench tasks, while Khatri
  ablates context-injection *strategy* across a different task set (17
  real tasks, 3 repos) with equivalence testing bounding any effect to
  ≤10-15pp. Both studies agree LLM-generated/auto-bloated files are the
  clearest problem case; they simply disagree on how much a *good*
  developer-written file helps (small-but-positive vs. statistically
  indistinguishable from zero). Flagging this here per MINER.md §4a
  guidance rather than picking a winner — this is a genuine open question
  in the literature this corpus is tracking, not yet at the bar of filing a
  formal contradiction issue since both papers point the same direction
  (auto-generated bad, presence-alone insufficient) and diverge only on the
  magnitude of developer-written-file benefit.
- **Extends**: `blog-addyosmani-code-agent-orchestra.md` Claim 7
  (LLM-generated AGENTS.md files offer no benefit and can reduce success
  rates ~3% while increasing costs 20%+, also citing the Gloaguen/ETH
  Zurich study) and Claim 11 (the AGENTS.md-for-compound-learning
  recommendation, which that note flags as in tension with Claim 7) — this
  source's audit-cadence framing (Claims 1, 10-13) gives the practical
  resolution that note's Claim 11 assessment calls for: the fix isn't
  choosing auto-generated vs. developer-written once, it's periodically
  re-auditing whichever kind of file you have, since even developer-written
  files decay as models/harnesses improve (Claim 1).
- **Extends**: `blog-addyosmani-intent-debt.md` Claim 8 (AGENTS.md as an
  intent ledger, not auto-generated config) — this source's Claim 2 (config
  smell prevalence) and Claim 3 (self-audit failure modes) give the
  concrete failure-mode evidence for why treating AGENTS.md as
  auto-generated/exhaustive config (rather than a curated intent ledger)
  goes wrong in practice.
- **Novel** (not present in any existing corpus source prior to this note):
  1. The 100-repo configuration-smell prevalence study (arXiv:2606.15828)
     and its exact percentages (Claim 2).
  2. The personalized-vs-generic-skills empirical study (arXiv:2608.10319)
     and its finding that personalization provides small, inconsistent
     gains while generic skills pooled across developers perform best
     (Claims 4-5).
  3. The context-file correctness ablation study (arXiv:2607.27250, 288
     runs/17 tasks) and its finding that context files change workflow
     efficiency without changing correctness (Claim 6).
  4. The prose-summary-vs-source-code study (arXiv:2607.09691) and its
     4/45 vs. 27/45 figure (Claim 8).
  5. The skill discovery-listing budget mechanic (1% of context window,
     body loads only on invocation) as a corrective to the assumption that
     every installed skill's full body taxes every prompt (Claim 12).
  6. The `/doctor`-vs-`claude doctor` naming trap (Claim 11).

## Guide Impact

- **Chapter 02 (Harness Engineering — CLAUDE.md/skill maintenance)**: Add a
  recurring-audit recommendation distinct from existing initial-authoring
  guidance, citing this source's Claim 1 (configuration half-life) and
  Claim 13 (audit cadence: run `/doctor` every 2-4 weeks; periodically test
  with skills disabled entirely). Currently the guide's harness-engineering
  content mostly covers how to *write* CLAUDE.md/skills well; this source
  supports adding a maintenance-loop subsection with a concrete cadence and
  a falsifiable test ("try the task with local skills disabled — is it
  actually worse?").
- **Chapter 02 (Harness Engineering — hard constraints)**: Add the
  "archive first, encode hard rules in a test/hook/permission rather than
  prose" principle (Concrete Artifacts) as an explicit rule, now
  corroborated by two independent sources (this note and
  `failure-claudemd-ignored-compaction.md` Lesson 5) that prose-based
  CLAUDE.md rules are advisory rather than enforced.
- **Chapter 03/04 (Skill authoring / Context Engineering)**: Update any
  existing guidance that treats personal-preference accumulation into
  skills or memory as low-cost, citing Claims 4-5: personalized skills
  showed small/inconsistent gains vs. generic skills in a 206-session
  study, and a preference should recur across multiple similar tasks
  before being promoted to a durable skill/memory entry — not be promoted
  on first mention.
- **Chapter 04 (Context Engineering — what belongs in CLAUDE.md)**: Add
  Claims 6-8 as evidence for a specific scoping rule: CLAUDE.md/AGENTS.md
  content should cover operational facts the model can't infer (expensive
  commands, generated files, safety rules) and should `@`-reference real
  code rather than restate it in prose, backed by the 4/45 vs. 27/45
  finding (Claim 8) and the 288-run correctness-null-result (Claim 6).
- **Chapter 02 (Harness Engineering — tooling reference)**: If the guide
  documents `/doctor`, add the naming-trap warning (Claim 11:
  session-`/doctor` vs. shell-`claude doctor` are different commands) and
  the specific hygiene checks Claim 10 describes it performing (unused
  skills/MCP/plugins by context cost, over-specified CLAUDE.md, slow
  hooks), while noting per this note's own hedge that this is a user
  account, not documented command internals.

## Extraction Notes

- The article is a single-page blog post (no paginated sub-sections). Per
  MINER.md §1, I followed the substantive external links found in the
  page: all four cited arXiv papers (fetched each paper's own abstract page
  directly to confirm Osmani's figures against the primary source, not just
  his paraphrase), the linked Claude Code skills documentation page
  (code.claude.com/docs/en/skills, to confirm the 1%-context-window listing
  budget claim), and the linked Anthropic "new rules of context
  engineering" blog post (to independently re-confirm the 80%+ system
  prompt reduction quote against Anthropic's own wording, beyond just
  relying on the existing corpus note). I did not follow the three
  "Related reading" links at the bottom of the page (Brownfield Agentic
  Engineering, Agentic Skill Decay, Human judgment doesn't leave the
  software factory) or the O'Reilly book link, since these are
  navigation/cross-promotion rather than sources this article's claims
  depend on — none of them are cited as evidence within the article body,
  and neither has an existing source note in this corpus to check against.
- No paywall or access issue: addyosmani.com and all four arXiv abstract
  pages, the Claude Code docs page, and the Anthropic blog post are all
  public and were fetched directly (not summarized) for this extraction.
- Article content was obtained by fetching the raw page HTML and stripping
  markup directly (not via a summarizing fetch), so all quotes above were
  copied character-for-character from the extracted plain text, including
  the article's own curly-quote punctuation.
- `confidence_overall` is set to `emerging` rather than `settled`: several
  of the underlying empirical papers (Claims 2, 8) are individually strong
  (precise, checkable, pre-registered-style methodology), but this note as
  a whole is a practitioner synthesis of recent (mid-to-late-2026) papers
  that have not yet been independently replicated or extensively discussed
  elsewhere in this corpus, and several claims (4-5, 10-13) rest on
  first-person anecdote or simulator-based methodology rather than settled
  measurement.
- The tension between this source's Claim 6 (context-file presence doesn't
  move correctness) and `paper-gloaguen-agentsmd-effectiveness.md`'s Claim
  2 (developer-written files improve success ~4%) is documented under
  Cross-References as an open nuance rather than filed as a formal
  contradiction issue, per MINER.md §4a's guidance that conditioning
  variables (different studies measuring different independent variables)
  are not the same as a real contradiction. If a future source directly
  reconciles or sharpens this gap, it should be filed as a contradiction at
  that point.
