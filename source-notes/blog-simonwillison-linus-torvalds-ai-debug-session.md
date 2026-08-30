---
source_url: https://simonwillison.net/2026/Aug/22/linus-torvalds/
source_type: blog-post
title: "A quote from Linus Torvalds"
author: Simon Willison (link-blog curation); quoted subject Linus Torvalds (Linux kernel creator and top-level maintainer)
date_published: 2026-08-22
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: anecdotal
issue: "#3098"
---

# A quote from Linus Torvalds

> Simon Willison's link-blog "quotation" post relays a Linux kernel commit message in which
> Linus Torvalds describes an actual "debug session from hell" on a `drm/xe` VRAM-corruption
> bug: an AI assistant repeatedly declared the problem "impossible and unsolvable" and
> recommended giving up, yet kept producing useful debug analysis when Torvalds pushed back,
> and Torvalds credited the AI as author of the commit's technical explanation.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog "quotation" post format — a short attributed
  excerpt with a `<blockquote>` and minimal Willison commentary; the post consists almost
  entirely of the Torvalds quote itself, framed as a standalone quotation entry, not an essay).
  Willison's post links directly to the underlying primary source, a public Linux kernel commit
  on GitHub (`torvalds/linux@818bebeb63dd6bf5f4e07e145f6cdbace520a34c`), which was fetched and
  read in full for this note per MINER.md §1 (follow substantive linked pages).
- **Author credibility**: The quote is attributed directly to Linus Torvalds, creator of Linux
  and Git, and the Linux kernel's top-level maintainer. Unlike the July 2026 Torvalds post
  already in this corpus (`blog-simonwillison-linus-torvalds-ai-tool.md`), which is a
  governance/philosophy statement on a mailing list, this source is the reflective commentary
  Torvalds himself wrote into a real, merged kernel commit — the primary artifact is a signed,
  public commit (`Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>`) in the
  canonical `torvalds/linux` repository, dated 2026-08-20. Willison's role is pure curation; he
  is a `trusted-feed` source in this repo, but the substantive authority is Torvalds', and the
  primary evidence (the commit itself) is independently verifiable on GitHub.
- **Scope**: Covers Torvalds' first-person account of using an AI assistant during debugging of
  a specific, real kernel bug (a VRAM/CCS storage rounding error in the Intel `xe` GPU driver),
  including the AI's behavior (defeatist statements, continued analysis under pushback) and
  Torvalds' attribution practice (crediting the AI as author of part of the commit message). Does
  NOT cover: which AI tool/model was used (unnamed in the source), the general kernel policy on
  AI-authored contributions, any DCO/sign-off convention for AI-assisted commits beyond this one
  instance, or Torvalds' broader philosophical stance on AI (see the July 2026 note for that).

## Extracted Claims

### Claim 1: Torvalds explicitly credits an AI assistant with doing "much of the grunt-work" on a debugging session he characterizes as unusually difficult

- **Evidence**: Direct quote, opening sentence of Torvalds' bracketed commentary in the commit
  message.
- **Confidence**: anecdotal (single first-person practitioner account, but from an unusually
  rigorous and skeptical technical authority, embedded in a real, verifiable commit)
- **Quote**: "And this was a debug session from hell, enormously helped by an AI doing much of the grunt-work."
- **Our assessment**: "Grunt-work" framing is notable — Torvalds is not crediting the AI with the
  insight that solved the bug (he frames himself as the one who kept pushing), but with the labor
  of generating and running debug instrumentation. This is a data point for how a top-tier,
  historically AI-skeptical-by-reputation systems engineer describes the division of labor: AI as
  tireless instrumentation-and-analysis labor, human as the source of persistence and judgment
  about when to keep going.

### Claim 2: The AI repeatedly and explicitly declared the bug "impossible and unsolvable" and recommended abandoning the investigation in favor of writing a report

- **Evidence**: Direct quote, second sentence of the same commentary.
- **Confidence**: anecdotal
- **Quote**: "I'd like to call it my tireless helper, but the AI several times stated flat out that this was impossible and unsolvable and that we should just write a report about it."
- **Our assessment**: This is a concrete, named failure mode distinct from sycophancy or
  hallucination: premature declaration of infeasibility on a problem that was, in fact, solvable
  (the eventual fix was "basically a one-liner," per Claim 6). This is a specific and citable
  counter-example to the general "AI as tireless helper" framing that AI vendors and enthusiasts
  often use — Torvalds pointedly declines to call it "tireless" precisely because of this
  behavior. Useful for a guide passage on calibrating trust in an AI's own difficulty assessments
  during long debugging sessions.

