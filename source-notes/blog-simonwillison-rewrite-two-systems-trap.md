---
source_url: https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/
source_type: blog-post
title: "Comment: There's No Limit to How Bad Code Can Get"
author: Simon Willison
date_published: 2026-09-06
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: anecdotal
issue: "#3346"
---

# Comment: There's No Limit to How Bad Code Can Get

> Simon Willison's own Lobste.rs comment, republished to his blog, names a
> five-step socio-technical failure sequence for "burn it down and rewrite"
> efforts — moving-target old system, developer disincentive, an
> understanding gap on the new team, a partial ship-pressure launch, and a
> resulting "two systems in production" trap that risks silent abandonment —
> and recommends automated testing plus targeted refactors instead. The post
> makes no mention of AI or coding agents anywhere, which sits in direct
> tension with Willison's own July 8, 2026 post on the Bun rewrite, where he
> argued frontier coding agents "change that equation" for full rewrites —
> see the filed contradiction, issue #3370.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a "Comment" post type — the
  site's format for republishing a comment Willison posted elsewhere,
  cross-linked back to the original). Very short: eight paragraphs, ~350
  words, posted 6 September 2026 at 9:08am. This is Willison's own
  first-person comment, not a quotation of someone else's writing — the "My
  comment" link on the page points to his own reply on the Lobste.rs thread
  `lobste.rs/s/rfn2mn/there_s_no_limit_how_bad_code_can_get#c_8kdtaw`, itself
  a discussion of an external article, "There's No Limit to How Bad Code Can
  Get" (zachkehs.com), which this note does not separately mine (the assigned
  source is Willison's comment specifically, per the Prospector's second
  triage comment).
- **Author credibility**: Simon Willison is a high-signal, frequently-cited
  commentator already extensively corroborated in this corpus (creator of
  Django, maintainer of Datasette/`sqlite-utils`/`llm`; see author-credibility
  discussion in `blog-simonwillison-not-locked-in.md` and dozens of other
  corpus notes). This specific post, however, is a first-person practitioner
  opinion/anecdote about general software engineering dynamics — it cites no
  data, no named incident, and no external authority beyond a pointer to Will
  Larson's "Migrations" article (not quoted). Treat as one experienced
  practitioner's stated hunch, not as measured or corroborated evidence.
- **Scope**: Covers the failure dynamics of "burn it down and start from
  scratch" rewrites of an existing production system, and Willison's stated
  preferred alternative (test-harden + targeted refactor). Does **not**
  mention AI, LLMs, coding agents, or any agentic tooling anywhere in the
  post — despite Willison discussing large-scale code rewrites extensively
  elsewhere in the corpus in explicitly AI-framed terms (see Cross-References
  → Contradicts). Does not cite data, a named company, or a specific incident
  — it is framed entirely as "in my experience" and "my hunch." Does not
  quote or engage with Will Larson's cited article beyond naming it as "the
  best article" on the topic.
- **Thread context** (read per MINER.md §1, "follow substantive linked
  pages"): Willison's comment was posted in direct reply to a Lobste.rs user,
  `gunduzc`, who wrote: "Perhaps I'm just a naive youngster, but I feel like
  sometimes it's necessary to burn it all to the ground and start from
  scratch." The broader thread (which this note does not mine as a separate
  source) contains open disagreement with Willison's position: user
  `greysonp` replied, "I feel like this is a common belief, that rewrites
  hardly ever work, but I think it's just because we're biased towards
  remembering the ones that fail really horribly. I think people rewrite
  systems successfully *all* the time. I've certainly done it plenty of
  times." This is useful context for confidence calibration: Willison's
  position is a stated opinion in an active, contested discussion, not an
  uncontroversial industry consensus — the guide should not cite it as
  settled.

## Extracted Claims

