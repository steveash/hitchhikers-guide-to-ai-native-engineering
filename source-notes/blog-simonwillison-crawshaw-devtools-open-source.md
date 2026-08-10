---
source_url: https://simonwillison.net/2026/Aug/3/david-crawshaw/
source_type: blog-post
title: "A quote from David Crawshaw's prompt"
author: David Crawshaw (quoted by Simon Willison); full essay "Devtools must be open source" by David Crawshaw, published on exe.dev's blog
date_published: 2026-08-03
date_extracted: 2026-08-10
last_checked: 2026-08-10
status: current
confidence_overall: anecdotal
issue: "#2602"
---

# A quote from David Crawshaw's prompt

> David Crawshaw's essay "Devtools must be open source" gives two concrete,
> reusable agent prompts for personalizing software by editing its source
> directly instead of using config/plugin systems — a one-time
> download-and-build prompt and a nightly-cron fetch/rebase/verify prompt —
> and argues the second only works if the agent itself is open source,
> naming Claude Code specifically as the tool this technique cannot reach.

## Source Context

- **Type**: blog-post. Simon Willison's page
  (`simonwillison.net/2026/Aug/3/david-crawshaw/`) is his "quotation" post
  format: a single `<blockquote>` (the nightly-cron prompt, verbatim) plus a
  one-line citation, ~40 words total, no added commentary from Willison.
  Auto-discovered via the `simon-willison` trusted feed. The blockquote's
  `cite` attribute and the citation link both point to the full essay at
  `https://blog.exe.dev/devtools-must-be-open-source`, dated 2026-08-02 and
  bylined "David Crawshaw" — an ~1,150-word first-person essay on exe.dev's
  company blog (exe.dev sells VM/sandbox infrastructure "for AI agents").
  Per MINER.md §1, this Miner read that full linked essay, not just
  Willison's blockquote, since it is where nearly all of the extractable
  content lives.
- **Author credibility**: David Crawshaw writes in the first person about
  building "Shelley" (exe.dev's own coding-agent product) and a personal
  side project (`meat.dev`, a diff-minimizing tool). The essay states his
  own history: "In my early years as an engineer at Google I did not even
  own a personal computer," and that he was "asking this question a lot as
  part of trying to understand how Tailscale could fit into engineers'
  lives" — first-person claims of prior Google and Tailscale experience,
  not independently verified by this Miner beyond the essay's own text. He
  writes as a builder of the agent (Shelley) whose personalization mechanism
  he is describing, not as an independent evaluator — the essay is a vendor
  engineer's account of his own product's design philosophy, dressed as a
  general argument about devtools. Two additional linked posts on the same
  exe.dev blog, both bylined "Philip Zeyliger" (a colleague at exe.dev, not
  Crawshaw), were also read in full because they document the same
  personalization mechanism in practice with screenshots: "Customizing
  Shelley, Customizing Software" (2026-07-22) and "Software as Wiki, Mutable
  Software" (2026-02-13, an earlier precedent post for the same idea).
- **Scope**: Covers a specific technique (agent-driven source-level
  personalization via two named prompts), one worked example
  (`meat.dev` integration), a broader economic argument (why plugin/config
  systems become less necessary as agent-driven code changes get cheaper),
  and a comparative claim about which coding agents the technique reaches
  (open-source: Shelley, Pi, Codex; not reachable: closed-source Claude
  Code). Does NOT cover: adoption metrics, a controlled comparison of
  personalized vs. non-personalized software, failure cases of the rebase
  prompt (e.g., what happens when upstream and local changes conflict), or
  any technical detail of how the "skill" is implemented beyond "some text
  instructions put somewhere discoverable to the agent."

## Extracted Claims

### Claim 1: A one-time prompt can direct an agent to fork a piece of software, build it locally, and durably record why the fork was made
- **Evidence**: Verbatim prompt text, presented as the first of "two general
  categories of prompts to an agent" that make personalizing software
  possible.
- **Confidence**: anecdotal (a single practitioner's prescribed prompt
  wording; not tested against a documented run or shown to work reliably
  across software types)
- **Quote**: "Download the source for <software> and build it for local use. Modify <whatever memory your agent uses> to know that any future changes to this software mean changing the sources and replacing the current version. Record in version control the original motivation behind the change."
- **Our assessment**: The "record in version control the original motivation" instruction is the most transferable detail here — it is a lightweight, generalizable practice (write down *why* a customization exists, not just what it is) independent of whether the reader ever personalizes an entire tool. It maps onto the guide's existing self-documenting-context theme (e.g., the "ratchet" practice already documented in `blog-addyosmani-loop-engineering.md`'s Linked Source Extractions: "Every line in a good `AGENTS.md` should be traceable back to a specific thing that went wrong") applied to fork-level customization instead of repo-level constraints.

