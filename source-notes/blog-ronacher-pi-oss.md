---
source_url: https://lucumr.pocoo.org/2026/5/24/pi-oss/
source_type: blog-post
title: "Building Pi With Pi"
author: Armin Ronacher
date_published: 2026-05-24
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: anecdotal
issue: "#911"
---

# Building Pi With Pi

> Armin Ronacher documents concrete failure modes from dogfooding Pi on its own codebase:
> AI-generated issue descriptions ("slop issues") misdirect downstream agents, LLM-generated
> code over-engineers by adding local defenses instead of fixing global invariants, and AI
> volume pressure is fragmenting the upstream collaboration that makes Open Source valuable.
> Provides the `/is` and `/wr` slash command patterns as operational mitigations.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~1,400 words; first-person practitioner
  analysis; published 2026-05-24)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2, Click, and Sentry, and
  the author of the Pi coding agent described throughout. His blog is a designated `trusted-feed`
  source in this repo. This post is first-hand operational reporting from a maintainer actively
  using AI agents on the same project that receives AI-generated issues and PRs. Claims are
  anecdotal but grounded in publicly verifiable production data (GitHub issue tracker) and direct
  operational experience. He uses the term "clanker" throughout instead of "agent" — explicitly
  footnoted as a preference: "Agency lies with humans, not with machines."
- **Scope**: OSS maintenance challenges under AI-generated issue and PR volume; the specific
  failure mode of AI agents treating issue text as authoritative evidence; Pi's slash command
  patterns for issue investigation (`/is`) and wrap-up (`/wr`); the over-engineering tendency of
  LLM-generated code; volume statistics from Pi's public GitHub tracker; and a broader argument
  about AI fragmenting Open Source collaboration. Does NOT cover: model capability benchmarks,
  Pi's architecture beyond the `.pi` folder patterns, or quantitative analysis beyond the 90-day
  tracker statistics.

## Extracted Claims

### Claim 1: AI-generated issue descriptions ("slop issues") that contain plausible but wrong diagnoses create more work than vague issues with no diagnosis

- **Evidence**: First-hand operational experience from the Pi issue tracker. Ronacher describes
  a specific pattern: issues that are "5% human and 95% clanker-generated" where the clanker
  has "reworded it and made a huge mess of it" — producing "complete guesswork on root causes,
  fake-minimal repros, suggested implementation strategies, analogies to adjacent but often the
  wrong code, and long lists of error classes that might or might not matter."
- **Confidence**: anecdotal (single maintainer's direct experience; publicly observable Pi GitHub
  tracker provides partial corroboration for the volume claims)
- **Quote**: "A bad issue that contains a plausible but wrong diagnosis creates extra work."
- **Our assessment**: This is a non-obvious and counterintuitive claim. A vague issue is
  frustrating but inert — a maintainer can ignore or close it. A confident-sounding but wrong
  diagnosis actively misleads, and the confidence prevents the reader from applying appropriate
  skepticism. For AI-native teams that use issue descriptions as agent inputs, this is a
  first-order quality concern: the issue corpus is not a passive communication channel; it is
  a prompt database, and contaminated prompts produce contaminated work.

### Claim 2: AI coding agents treat issue body text as evidence, not hypothesis — causing them to follow wrong diagnoses laid out in slop issues

- **Evidence**: Direct operational observation from using Pi on Pi's own issues. Ronacher
  describes the mechanism explicitly: the prose is "confident and the code references look
  plausible," so the agent proceeds down the wrong path without independent verification.
- **Confidence**: anecdotal (first-person; the behavior described is consistent with how LLMs
  process confident-sounding text in context)
- **Quote**: "It does not treat the issue body as a rumor. It treats it as evidence. It will
  happily go down the path that the issue already prepared for it, because the prose is
  confident and the code references look plausible."