### Claim 1: In Willison's experience, "burn it down and rewrite from scratch" efforts to replace a system drowning in technical debt are rare to succeed
- **Evidence**: Willison's own stated experience, as the opening framing of the entire comment.
- **Confidence**: anecdotal
- **Quote**: "In my experience it's *so rare* for that to work."
- **Our assessment**: This is a first-person practitioner claim with no named incident, data, or citation — it is exactly the kind of confident generalization the guide should attribute clearly to one commentator's experience rather than present as settled. It is also the specific claim directly in tension with Willison's own framing of the Bun rewrite two months earlier (see Cross-References → Contradicts).

### Claim 2: The old system remains a "moving target" throughout a rewrite because it is still running the core business, forcing continued changes to it
- **Evidence**: Willison's structural description of the first failure mechanism.
- **Confidence**: anecdotal
- **Quote**: "Meanwhile the old thing remains a moving target: it's running the core business, so changes are still necessary."
- **Our assessment**: This is a specific, plausible mechanism (not just "rewrites are hard") — the old system cannot be frozen as a stable target because business requirements keep landing on it. This is the first link in a five-step causal chain (Claims 2-6) rather than an isolated observation.

### Claim 3: Developers who remain on the old system, knowing it is slated for replacement, lose incentive to do more than the smallest effort needed to ship new features, so technical debt continues to accumulate on the system being replaced
- **Evidence**: Willison's structural description of the second mechanism, a developer-incentive argument.
- **Confidence**: anecdotal
- **Quote**: "The developers working on it know that it's going to be made obsolete by the new thing soon, so they don't have any incentive to go beyond the smallest effort possible to add the new features. Technical debt continues to mount."
- **Our assessment**: This names a specific perverse-incentive mechanism: announcing a replacement is imminent actively degrades the thing being replaced, working against the moving-target problem in Claim 2 (the old system needs more changes, but gets lower-effort ones). This compounding-in-the-wrong-direction dynamic is a useful, citable specific for a guide discussion of rewrite risk, distinct from a generic "rewrites are risky" warning.

### Claim 4: The team building the replacement starts fast but is "probably a little naive," and over time discovers nobody fully understands the behavior and scope of the system they are replacing — because if it had been well documented and tested, it wouldn't have needed replacing in the first place
- **Evidence**: Willison's structural description of the third mechanism, including a self-referential aside.
- **Confidence**: anecdotal
- **Quote**: "Meanwhile, the team working on the new thing are ambitious and probably a little naive. They start out at a great pace - it's greenfield after all - but as time progresses it becomes apparent that nobody fully understands the behavior and scope of the thing they are replacing. If it was well documented and tested it wouldn't *need* to be replaced, after all..."
- **Our assessment**: The closing aside is the sharpest point in the post: it identifies a structural irony — the systems most in need of rewriting are, by that same logic, the ones with the least reliable understanding available to guide a rewrite. This directly echoes the corpus's existing "intent debt"/"comprehension debt" framing (see Cross-References → Corroborates) applied specifically to the rewrite-decision moment rather than to day-to-day agentic work.

### Claim 5: Pressure to "ship it" after months or years without delivering value causes the new system to launch handling only a subset of the old system's scope, or a new feature that was hard to build on the increasingly unmaintained old system
- **Evidence**: Willison's structural description of the fourth mechanism.
- **Confidence**: anecdotal
- **Quote**: "After months (or even years) without delivering value, the pressure is on to \"ship it\", so the new system is launched to handle a subset of what the old system handled - or often for some new feature that was too hard to build with the now mostly unmaintained old system."
- **Our assessment**: This is the pivot point of the causal chain — the moment a "rewrite" project quietly becomes a "partial system" project under delivery pressure, which sets up Claim 6's two-systems outcome. It is a specific, recognizable failure mode (ship a subset to show progress) rather than a vague "projects run late" observation.

