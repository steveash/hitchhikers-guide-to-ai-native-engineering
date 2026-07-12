---
source_url: https://simonwillison.net/2026/Jul/8/kenton-varda/
source_type: blog-post
title: "A quote from Kenton Varda"
author: Kenton Varda (quoted by Simon Willison)
date_published: 2026-07-08
date_extracted: 2026-07-12
last_checked: 2026-07-12
status: current
confidence_overall: anecdotal
issue: "#1781"
---

# A Quote from Kenton Varda — Moratorium on AI-Written Change Descriptions

> Kenton Varda (Cap'n Proto creator, Cloudflare capability-security practitioner),
> quoted via a tweet on Simon Willison's link blog, reports banning AI-written PR
> descriptions, commit messages, and issue/ticket text from his team because they
> consistently restated code-visible detail while omitting the higher-level intent
> a reviewer actually needs.

## Source Context

- **Type**: blog-post (Simon Willison link-blog "quotation" entry, published 8th
  July 2026 at what the page reports as a single-paragraph-pair blockquote with
  no additional Willison commentary — confirmed by two independent fetches of
  the page, both returning identical content and neither surfacing any
  Willison-authored framing text beyond the quote itself).
- **Author credibility**: Kenton Varda is the creator of Cap'n Proto (a
  capability-based RPC/serialization system) and a security engineer at
  Cloudflare with a public track record in capability-security design. He is
  already a named source in this corpus via `blog-latentspace-ainews-meta-harness-summer.md`
  (Claim 4: a secondhand digest paraphrase of a separate Varda tweet critiquing
  Anthropic's per-agent identity/ACL permissioning model). This entry is a
  *different* tweet on a *different* topic — team practice around AI-generated
  change descriptions, not permissioning architecture — quoted directly rather
  than paraphrased by a third party. Varda's practitioner standing (he runs an
  engineering team and is describing his own team's policy, not a hypothetical)
  gives the claim first-person authority; Willison's selection of it for his
  curated feed is a secondary relevance signal, consistent with how this corpus
  treats other Willison quotation entries (e.g.
  `blog-simonwillison-tom-macwright-accidental-anonymity.md`).
- **Scope**: The entire accessible content is a single tweet (two sentences)
  reproduced as a blockquote, linked to
  `https://twitter.com/kentonvarda/status/2074924213983740233`. It covers: (1)
  the decision itself (a moratorium, scoped to three artifact types, applied to
  "my team"); (2) the specific failure mode that motivated it (misallocated
  detail: code-visible specifics present, high-level framing absent). It does
  NOT cover: how long the AI-written descriptions were in use before the ban,
  which tool(s) generated them, what team size or codebase this applies to,
  what (if anything) replaced the AI-written descriptions, whether the ban is
  permanent or a temporary "moratorium," or any data/count beyond Varda's own
  characterization. The tweet itself is the entire source; there is no linked
  article, thread continuation, or Willison commentary to follow per MINER.md
  §1's "follow up to 5 linked pages" guidance — the only link is the tweet URL
  itself, which is unreachable via WebFetch (X/Twitter requires authentication)
  and is not treated as a separate substantive page.

## Extracted Claims

### Claim 1: Kenton Varda declared a moratorium banning AI-written change descriptions — PR messages, commit messages, and issue/ticket text — from his engineering team
- **Evidence**: Direct first-person statement of a policy decision, by a named practitioner about his own team.
- **Confidence**: anecdotal (single practitioner's self-reported policy change; no data on team size, duration, or enforcement mechanism)
- **Quote**: "I just declared a moratorium against AI-written change descriptions (e.g. PR and commit messages, also issues/tickets) from my team."
- **Our assessment**: This is a concrete, named instance of a practitioner actively *restricting* AI use for a specific artifact type, rather than the more commonly documented pattern of expanding AI use. The scope is notably broad — not just PR descriptions but commit messages and issue/ticket text as well, i.e. every text artifact that documents "what changed and why" across the whole change-management surface. The word "moratorium" (rather than "policy" or "rule") implies this is framed as temporary/reversible, though the tweet does not state a review date or reversal condition.

### Claim 2: The specific failure mode was a content-allocation problem — AI-written descriptions restated low-level detail already visible in the code, while omitting the higher-level framing needed to understand what the change does
- **Evidence**: Varda's own diagnostic explanation of why the AI-written descriptions failed, given as the direct reason for Claim 1's decision.
- **Confidence**: anecdotal (single practitioner's diagnosis, not a systematic comparison or study)
- **Quote**: "AI was writing change descriptions that were worse than useless to me as I tried to review PRs: outlining details of the code that could easily be seen by looking at the code, but omitting the higher-level framing needed to understand broadly what the code is doing."
- **Our assessment**: This names a specific, checkable pattern rather than a vague complaint: the AI descriptions get the *direction* of abstraction backwards for the review use case — restating what a reviewer can already see in the diff, while failing to supply the one thing a diff cannot show on its own (why the change exists, what it's trying to accomplish, how the pieces relate). This is a distinct failure mode from generic "AI-generated text is low quality" — it's specifically that the model over-indexes on describing observable code mechanics and under-indexes on synthesizing intent, which is architecturally close to (but not identical to — see Cross-References) the "agent can't generate intent, only infer a plausible rationale" mechanism documented elsewhere in this corpus.

### Claim 3: Varda characterizes the AI-written descriptions as "worse than useless" for his specific use case (reviewing PRs) — not merely low-value, but actively counterproductive
- **Evidence**: Varda's explicit value judgment, stated as the direct consequence of the content-allocation failure in Claim 2.
- **Confidence**: anecdotal (a single practitioner's subjective assessment of review cost, not a measured comparison of review time with vs. without AI descriptions)
- **Quote**: "AI was writing change descriptions that were worse than useless to me as I tried to review PRs"
- **Our assessment**: "Worse than useless" is a stronger claim than "unhelpful" or "no better than nothing" — it implies the descriptions actively cost reviewer time or attention (e.g., by requiring the reviewer to first read the description, recognize it doesn't answer the question they need answered, then discard it and read the diff directly to reconstruct intent themselves) rather than simply failing to help. The tweet does not quantify this cost, so it should be treated as Varda's framing of the experience, not a measured finding — but the framing is specific and directional (the descriptions are actively in the way, not merely absent value) which is a useful, quotable data point distinct from generic "AI text is low quality" complaints.

## Concrete Artifacts

### The Willison Page Blockquote (verbatim, verified across two independent fetches)
```
Source: Simon Willison, https://simonwillison.net/2026/Jul/8/kenton-varda/
Title: A quote from Kenton Varda
Published: 8th July 2026
(Quoting Kenton Varda, https://twitter.com/kentonvarda/status/2074924213983740233)
Tags: ai, generative-ai, llms, ai-assisted-programming, kenton-varda

"I just declared a moratorium against AI-written change descriptions (e.g.
PR and commit messages, also issues/tickets) from my team.

AI was writing change descriptions that were worse than useless to me as I
tried to review PRs: outlining details of the code that could easily be
seen by looking at the code, but omitting the higher-level framing needed
to understand broadly what the code is doing."
```

## Cross-References

- **Corroborates**: `blog-addyosmani-intent-debt.md` Claim 2 ("An agent cannot
  generate intent — it can only infer a plausible-sounding rationale from the
  code, which is not the same as the actual intent") and Claim 7 ("High intent
  debt shows up as a specific pattern — agents make silent behavioral changes
  and nobody can say whether the change was safe, because the reason for the
  prior behavior was never recorded... no doc or commit message ever recorded
  why it was there"). Varda's complaint is a first-person, named-practitioner
  instance of exactly the mechanism Osmani names abstractly: the AI-written
  artifact (here, the change description itself, not just the code) fails to
  carry forward the *why*, even though it readily reproduces the *what*.
  Osmani's framework predicts this outcome; Varda's tweet is a concrete report
  of a team hitting it badly enough to ban the practice.
- **Corroborates**: `blog-addyosmani-agentic-code-review.md` Claim 8 ("AI
  agents reason through problems but discard that reasoning once the diff is
  produced, forcing reviewers to reconstruct intent that was never recorded")
  and Claim 9 ("Attaching the agent's stated goal and rejected alternatives to
  the PR as a decision log removes most of the reconstruction cost that makes
  review slow"). Claim 8 there describes the identical review-time cost Varda
  is reacting to — the reviewer must reconstruct intent the agent never
  externalized. Notably, Claim 9's prescribed fix (have the *coding* agent
  attach its own stated goal and rejected alternatives as a decision log) is
  the inverse of what Varda observed: Varda's team apparently had a
  *separate* AI-generation step producing the change description itself
  (rather than the coding agent's own reasoning trace being attached
  directly), and that separate step produced description text disconnected
  from the actual rationale — regenerating surface detail rather than
  surfacing the reasoning that produced the diff. This is a useful distinction
  for the guide: "have the agent describe its own change" and "have the agent
  that already reasoned about the change attach that reasoning" are not the
  same mechanism, and Varda's failure is evidence for preferring the latter.
- **Extends**: `blog-latentspace-ainews-meta-harness-summer.md` Claim 4 (a
  secondhand digest paraphrase of a different Kenton Varda tweet critiquing
  Anthropic's per-agent-identity permissioning model as not scaling). Both
  claims trace to the same named practitioner raising concrete, specific
  objections to how AI/agent tooling is deployed inside real engineering
  teams — one about permissioning architecture, this one about change
  documentation — which somewhat strengthens Varda's standing in this corpus
  as a repeat source of concrete, critical, hands-on practitioner pushback
  rather than one-off commentary. The two claims are on unrelated topics and
  are not evidence for or against each other.
- **Contradicts**: None identified. No existing corpus note argues that
  AI-generated PR/commit/issue descriptions reliably supply the higher-level
  framing reviewers need; this source adds a negative data point to a gap the
  corpus had not yet covered with a named, first-person practitioner report,
  rather than opposing an existing claim.
- **Novel**: The specific "moratorium" framing (an explicit ban on a
  previously-adopted AI use case, applied team-wide) is a new pattern for this
  corpus — most existing sources document AI adoption expanding or AI
  assistance being tuned/scoped, not a category of AI use being withdrawn
  outright after being tried. The precise failure mechanism as stated —
  restating code-visible detail while omitting higher-level framing, applied
  specifically to *change descriptions* (not code, not comments, not specs)
  — is also new; the corpus's existing "agent can't generate intent"
  material (Osmani) is about code/decisions generally, not about the PR/
  commit/issue description artifact type specifically.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: The guide's PR-review workflow guidance
  should not assume AI-generated PR/commit descriptions are a net-positive
  default. Cite Claim 2 and Claim 3 as a named counter-example: at least one
  practitioner found AI-generated descriptions actively counterproductive for
  review specifically because they restate diff-visible detail instead of
  supplying intent, and responded by banning the practice team-wide rather
  than tuning it. Pair with `blog-addyosmani-agentic-code-review.md` Claim 9's
  proposed fix (attach the *coding* agent's own stated goal/rejected
  alternatives as a decision log, rather than generating a description as a
  disconnected second step) as the alternative the guide should recommend
  instead of a blanket ban or a blanket default-on.
- **Chapter 03 (Verification)**: Add this source as evidence that AI-generated
  change descriptions cannot be trusted as a verification aid on their own —
  a reviewer using an AI-written description to decide what to focus on risks
  missing the actual intent of the change, since the description may omit
  exactly the framing needed to verify the change is doing what it's supposed
  to. This reinforces (via a different artifact type) the general corpus
  pattern that AI-generated summaries of AI-generated work should not
  substitute for a human reconstructing intent from source material.
- **Chapter 05 (Team Adoption)**: Document the "moratorium" pattern as a real
  team-adoption move: a team can and did fully withdraw an AI use case after
  trying it, rather than only ever expanding AI use, when the practitioner cost
  outweighed the benefit for that specific artifact type. Recommend this as a
  concrete example for the guide's team-adoption chapter of matching AI-tool
  scope to demonstrated value per artifact type, rather than applying AI
  generation uniformly across all change-management text (code, commits, PRs,
  issues) once adopted for one of them.

## Extraction Notes

- **Source is a single two-sentence tweet**: reproduced in full above. There is
  no linked article, thread, or additional Willison commentary to follow per
  MINER.md §1 — the only outbound link is to the tweet itself
  (`https://twitter.com/kentonvarda/status/2074924213983740233`), which is not
  independently fetchable (X/Twitter requires authentication) and was not
  treated as a separate substantive source; the Willison page's blockquote
  reproduces the tweet in full, so no content was lost by not fetching the
  tweet URL directly. Given the source's genuine brevity, only 3 claims are
  extracted here rather than the 5–15 the template suggests as a rough target
  — the two-sentence tweet contains three logically distinct assertions (the
  decision, the diagnosed mechanism, the value judgment) and stretching
  further would mean inventing sub-claims the source does not actually make.
  This matches the Prospector's own second-pass triage assessment on this
  issue, which independently flagged the source as thin ("a single short
  quotation without elaboration").
- **Verified via two independent WebFetch passes**: both against
  `https://simonwillison.net/2026/Jul/8/kenton-varda/#atom-everything` (the
  issue URL) and `https://simonwillison.net/2026/Jul/8/kenton-varda/` (without
  the fragment). Both passes returned character-for-character identical
  quoted text, the same publish date, the same tweet URL, and no additional
  Willison commentary. The quote used throughout this note was copied from
  that verified text.
- **Two conflicting Prospector triage comments exist on the source issue**
  (one rating novelty "high" with chapters Ch01/Ch03/Ch05, one rating novelty
  "low" with no chapters clearly applicable). Both were read. This note
  follows the higher-novelty assessment's chapter guidance (Ch01/Ch03/Ch05)
  because, on independent reading, the source does supply a specific,
  checkable, named-practitioner failure mode not previously documented in
  this corpus (see Novel, above) — but the extraction is scoped conservatively
  (3 claims, "anecdotal" confidence, explicit acknowledgment of the source's
  brevity) in deference to the low-novelty assessment's correct observation
  that the source itself is thin.
- **No contradiction issue filed**: this source does not oppose any existing
  corpus claim (see Cross-References → Contradicts); it corroborates and
  extends existing material on intent debt and agentic code review.