### Claim 2: A nightly cron job can be configured to have an agent fetch upstream changes, rebase local customizations on top, verify the result, and replace the running version — unattended
- **Evidence**: Verbatim prompt text, the second and ("more importantly") of
  the two prompts, and the exact text Willison chose to excerpt as the
  entire content of his quotation post.
- **Confidence**: anecdotal (single practitioner's prescribed prompt
  wording; the essay does not report a specific incident of this prompt
  succeeding or failing on a real rebase conflict)
- **Quote**: "Set up a nightly cron job that executes the prompt: fetch upstream changes to the <software> and rebase all local changes on top of upstream. Check that the software works as intended and replace the current version."
- **Our assessment**: This is the anchor content of the source (it is the
  only text Willison chose to quote). It is a specific instance of the
  scheduled-automation pattern already documented from two vendors
  (`blog-anthropic-claude-code-routines.md` Claim 3: "Every night at 2am:
  pull the top bug from Linear, attempt a fix, and open a draft PR";
  `blog-cognition-devin-schedule-devins.md` Claim 1: natural-language
  cadence configuration for recurring Devin sessions) — but applied to a
  narrower and more specific job than either: not arbitrary backlog work,
  but self-maintenance of a customized fork against a moving upstream. No
  existing corpus source documents this specific "rebase my fork nightly"
  use of scheduled agent automation; see Cross-References → Novel.

### Claim 3: The two personalization prompts can be built directly into an agent as a skill (plain text instructions), requiring no additional programming, but only if the agent itself is open source
- **Evidence**: Direct statement, illustrated by exe.dev's own
  implementation in their agent product Shelley.
- **Confidence**: anecdotal (first-person account of the essay author's own
  company building this into their own product; not independently verified
  by a third party)