### Claim 6: The predictable outcome is two systems simultaneously in production — the old, unmaintained system nobody wants to touch, and a new system handling only a few production features while being roughly 80% inactive code
- **Evidence**: Willison's naming of the resulting end state, with a specific proportion estimate.
- **Confidence**: anecdotal
- **Quote**: "... so now you have TWO systems in production - the janky old system that nobody wants to touch, and a new system which handles just a few production features and is 80% inactive code that is meant to replace the old system, eventually."
- **Our assessment**: The "80% inactive code" figure is stated as an illustrative estimate, not a measured statistic from any named project — treat it as color, not data. The naming of the end state itself ("two systems in production") is the most citable, memorable artifact in this source and is a useful diagnostic label for a guide callout: if a migration project reaches a state where both the old and new systems are simultaneously live and neither is fully retired, that is the specific failure state this source describes, not a transitional phase to be patient with.

### Claim 7: Even in the best case where a company doesn't lose patience, the longer the two-systems state persists the higher the risk that "priorities have changed" and the rewrite is abandoned, permanently leaving two systems where there used to be one
- **Evidence**: Willison's closing description of the risk trajectory from the two-systems state.
- **Confidence**: anecdotal
- **Quote**: "If you're *really lucky* the company won't have lost patience with the new system and will allow that work to continue. The longer this all takes, and the longer the old system stays in production and stubbornly continues to work, the higher the risk that \"priorities have changed\" and the new system total replacement work is abandoned, leaving you with two systems where you used to have one."
- **Our assessment**: This names abandonment risk as compounding over time (not a fixed probability), and specifically identifies "the old system stubbornly continues to work" as a driver of that risk — success at keeping the old system limping along removes the urgency that would otherwise force the rewrite to completion. This is a distinct, generalizable organizational-attention argument, not just a restatement of Claim 6.

### Claim 8: Willison's stated go-forward recommendation, if he faces a similar situation again, is to shore up the old system with as much automated testing as possible and then attempt targeted refactors toward the desired shape, which he believes has a much higher chance of success than a greenfield replacement
- **Evidence**: Willison's own closing recommendation, explicitly hedged as a "hunch" rather than a proven rule.
- **Confidence**: anecdotal
- **Quote**: "If I run into a situation like this in the future, my strong recommendation will be to shore up the old system with as much automated testing as possible and then seeing if targeted refactors can get it to the desired shape. My hunch is that in many cases that will have a much higher chance of success than the siren call of a greenfield replacement."
- **Our assessment**: This is the post's prescriptive payoff and the claim most directly usable as guide advice — but note it is explicitly self-labeled a "hunch," with no comparative data (e.g., no stated success-rate difference between the two approaches). It is also, notably, silent on where AI/agentic tooling fits into either path — this source neither recommends nor rules out AI assistance for the testing/refactor path, it simply doesn't address the tooling question at all.

### Claim 9: Will Larson's "Migrations: the sole scalable fix to tech debt" is named as the best available reference for completing a legacy-system replacement process responsibly
- **Evidence**: A direct attribution and link, without a supporting quote from Larson's piece itself.
- **Confidence**: anecdotal (an endorsement/pointer, not independently evaluated content)
- **Quote**: "The best article I've read about completing this process responsibly is *Migrations: the sole scalable fix to tech debt* by Will Larson."
- **Our assessment**: This is a pointer to a resource, not a claim in itself — flagged here as a candidate for a future source-note extraction (`lethain.com/migrations/` is not currently in the corpus) if the guide wants a deeper, more structured migrations methodology to sit alongside Willison's informal failure-mode account.

## Concrete Artifacts

### Full verbatim text of the comment (simonwillison.net, fetched via raw HTML)