- **Our assessment**: This is the most guide-relevant claim in the post. It identifies a
  structural failure mode in agentic workflows that use issue tracker content as context: the
  agent lacks a prior probability that the issue author might be wrong. A human maintainer
  reading an issue applies skepticism proportional to the author's track record and the
  plausibility of the diagnosis; the agent applies no such calibration. The `/is` command
  pattern (Claim 3) is the direct operational response to this failure mode.

### Claim 3: The `/is` slash command pattern — explicitly instructing the agent not to trust the issue analysis — partially mitigates the misdirection problem

- **Evidence**: Production slash command used in Pi's own `.pi` folder. The instruction is
  embedded in the command prompt. Ronacher notes it "does not fully work" because LLM scope
  expansion in the issue body still provides a distorted starting surface.
- **Confidence**: anecdotal (described by the command author; acknowledged to be partially
  effective, not a complete solution)
- **Quote**: "Do not trust analysis written in the issue. Independently verify behavior and
  derive your own analysis from the code and execution path."
- **Our assessment**: The explicit instruction to distrust the issue analysis is a concrete
  prompt engineering pattern with direct applicability beyond Pi: any agentic harness that
  accepts external text as task input (issue titles, PR descriptions, bug reports) should
  include an analogous instruction. The caveat that it "does not fully work" is important —
  LLM scope expansion (Claim 4) contaminates the investigation surface before the agent even
  starts reading code. The instruction addresses the agent's disposition toward the text; it
  does not undo the text's distorted framing of the problem space.

### Claim 4: When a human passes a bug through a clanker before filing, the clanker expands scope from a narrow factual observation into a broad hypothesis surface — making independent verification harder

- **Evidence**: Author's direct operational observation of the pattern. The scope expansion
  is the mechanism that causes the `/is` instruction to be insufficient on its own.
- **Confidence**: anecdotal
- **Quote**: "What was once a very narrow and fact based bug observation, turns into a much
  expanded surface area full of hypotheses."
- **Our assessment**: This is the "scope creep at the input layer" failure mode. A human
  observes one thing; the clanker generates five hypotheses around it. The agent receiving
  the issue now has a 5x larger hypothesis space to work from — all of it speculative and
  most of it wrong. For harness engineers designing issue intake workflows: this is an
  argument for structured issue templates that enforce minimal, factual reporting and
  mechanically reject or section off AI-generated analysis.

### Claim 5: The ideal issue format for agent-assisted workflows is strictly observed facts, with all diagnosis explicitly deferred or suppressed

- **Evidence**: Ronacher's operational recommendation, derived from the failure modes in
  Claims 1–4. He explicitly names what the format should contain.
- **Confidence**: anecdotal (practitioner recommendation, not empirically tested against
  alternatives)
- **Quote**: "I increasingly want issue reports to be condensed to what the human actually
  observed: [1] I ran this command. [2] I expected this to happen. [3] This happened instead.
  [4] Here is the exact error or log."
- **Additional quote**: "If you used an LLM to understand the problem, great, maybe leave it
  as a follow-up comment. But the issue and the issue text should be something you own."
- **Our assessment**: This is the direct prescriptive counterpart to Claim 1. The 4-step
  format is a specific, actionable template that any team can adopt for issue reporting norms.
  The "leave diagnosis as a follow-up comment" policy is particularly pragmatic: it does not
  prohibit AI-assisted analysis, it just quarantines it from the primary issue text that agents
  will receive as context. For teams writing agent harnesses that ingest issue tracker content:
  this 4-step format constraint is worth encoding as both a contributor norm and a harness-side
  validation rule.

### Claim 6: LLM-generated code over-engineers solutions by adding local defenses (fallbacks, migrations, tests, tolerant readers) instead of fixing root causes

- **Evidence**: Repeated first-hand observation from Pi codebase maintenance. Specific example:
  a malformed session log crash leads the clanker to add a tolerant reader, then a fallback,
  then a migration, then more debug output, then a test — rather than making the bad state
  impossible.