- **Quote**: "Another astonishing thing about the two prompts above for editing software is that you can build them right into an agent. As long as the agent is open source, it does not even require programming. The two prompts can be loaded into a skill (i.e., some text instructions) put somewhere discoverable to the agent. We built this into Shelley, so now if you want to edit Shelley you don't even need the preamble or to configure the timer."
- **Our assessment**: This reframes "skill" (already a heavily documented
  concept in this corpus, e.g. `blog-anthropic-claude-code-skills-lessons.md`
  Claim 1: "Skills have become one of the most used extension points in
  Claude Code... flexible, easy to make, easy to distribute") for a use case
  not covered elsewhere in the corpus: using a skill not to teach the agent
  about the *codebase it's operating on*, but to teach the agent how to
  maintain and personalize *itself*. This is a meaningfully different scope
  of self-application than the corpus's existing skill-usage examples.

### Claim 4: A single natural-language prompt was sufficient to integrate a separate command-line tool (meat.dev) into Shelley's UI, including background processing and a view toggle, with only a stylistic side-effect (an unrequested emoji) as the "unfortunate" outcome
- **Evidence**: A worked first-person example, including the exact prompt
  text used and the author's own account of the result.
- **Confidence**: anecdotal (single practitioner, single worked example, no
  before/after time measurement or independent replication)
- **Quote**: "Please build meat.dev into Shelley. Install the latest version in the PATH. When a git commit is created by Shelley, start meat processing in the background on the commit. Add a toggle to the Shelley `Diffs` view for meat. If the commit is still being processed, so the user it is in process."
- **Our assessment**: The essay's own follow-up line is worth citing
  alongside this prompt: "This single prompt was all it took not just to add
  meat to Shelley, but to appropriately pre-process commits in the
  background... The only unfortunate choice the model made was using the 🥩
  emoji for the toggle button." The prompt itself has a minor internal
  grammar slip ("so the user it is in process") that this Miner preserved
  verbatim per MINER.md §2a rather than silently correcting — worth noting
  since it shows the author did not visibly edit/polish the prompt before
  publishing it, i.e. this reads as an actual prompt used, not a cleaned-up
  illustrative example.

### Claim 5: The economic case for plugin systems and configuration files was that the cost of learning a codebase well enough to modify it was high, so it made sense to amortize a shared extension mechanism across many users; agents have dropped that learning cost, undermining the case for building plugin/config systems at all
- **Evidence**: Extended argument spanning two paragraphs, contrasting the
  historical cost structure ("The core code of even a moderate project like
  Vim is huge and baroque, and takes weeks for a human to digest") against
  the present one.
- **Confidence**: anecdotal (an economic/design argument asserted by the
  author, not measured — no data on actual engineer-hours saved or a
  comparison of maintenance burden between personalized-fork software and
  plugin-based software)
- **Quote**: "Now the expense of learning the code and making a change has dropped dramatically. Agents do the heavy lifting... The result is that software that can be personalized doesn't need a plugin system or a config file."
- **Our assessment**: This is the essay's central normative claim and the
  one most likely to be contested. It is stated as a general principle, but
  the author's own worked examples (Shelley, meat.dev, the font-size/bitmap-
  font example) are all single-user, single-maintainer tools where the
  "constrained conditions" caveat in Claim 6 applies. The essay does not
  address multi-tenant or team-shared software, where a plugin system still
  serves a coordination function (shared, reviewable extension points across
  many contributors) that a private, unreviewed source fork does not
  replace — this is a gap in the argument's scope that the guide should
  flag rather than adopt uncritically.

### Claim 6: For single-user software, the need for careful code review can often be replaced by simply checking whether the result seems to work
- **Evidence**: Direct statement, explicitly scoped by the author to
  single-user conditions.
- **Confidence**: anecdotal (a general assertion, not measured against any
  defect or regression rate)
- **Quote**: "For a single user—which implies extremely constrained conditions under which the program runs—a top-end agent can usually now add a feature in a single shot. For single-user software, the need for careful code review can often be replaced by "does it seem to work?""
- **Our assessment**: The author explicitly scopes this claim to single-user
  software with "extremely constrained conditions," which keeps it from
  directly opposing the guide's broader, team-scale code-review guidance
  (e.g., the line-by-line review posture in
  `blog-simonwillison-udell-human-agent-loop.md`, or the maintainer-review
  detection account in `blog-simonwillison-andrew-kelley.md`). This Miner
  considered filing a contradiction per MINER.md §4a and rejected it: the
  scoping ("single-user," "extremely constrained conditions") is an explicit
  conditioning variable, not a claim that a general engineering team should
  drop review discipline — per §4a's "when NOT to file" guidance ("differ
  only in context... that's a conditioning variable"). The guide should
  still flag this claim as narrower than it may read on a skim: it is not
  general permission to skip review, only a claim about tools with exactly
  one user who is also the only person exposed to the risk.

### Claim 7: The same personalization economics apply at small-team scale — a team could assemble a bespoke tool from building blocks rather than buy, learn, and configure an off-the-shelf configurable product (task manager, CMS, or CRM)
- **Evidence**: Direct extension of the single-user argument to teams,
  framed as a rhetorical question.
- **Confidence**: anecdotal (a hypothetical extrapolation; the essay gives no
  worked example of a team actually doing this, unlike the single-user
  Shelley/meat.dev example)
- **Quote**: "Personal software applies well to small teams too. Why would an engineering team purchase an extremely configurable task manager (or a CMS or CRM), spend time learning and configuring it, and contort their team to its limits, when they can assemble just the features they want from common building blocks?"
- **Our assessment**: This is the essay's least-evidenced claim — it is
  posed as a rhetorical question with no worked team-scale example, in
  contrast to Claim 4's concrete single-user worked example. The guide
  should treat this as speculative extrapolation from the single-user case,
  not as a separately-demonstrated finding.

### Claim 8: The author's own company blog (blog.exe.dev, where this essay itself is published) is bespoke software built and personalized via Shelley rather than a configured, off-the-shelf CMS
- **Evidence**: Direct first-person statement about the specific artifact
  the reader is looking at.
- **Confidence**: anecdotal (a single self-referential example; not
  independently verifiable by this Miner beyond the author's own claim)
- **Quote**: "The blog you are reading is bespoke software, written in Shelley, because it was easier to piece together and personalize libraries like Tiptap than it is to try and customize traditional software products."
- **Our assessment**: This is a "dogfooding" claim — the essay's own
  publishing platform is offered as evidence for its thesis. It is a real,
  checkable-in-principle existence proof (this Miner did directly load and
  read the page, which functioned as an ordinary blog), but it is still a
  single example from the company whose product is being promoted, not
  independent validation.

### Claim 9: The source-editing personalization technique can be trivially applied to other open-source coding agents (named: Pi, Codex) but Claude Code is closed-source, so this technique cannot reach it — leaving Claude Code's built-in customization hooks as the ceiling
- **Evidence**: Direct comparative statement under the essay's closing
  section, "Where Codex and Claude Code Diverge."
- **Confidence**: anecdotal (a single practitioner's comparative
  assessment of three named products' extensibility; no test of Codex or
  Claude Code customization was described, and Codex's open-source status
  is asserted without citation)
- **Quote**: "This same skill-based technique that was applied to Shelley to make it personalizable can be trivially applied to other open-source agents like Pi... It would require a lot more tokens, but you could do the same to Codex, which is an open-source agent. Where you would hit a wall, however, is Claude Code. It is closed-source software, so you don't get to personalize it. There are a lot of old-fashioned customization hooks in Claude Code. Hopefully, how you want an agent to work fits in their hooks. If not, switch to an agent that lets you personalize it."
- **Our assessment**: This claim is worth flagging alongside, not directly
  against, `blog-anthropic-claude-code-skills-lessons.md` Claim 1 (skills as
  Claude Code's most-used extension point) and Claim 13 (on-demand hooks for
  session-scoped safeguards): those describe hooks/skills as a genuinely
  well-used, flexible extension surface *for the tasks Claude Code performs
  on a target codebase*. Crawshaw's claim is about a different, narrower
  target — personalizing the Claude Code *tool itself* (its own UI,
  behavior, internals) — which hooks and skills are not designed to reach
  regardless of how well-used they are for their intended scope. Read this
  way, the two are compatible rather than opposed: hooks can be a genuinely
  strong extension point for what Claude Code does to your code, while
  still being a hard ceiling for what you can do to Claude Code itself. Not
  filed as a contradiction under MINER.md §4a — the claims address different
  scopes (agent-as-tool-you-use vs. agent-as-software-you-modify), not the
  same claim under different conditions.

### Claim 10: In Shelley's shipped implementation, the nightly-rebase prompt (Claim 2) is realized as a UI feature — new Shelley releases automatically rebase a user's customizations onto the latest version, surfaced as a "CUSTOMIZED" build label with an explicit "Upgrade: rebase onto latest" action
- **Evidence**: A companion post on the same blog, "Customizing Shelley,
  Customizing Software" (Philip Zeyliger, 2026-07-22, linked directly from
  the main essay via "It takes care of it for you."), including three
  screenshots the author describes in alt text.
- **Confidence**: anecdotal (first-party product description with
  screenshots from the vendor's own blog; not independently tested by this
  Miner or a third party)
- **Quote**: "If you want to customize Shelley, open up a conversation, and ask the agent to change itself. It will do so. When a new version of Shelley ships, it rebases your customizations onto the latest version, so your changes always carry forward."
- **Additional quote (screenshot alt text, verbatim)**: "Shelley's Version dialog showing a CUSTOMIZED build with an 'Upgrade: rebase onto latest' button."
- **Our assessment**: This is the strongest evidence in the source set that
  Claim 2's nightly-cron prompt is not merely a hypothetical prompt
  suggestion but has a real, named, shipped UI surface behind it (a labeled
  build state and an explicit rebase action) — moving Claim 2 from "a prompt
  someone wrote in a blog post" to "a prompt describing a real product
  feature," even though this Miner did not use Shelley directly to confirm
  the screenshots' behavior firsthand.

### Claim 11: An earlier example (Slinky, a link shortener) demonstrates the same "edit the software directly instead of configuring it" pattern predating this essay — a single natural-language prompt added a templating feature to a live tool in minutes via an "Edit with Shelley" button
- **Evidence**: A second companion post on the same blog, "Software as Wiki,
  Mutable Software" (Philip Zeyliger, 2026-02-13, linked from the
  "Customizing Shelley" post via the phrase "treat it like a wiki"),
  documenting an earlier, unrelated worked example with the exact prompt
  used.