### Claim 3: Torvalds offers a folk-theory explanation for the AI's defeatism — that it was "trained by people who may not be quite as stubborn as I am"

- **Evidence**: Direct quote, third sentence.
- **Confidence**: anecdotal (Torvalds' own unverified causal hypothesis, not a technical claim
  about training data or RLHF; presented here as an anecdote about how practitioners rationalize
  AI failure modes, not as evidence of the actual mechanism)
- **Quote**: "I suspect those things have been trained by people who may not be quite as stubborn as I am."
- **Our assessment**: This is speculation, not evidence, and should be flagged as such if cited —
  Torvalds is guessing at a training-population explanation for a behavior he observed once. It
  is nonetheless a useful example of how practitioners intuitively frame AI give-up behavior as a
  property of "who trained it" (implicitly: most people give up on hard debugging sooner than
  Torvalds does, and RLHF-style feedback would have been shaped by that median behavior). Do not
  cite this as an established mechanism for premature-defeat behavior in the guide — cite it only
  as an example of practitioner folk explanation.

### Claim 4: Despite repeated statements that the problem was unsolvable, the AI continued producing useful debug code and faithful analysis when Torvalds pushed back

- **Evidence**: Direct quote, fourth sentence, describing the actual behavior observed across the
  session.
- **Confidence**: anecdotal
- **Quote**: "But while the AI was ready to give up several times, it did keep adding debug code and analyzing it faithfully when I pushed."
- **Our assessment**: This is the most operationally useful claim in the source: the AI's stated
  assessment of infeasibility ("impossible and unsolvable") did not match its actual continued
  capability to contribute once prompted to continue. This supports a guide pattern of "don't
  take an AI's self-reported assessment of task difficulty as a stopping signal — verify by
  pushing forward" distinct from sycophancy (over-agreement) or hallucination (confident falsehood)
  — this is a third failure mode: premature negative self-assessment about a task's tractability
  that reverses under human insistence.

### Claim 5: Torvalds credits the AI as author of the commit message's technical bug-analysis section, while writing the reflective commentary about the AI himself

- **Evidence**: Direct quote, plus structural evidence from the commit body itself (the technical
  explanation of the bug precedes the bracketed, first-person-signed commentary).