- **Confidence**: anecdotal (one maintainer's experience with one codebase; but the pattern is
  consistent with known LLM behavior in code generation)
- **Quote**: "If you tell them that 'this malformed session log crashes the reader,' the clanker
  will often add a tolerant reader. Then it will add a fallback, then maybe a migration, then
  more debug output, then a test for all of this. None of this is necessarily wrong in isolation,
  but it can be the wrong move for the system."
- **Our assessment**: This claim is corroborated by CMU paper-miller-speed-cost-quality.md
  (Claims 2 and 3: persistent 41.6% increase in cognitive complexity and 30.3% increase in
  static analysis warnings post-Cursor adoption). The mechanism Ronacher describes — local
  defenses accumulating as individual LLM responses to individual failures — is the
  micro-level explanation for the macro-level complexity increase the CMU study measures across
  806 repositories. The LLM doesn't see the system; it sees the symptom.

### Claim 7: The correct response to bad persisted data is to make bad state impossible, not to handle it — but AI agents default to the opposite

- **Evidence**: Author's architectural observation from Pi's session log design. Pi's session
  log has explicit invariants; the clanker ignores them and adds permissive handling instead.
- **Confidence**: anecdotal (one maintainer's one system; the principle generalizes but the
  evidence is first-person)
- **Quote**: "The clanker's present-day behavior is to just assume that no such invariants exist,
  and instead to make the system work with all kinds of malformedness, blowing up the complexity
  in the process."
- **Additional quote**: "Almost always, the correct fix is not to handle the bad state, but to
  make the bad state impossible."