```
Source: https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/
Posted: 6th September 2026 at 9:08am
Page type: "Comment" — "My comment" on "There's No Limit to How Bad Code Can
  Get — Lobste.rs" (lobste.rs/s/rfn2mn/there_s_no_limit_how_bad_code_can_get)

[In reply to a comment about burning it down to start from scratch when
technical debt becomes overwhelming]

In my experience it's so rare for that to work.

You announce the old thing is irrecoverably drowning in tech debt. You spin
up a team to rewrite it from scratch. Work begins.

Meanwhile the old thing remains a moving target: it's running the core
business, so changes are still necessary. The developers working on it know
that it's going to be made obsolete by the new thing soon, so they don't
have any incentive to go beyond the smallest effort possible to add the new
features. Technical debt continues to mount.

Meanwhile, the team working on the new thing are ambitious and probably a
little naive. They start out at a great pace - it's greenfield after all -
but as time progresses it becomes apparent that nobody fully understands the
behavior and scope of the thing they are replacing. If it was well
documented and tested it wouldn't need to be replaced, after all...

After months (or even years) without delivering value, the pressure is on to
"ship it", so the new system is launched to handle a subset of what the old
system handled - or often for some new feature that was too hard to build
with the now mostly unmaintained old system.

... so now you have TWO systems in production - the janky old system that
nobody wants to touch, and a new system which handles just a few production
features and is 80% inactive code that is meant to replace the old system,
eventually.

If you're really lucky the company won't have lost patience with the new
system and will allow that work to continue. The longer this all takes, and
the longer the old system stays in production and stubbornly continues to
work, the higher the risk that "priorities have changed" and the new system
total replacement work is abandoned, leaving you with two systems where you
used to have one.

The best article I've read about completing this process responsibly is
Migrations: the sole scalable fix to tech debt by Will Larson
(https://lethain.com/migrations/).

If I run into a situation like this in the future, my strong recommendation
will be to shore up the old system with as much automated testing as
possible and then seeing if targeted refactors can get it to the desired
shape. My hunch is that in many cases that will have a much higher chance of
success than the siren call of a greenfield replacement.
```

### Thread context (Lobste.rs, `lobste.rs/s/rfn2mn/there_s_no_limit_how_bad_code_can_get`, fetched via raw HTML)

```
Article discussed: "There's No Limit to How Bad Code Can Get"
  (zachkehs.com/blog/theres_no_limit_to_how_bad_code_can_get/) — not
  separately mined by this note; out of scope for this issue.

Parent comment Willison was replying to (user: gunduzc):
  "Perhaps I'm just a naive youngster, but I feel like sometimes it's
  necessary to burn it all to the ground and start from scratch."
  "(In business contexts, the starting from would scratch have to happen
  before ditching the old codebase, I'm assuming.)"

Opposing reply elsewhere in the same thread (user: greysonp):
  "I feel like this is a common belief, that rewrites hardly ever work, but
  I think it's just because we're biased towards remembering the ones that
  fail really horribly. I think people rewrite systems successfully all the
  time. I've certainly done it plenty of times. But I think it's heavily
  dependent on domain, the size of the system, the reasons for the rewrite,
  etc. I just don't like discouraging people from cleaning up messes :)"
```

## Cross-References

- **Contradicts**: `blog-simonwillison-rewriting-bun-rust.md` (Claim 1: "Coding
  agents powered by today's frontier models change that equation" that
  previously made full rewrites inadvisable, framed around the Bun
  Zig-to-Rust rewrite). **Filed as issue #3370.** Both are Willison's own
  stated positions on the same underlying question — full rewrite vs.
  refactor — roughly two months apart on the same blog. The July 8 post
  argues AI agents overturn the "never rewrite" heuristic; this September 6
  post argues rewrites are rare to succeed and recommends test-harden +
  targeted refactor instead, without mentioning AI/agents as a mitigating
  factor at all. Per MINER.md §4a, no verdict is picked here — see the filed
  issue for both sides and a possible reconciling conditioning variable
  (mechanical AI-driven port with a pre-existing implementation-independent
  test suite and single-owner continuity, vs. a socio-technical greenfield
  redesign by a new team) that neither Willison post states explicitly.