- **Confidence**: anecdotal (single practitioner, single worked example,
  older than the main essay by roughly six months, self-published by the
  same company)
- **Quote**: "Some slinky URLs have "template" parameters. For example, I want http://slinky.exe.xyz/trace/foo to become https://ui.honeycomb.io/[%20 %20 so much quoting %20]foo[...] Note how "foo" has to be replaced in that mess of escaping. Create a way to put a placeholder in the link, and reference it like I mention. While you're add [sic] it, add a link for this one."
- **Our assessment**: This predates the main essay and establishes that
  exe.dev's "personalization via direct prompt-driven editing" thesis is not
  a new argument invented for this essay — it is a company talking point
  going back at least to February 2026, with this essay being the most
  fully argued (and most widely circulated, via Willison's amplification)
  version of it. The "[sic]" in the extracted quote is the source's own
  annotation of the prompt's grammar error ("While you're add it"), not this
  Miner's addition — preserved per MINER.md §2a.

## Concrete Artifacts

```
Source: David Crawshaw, "Devtools must be open source,"
https://blog.exe.dev/devtools-must-be-open-source (2026-08-02)

The two personalization prompts, verbatim:

1. "Download the source for <software> and build it for local use. Modify
   <whatever memory your agent uses> to know that any future changes to
   this software mean changing the sources and replacing the current
   version. Record in version control the original motivation behind the
   change."

2. "Set up a nightly cron job that executes the prompt: fetch upstream
   changes to the <software> and rebase all local changes on top of
   upstream. Check that the software works as intended and replace the
   current version."

The meat.dev integration prompt, verbatim:

"Please build meat.dev into Shelley. Install the latest version in the
PATH. When a git commit is created by Shelley, start meat processing in
the background on the commit. Add a toggle to the Shelley `Diffs` view for
meat. If the commit is still being processed, so the user it is in
process."
```

```
Source: Simon Willison's Weblog, blockquote as published,
https://simonwillison.net/2026/Aug/3/david-crawshaw/ (2026-08-03)
cite attribute: https://blog.exe.dev/devtools-must-be-open-source
Citation line: "— David Crawshaw's prompt, Devtools must be open source"
Tags applied: open-source, ai, prompt-engineering, generative-ai, llms, coding-agents
```

```
Source: Philip Zeyliger, "Software as Wiki, Mutable Software,"
https://blog.exe.dev/software-as-wiki (2026-02-13)

Slinky templating-feature prompt, verbatim:

"Some slinky URLs have "template" parameters. For example, I want
http://slinky.exe.xyz/trace/foo to become
https://ui.honeycomb.io/[%20 %20 so much quoting %20]foo[...]
Note how "foo" has to be replaced in that mess of escaping. Create a way to
put a placeholder in the link, and reference it like I mention. While
you're add [sic] it, add a link for this one."

Result, as stated: "And then a few minutes later, Shelley had one-shotted
this small feature to Slinky."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-routines.md` Claim 3 (scheduled routines run
    on practitioner-configured cadences, example: "Every night at 2am: pull
    the top bug from Linear, attempt a fix, and open a draft PR") and
    `blog-addyosmani-loop-engineering.md` Claim 3 ("Automations... are the
    primitive that makes a system a loop rather than a single agent run") —
    Claim 2 here is a specific instance of the same nightly-scheduled-agent
    pattern, corroborating that unattended, cron-triggered agent work is a
    recognized and repeatedly-independently-described pattern across
    multiple vendors and practitioners.
  - `blog-cognition-devin-schedule-devins.md` Claim 1 (natural-language
    scheduling eliminates the need to configure a cron job) — both sources
    frame agent-driven scheduling as removing traditional cron/infrastructure
    management, though this source's version is explicitly a cron job the
    user still sets up ("Set up a nightly cron job..."), while Cognition's
    is agent-inferred cadence from a natural-language request. This is a
    difference in mechanism, not a contradiction — see Guide Impact.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 1 (skills as
    Claude Code's most-used extension point, "flexible, easy to make, easy
    to distribute") — corroborates the general claim that a "skill" (plain
    text instructions discoverable to the agent) is a low-effort,
    widely-adopted mechanism for extending agent behavior, which this
    source applies to a novel target (personalizing the agent itself).

- **Contradicts**: None filed. Two candidate tensions were identified and
  explicitly evaluated against MINER.md §4a, and neither met the filing
  bar:
  1. Claim 6 ("for single-user software, code review can often be replaced
     by 'does it seem to work?'") against the team-scale review discipline
     implied elsewhere in the corpus (e.g. `blog-simonwillison-andrew-
     kelley.md`, `blog-simonwillison-udell-human-agent-loop.md`) — rejected
     as a conditioning-variable difference (single-user vs. team/production
     software), not a same-conditions disagreement. See Claim 6's
     assessment.
  2. Claim 9 (Claude Code's hooks are a "wall" the personalization
     technique cannot cross) against `blog-anthropic-claude-code-skills-
     lessons.md` Claim 1/Claim 13 (hooks and skills as flexible, widely-used
     extension points) — rejected as a scope difference: one source
     describes hooks as an extension point for *what Claude Code does to
     your code*, the other describes a ceiling on *modifying Claude Code
     itself*. See Claim 9's assessment.

- **Extends**:
  - `blog-addyosmani-loop-engineering.md` and
    `blog-anthropic-claude-code-routines.md`: both document the general
    "scheduled/automated agent work" primitive; this source adds a specific,
    previously undocumented application of it — self-maintaining a
    personalized fork of a piece of software against upstream, rather than
    working an arbitrary backlog or triage queue.
  - `blog-anthropic-claude-code-skills-lessons.md`: extends the documented
    "skill" concept (a folder of text instructions discoverable to the
    agent) to a new use case — teaching an agent how to modify and maintain
    itself, not just how to operate on an external codebase.

- **Novel**:
  - The specific "nightly cron: fetch upstream, rebase local changes,
    verify, replace" prompt as a named, reusable pattern for maintaining a
    personalized fork of a tool is new to this corpus — no existing source
    note documents agent-driven fork maintenance as a distinct pattern from
    general scheduled/backlog automation.
  - The explicit claim that a coding agent's *own* openness (open-source vs.
    closed-source) determines whether users can apply source-level
    personalization to the agent itself is new to this corpus. Prior
    corpus sources on open vs. closed tooling
    (`blog-simonwillison-gemini-spark-antigravity.md` Claims 6-7) document
    open-vs-closed transitions for a product's *distribution* model, not a
    claim tying agent openness to a specific downstream capability
    (self-personalization by the agent's own users).
  - The "record in version control the original motivation behind the
    change" instruction (Claim 1) as an explicit sub-step of a
    personalization prompt is a specific, actionable detail not present in
    the corpus's existing self-documenting-context material.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the two-prompt personalization
  pattern (Claims 1-2, full text in Concrete Artifacts) as a named, reusable
  template distinct from the general-purpose scheduled-automation guidance
  already sourced from `blog-anthropic-claude-code-routines.md` and
  `blog-cognition-devin-schedule-devins.md`. Specifically: existing guide
  content on scheduled automation should distinguish "automate an arbitrary
  recurring task" (the Routines/Scheduled-Devins framing) from "automate the
  maintenance of a tool you have personally customized against a moving
  upstream" (this source's framing) — the second is a narrower, more
  specific and immediately actionable pattern for readers who maintain
  personalized forks of dependencies or internal tools.

- **Chapter 02 (Harness Engineering) — tool selection**: Add Claim 9 (open-
  source agents like the essay's named Shelley/Pi/Codex permit source-level
  self-personalization; closed-source Claude Code does not, leaving its
  built-in hooks as the customization ceiling) as a new axis for any guide
  discussion of choosing a coding agent: not just capability/cost/plan-tier
  comparisons already covered elsewhere in the corpus, but whether a team
  or individual practitioner wants to be able to modify the agent tool's
  own behavior beyond what its built-in extension points (hooks, skills,
  plugins) expose. Cross-reference `blog-anthropic-claude-code-skills-
  lessons.md`'s hooks/skills content so the guide presents this as a scope
  distinction (extending what the agent does to your code vs. modifying the
  agent itself), not an unqualified "open beats closed" claim.

- **Chapter 04 (Context Engineering, skeleton)**: Add Claim 1's "record in
  version control the original motivation behind the change" as a concrete,
  minimal-effort instruction pattern for keeping a customization's *why*
  attached to the change itself — applicable to any fork-and-customize
  workflow, not only full-agent personalization.

- **Chapter 03 (Verification)**: If/where the guide discusses when reduced
  review rigor is appropriate, cite Claim 6 with its explicit scoping
  ("single-user... extremely constrained conditions") as a concrete,
  citable instance of a practitioner narrowing rather than rejecting review
  discipline — useful as a worked example of the boundary condition, paired
  with a caution that the guide should not let this be read as general
  permission to relax review on team-shared or production software.

## Extraction Notes

1. **WebFetch produced an incorrect URL on first attempt**: an initial
   WebFetch of the Simon Willison page returned a summary that stated the
   linked essay's URL as `blog.exe.dev/devtools-must-open-source`, which
   404s. Fetching the page's raw HTML directly via `curl` showed the actual
   `cite` attribute and citation link both point to
   `blog.exe.dev/devtools-must-be-open-source` (note "must-**be**-open-
   source"). All further fetching in this note used the corrected URL and
   was independently verified by re-fetching that URL directly (HTTP 200).
   This is flagged because it demonstrates WebFetch's summarizing pass can
   silently fabricate a plausible-looking but wrong URL, not just a
   paraphrased quote — the Assayer should re-verify this note's URLs
   directly rather than trusting a summarizer.
2. **All quotes verified against raw HTML, not summarizer output**: per
   MINER.md §2a, every quote in this note (from all three fetched pages —
   the Willison page, the main Crawshaw essay, and both Philip Zeyliger
   companion posts) was extracted by fetching raw HTML with `curl` and
   locating the exact source text via direct string search in the raw
   bytes (not `html2text` or WebFetch's model-summarized output), to
   guarantee character-for-character accuracy including the source's own
   typos, curly quotes, and one explicit "[sic]" annotation. No quote in
   this note was reconstructed from a paraphrase or an AI-generated
   summary.
3. **Followed 2 of the essay's linked pages, per MINER.md §1's "follow up
   to 5 linked pages that seem substantive"**: "Customizing Shelley,
   Customizing Software" (linked directly from the main essay) and
   "Software as Wiki, Mutable Software" (linked from the Customizing
   Shelley post, one link deep). Both were read in full; both contributed
   claims (10 and 11). The `meat.dev` link and the `exe.dev` navigation/
   product links (Sandbox, VPS, Devbox, Dashboard, pricing) were not
   followed — they are product marketing pages, not further exposition of
   the essay's claims.
4. **No contradiction issue filed**: two candidate tensions were
   identified and evaluated against MINER.md §4a; both were judged to be
   conditioning-variable or scope differences rather than same-conditions
   disagreements. See Cross-References → Contradicts for the reasoning on
   each. The Assayer should independently check both judgments.
5. **Cross-reference verification**: before writing citations above,
   `blog-anthropic-claude-code-routines.md`,
   `blog-addyosmani-loop-engineering.md`,
   `blog-cognition-devin-schedule-devins.md`,
   `blog-anthropic-claude-code-skills-lessons.md`, and
   `blog-simonwillison-gemini-spark-antigravity.md` were each re-read
   directly and all cited claim numbers were confirmed against those
   notes' numbered `### Claim N:` headings in document order; no claim
   number was guessed.
6. **Confidence rated `anecdotal` overall**: every claim in this source
   traces to a single company (exe.dev) describing its own product and its
   own author's personal side project, with no independent adoption data,
   no controlled comparison, and no third-party corroboration of any
   specific outcome (the meat.dev integration, the Slinky templating
   feature, or the Shelley rebase-on-upgrade UI). This matches the
   confidence tier already assigned to this corpus's other single-
   practitioner, single-company Simon-Willison-quotation source notes
   (`blog-simonwillison-andrew-kelley.md`,
   `blog-simonwillison-udell-human-agent-loop.md`). The prompts themselves
   (Claims 1, 2, 4, 11) are concrete and independently reusable regardless
   of confidence tier — the `anecdotal` rating reflects the evidentiary
   backing for the essay's broader economic and comparative claims (Claims
   5-9), not a judgment that the prompt text itself is unreliable or
   fabricated.