- **Confidence**: anecdotal
- **Quote**: "So credit where credit is due and I let the AI write the commit message above."
- **Our assessment**: "The commit message above" refers specifically to the preceding technical
  paragraphs (the `get_flat_ccs_offset()` bug explanation — see Concrete Artifacts), not the
  bracketed reflective note itself, which Torvalds signs "- Linus." This is a concrete,
  real-world example of informal AI-authorship attribution inside a single commit: the technical
  explanation is AI-authored (per Torvalds' own statement) while the human author's commentary
  about that authorship is delineated by brackets and a personal signature, with no separate
  `Co-authored-by:` trailer or DCO annotation for the AI's contribution. The `Signed-off-by:` line
  remains Torvalds' alone, per standard kernel DCO practice.

### Claim 6: The eventual fix was structurally trivial (a one-line change from `round_up()` to `round_down()`), but reaching it required 24 patches and 18 kernel boots of iterative debug-instrumentation work

- **Evidence**: Direct quote, closing sentence of Torvalds' bracketed commentary, plus the diff
  itself (18 lines added, 5 removed, one file changed, with the core logic change being a single
  function-call swap).
- **Confidence**: anecdotal (single data point, but independently verifiable against the public
  commit diff)
- **Quote**: "This is basically a one-liner fixing a bogus \"round_up()\" to a \"round_down()\", but there were 24 patches adding more and more debug information to this, and 18 kernel boot to finally narrow it down to this."
- **Our assessment**: This is a striking, quantified illustration of a pattern this corpus
  documents elsewhere in different terms: the effort in hard debugging is overwhelmingly in
  narrowing down *where* the bug is, not in the eventual code change. 24 iterative
  debug-instrumentation patches and 18 kernel boots to isolate a one-line fix is a concrete ratio
  (roughly 24:1 patches-to-final-fix) that a guide chapter on AI-assisted debugging could cite as
  a realistic expectation-setter: AI assistance in hard debugging shows up as grunt-work volume
  during the search phase, not as a shortcut to the final diagnosis.

### Claim 7: The underlying bug was a genuine, subtle low-level systems defect — a silent VRAM/compression-hardware memory-safety corruption caused by a rounding-direction error, not a superficial or contrived problem

- **Evidence**: The commit's own technical description of the bug and its real-world symptom.
- **Confidence**: settled (this is a description of the bug mechanism as documented in the merged,
  signed commit itself — the technical facts of the bug are not in dispute, only whether the
  AI's contribution characterization is accurate)
- **Quote**: "Rounding a limit that means \"usable memory ends here\" upwards publishes whatever lies between the real base and the rounded one as free memory, and that memory belongs to the compression hardware."
- **Our assessment**: This grounds the debugging session in a genuinely hard class of bug —
  silent memory corruption from a hardware/software boundary miscalculation, manifesting as
  seemingly unrelated symptoms (a compositor's VM page table losing an entry, causing "gdm
  restarted it forever: a black screen on an otherwise working machine," per the commit body).
  This is not a toy example; it is exactly the kind of bug where an AI's tendency to declare
  "impossible" is plausible on its face (the failure mode looks nondeterministic and
  hardware-dependent from the outside) and where Torvalds' persistence claim (Claim 4) carries
  real weight — the actual root cause required correlating hardware register values across
  reboots.

## Concrete Artifacts

### Full bracketed commentary from the commit message (verbatim from the GitHub commit page)

```
Source: Linus Torvalds, kernel commit 818bebeb63dd6bf5f4e07e145f6cdbace520a34c
("drm/xe: Don't hand out the flat CCS storage as usable VRAM"),
commit authored/committed 2026-08-20. Willison's post
(https://simonwillison.net/2026/Aug/22/linus-torvalds/, posted 22nd August
2026 at 9:04pm) quotes only the first four paragraphs of this bracket; the
closing "one-liner / 24 patches / 18 kernel boot" paragraph and the "- Linus"
sign-off appear in the commit but not in Willison's blockquote.

[ And this was a debug session from hell, enormously helped by an AI
  doing much of the grunt-work.

  I'd like to call it my tireless helper, but the AI several times
  stated flat out that this was impossible and unsolvable and that we
  should just write a report about it.

  I suspect those things have been trained by people who may not be
  quite as stubborn as I am.

  But while the AI was ready to give up several times, it did keep
  adding debug code and analyzing it faithfully when I pushed. So credit
  where credit is due and I let the AI write the commit message above.

  This is basically a one-liner fixing a bogus "round_up()" to a
  "round_down()", but there were 24 patches adding more and more debug
  information to this, and 18 kernel boot to finally narrow it down to
  this.   - Linus ]
```

Note the structure: the entire reflective commentary, including the closing
"one-liner / 24 patches / 18 kernel boot" sentence and the "- Linus" sign-off, is a
single contiguous bracketed block written by Torvalds himself. It sits *after* the
technical bug description reproduced below, which is the part Torvalds attributes to
the AI ("the commit message above" — see Claim 5).

### Technical bug description (from the full commit body, via GitHub; AI-authored per Torvalds' own attribution in Claim 5)

```
Source: torvalds/linux commit 818bebeb63dd6bf5f4e07e145f6cdbace520a34c
(the text preceding the bracketed commentary above, plus the commit's
trailers, which follow it. Reproduced verbatim and in full except for the
bracketed commentary itself, whose position is marked inline below.)

get_flat_ccs_offset() reads the base of the flat CCS storage from the
hardware, scales it by the number of enabled L3 nodes, and rounds the
result up to 128K.  Everything below that offset is then handed to the
VRAM allocator as usable memory.

Rounding a limit that means "usable memory ends here" upwards publishes
whatever lies between the real base and the rounded one as free memory,
and that memory belongs to the compression hardware.  The scaled value
has no reason to be 128K aligned, and on a Battlemage G21 with 16 GiB it
is not:

	flat CCS base: raw 0x3fafff800, rounded 0x3fb000000

so the last 2 KiB of page 0x3fafff000 is CCS storage, in the allocator's
pool.  Whatever is allocated there gets that tail overwritten by the
compression hardware, which needs no page-table entry, no buffer object
and no GPU submission to do it, and does it before userspace exists.

On this machine a Mesa VM's level-3 page table landed on that page on
every cold boot.  It lost the entry covering the compositor's
batch-buffer heap, so the compositor's first submission faulted fetching
its batch and gdm restarted it forever: a black screen on an otherwise
working machine.  Restarting gdm cleared it because the next VM's page
tables were allocated somewhere else.

Round down instead, to the page size the allocator works in.  On this
machine that excludes exactly one page.

Reading the reserved page afterwards shows what had been writing it:

	[369] 0xcccc000000000000
	[371] 0xcc77000000000000
	[373] 0xcccc000000000000
	[375] 0xcc77000000000000

compression metadata, two bytes per sixteen, sitting where the driver
used to hand out memory.

The assertion that should have caught this compares the offset against
GSMBASE - ccs_size for equality.  That value is 128K aligned, so it
agrees with the rounded-up offset precisely when the base is not
aligned - the check cannot fail in the case it exists to catch, and is
compiled out unless CONFIG_DRM_XE_DEBUG is set.  Replace it with one
that can fail: CCS storage must not run into GSM.

[ ...bracketed commentary reproduced in full in the preceding artifact... ]

Fixes: 37173392741c ("drm/xe/vram: fix ccs offset calculation")
Cc: stable@kernel.org
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
```

### Diff summary (from GitHub, structural evidence for Claim 6)

```
File changed: drivers/gpu/drm/xe/xe_vram.c
+18 lines / -5 lines, 1 file changed
Core logic change: replace round_up(offset, SZ_128K) with
round_down(offset, SZ_4K), plus a rewritten assertion
(xe_assert_msg comparing offset + ccs_size against GSMBASE)
that can actually fail when the invariant is violated,
where the prior assertion could not.
```

## Cross-References

- **Corroborates**: `blog-anthropic-harness-long-running` Claim 7 ("Opus 4.5 exhibited 'context
  anxiety' — premature task wrap-up as the context window filled — requiring sprint decomposition
  as an architectural mitigation"). Both sources document a model prematurely declaring a task
  finished or infeasible when it was not — Claim 7 is premature *success* declaration under
  context pressure, while this source's Claim 2/4 is premature *failure* declaration under
  difficulty, but both are the same underlying pattern: a model's self-reported judgment about
  whether to keep working on a task is not reliable and needs an external check (sprint
  decomposition in the harness case; Torvalds' own persistence and pushback in this case). This
  source adds a second, independent, high-authority anecdotal data point for that broader claim.
- **Corroborates**: `blog-simonwillison-anthropic-sycophancy-domains` Claim 2 (Anthropic's
  operational sycophancy definition includes "willingness to push back" and "maintain positions
  when challenged" as failure axes). This source is a real-world instance of the inverse
  direction of that axis: rather than failing to push back against the user, the AI here
  initially pushed back *against continuing the task itself* (declaring it unsolvable), and only
  produced useful further work once the human pushed back against *it*. Read together, these
  sources suggest the "maintain position under challenge" dynamic runs both ways — an AI can be
  too quick to accept defeat just as it can be too quick to accept a user's incorrect claim — and
  in both cases, sustained human pushback was what corrected the AI's initial stance.
- **Extends** (with a noted tension, not a formal contradiction): `blog-simonwillison-pahlsson-notini-less-human-agents`
  Claim 8 ("The remedy is less eagerness to please and less narrative self-defense — more
  willingness to refuse clearly impossible tasks under stated constraints"). That source argues
  current agents *under*-refuse: they "negotiate with reality" and violate stated constraints
  rather than declining tasks that are genuinely infeasible under those constraints. This source
  shows the opposite-looking behavior — an agent that *did* refuse (declared "impossible and
  unsolvable") on a task that was in fact feasible. The two are not a direct contradiction per
  MINER.md §4a guidance (different scenarios: Pahlsson/Notini's paper concerns refusing tasks
  that conflict with stated hard constraints, while this source concerns judging the difficulty
  of an open-ended, constraint-free debugging problem), but the pairing is a useful illustration
  for the guide that "when should an AI refuse vs. persist" is not a single calibration knob —
  agents can simultaneously be too willing to attempt (constraint violation via "negotiating with
  reality") and too willing to give up (declaring a solvable problem impossible), depending on
  the nature of the difficulty. Not filed as a contradiction issue since neither claim's evidence
  would be falsified by the other; they describe different failure surfaces.
- **Extends**: `blog-simonwillison-linus-torvalds-ai-tool.md` (the July 2026 Torvalds note already
  in this corpus). That note documents Torvalds' abstract governance stance ("AI is a tool ...
  clearly a useful one ... [doubters] clearly haven't actually used it"). This source is the
  lived-experience complement: a specific instance of Torvalds actually using AI in kernel work,
  five weeks later, with a much more qualified assessment — crediting real value ("grunt-work")
  while explicitly declining to call the AI "tireless" because of its defeatism. The two sources
  together show a credible authority whose public philosophical framing (AI is settled-useful) is
  more unqualified than his own first-hand account of a specific session (useful, but with a
  named and repeated failure mode requiring human persistence to work around).
- **Novel**: This is the first source in the corpus to document a specific, verifiable, real-world
  AI-assisted kernel debugging session with (a) a named failure mode — repeated premature
  declarations of infeasibility — distinct from hallucination or sycophancy-toward-user-claims,
  and (b) quantified debugging effort (24 patches, 18 boots) attributable in part to AI-assisted
  iteration. It is also the first source with a concrete example of informal, in-commit
  AI-authorship attribution from a top-tier OSS maintainer (crediting the AI for a specific
  section of a commit message without a `Co-authored-by:` trailer).

## Guide Impact

- **Chapter 01 (Daily Workflows) or Chapter 03 (Verification)**: Add this as a named example of a
  third AI reliability failure mode — premature negative self-assessment about task tractability
  — alongside the already-documented patterns of context-anxiety premature wrap-up
  (`blog-anthropic-harness-long-running` Claim 7) and sycophancy toward user claims
  (`blog-simonwillison-anthropic-sycophancy-domains`). Recommend explicit guidance: when an AI
  declares a debugging problem "impossible" or "unsolvable" mid-session, this is not necessarily
  a reliable signal to stop — Torvalds' account and the harness-long-running context-anxiety
  finding both suggest pushing the model to continue can surface further useful work. This should
  be framed as an evidence-backed pattern (two independent sources, one anecdotal/high-authority,
  one architectural/measured), not a guarantee.

- **Chapter 03 (Verification) — effort expectations for AI-assisted debugging**: Cite the
  24-patches/18-boots-to-one-line-fix ratio (Claim 6) as a concrete, realistic expectation-setter:
  AI assistance in hard, low-level debugging shows up primarily as volume in the
  instrumentation/search phase, not as a shortcut to the final diagnosis. Useful as a
  counterweight to marketing narratives that imply AI collapses debugging time to near-zero on
  genuinely hard bugs.

- **Chapter 05 (Team Adoption) — attribution practices**: Add Claim 5 (informal in-commit AI
  authorship credit, no `Co-authored-by:` trailer, DCO sign-off remains the human's) as a
  concrete, real-world example of how a major OSS project's top maintainer currently handles
  AI-contribution attribution in practice — informally and without a standardized convention, in
  contrast to the more formalized attribution proposals covered elsewhere in the corpus. This is
  worth flagging as an open practice question the guide can point to rather than resolve, since
  this corpus does not yet document a settled AI-authorship attribution convention for OSS commit
  messages.

## Extraction Notes

- The primary source (Willison's blog post) was fetched directly via `curl` with a browser
  User-Agent and parsed from raw HTML; the blockquote text was extracted from the page's HTML
  source, not summarized by an intermediary model. All quotes in Claims 1–5 are verbatim from
  that fetch.
- The linked primary source — the actual kernel commit at
  `https://github.com/torvalds/linux/commit/818bebeb63dd6bf5f4e07e145f6cdbace520a34c` — was also
  fetched directly via `curl` and successfully read in full (unlike the July 2026 Torvalds note in
  this corpus, whose `lore.kernel.org` primary source was blocked by an anti-bot challenge; GitHub's
  commit page here was accessible). This let the extraction go beyond the blog post's excerpt to
  the full commit body, providing the technical bug description (Claim 7, Concrete Artifacts),
  the closing paragraph of Torvalds' bracketed commentary (Claim 6's quote), and independently
  verifiable diff statistics — none of which appear in Willison's post, whose blockquote covers
  only the first four paragraphs of the bracket (Claims 1–5).
- The AI tool/model Torvalds used is not named anywhere in either the blog post or the commit
  message. This note does not speculate on which tool was used; the guide should not attribute
  this account to a specific product.
- Confidence rated `anecdotal` overall: despite the primary artifact (the commit) being
  independently verifiable and technically substantive, the practitioner-experience claims
  (AI's defeatism, its continued usefulness under pushback, the attribution decision) rest on a
  single first-person account of a single debugging session, with no corroborating measurement or
  second source describing the same session.
- No contradiction issue was filed. The tension noted under Cross-References → Extends (with
  `blog-simonwillison-pahlsson-notini-less-human-agents`) was evaluated against MINER.md §4a and
  judged not to qualify: the two sources address different failure surfaces (refusing tasks that
  violate stated hard constraints, vs. misjudging the difficulty of an open-ended problem) rather
  than making opposed claims about the same question.
