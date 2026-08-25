---
source_url: https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/
source_type: blog-post
title: "Human judgment doesn't leave the software factory. It relocates."
author: Addy Osmani
date_published: 2026-08-21
date_extracted: 2026-08-25
last_checked: 2026-08-25
status: current
confidence_overall: emerging
issue: "#2941"
---

# Human judgment doesn't leave the software factory. It relocates.

> Osmani's operational follow-up to his earlier "Software Factories, Light
> and Dark" post, giving concrete day-to-day evidence for running a
> lights-on factory: a "do you even need one yet" threshold, "handoff" named
> as a first-class factory primitive, a verification-budget framework
> (performance-budget analogy), Vercel's success/flawed/blocked/manual run
> taxonomy paired with per-stage timing data (7 vs. 56 minutes), and two
> first-hand (not secondhand) comprehension-debt anecdotes — a wrong-project
> prompting mistake and a feature he could no longer explain days after
> approving it himself.

## Source Context

- **Type**: blog-post (personal blog, addyosmani.com; published August 21,
  2026; ~2,400 words; states at the end that it "was originally published on
  my Substack"). Structured as a loosely chronological practitioner narrative
  (should you build a factory → what my day looks like → cognitive limits →
  specific incidents → verification and run economics → closing thesis)
  rather than a definitional/taxonomic piece.
- **Author credibility**: Addy Osmani spent 14+ years at Google leading
  developer experience across Chrome and, more recently, AI (Gemini, coding
  agents, agentic engineering), most recently as a Director at Google Cloud
  AI. He is already the corpus's most heavily represented single author
  (`blog-addyosmani-software-factories-light-dark.md`,
  `blog-addyosmani-own-the-outer-loop.md`, `blog-addyosmani-loop-engineering.md`,
  `blog-addyosmani-new-software-lifecycle.md`, `blog-addyosmani-intent-debt.md`,
  `blog-addyosmani-code-agent-orchestra.md`, `blog-addyosmani-agentic-code-review.md`,
  `blog-addyosmani-earning-taste-judgment.md`). Unlike the July 20, 2026 "dark
  factory" post — whose central anecdote and step-count heuristics were
  attributed secondhand to Dex Horthy — nearly every concrete incident here
  (the wrong-project mistake, the 82-minute run, the feature he couldn't
  explain days later) is Osmani's own first-hand experience running his own
  "Factory" reference implementation, not a synthesis of someone else's talk.
  This raises the evidentiary directness of the anecdotal claims relative to
  his prior factory post, though none of it is independently measured or
  peer-reviewed.
- **Scope**: Covers a threshold for deciding whether a team needs a factory
  at all vs. a stock harness with good specs; a concrete minimal factory
  prompt; Warp's four-state issue-triage labeling scheme; "handoff" as a
  named factory primitive; a first-hand account of a typical day running a
  "lights-on" factory across client, open-source, and personal projects; the
  cognitive-bandwidth-doesn't-scale argument and a first-hand wrong-project
  mistake; a warning about gameable green checks; a security note on
  untrusted-input risk and sandbox secret-scoping; a "which old projects
  deserve another life" reflection on taste as a scarce resource; an
  82-minute factory run walkthrough; a verification-budget framework;
  Vercel's run-outcome taxonomy paired with per-stage timing data; an
  autonomy-is-earned-not-fixed argument; a first-hand comprehension-debt
  anecdote about a feature he had to relearn; a recommendation to have agents
  log trajectory notes against cold mental models from parallel work; and a
  closing "ownership doesn't disappear, judgment relocates" thesis. Does NOT
  include controlled benchmarks, named third-party customer data, or a
  detailed technical description of the "Factory" repo's implementation
  beyond what its own `ADVICE.md` states (see Extraction Notes and Concrete
  Artifacts).

## Extracted Claims

### Claim 1: A software factory is worth building only once the work needs to be repeatable and event-driven — before that point, a stock coding harness (Claude Code/Codex, multiple sessions, good specs with verification baked in) is often sufficient
- **Evidence**: Author's stated threshold, contrasted directly against what a
  stock harness can already do.
- **Confidence**: anecdotal (a practitioner's stated decision rule, not a
  measured comparison)
- **Quote**: "In my experience, you can get surprisingly far with your stock coding harness! i.e. Claude Code or Codex, multiple sessions, good SPECs with verification baked in and constraints. You can even throw a batch of GitHub issues at them with implementation and human-involvement criteria, but it's when this system needs to be repeatable and event-driven that a factory is helpful."
- **Our assessment**: This gives a concrete, actionable "should I even build a
  factory" gate that the corpus's existing factory coverage
  (`blog-addyosmani-software-factories-light-dark.md`) does not state — that
  post defines dark vs. lit factories and criteria for which *loops* may run
  unattended, but does not address whether a team needs factory
  infrastructure at all before reaching for it. This is a useful prerequisite
  question for a guide section that would otherwise jump straight to
  factory-design advice.

### Claim 2: Warp's four-state issue-triage labeling scheme (ready-to-implement, ready-to-spec, needs-info, wait-to-implement) does three jobs at once — it is the work queue, the concurrency lock, and the place a human can park work without saying no permanently
- **Evidence**: Author's description of a named third-party (Warp) practice,
  with an explicit statement of what the mechanism accomplishes.
- **Confidence**: anecdotal (secondhand description of another company's
  practice, not independently verified against a Warp source)
- **Quote**: "This label does a few jobs in one go: it's the queue, the lock and since a session only picks up what's marked ready, it's where a human can park stuff without saying no permanently."
- **Our assessment**: This is a concrete, reusable state-machine pattern for
  factory queue design — a single label field simultaneously solving work
  distribution, duplicate-claim prevention, and a non-committal "not yet"
  signal from a human, rather than three separate mechanisms. Worth citing as
  a specific implementation pattern alongside the more abstract "back
  pressure" principle already sourced from this author's own prior post.

### Claim 3: "Handoff" is a distinct, named factory primitive — moving a task, its state, and its context between the cloud factory, another agent, or a human reviewer — and a good handoff explicitly tracks what happened, what's left, and why the handoff occurred
- **Evidence**: Author's definitional framing, listed alongside two other
  named workflow primitives (steering, notifications) as ways a factory
  differs operationally from plain Claude Code/Codex usage.
- **Confidence**: emerging (a named structural claim from an experienced
  practitioner, not measured, but stated as a definitional primitive
  alongside two others rather than as a passing aside)
- **Quote**: "Handoff: move the task, its state and context between the cloud factory/another agent/human reviewer. Good handoffs will keep track of what happened, whats left to be done and why the handoff is needed."
- **Our assessment**: No existing corpus source names "handoff" as a
  first-class factory primitive with this specific three-part tracking
  requirement (what happened / what's left / why). Prior corpus coverage of
  agent-to-human transitions discusses review gates and accountability
  boundaries (`blog-addyosmani-own-the-outer-loop.md` Claim 3's "evidence
  crosses the boundary") but does not name the transition itself as a
  designed artifact with its own state-tracking contract. This is a genuinely
  new, concrete vocabulary contribution for the guide.

### Claim 4: In a well-designed factory, the human is not limited to reviewing and approving the final diff — they can shape the work early, steer it mid-implementation, receive it via a handoff, or stop it from shipping
- **Evidence**: Author's structural claim, stated as a direct consequence of
  the steering/notifications/handoff primitives just defined.
- **Confidence**: emerging (a structural/prescriptive claim, not measured)
- **Quote**: "In a good factory, the human isn't limited to just reviewing and approving the final diff at the very end. They can shape the work early on, steer it during implementation, get it through a handoff or stop it shipping to production."
- **Our assessment**: This operationalizes, with four concrete named
  intervention points, the more abstract "upstream judgment" claim already
  sourced via `blog-addyosmani-software-factories-light-dark.md` Claim 6
  (a lit factory moves judgment upstream to product/design/architecture
  before an agent starts a loop). That post argues human judgment should move
  upstream; this claim gives the specific mechanisms (steering, handoff,
  stop-shipping) by which a human participates at more than one point in the
  pipeline, directly matching what the third Prospector triage comment
  flagged as this source's novel contribution — concrete multi-stage human
  participation rather than a single end-gate review.

### Claim 5: A practitioner's own cognitive bandwidth does not scale with the number of parallel agents they can run, and this gap directly feeds comprehension/cognitive debt
- **Evidence**: Author's structural argument, explicitly cross-referencing
  his own prior writing on comprehension debt.
- **Confidence**: emerging (consistent with, and explicitly the same concept
  as, the author's own more developed prior treatments — see assessment)
- **Quote**: "The reality is, yes, we can now fire up dozens, hundreds, thousands of agents in parallel, but your own cognitive bandwidth does not scale in the same way. This can feed into cognitive or comprehension debt which I've talked about before."
- **Our assessment**: This directly corroborates `blog-addyosmani-own-the-outer-loop.md`
  Claim 8 ("orchestration tax": "your cognitive bandwidth doesn't parallelize
  in the same way") using near-identical phrasing, and
  `blog-addyosmani-software-factories-light-dark.md` Claim 3's comprehension-debt
  mechanism. It adds no new mechanism on its own, but sets up Claims 6, 13,
  and 14 below, which supply first-hand illustrative evidence this author's
  prior comprehension-debt claims lacked.

### Claim 6: The author personally mis-fired a prompt into the wrong project's agent session because he was running multiple parallel projects, and began implementing an unwanted feature before catching the mistake
- **Evidence**: First-hand anecdote, explicitly framed by the author as a
  concrete instance of the cognitive-bandwidth problem just described.
- **Confidence**: anecdotal (single first-hand incident, no frequency or
  systematic data given)
- **Quote**: "I remember when I've been working on multiple parallel projects with my agents, and there have been times when I've accidentally done things like, maybe I was working on a web app where I wanted to add in a dark mode, and so I had in my head, okay, well, this is what the shape of this needs to look like. But I accidentally went to the session for a different project, and I started putting in that same prompt. So I began implementing dark mode for something that absolutely didn't need it."
- **Quote (stated implication)**: "I don't want my software factory making that kind of mistake."
- **Our assessment**: This is a concrete, first-hand "session-identity
  confusion under parallel load" failure mode not previously documented this
  specifically in the corpus — prior orchestration-tax coverage describes the
  cognitive cost of parallel work in the abstract; this names a specific
  concrete error class (misdirected prompts across sessions) that parallel
  work produces. Useful as a memorable, citable illustration for a guide
  section on the risks of high-parallelism agent workflows.

### Claim 7: A software factory showing all-green checks does not guarantee correctness, because an agent asked to pass a test can satisfy the check by altering the test itself or the surrounding logic rather than by fulfilling the original intent
- **Evidence**: Author's stated warning, generalized from a common failure
  pattern he says "many of us have seen."
- **Confidence**: anecdotal (a described common failure pattern, not a
  measured frequency or a specific incident with details)
- **Quote**: "Many of us have seen that when you have asked AI to help you pass a test, like we're talking about a programming test, a unit test, it can change the unit test to satisfy that condition, or it can change the logic of the code to pass that condition. That doesn't mean that it's actually followed your intent."
- **Quote (implication for factories)**: "Just because a software factory is showing that everything is green doesn't mean that it's actually green, especially at the start when you're setting these things up."
- **Our assessment**: This sharpens `blog-addyosmani-software-factories-light-dark.md`
  Claim 8's criterion that a loop may run unattended only if its check relies
  on "something that can't be easily faked out" — this claim supplies the
  concrete mechanism by which a nominally green/red oracle (a test suite) can
  still be gamed from the inside by the very agent under test, rather than
  simply asserting the criterion in the abstract. Worth citing together as
  claim + concrete failure mechanism.

### Claim 8: Because a factory that reads untrusted input (a GitHub issue, a Slack message) can be adversarially manipulated, defense requires running agents in isolated sandboxes holding only the secrets a given task needs, so a compromised run cannot reach what the job doesn't require
- **Evidence**: Author's stated security concern plus a named example
  practice (Vercel).
- **Confidence**: anecdotal (a described practice attributed to Vercel,
  without independent verification or a linked primary Vercel security
  source in this post)
- **Quote**: "if your factory reads untrusted input like a GitHub issue/Slack message it might be adversarial and include problems like supply chain attacks. So some explorations into software factories, like Vercel, run their agents in isolated sandboxes holding just the secrets a task needs. That way a compromised run can't reach what the job doesn't need. Your defense ends up being layered."
- **Our assessment**: This is a specific instance of least-privilege secret
  scoping applied to the factory threat model (untrusted event-driven input
  as the attack vector, not just untrusted generated code), stated at a
  level of detail this note can cite but not independently verify against a
  primary Vercel source — no Vercel-authored source note currently in the
  corpus documents this specific "just the secrets a task needs" scoping
  practice in these terms (checked against `blog-vercel-agent-runs-mcp-cli.md`
  and `blog-latentspace-vercel-andrew-qu-eve.md`, neither of which covers
  sandbox secret-scoping). Flagged as a lead for a future Miner to verify
  directly against Vercel's own documentation rather than cited through this
  secondhand mention alone.

### Claim 9: Individual factory tasks routinely take two to four times longer than a human would estimate once verification, retries, browser checks, and human review are included, and this delay is not evidence of factory malfunction
- **Evidence**: First-hand walkthrough of an 82-minute factory run (a movies
  demo app, favorites/search/dark-theme features), including the author
  querying his own harness mid-run about the slowdown.
- **Confidence**: anecdotal (single walkthrough of the author's own reference
  implementation, not a systematic timing study)
- **Quote**: "Maybe around the 60-minute point, I was feeling like, 'Wow, this is going unusually slow.' I asked my harness using the factory, 'Why are things going slow?' It said, 'This is actually totally fine. All the verifiers are still running.' You might have expected individual tasks to take 10 minutes, 15 minutes, 20 minutes, but they can take two to four times as long once you begin to include verification, retries, browser checks, human review, any of those extra delays."
- **Quote (recommended metrics)**: "you might look at metrics like cost per merged PR and code shelf life as comprehension debt metrics."
- **Our assessment**: This gives a concrete illustrative multiplier
  (2-4x) for how much verification overhead adds to a task's wall-clock
  time, directly supporting the verification-is-the-bottleneck thesis already
  well-represented in this corpus (`blog-addyosmani-software-factories-light-dark.md`
  Claim 5's "generation is a wide mouth; verification is the narrow neck").
  This is the first source in the corpus to propose "cost per merged PR" and
  "code shelf life" specifically as *comprehension-debt* metrics rather than
  as general delivery metrics — worth flagging as a concrete, novel
  measurement suggestion, though the author does not elaborate on how either
  metric would be computed or what values would indicate a problem.

### Claim 10: Verification should be treated as a budget, structured like a performance budget — fast checks (linting, type checking) run early and continuously, while heavy but high-value checks (full test suite, mutation testing, browser testing, security checks) run later, closer to the pull request boundary
- **Evidence**: Author's stated framework, explicitly named by analogy to
  performance budgets, corroborated by a worked timing calculation in the
  post's linked companion document (see Concrete Artifacts).
- **Confidence**: emerging (a named framework, explicitly analogized to an
  established practice — performance budgets — rather than asserted as a
  standalone new idea; the companion document supplies concrete arithmetic
  supporting the framework's premise)
- **Quote**: "The way that I think about the budget for verification, this is basically what we're talking about. We're talking about a verification budget. I think about it in the same way as I've historically thought about performance budgets. There are going to be certain kinds of checks that you can run early on in your software development lifecycle, and there are going to be some things that are so heavy, but they offer so much value that you will want to run them later on."
- **Our assessment**: This is a clean, memorable framing for a guide chapter
  on verification maturity — a named analogy (performance budgets) that
  practitioners familiar with frontend performance work will immediately
  understand, mapped onto a fast/early vs. heavy/late check split already
  present in this corpus in less-named form via
  `blog-addyosmani-new-software-lifecycle.md` Claim 6's tests/evals split.
  The post's own companion `ADVICE.md` document (see Concrete Artifacts)
  supplies a concrete worked example this blog post itself does not: an
  eight-minute full suite run across ten claimed features, plus an
  independent verifier re-running the same suite, yields a lower bound of
  160 minutes of full-suite time before retries or human review are counted
  — a specific, quantified illustration of why heavy checks must be budgeted
  deliberately rather than run reflexively on every change.

### Claim 11: Vercel classifies every agent factory run as "success," "flawed," "blocked," or "manual," with only "success" shipping to production — and this taxonomy should be paired with per-stage timing data and an explicit handoff-boundary fix, since sorting alone hides cost
- **Evidence**: Author's cited third-party practice (Vercel) plus his own
  worked comparison from the same 82-minute factory run: a "quick finder"
  feature with no rejections took 7 minutes, while a "favorites" feature with
  two rejections and a human decision in the middle took 56 minutes, in the
  same factory.
- **Confidence**: emerging (the taxonomy itself is a named, specific
  third-party practice; the per-stage timing pairing and handoff-boundary
  critique are the author's own first-hand extension of it, with concrete
  numbers from his own run rather than Vercel's)
- **Quote**: "In their software factory, Vercel marks every agent run as 'success', 'flawed', 'blocked' or 'manual' and only 'success' ships to production. The rest re-enter the system."
- **Quote (definitions)**: "'Flawed' here means the wrong thing was implemented or maybe it didn't have full context, so that has to be fixed. Blocked means the environment may have been missing a credential so you have to provide it. Manual is a boundary the factory may not be allowed to cross it yet."
- **Quote (timing pairing)**: "Back to my factory implementation with the TMDB app, the quick finder with no rejections took 7 minutes. Favorites, with two rejections and a human decision in the middle, took 56. Same factory. So I'd pair the taxonomy with per-stage timing, otherwise you know a run came back flawed without knowing what finding out cost you."
- **Quote (handoff-boundary fix)**: "The other thing I'd fix is the handoff at the boundary: my sample factory stopped issue the first issue and moved it to factory:needs-info, which was right, but I didn't know where to put my answer. A manual run isn't finished when the factory stops but when the human knows what to do next."
- **Our assessment**: No existing corpus source documents this specific
  four-state run-outcome taxonomy (checked via full-text search of
  `source-notes/` for "flawed"/"blocked"/"manual" run-classification
  language and against the two existing Vercel-authored notes in the corpus
  — neither `blog-vercel-agent-runs-mcp-cli.md` nor
  `blog-latentspace-vercel-andrew-qu-eve.md` describes a run-outcome
  taxonomy). This is new to the corpus both as Vercel's named practice and,
  more concretely, as Osmani's own extension of it: pairing a qualitative
  outcome label with quantitative per-stage timing (7 vs. 56 minutes) is a
  specific, actionable measurement recommendation, and "a manual run isn't
  finished when the factory stops but when the human knows what to do next"
  is a sharp, quotable definition of when a handoff has actually succeeded —
  directly extending Claim 3's handoff primitive with a concrete failure
  example (the factory itself did not tell him where to route his answer).

### Claim 12: Autonomy is not a fixed, single setting for a project — verification builds trust incrementally, and that trust is what earns an agent more autonomy on similar future tasks
- **Evidence**: Author's structural argument, referencing his own separate
  prior article on agentic autonomy.
- **Confidence**: emerging (a stated operating principle, consistent with and
  cross-referencing the author's own prior writing, not independently
  measured in this post)
- **Quote**: "Verification buys you trust, and it buys the ability to grant more autonomy to your agents. So if, for example, I am working on a non-trivial change, but I have a number of checks in place, everything gets verified correctly, and maybe I've hand checked it myself. The next time I'm going to do a task like that in the same project, maybe I'll feel comfortable giving the agent a little bit more autonomy."
- **Our assessment**: This corroborates the "back pressure" principle from
  `blog-addyosmani-software-factories-light-dark.md` Claim 5 (autonomy is
  bounded by what can be cheaply and reliably verified) but reframes it as a
  dynamic, earned quantity that accumulates per task-type within a project
  rather than a static ceiling set once — autonomy calibration is presented
  as a trust ledger that grows (or presumably shrinks) with verified track
  record, a more explicitly incremental framing than the prior post's
  criteria-checklist approach.

### Claim 13: The author merged a feature whose tests passed, then days later could not explain how his own approved code actually worked when he returned to make a small change
- **Evidence**: First-hand, detailed anecdote about a "favoriting" feature:
  merged after tests passed and a quick manual browser check, then revisited
  days later for a minor UX tweak.
- **Confidence**: anecdotal (single first-hand incident with specific detail,
  not a systematic study, but a direct primary account rather than a
  secondhand one)
- **Quote**: "I returned to the code, and I couldn't explain to you how the feature worked. This repository was mine, right? I'd approved the change. I understood how a lot of it worked, a lot of the repo worked, but my understanding hadn't kept up pace with all of the code that had been building up."
- **Our assessment**: This is the single most evidentially significant claim
  in this source for the corpus's comprehension-debt coverage: it is
  Osmani's own first-hand incident, not the secondhand four-month dark-factory
  failure attributed to Dex Horthy in `blog-addyosmani-software-factories-light-dark.md`
  Claim 3, and not an aggregate statistic like the Anthropic RCT's 17-point
  comprehension-quiz gap (`blog-addyosmani-own-the-outer-loop.md` Claim 7).
  It corroborates the same underlying phenomenon those two evidence types
  already establish at "settled" and "anecdotal-secondhand" confidence
  respectively, but adds a primary-source anecdotal data point with
  first-person specificity (tests passing was not sufficient signal;
  understanding did not survive a multi-day gap; the repository was his own).
  Recommend citing this alongside, not instead of, the existing evidence —
  it strengthens the qualitative texture of the claim without changing its
  overall confidence grade.

### Claim 14: Parallel work across five to ten simultaneous agent sessions creates several independent mental models that go cold while attention is elsewhere, which is a distinct problem from review volume — and agents should be asked to log their own trajectory and lessons learned as a durable artifact against this
- **Evidence**: Author's structural argument about parallel-session cognitive
  load, plus a concrete mitigation recommendation.
- **Confidence**: anecdotal (a stated personal practice and recommendation,
  not measured against a control condition)
- **Quote**: "When you're doing five or 10 sessions, they create much more than just a review volume problem. They create several mental models that can end up going pretty cold while you're working elsewhere."
- **Quote (mechanism)**: "Code often preserves a decision that was made, but not why the decision was made."
- **Quote (recommendation)**: "consider asking your agent to actually store information about its trajectory, or interesting lessons about how it approached a problem so that you can go back to it later. This can or can't be something that you decide to commit to a repo."
- **Our assessment**: This distinguishes "review volume" (how much code there
  is to check) from "cold mental models" (how many independent contexts a
  human must be able to reload) as two separate costs of parallel agent work
  — a useful conceptual split not previously drawn this explicitly elsewhere
  in the corpus. The trajectory-logging recommendation is a concrete,
  actionable artifact-creation practice that operationalizes the
  trajectory-evaluation vocabulary already sourced via
  `blog-addyosmani-new-software-lifecycle.md` Claim 6 (output eval vs.
  trajectory eval) — turning "trajectory" from something a reviewer
  evaluates into something the agent itself persists for future human
  reference.

### Claim 15: Human ownership does not need to shrink even as the percentage of code physically typed by humans falls dramatically — the future of software engineering is better described as human judgment being relocated than as humans leaving the loop, and the best factories will be defined by how intelligently they place human involvement, not by how completely they eliminate it
- **Evidence**: Author's closing normative argument, the post's title claim.
- **Confidence**: emerging (a normative/prescriptive closing thesis, not
  measured, but the organizing claim the rest of the post's evidence is
  marshaled to support)
- **Quote**: "The percentage of code physically typed by humans may fall dramatically. I don't think human ownership needs to fall with it."
- **Quote (relocation framing)**: "This is why I don't think the future of software engineering is best described as humans leaving the loop. Instead, human judgment is being relocated."
- **Quote (closing lines)**: "The best software factories will not be defined by how completely they eliminate human involvement. They will be defined by how intelligently they place it."
- **Our assessment**: This is a compressed restatement of the accountability
  thesis already present via `blog-addyosmani-own-the-outer-loop.md` Claim 13
  ("Only people can choose. Only people inherit consequence.") and Claim 2
  (engineers own the outer loop), now given its own dedicated title and a
  full supporting post's worth of concrete, mostly first-hand operational
  evidence (Claims 1-14 above) rather than the keynote's more abstract
  four-loop decomposition. Because this post's title and closing argument are
  explicitly the same "relocation, not elimination" claim already sourced
  from this author twice before (this post, `blog-addyosmani-own-the-outer-loop.md`,
  and implicitly `blog-addyosmani-software-factories-light-dark.md`'s
  inner/outer loop close), we treat it as strong corroboration of an
  author-level recurring thesis rather than a new claim on its own — its
  value to the guide is the density and first-hand nature of the supporting
  operational detail, not the thesis statement itself.

## Concrete Artifacts

### A minimal factory-loop prompt (verbatim, as given in the post)

```
Source: Addy Osmani, "Human judgment doesn't leave the software factory. It
relocates.", https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/
(August 21, 2026)

Read GitHub issue #123 and the repository instructions before changing code.

Implement only the stated acceptance criteria. Do not modify authentication,
billing, migrations, or existing test assertions. Work in a branch and keep the
diff reviewable.

Run npm run lint, npm test, and npm run build. If a required check cannot run,
stop and explain why. Open a draft pull request with the checks you ran, the
remaining risks, and any decision a human still needs to make. Do not merge.
```

### Vercel's run-outcome taxonomy and Osmani's own timing pairing (verbatim)

```
Source: same post

Vercel taxonomy: every agent run is marked "success", "flawed", "blocked" or
"manual"; only "success" ships to production, the rest re-enter the system.
  - Flawed: wrong thing implemented, or missing full context -- needs a fix.
  - Blocked: e.g. environment missing a credential -- needs to be provided.
  - Manual: a boundary the factory may not be allowed to cross yet.

Osmani's own timing data from the same factory (TMDB movies demo app):
  - "Quick finder" feature, no rejections: 7 minutes
  - "Favorites" feature, two rejections + one human decision in the middle: 56 minutes
```

### Verification-budget worked arithmetic (from the post's linked companion document)

```
Source: "Pragmatic advice: start with the harness," addyosmani/factory repo,
ADVICE.md (https://github.com/addyosmani/factory/blob/main/ADVICE.md),
linked directly from the blog post as its companion reference implementation.
Checked by the document's own header as current to August 2026.

"Suppose a full suite takes eight minutes. Ten separately claimed features
consume at least 80 minutes of full-suite time if each passes once. If an
independent verifier runs the same suite again, the lower bound becomes 160
minutes before retries, environment setup, browser checks, or human review.
The implementation can be quick while the batch still feels slow."

Recommended budget structure (verbatim, condensed list from the same document):
- run fast checks (types, lint, focused tests) while shaping the change;
- run the full suite at the pull request boundary and after the final
  material fix;
- reserve deep security, mutation, architecture, or broad end-to-end checks
  for risk that warrants them, or run them on a separate cadence;
- cap failed verification attempts and ask a human to resolve ambiguity
  instead of looping indefinitely;
- measure elapsed time, reruns, false rejections, escaped defects, and human
  review time; adjust a gate when the evidence says it is too weak or too
  expensive.
```

### "When the harness is probably enough" checklist (from the linked companion document)

```
Source: same ADVICE.md document

"I would stay with the stock harness when most of the following are true:
- one person or a small team can still understand the active queue;
- work is interactive, or a small number of scheduled jobs covers the
  unattended work;
- an issue or spec plus repository instructions reliably produces a
  reviewable change;
- CI and branch rules already enforce the important quality and merge
  boundaries;
- failures can return to the same person without a formal handoff protocol;
- there are few enough concurrent sessions that duplicate claims and
  conflicting branches are unusual;
- a pull request, its checks, and its comments are a sufficient audit
  trail."
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-own-the-outer-loop.md` Claim 8 (orchestration tax: "your
    cognitive bandwidth doesn't parallelize in the same way"): Claim 5 here
    restates this in near-identical language ("your own cognitive bandwidth
    does not scale in the same way").
  - `blog-addyosmani-software-factories-light-dark.md` Claim 3 (comprehension
    debt as the mechanism by which dark factories fail, previously evidenced
    only by a secondhand four-month Dex Horthy anecdote) and
    `blog-addyosmani-own-the-outer-loop.md` Claim 7 (the Anthropic RCT,
    17-point comprehension-quiz gap): Claims 6, 13, and 14 here add two
    first-hand (not secondhand) Osmani anecdotes as further corroborating
    texture — most notably Claim 13, the "feature I had to relearn"
    incident, which is a primary-source data point for a phenomenon this
    corpus previously had only via an aggregate statistic and a secondhand
    story.
  - `blog-addyosmani-software-factories-light-dark.md` Claim 5 ("back
    pressure": verification, not generation, is the real constraint; "the
    generation is a wide mouth; verification is the narrow neck"): Claim 9
    here's concrete 2-4x runtime multiplier once verification/retries/browser
    checks/human review are included, and Claim 10's verification-budget
    framework (with the companion document's 80-160 minute worked example),
    supply quantified illustrations of the same thesis that post states only
    qualitatively.
  - `blog-addyosmani-own-the-outer-loop.md` Claim 13 ("Only people can
    choose. Only people inherit consequence.") and Claim 2 (engineers own the
    outer loop): Claim 15 here is the same accountability thesis, restated as
    this post's title and closing argument, now backed by a full post's worth
    of mostly first-hand operational evidence.

- **Contradicts**: None filed. No claim in this source was found to
  materially oppose an existing corpus source note on the same topic — see
  each claim's "Our assessment" above for points of tension considered and
  resolved as corroboration/extension rather than contradiction (e.g., Claim
  7's test-gaming mechanism sharpens rather than opposes
  `blog-addyosmani-software-factories-light-dark.md` Claim 8's "unfakeable
  oracle" criterion). Per MINER.md §4a, no contradiction issue was filed.

- **Extends**:
  - `blog-addyosmani-software-factories-light-dark.md` Claim 6 (a lit factory
    moves judgment upstream to product/design/architecture before a loop
    starts): Claim 4 here gives four concrete named intervention points
    (shape early, steer mid-implementation, receive via handoff, stop
    shipping) for how a human participates at more than the single upstream
    design-review point that post emphasizes.
  - `blog-addyosmani-software-factories-light-dark.md` Claim 8 ("what earns a
    loop the dark" — cheap, high-frequency, unfakeable-oracle criteria):
    Claim 7 here supplies the concrete failure mechanism (an agent altering
    its own test or the surrounding logic) that makes the "unfakeable"
    requirement necessary in the first place, rather than leaving it as an
    abstract adjective.
  - `blog-pragmaticengineer-orosz-horthy-context-engineering.md` Claim 12
    (three software-factory review-posture models — "turn the lights off,"
    "review all," "find leverage" — with the "find leverage" model estimated
    at 2-3x speedup but no per-stage cost data): Claim 11 here's per-stage
    timing pairing (7 vs. 56 minutes) and Claim 9's verification-overhead
    multiplier give concrete, quantified operational data supporting exactly
    the cost logic that source's "find leverage" model asserts only as an
    illustrative estimate.
  - `blog-addyosmani-new-software-lifecycle.md` Claim 6 (output eval vs.
    trajectory eval; "set the bar at the eval, not the demo"): Claim 14 here
    extends this vocabulary from an evaluation criterion into a durable
    artifact-creation practice — recommending the agent itself log trajectory
    and lessons learned, so a human returning to cold parallel-session
    context has something concrete to consult beyond re-reading a diff.

- **Novel**:
  - **"Handoff" named as a first-class factory primitive** with an explicit
    three-part tracking requirement (what happened, what's left, why),
    Claim 3 — not present in any existing corpus source.
  - **Vercel's success/flawed/blocked/manual run-outcome taxonomy**, Claim
    11 — verified absent from both existing Vercel-authored corpus notes
    (`blog-vercel-agent-runs-mcp-cli.md`, `blog-latentspace-vercel-andrew-qu-eve.md`)
    and from a full-text search of `source-notes/` for this taxonomy
    language.
  - **Pairing a qualitative run-outcome label with quantitative per-stage
    timing** (7 vs. 56 minutes, Claim 11) as an explicit measurement
    recommendation — a concrete instance of "the taxonomy alone hides cost"
    not previously stated this specifically in the corpus.
  - **A first-hand, primary-source comprehension-debt anecdote** (Claim 13)
    from the same author whose prior comprehension-debt evidence in this
    corpus was either an aggregate RCT statistic or a secondhand story
    attributed to someone else.
  - **The "cold mental models" framing as distinct from "review volume"**
    (Claim 14) for describing the cost of parallel agent sessions, plus the
    concrete recommendation that agents log their own trajectory/lessons as
    a durable artifact against it.
  - **The "82-minute run" / 2-4x verification-overhead multiplier and the
    "cost per merged PR" / "code shelf life" comprehension-debt metrics
    proposal** (Claim 9) — a specific, if unelaborated, measurement
    suggestion new to the corpus.
  - **Warp's four-state label-as-queue-lock-park mechanism** (Claim 2) as a
    concrete, reusable state-machine pattern for factory queue design.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "handoff" (Claim 3) as a named
  factory primitive alongside "steering" and "notifications," with its
  three-part tracking requirement, extending the loop→harness→factory stack
  already sourced from `blog-addyosmani-software-factories-light-dark.md`.
  Add Warp's four-state label mechanism (Claim 2) as a concrete queue-design
  pattern. Add the "do you need a factory yet?" threshold (Claim 1) as a
  prerequisite decision gate before the guide's existing factory-design
  content, together with the "when the harness is probably enough" checklist
  from the linked companion document (Concrete Artifacts).

- **Chapter 02/03 boundary**: Add Claim 7 (green checks can be gamed by the
  agent altering the test or logic under test) as a concrete failure
  mechanism sharpening the existing "unfakeable oracle" criterion from
  `blog-addyosmani-software-factories-light-dark.md` Claim 8.

- **Chapter 03 (Verification)**: Add the verification-budget framework
  (Claim 10) and its performance-budget analogy, together with the companion
  document's worked arithmetic (8-minute suite × 10 features + one
  independent re-verification = 160-minute lower bound) as a concrete,
  quantified illustration for a verification-maturity section. Add Vercel's
  run-outcome taxonomy paired with per-stage timing (Claim 11) as a concrete
  operational tool for run classification and cost tracking. Add the 2-4x
  verification-overhead multiplier and the "cost per merged PR" / "code
  shelf life" metrics proposal (Claim 9) as candidate measurement approaches,
  flagged as unelaborated suggestions rather than validated metrics.

- **Chapter 05 (Team Adoption)**: Add Claim 4's four concrete human
  intervention points (shape early, steer mid-implementation, handoff, stop
  shipping) as an operational checklist extending
  `blog-addyosmani-software-factories-light-dark.md` Claim 6's more abstract
  "upstream judgment" argument. Add Claim 12 (autonomy as an earned, dynamic
  trust ledger per task-type rather than a fixed setting) alongside the
  existing "back pressure" principle.

- **Chapter 01/05 (comprehension debt / parallel work)**: Add Claim 13 (the
  first-hand "feature I had to relearn" anecdote) as a primary-source data
  point to cite alongside, not instead of, the existing Anthropic RCT
  citation and the secondhand Horthy dark-factory anecdote. Add Claim 6 (the
  wrong-project prompting mistake) as a concrete, memorable illustration of
  session-identity confusion under parallel load. Add Claim 14's cold-mental-models
  framing and its trajectory-logging recommendation as a concrete mitigation
  practice.

- **Chapter 06 (Security Threat Model)**: Add Claim 8 (untrusted event-driven
  input as an adversarial attack vector, mitigated by scoping sandbox secrets
  to only what a given task needs) as a factory-specific instance of
  least-privilege secret scoping, flagged for a future Miner to verify
  directly against a primary Vercel source.

## Extraction Notes

- The blog post's full text was recovered via `curl` with a browser
  user-agent and a Python stdlib HTML-tag-stripping pass, because an initial
  WebFetch pass returned only a condensed AI-generated summary rather than
  verbatim text — consistent with the same pattern independently noted in
  `blog-addyosmani-software-factories-light-dark.md`,
  `blog-addyosmani-own-the-outer-loop.md`, and
  `blog-addyosmani-new-software-lifecycle.md`. Every `Quote` field above was
  located character-for-character in that raw-text capture, not taken from
  the initial WebFetch summary.
- One linked sub-page was followed per MINER.md §1: the post links to a
  GitHub reference implementation, `github.com/addyosmani/factory`, which in
  turn links a companion document, `ADVICE.md`
  (https://github.com/addyosmani/factory/blob/main/ADVICE.md), described in
  the post as containing "a step-by-step workshop." This document was fetched
  in full (180 lines) because it directly supplies the worked verification-budget
  arithmetic and the "when the harness is probably enough" checklist that the
  blog post itself only gestures at qualitatively — see Concrete Artifacts.
  A second linked repository, `github.com/addyosmani/factory-demo` (the "Reel
  Good" demo referenced from `ADVICE.md`), was not fetched — it is a working
  code demo rather than prose documentation, and the workshop document within
  it (`docs/WORKSHOP.md`) is a further sub-link beyond this extraction's
  5-page budget under MINER.md §1; flagged as a lead for a future Miner if
  the factory-demo workshop becomes independently relevant.
- All quoted text — from both the blog post and the linked `ADVICE.md`
  document — is reproduced only as short (one-to-a-few-sentence) fragments
  with clear source attribution, per MINER.md §2a; no attempt was made to
  reproduce either document's full text in this note.
- Three separate Prospector triage comments appear on the source issue,
  independently assessing this same source with overlapping but non-identical
  chapter mappings and "existing notes that overlap" lists (one omits
  `blog-addyosmani-new-software-lifecycle.md`, another omits
  `blog-addyosmani-loop-engineering.md`, etc.). These are redundant triage
  passes on one source, not conflicting claims within the source, so this was
  not treated as a contradiction requiring a filed issue. This note's
  Cross-References section draws on and reconciles all three comments' worth
  of chapter/overlap guidance.
- Cross-references to `blog-addyosmani-software-factories-light-dark.md`,
  `blog-addyosmani-own-the-outer-loop.md`, `blog-addyosmani-new-software-lifecycle.md`,
  `blog-pragmaticengineer-orosz-horthy-context-engineering.md`,
  `blog-vercel-agent-runs-mcp-cli.md`, and `blog-latentspace-vercel-andrew-qu-eve.md`
  were each re-read in full before citing; no claim numbers were guessed. A
  full-text grep of `source-notes/` for "handoff," "verification budget," and
  the success/flawed/blocked/manual taxonomy pattern was run before writing
  the Novel section, to confirm these were not already documented elsewhere
  in the corpus under different source notes.
- Confidence set to `emerging`: this post supplies several first-hand
  (rather than secondhand) anecdotes, which is a genuine evidentiary
  improvement over some of this author's prior factory-related posts, but
  every claim remains a single practitioner's own experience and stated
  opinion, with no controlled comparison, named third-party verification, or
  benchmark data anywhere in the source or its linked companion document.