- **Our assessment**: This names a specific, fixable failure mode in AI-assisted code review and
  generation. The agent's local-failure/local-defense heuristic produces correct individual edits
  that degrade the system. Pulling the conversation back to the global invariant ("the goal is
  to never write bad session data") is the maintainer's job, and Ronacher notes it is "harder
  than it should be, and it's laborious." For harness engineers: this is an argument for
  invariant documentation in CLAUDE.md/AGENTS.md files — explicitly stating the global
  invariants the agent must not violate is a prerequisite for avoiding local-defense
  over-engineering.

### Claim 8: Pi's public GitHub tracker received 3,145 external issues/PRs in 90 days; 2,504 were auto-closed; roughly 17–26% were ultimately addressed; only ~8% of new-contributor PRs were merged

- **Evidence**: Ronacher pulled the public GitHub tracker data while writing the post. The 17%
  figure is reopen events; the 26% figure adds issues referenced by main-branch commits or merged
  PRs. The PR merge rate (8%) is the most pessimistic metric: 60 of 714 auto-closed PRs merged.
- **Confidence**: anecdotal (single-project data from author; methodology is described but not
  independently auditable; metrics are self-reported)
- **Quote**: "that leaves 3,145 external issues and pull requests. Of those, 2,504 were
  auto-closed because they were from non-approved individuals. 17% were re-opened but that
  somewhat undercounts issues, because some remain closed while we still fix them. If we also
  count issues referenced by a main-branch commit or merged pull request that number rises to
  26%. For pull requests the number is worse: 60 of 714 auto-closed PRs were ultimately merged,
  or about 8%."
- **Our assessment**: These numbers are the most concrete public data available on AI-generated
  OSS issue/PR volume and acceptance rates. The 79% auto-close rate (2,504/3,145) reflects Pi's
  policy of closing all external contributions from non-approved individuals — an aggressive but
  operational response to volume pressure. The 8% PR merge rate for new contributors is the most
  striking figure: it suggests the vast majority of external AI-assisted PRs are not aligned with
  what the maintainers want or need. Teams designing contribution policies for AI-adjacent
  projects now have a concrete reference point.

### Claim 9: Sources of low-quality issue/PR spam include autonomous AI agent instances (OpenClaw) and user context configurations that encourage issue creation without user intent

- **Evidence**: Author's categorization of the spam sources observed on Pi's tracker. The
  "without the knowledge of the author" pattern is corroborated by the earlier blog post
  (blog-ronacher-content-for-contents-sake.md, Claim 7).
- **Confidence**: anecdotal (maintainer's direct observation; the OpenClaw name is specific
  and verifiable)
- **Quote**: "Sources of low-quality spam include OpenClaw instances, as well as some skills
  that people put into their context that seemingly encourage issue creation."
- **Our assessment**: This is a specific operational taxonomy that extends Claim 7 of the
  earlier Ronacher post. Two categories are named: (1) fully automated agents (OpenClaw) with
  no human in the loop, and (2) context skills that trigger issue creation as a side effect of
  other user-intent actions. Category 2 is particularly important for harness engineers: a
  skill that "encourages issue creation" may be doing exactly what the user configured it for,
  but the downstream recipient experiences it as automated spam. The distinction between
  intentional automation and accidental automation matters for designing policy responses.

### Claim 10: Pi uses a parallelism pattern — multiple agent windows running `/is` against different issues simultaneously, with session naming that keeps investigations visually distinct

- **Evidence**: Operational description of the Pi `.pi` folder tooling. The `prompt-url-widget`
  extension is described with specific behavior: watches the prompt before agent start, fetches
  issue metadata via `gh`, renames the session, rebuilds state on session start/switch.
- **Confidence**: anecdotal (author's own tool, described first-hand)
- **Quote**: "In practice this means it's possible to have several Pi windows open, each running
  `/is` against a different issue, and the UI keeps the investigations visually distinct while
  the agents do their independent reproduction and code reading. Once the investigations are done,
  one can work through them sequentially."
- **Our assessment**: This is a concrete parallelism pattern for issue triage that decouples
  investigation from resolution. Multiple agents reproduce in parallel; the human processes the
  results sequentially. The session naming mechanism (auto-retitled to issue title/author) is a
  low-friction UX decision that eliminates the cognitive overhead of managing parallel agent
  sessions. For harness engineers: this is an operational workflow pattern, not just a Pi-specific
  feature — the equivalent pattern can be implemented in any coding agent that supports named
  sessions.

### Claim 11: The `/wr` (wrap-up) slash command automates all end-of-session boilerplate — changelog, issue comment with disclaimer, scoped commit, closes reference, and push

- **Evidence**: Author's description of the production `/wr` command in Pi's `.pi` folder.
  The description enumerates the specific automated operations.
- **Confidence**: anecdotal (author's own tool; first-hand description)
- **Quote**: "it infers the GitHub context from the session, updates the changelog, drafts or
  posts the final issue comment with a disclaimer, commits only the files changed in that
  session, adds the appropriate `closes #...` when there is exactly one issue, and pushes
  from `main`."
- **Our assessment**: The `/wr` command is the closing bookend to `/is`. Together they define
  an agentic issue workflow with a clear start (investigate, don't trust the issue) and a clear
  end (wrap up, post, commit, close). The "posts the final issue comment with a disclaimer" is
  significant — the agent explicitly signals its involvement at the close of the workflow rather
  than presenting output as purely human. This is a concrete implementation of the transparency
  norm Ronacher advocated in blog-ronacher-content-for-contents-sake.md (Claim 8). The "commits
  only the files changed in that session" scope constraint is also notable: it prevents agents
  from accidentally committing unrelated work touched in the same working directory.

### Claim 12: AI makes local workarounds cheap, discouraging the upstream collaboration that improves shared infrastructure for everyone

- **Evidence**: Author's synthesis from Pi maintenance experience and the broader OSS
  observation. Named as a structural problem, not an individual failure.
- **Confidence**: anecdotal (normative/structural argument from a single practitioner; consistent
  with the over-engineering observations in Claims 6–7)
- **Quote**: "Instead of humans talking to humans about where a fix belongs, one human and one
  machine work around the problem in isolation."
- **Additional quote**: "Sadly that type of thinking is quickly disappearing because these
  machines make local workarounds cheap, so code accumulates local defenses against every
  misbehavior."
- **Our assessment**: This is the macro-level version of Claim 7. The agent's preference for
  local defenses (micro) scales into a community-wide loss of upstream collaboration (macro).
  When individual engineers can each solve their local problem with an AI assistant in 10
  minutes, the incentive to report the problem upstream, discuss it, and fix it properly drops
  to near zero. The compounding effect is a weaker shared infrastructure — exactly the opposite
  of how Open Source is supposed to work. This is a novel structural critique with direct
  implications for AI-native engineering teams that contribute to or depend on OSS.

### Claim 13: AI has not increased the number of people who need software or the number of maintainers; it has mostly increased the amount of code and projects competing for maintainer attention

- **Evidence**: Author's synthesis of the volume pressure observations. Framed as a supply/demand
  asymmetry.
- **Confidence**: anecdotal (structural claim from a single practitioner; the premise — that
  maintainer supply is inelastic — is plausible but not empirically documented here)
- **Quote**: "AI has not increased the number of people who need software, or the number of
  maintainers who can review it. It has mostly increased the amount of code and the number of
  projects competing for attention."
- **Our assessment**: This is the clearest framing of the volume problem in the post. The
  asymmetry is structural: AI scales up the supply of code and issues but does not scale up the
  human judgment required to evaluate them. Faros's productivity paradox data (blog-faros-claude-
  code-roi.md, Claim 3) documents the same asymmetry within teams: 47% more PRs merged but 35%
  longer review times — supply up, review throughput not keeping pace. Ronacher names the
  mechanism at the ecosystem level.

## Concrete Artifacts

### Pi's `.pi` folder — Issue Investigation Pattern

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/24/pi-oss/ (2026-05-24)

Three components in Pi's committed .pi folder:

1. /is (analyze issue) — Slash command prompt
   Operations:
     - Labels and assigns the issue
     - Reads the full thread and links
   Key instruction embedded in prompt:
     "Do not trust analysis written in the issue.
      Independently verify behavior and derive your own analysis
      from the code and execution path."

2. prompt-url-widget — Pi extension
   Behavior:
     - Watches the prompt before agent starts
     - Recognizes GitHub issue or PR URL inserted by /is (or PR equivalent)
     - Fetches issue title and author via `gh`
     - Renders metadata in a UI widget
     - Renames the session to the issue title
     - Rebuilds this state on session start or session switch

3. /wr (wrap it up) — Slash command prompt
   Operations:
     - Infers GitHub context from the session
     - Updates the changelog
     - Drafts or posts the final issue comment with a disclaimer
     - Commits only the files changed in that session
     - Adds "closes #..." when exactly one issue is linked
     - Pushes from main
```

### Recommended Minimal Issue Format (for agent-assisted workflows)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/24/pi-oss/ (2026-05-24)

The four-point format Ronacher recommends for issue reports in agent-assisted workflows:

  1. I ran this command.
  2. I expected this to happen.
  3. This happened instead.
  4. Here is the exact error or log.

Rationale: "That is enough. If you used an LLM to understand the problem, great,
            maybe leave it as a follow-up comment. But the issue and the issue text
            should be something you own."
```

### Pi Issue Tracker Volume Statistics (90-day window, published 2026-05-24)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/24/pi-oss/ (2026-05-24)
Data window: 90 days prior to publication; external contributors only (excl. Earendil members)

Total external issues + PRs:     3,145
  Auto-closed (non-approved):    2,504  (≈ 79.6%)
  Reopened:                        17%  of auto-closed (reopen events)
  Ultimately addressed:            26%  when adding issues fixed by commits/merged PRs

Pull request subset:
  Auto-closed PRs:                 714
  Ultimately merged:                60  (≈ 8.4%)
```

## Cross-References

- **Extends**: `blog-ronacher-content-for-contents-sake.md` — Same author. The earlier post
  (2026-05-04) documents the societal-level problem of AI-generated content flooding platforms
  and eroding trust; this post provides the operational follow-up from the same author's own
  project: concrete volume statistics, specific failure modes with named patterns, and working
  mitigations. In particular:
  - Claim 5 of the earlier note (infrastructure systems failing under AI content flooding) is
    now documented with specific numbers (3,145 issues, 79% auto-close rate) from Pi.
  - Claim 7 of the earlier note (AI-generated issues filed without user knowledge) is now
    taxonomized with named source categories: OpenClaw instances, context skills that encourage
    issue creation.
  - Claim 8 of the earlier note (transparency norm when using AI) is implemented in the `/wr`
    command's "posts the final issue comment with a disclaimer" behavior.
  - The engagement-metrics critique (Claim 9 of the earlier note) is grounded here with the
    specific volume statistics that illustrate why raw issue/PR counts are a poor signal.

- **Corroborates**: `paper-miller-speed-cost-quality.md` Claims 2 and 3 (persistent 41.6%
  increase in cognitive complexity and 30.3% increase in static analysis warnings post-Cursor
  adoption across 806 OSS repositories). Ronacher describes the micro-level mechanism — agents
  add tolerant readers, fallbacks, migrations, and debug output to each local failure — that
  the CMU paper's macro-level metrics quantify. The two sources together provide both the
  mechanism (how individual LLM responses accumulate complexity) and the measured outcome (how
  that accumulation manifests across repositories at scale).

- **Corroborates**: `blog-faros-claude-code-roi.md` Claim 3 (Team B at 60% Claude adoption: 47%
  more PRs merged daily but 35% longer review times). Ronacher names the same volume-without-
  quality asymmetry at the OSS ecosystem level: AI increases code and issue supply without
  increasing the human review capacity needed to process it. The Faros data documents this
  within teams; Ronacher documents it across an entire project's external contributor base.

- **Novel**:
  - **"Slop issue" as a named failure category**: No existing corpus note names AI-generated
    issue descriptions with wrong diagnoses as a distinct quality problem. The concept of an
    issue that is confident, detailed, and wrong — worse than a vague issue — is new to the
    corpus.
  - **Issue body as agent evidence vs. hypothesis**: No existing corpus source documents the
    failure mode where an AI agent treats issue text as authoritative evidence rather than an
    unverified claim. This is a specific, named vulnerability in agentic issue-triage workflows.
  - **The `/is` instruction pattern ("do not trust analysis in the issue")**: No existing corpus
    source documents an explicit "distrust the input" instruction as a harness-level safety
    mechanism for agent workflows that consume external text. This is a novel prompt engineering
    pattern with broad applicability.
  - **The `/wr` wrap-up command with scoped commit and transparency disclaimer**: The combination
    of inferred GitHub context, scoped commit (session-only files), and auto-posted disclaimer is
    a novel end-of-session workflow automation pattern not documented in any other corpus note.
  - **LLM preference for local defenses over global invariant enforcement**: While the CMU paper
    measures the complexity outcome, no prior corpus source names the specific mechanism: agents
    default to making bad state tolerable rather than impossible, because they lack visibility into
    global system invariants. This is a new and precise failure mode description.
  - **Upstream collaboration as the casualty of cheap local workarounds**: The argument that AI
    makes local workarounds so cheap that upstream collaboration atrophies is not documented
    elsewhere in the corpus. The framing — not that AI is bad, but that it shifts the
    economic calculus away from shared infrastructure investment — is novel.

## Guide Impact

- **Chapter 00 (Principles — Verification Over Generation)**: Extend the verification principle
  to agent *inputs*, not just agent *outputs*. Claim 2 documents that agents treat issue text as
  evidence rather than hypothesis — this is a specific case where the agent needs to be explicitly
  instructed to apply skepticism to its context before acting. The `/is` instruction pattern
  (Claim 3) is a concrete implementation of input verification discipline.

- **Chapter 02 (Harness Engineering)**: Three additions warranted:
  1. **Issue intake and the 4-step format** (Claim 5): Recommend the 4-step issue format for
     any team using issues as agent task inputs. The format should be enforced via issue template
     and ideally validated by the harness before passing the issue to an agent.
  2. **The `/is` distrust instruction** (Claim 3): Any harness that feeds external text (issues,
     tickets, bug reports) to an agent should include an explicit instruction to independently
     verify claims rather than treating the input as authoritative.
  3. **The `/wr` wrap-up pattern** (Claim 11): The scoped-commit (session-only files) and
     auto-disclaimer pattern are worth documenting as a harness design reference.

- **Chapter 03 (Code Quality)**: Add the local-defense over-engineering failure mode (Claims 6–7)
  alongside the existing complexity increase evidence from Miller et al. The combined picture:
  AI code tends to accumulate local defenses rather than fix root causes, and this accumulation
  is measurable at scale as persistent complexity increase. The mitigation is explicit invariant
  documentation in AGENTS.md files that constrains where the agent can add permissive handling.

- **Chapter 05 (Team Adoption — Measuring Impact)**: Add the issue/PR volume statistics (Claim 8)
  as a calibration reference for teams measuring AI adoption productivity. Raw PR and issue counts
  inflate under AI adoption without reflecting quality; Pi's 8% merge rate for new-contributor PRs
  is a concrete benchmark for what "lots of activity" looks like when most contributions are
  AI-generated.

- **Chapter 06 (Open Source and Community)**: If such a chapter exists or is planned, Claim 12
  (local workarounds vs. upstream collaboration) and Claim 13 (maintainer supply is inelastic)
  are the primary contributions from this post. The argument that AI fragments OSS collaboration
  by making individual workarounds cheaper than shared fixes is novel and directly actionable for
  practitioners deciding when to file upstream issues vs. patch locally.

## Extraction Notes

- Full post text was fetched from https://lucumr.pocoo.org/2026/5/24/pi-oss/ via WebFetch. All
  quotes verified against the fetched content character-for-character.
- The post references a chart ("Weekly external volume and acceptance rate of Pi issues and pull
  requests") and an image ("Pi terminal session showing an agent analysis with a GitHub issue
  widget") that are image/chart artifacts not extractable as text. The numerical data underlying
  the chart is presented verbatim in the prose (Claim 8).
- The footnote about "clanker" terminology ("To me, clanker is a much preferable term for agent.
  Agency lies with humans, not with machines. Calling these things agents I still believe is a
  mistake, but alas.") is preserved in the Source Context section as relevant practitioner
  nomenclature context.
- The `.pi` folder is described operationally in the post but the actual file contents are not
  published in the post. The concrete artifact above is reconstructed from the prose description,
  not from the actual prompt files. The GitHub repository for Pi may contain these files.
- Confidence rated anecdotal overall: all claims originate from one maintainer's first-person
  experience with one project. The 90-day tracker statistics are publicly verifiable (GitHub) but
  not independently audited here. The structural arguments (local workarounds, upstream
  collaboration) are plausible but normative.
- Three Prospector triage comments were included in the issue, each emphasizing slightly different
  angles (Ch00 Verification / Ch02 / Ch05 framing; Ch04 / Ch05 practical deployment; Ch03 / Ch06
  coordination). The extraction covers all three angles.
- No contradiction issues filed: no existing corpus note disagrees with the core claims here.
  The local-defense over-engineering thesis is consistent with (not opposed to) Miller et al.'s
  complexity measurement. The volume fragmentation argument extends rather than contradicts the
  content-for-contents-sake post.