- **Corroborates**:
  - `blog-addyosmani-intent-debt.md` (Claim 2: "A guess about intent isn't
    the intent... It will invent a confident-sounding reason, which is worse
    than admitting it doesn't know," and Claim 4, on agents/new joiners
    lacking the tacit intent that accumulated in departed humans' heads) —
    Claim 4 here ("nobody fully understands the behavior and scope of the
    thing they are replacing... if it was well documented and tested it
    wouldn't need to be replaced") is the same underlying risk — undocumented
    rationale/behavior — applied specifically to the moment a team decides to
    rewrite rather than to day-to-day agentic work. Osmani's corpus note
    supplies the mechanism (intent debt compounds because nobody wrote down
    the why); this source supplies a concrete consequence (that debt is
    exactly what makes a rewrite team's early confidence misplaced).
  - `blog-fowler-malykhin-archaeologist-copilot.md` (Claim 3: a legacy test
    suite that appears to pass can mask complete absence of coverage on the
    riskiest code paths, because the tests exercise only a mock rather than
    the real networked/thread-unsafe code; Claim 10: a TestContainers
    replacement was deliberately abandoned mid-migration after it turned
    into a multi-front "Big Bang" refactor, reverting to the simpler
    already-working pattern) — both are small-scale, concrete instances of
    the exact dynamics this source describes abstractly: a test suite that
    *looks* like a safety net but isn't (echoing Claim 4's "if it was well
    documented and tested" caveat) and a scope-creeping rewrite attempt
    voluntarily aborted in favor of the more conservative, already-working
    path (echoing Claim 8's targeted-refactor recommendation) — but at the
    scale of a single subsystem migration within an otherwise successful
    modernization, not a whole-system rewrite.
  - `blog-thoughtworks-harrison-insurance-legacy-modernization.md` (Claim 10:
    "Modernization programs that are not connected to specific business
    outcomes usually lose momentum"; Claim 11: "The best modernization
    programs do not begin with a mandate to transform everything; they start
    where legacy most clearly constrains value") — Claim 10 there directly
    corroborates this source's Claim 7 (abandonment risk rising the longer a
    rewrite drags on without clear business payoff), and Claim 11 there
    corroborates this source's Claim 8 (targeted, scoped work over
    wholesale replacement) from an independent, enterprise-consulting
    vantage point rather than a single practitioner's blog comment.
- **Extends**: `blog-pragmaticengineer-bun-rust-rewrite.md` and
  `blog-anthropic-code-migration-playbook.md` (Jarred Sumner's Bun
  Zig-to-Rust rewrite and Mike Krieger's Python-to-TypeScript port) — both
  are large-scale full rewrites that succeeded, and both are structurally
  consistent with this source's own Claim 8 recommendation rather than with
  the failure mode in Claims 2-7: neither was a new team redesigning a
  system it didn't understand (both were done by the original owner/a small
  dedicated team with deep familiarity), and both used a pre-existing,
  exhaustive, language-independent test suite as a behavioral oracle — which
  is arguably the AI-native instantiation of exactly "shore up the old
  system with as much automated testing as possible" that this source
  recommends, applied to a full port rather than a partial refactor. This
  reframing is not stated by any of the three sources themselves; it is this
  note's synthesis, offered as the more specific answer to the Prospector's
  triage question ("how do AI agents change the calculus of rewrites vs.
  targeted refactoring?") — see Guide Impact.
- **Novel**: The specific five-step causal chain named here (moving-target
  old system → developer disincentive → new-team understanding gap →
  ship-pressure partial launch → two-systems-in-production trap →
  compounding abandonment risk) is not previously documented in the corpus
  as a named sequence. No existing source note names "two systems in
  production" as the specific, recognizable failure state of a stalled
  rewrite.

## Guide Impact

- **Chapter 05 (Team Adoption)**: The current NAB Assembly-migration
  discussion (around the "27% finding: measure new categories of work"
  section) covers migration *viability* (a project a team wouldn't have
  attempted without AI) but not migration *failure modes*. Add this source's
  five-step failure sequence as an explicit risk checklist for any team
  considering a full rewrite (AI-assisted or not): is the old system still
  taking required changes (moving target)? Are the developers maintaining it
  aware it's being replaced (disincentive)? Does the new team have verified
  (not assumed) understanding of the old system's real behavior? Is there a
  live risk of a "ship a subset" compromise under delivery pressure? Pair
  this with the Bun/Krieger case studies already cited elsewhere (per
  Cross-References → Extends) as the counter-example: those succeeded
  specifically because they avoided the "new team, undocumented system"
  precondition this source's failure mode depends on — a distinction the
  guide should make explicit rather than let the two source families read as
  simply contradictory.
- **Chapter 03 (Verification)**: The existing "Green tests that never touch
  the risky code" section (citing `blog-fowler-malykhin-archaeologist-copilot.md`)
  already makes the point that a passing suite can mask real risk. Add this
  source's Claim 4 aside — "if it was well documented and tested it wouldn't
  need to be replaced" — as a sharper framing for *why* that verification
  gap tends to concentrate precisely in the systems most likely to be
  targeted for a rewrite: the decision to rewrite is itself evidence the
  existing safety net is unreliable, which argues for verifying (not
  assuming) test-suite quality before either a rewrite or a refactor.
- **Do not cite Claim 1's headline ("so rare for that to work") or the "80%
  inactive code" figure in Claim 6 as measured statistics** — both are
  stated by the author as impression/estimate, not data, and the guide
  should preserve that hedge if either is quoted.

## Extraction Notes

- The source was fetched twice: once via WebFetch (which correctly identified
  it as Willison's own first-person comment, not a blockquote of someone
  else), and once via direct `curl` to get raw HTML for verbatim quote
  verification. All quotes above were checked character-for-character
  against the raw HTML (`<div class="note">` block), not the WebFetch
  summary, per MINER.md §2a.
- Per MINER.md §1, the linked Lobste.rs thread (the direct "via"/"My comment"
  link, and the top of the linked discussion) was fetched and read to confirm
  (a) that Willison's post is his own first-person comment rather than a
  quotation of another commenter, (b) the exact text of the comment he was
  replying to, and (c) that the thread contains live disagreement with his
  position (`greysonp`). The linked external article the Lobste.rs thread
  itself discusses (`zachkehs.com`) was not fetched — it is two hops removed
  from the assigned source URL and the Prospector's triage comments scope
  this issue to Willison's comment specifically. The `lethain.com/migrations/`
  article Willison cites by name (Claim 9) was likewise not fetched in full:
  it is a candidate for a future, separate source submission rather than a
  sub-page of this one, since Willison does not quote or summarize its
  content here beyond naming it "the best article."
- **Two Prospector triage comments exist on issue #3346 with different
  novelty/chapter assessments** (first: novelty "low," relevant chapter
  Ch05, framing this as generic non-AI-specific commentary; second: novelty
  "high," relevant chapters Ch02/Ch03/Ch04, framing this as a practitioner
  comment worth extracting in full detail with an explicit extraction
  brief). Both comments are legitimate triage assessments (author `steveash`,
  `OWNER` association) rather than an injected/spoofed instruction, but they
  disagree with each other. This note follows the second, more specific
  comment's extraction brief (it correctly identifies the source as a
  Lobste.rs comment, gives concrete extraction targets, and points at real
  chapter numbers), while landing the actual Guide Impact chapter mapping on
  Ch05 and Ch03 — the two chapters, verified against the real `guide/`
  directory contents, that this source's content concretely extends. Neither
  triage comment's proposed chapter list was accepted uncritically; both were
  checked against what `guide/02-harness-engineering.md`,
  `guide/03-verification.md`, and `guide/05-team-adoption.md` actually
  contain before finalizing Guide Impact above.
- No source content was paywalled, thin, or unreadable. The source itself is
  short (~350 words); the claim count above (9) reflects genuine claim
  density in the text, not padding — each claim corresponds to a distinct
  sentence-or-paragraph-level assertion in the original, per MINER.md §2's
  instruction not to paraphrase into generic bullets.
