---
source_url: https://sourcegraph.com/blog/agentic-batch-changes-pricing
source_type: blog-post
title: "Coding agents usually can't price on outcomes. Ours can."
author: Dan Adler (Sourcegraph)
date_published: 2026-09-16
date_extracted: 2026-09-17
last_checked: 2026-09-17
status: current
confidence_overall: emerging
issue: "#3504"
---

# Coding agents usually can't price on outcomes. Ours can.

> Sourcegraph's rationale post (published two days after the Agentic Batch
> Changes GA launch) for why the product is priced on merged changesets
> rather than tokens or seats: it argues general-purpose coding agents
> can't support outcome-based pricing because their open-endedness makes
> ROI unmeasurable, while a deliberately scoped special-purpose agent that
> defaults to scripts over agent invocations can, and offers the Canva
> customer case as a worked example of what an outcome-based bill looks
> like in practice.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, published September 16,
  2026, one day after the source date the Prospector's triage comments
  reference — auto-discovered via the `sourcegraph` trusted feed named in
  the triage issue). Short-form (~600 words) opinion/rationale post: an
  opening framing on engineering-leader budget conversations, a pricing
  announcement, a "why would we do this to ourselves?" section explaining
  the internal and philosophical justification, the Canva customer quote,
  and a closing section tying the launch back to an earlier Adler post
  about codebase ownership. No embedded video or additional linked
  sub-pages beyond two in-line links (to the Agentic Batch Changes launch
  post and to Adler's June post `sourcegraph.com/blog/owning-a-codebase`,
  neither of which was followed as a separate extraction pass — see
  Extraction Notes).
- **Author credibility**: Byline is Dan Adler, published on Sourcegraph's
  official company blog (confirmed via the page's embedded post metadata,
  which lists `authors:["Dan Adler"]` alongside the same title and
  2026-09-16 date). No role or title is given for Adler anywhere in the
  post itself, so this note does not assert one. This is first-person
  vendor rationale content ("I talk to engineering leaders every week"):
  Sourcegraph sells the product being justified, and the post explicitly
  frames the finance-team-conversion anecdote and the "ROI is an
  impossible question" critique of competitors as arguments for why
  Sourcegraph — specifically — can do something rivals can't. The one
  named customer quote (Canva) is attributed to a specific individual and
  title and is the strongest evidence in the post; the industry-pricing
  claim (Sierra/Fin/Decagon billing per resolution) and the finance-team
  anecdote are unsourced and unverifiable by this Miner.
- **Scope**: Covers the pricing-model announcement and its business
  rationale, a contrast with how other AI verticals and coding-agent
  vendors price, the architectural reason (special-purpose agent design,
  script-over-agent-invocation cost minimization) the company believes
  makes outcome-based pricing viable, and one customer case (Canva) framed
  in outcome-billing terms. Does NOT cover: an actual per-changeset price,
  the underlying merge/reject ratio needed to judge whether outcome
  pricing is cheaper than token pricing at scale, any technical detail of
  how the system decides "needs judgment vs. needs doing" (covered instead
  in the companion launch post), or any customer who used the product and
  had a worse economic outcome under the new pricing model.

## Extracted Claims

### Claim 1: Agentic Batch Changes prices on outcomes — customers pay only when a changeset it generates is merged into their codebase, and pay nothing if it isn't
- **Evidence**: Author's own pricing-policy statement, stated as fact about
  the shipped commercial model.
- **Confidence**: settled (a verifiable, specific fact about how a shipped,
  GA commercial product is priced)
- **Quote**: "we are pricing based on outcomes: you only pay when a changeset it generates is merged into your codebase. If it doesn't get merged, you don't pay."
- **Our assessment**: This is the same pricing fact already documented as
  Claim 11 in `blog-sourcegraph-preston-agentic-batch-changes.md`
  ("You pay per changeset merged into your codebase, not per token, seat,
  or attempt"), restated here by a different author two days later. This
  note treats it as corroborated rather than novel — see Cross-References.

### Claim 2: Despite outcome/resolution-based pricing already being used by AI vendors in other verticals (customer support), dev-tool coding agents remain tied to seat- and usage-based pricing
- **Evidence**: Author's own comparative industry claim, naming three
  specific competitors in an adjacent vertical.
- **Confidence**: anecdotal (an unsourced industry generalization — no
  citation, pricing page, or methodology given for how "Sierra, Fin,
  Decagon, and more" price, and no accounting of any dev-tool competitor
  that might already price on outcomes)
- **Quote**: "Despite the innovation in other verticals (Sierra, Fin, Decagon, and more all charge per resolution), dev tools remain firmly tied to seat- and usage-based pricing."
- **Our assessment**: This corpus has a separate, independently-reported
  source on Sierra (`blog-latentspace-meurer-agent-engineer-fde.md`, an
  interview with Sierra's Head of Agent Engineering) but that note covers
  role-naming ("agent engineer" vs. "forward deployed engineer"), not
  pricing — so this claim about Sierra's per-resolution billing is
  currently uncorroborated elsewhere in the corpus and should be treated
  as an assertion, not a verified fact, if cited in the guide.

### Claim 3: The company's framing of what it charges for is a merged changeset, not a diff — because producing a diff is not the hard or valuable part of a migration
- **Evidence**: Author's own thesis-statement sentence, the rhetorical
  pivot point of the post.
- **Confidence**: anecdotal (a marketing/philosophical framing statement,
  not an empirical claim)
- **Quote**: "A diff is not an outcome; a merged changeset is, so that's what we'll be charging for."
- **Our assessment**: This is the load-bearing rhetorical claim tying
  Claim 1 (the pricing mechanism) to Claim 4 below (the backlog problem)
  — it reframes "outcome" specifically as "merged," not "generated" or
  "reviewed," which matters for a guide section distinguishing agent
  *output* volume from agent *impact*.

### Claim 4: The real bottleneck on large migrations is not producing changes but following through on them — migrations stall in backlog because owning one means months of stakeholder management with no way to prove completion, not because the diffs are hard to write
- **Evidence**: Author's own diagnosis of the customer pain point the
  pricing model is meant to address, based on unspecified conversations
  ("the teams I talk to").
- **Confidence**: anecdotal (an aggregated first-person claim about
  unnamed customer conversations, no count or named example given for
  this specific claim, though it is thematically consistent with the
  Canva and Mercari cases documented in the companion Preston note)
- **Quote**: "Producing pull requests just isn't that hard. Code is cheap. Following through is what the teams I talk to struggle with. The changes, the migrations that touch every repository, are the ones that sit in a permanent backlog, because owning one means three months of stakeholder management and negotiations, and never being able to prove the work is complete. The pull requests sit unreviewed and go stale, and the migration that looked finished in week one is still open in month six."
- **Our assessment**: This is the most specific and guide-relevant framing
  in the post: it names the failure mode as a *coordination and proof-of-
  completion* problem, not a code-generation problem — directly consistent
  with the "ticket-per-team, PR-per-repo, status-by-spreadsheet" bottleneck
  already documented in `blog-sourcegraph-tanner-vulnerability-remediation-scale.md`.
  It also explains *why* outcome-based (merge-based) pricing is the
  economically coherent choice given this specific failure mode: if the
  actual cost center is unreviewed/stale PRs rather than diff generation,
  billing for diffs (tokens) misprices the product relative to the
  customer's actual problem.

### Claim 5: The company's finance team initially rejected the outcome-based pricing proposal outright, and was only persuaded after understanding that the underlying agent defaults to scripts rather than full agent invocations for repetitive work
- **Evidence**: Author's own first-person anecdote about an internal
  decision-making process.
- **Confidence**: anecdotal (a first-person internal anecdote with no
  detail on how many people were involved, over what timeframe, or what
  specific data convinced them)
- **Quote**: "Our finance team's first reaction when we proposed this was a \"hard no.\" What changed their mind was understanding how the agent operates. It does not immediately reach for a coding agent when a script will do, and on a migration, that's most of the time."
- **Our assessment**: This is a rare instance of a vendor admitting internal
  skepticism about its own product's viability before shipping — worth
  noting as an authenticity signal, though it is still self-reported and
  unverifiable, and conveniently supports the same architectural claim
  (script-over-agent as the efficiency mechanism) the post needs to make
  its pricing model sound sustainable.

### Claim 6: A single agent can generate a large conditional/switch-style script to apply a repetitive change across many repositories, instead of deploying a separate agent invocation per repository — and this is what keeps per-outcome pricing affordable
- **Evidence**: Author's own cost-mechanism explanation, given as the
  concrete technical justification following the finance-team anecdote.
- **Confidence**: emerging (a specific, first-party mechanism description
  tied directly to a shipped pricing model, consistent with the same
  mechanism described architecturally in the companion launch post)
- **Quote**: "A single agent can generate a thousand-case switch statement instead of deploying a thousand agents, which cuts the cost of getting there."
- **Our assessment**: This restates, with a more vivid and countable
  image ("a thousand-case switch statement" vs. "a thousand agents"), the
  same script-vs-agent-judgment routing decision documented as Claim 5 in
  `blog-sourcegraph-preston-agentic-batch-changes.md` ("Most of the time it
  writes a script, because a large migration is mostly the same change
  made over and over"). This note treats the underlying mechanism as
  corroborated, not novel — see Cross-References. The novel contribution
  here is the explicit causal link the author draws from this mechanism to
  the *pricing model's* viability (cheap cost-per-outcome enables
  charging per-outcome), which the Preston post does not make.

### Claim 7: Most coding agents were built from the start as general-purpose problem solvers — equally suited to open-ended exploration as to executing a specific change — and this generality is precisely what makes measuring their ROI impossible
- **Evidence**: Author's own architectural critique of (unnamed) competing
  coding agents, presented as a block-quoted callout in the original post.
- **Confidence**: anecdotal (an unsupported generalization about
  competitors' design intent — no competitor is named, and no example is
  given of a specific general-purpose agent whose ROI was in fact
  unmeasurable)
- **Quote**: "Most coding agents were designed from the beginning to be general-purpose problem solvers, just as likely to be used for vacation planning or open-ended exploration as executing a change. That openness makes them powerful, but it also makes ROI an impossible question."
- **Our assessment**: This is the post's central strategic argument and the
  most novel claim in this source relative to the companion Preston
  launch post, which describes Agentic Batch Changes' own scoping (Claim 5
  there) but never argues that general-purpose agent design is
  *structurally incompatible* with outcome-based pricing. Read skeptically:
  this is also a competitive-differentiation argument in a vendor's own
  favor, and "vacation planning" is a rhetorical exaggeration rather than
  a real example of what a general-purpose coding agent is used for in
  practice.

### Claim 8: Agentic Batch Changes is a special-purpose agent, deliberately scoped in its harness, system prompt, permissions, and tools to solve one concrete problem, built specifically to minimize cost at scale rather than to repeatedly re-solve the same task
- **Evidence**: Author's own architectural self-description, in the same
  block-quoted callout as Claim 7, presented as the contrasting positive
  case to the general-purpose-agent critique.
- **Confidence**: emerging (a specific, first-party architectural
  description of a shipped product's design intent, not independently
  audited by this Miner)
- **Quote**: "Agentic Batch Changes is a special-purpose agent, scoped deliberately in its harness, its system prompt, its permissions, and its tools, to solve one concrete problem. We built that harness to minimize cost at scale, rather than paying for an agent to do the same job a hundred or a thousand times over."
- **Our assessment**: This names four specific scoping dimensions (harness,
  system prompt, permissions, tools) as the levers used to narrow a
  general-purpose coding agent into a special-purpose one — this is a more
  concrete, reusable checklist than a generic "scope your agent narrowly"
  recommendation, and pairs directly with Claim 7's framing of *why*
  narrowing matters (it's what makes outcome-based economics tractable).

### Claim 9: Outcome-based pricing lets an engineering budget owner justify spend against a number they can count (merged changes) rather than a compute forecast or a seat that has no relationship to whether the migration actually finished
- **Evidence**: Author's own framing of the pricing model's value
  proposition to budget owners.
- **Confidence**: anecdotal (a value-proposition/marketing framing, not an
  empirical or verifiable claim)
- **Quote**: "If you own a budget, you can now justify this spend against a number you can count. Not a forecast of compute, and not a seat that has nothing to do with whether the migration finished. A merged change is something you can point at."
- **Our assessment**: This directly addresses the "VP of Engineering who
  has to answer for the bill" framing introduced in the post's opening
  paragraph — the specific rhetorical move is replacing an abstract
  forecast (compute) or a fixed cost with no outcome linkage (seat) with a
  literal, auditable count (merges). This is a genuinely reusable
  budget-justification framing for a guide chapter on agent cost
  governance, independent of whether one accepts the vendor's broader
  claims about ROI on general-purpose agents.

### Claim 10: Canva used Agentic Batch Changes to raise and merge 50+ pull requests across repos as part of a library migration during the beta, and their actual bill for that migration is calculated only from the pull requests that merged — not the ones opened, and not agent runtime
- **Evidence**: Named customer quote (attributed to William L., Senior
  Software Engineer at Canva) plus the author's own follow-up sentence
  translating the quote into billing terms.
- **Confidence**: anecdotal (a single named customer's account plus the
  vendor's own restatement of how that customer's bill was calculated —
  not independently verified by this Miner, but attributed to a specific
  named individual, company, and role)
- **Quote**: "We used Agentic Batch Changes to raise and merge 50+ pull requests across our repos as part of a library migration. The web UI made it easy to track each PR and its status. Without it, we would have been managing either huge PRs or spreadsheets; instead, Agentic Batch Changes made the process easier for both reviewers and me." — followed by: "Their bill for that migration is based on the fifty-plus pull requests that merged. Not the ones we opened, and not the hours the agent spent getting there."
- **Our assessment**: The customer quote itself is identical to Claim 10 in
  `blog-sourcegraph-preston-agentic-batch-changes.md` (same source
  attribution, same wording), so it is corroborated rather than novel.
  What IS new in this note is the author's explicit follow-up translating
  the same case into concrete outcome-billing terms ("based on the
  fifty-plus pull requests that merged") — this is the only place in
  either post where a named customer's bill is described in terms of the
  outcome-pricing mechanism, rather than just the workflow outcome.

### Claim 11: The post frames the Agentic Batch Changes launch and pricing as a continuation of an earlier argument (referenced but not reproduced here) that owning a codebase is one of the hardest jobs in software, and that a vendor should only get paid when its tool actually works
- **Evidence**: Author's own closing paragraph, linking to an earlier post
  (`sourcegraph.com/blog/owning-a-codebase`, dated "June" per the author's
  own reference) not otherwise in this corpus.
- **Confidence**: anecdotal (a self-referential framing/thesis
  continuation, not a standalone empirical claim)
- **Quote**: "I wrote in June that owning a codebase may be the hardest job in software, and that the people doing it deserve better tools. Part of better is a tool that works. Another part is a vendor that only gets paid when it does."
- **Our assessment**: This ties outcome-based pricing explicitly to a
  vendor-accountability argument ("a vendor that only gets paid when it
  does [work]") rather than purely a cost-efficiency argument — a subtly
  different framing from Claim 9's budget-justification angle. The linked
  June post is not in this corpus and was not fetched as part of this
  extraction (see Extraction Notes); it may be worth a separate mining
  pass if the guide wants the "codebase ownership as hardest job" argument
  in more depth.

## Concrete Artifacts

### Full pricing-rationale block-quote callout (verbatim, set apart as a `>` blockquote in the original markdown source)
```
Source: https://sourcegraph.com/blog/agentic-batch-changes-pricing

"As much as I like to believe that this is the future of the industry,
there is a reason we can do this while others cannot. Most coding agents
were designed from the beginning to be general-purpose problem solvers,
just as likely to be used for vacation planning or open-ended exploration
as executing a change. That openness makes them powerful, but it also
makes ROI an impossible question.

Agentic Batch Changes is a special-purpose agent, scoped deliberately in
its harness, its system prompt, its permissions, and its tools, to solve
one concrete problem. We built that harness to minimize cost at scale,
rather than paying for an agent to do the same job a hundred or a
thousand times over."
```

### Canva customer quote (verbatim, identical wording to the companion Preston launch post)
```
Source: https://sourcegraph.com/blog/agentic-batch-changes-pricing

William L., Senior Software Engineer, Canva:
"We used Agentic Batch Changes to raise and merge 50+ pull requests across
our repos as part of a library migration. The web UI made it easy to
track each PR and its status. Without it, we would have been managing
either huge PRs or spreadsheets; instead, Agentic Batch Changes made the
process easier for both reviewers and me."
```

### Section headings (verbatim, in document order)
```
Source: https://sourcegraph.com/blog/agentic-batch-changes-pricing

"Why would we do this to ourselves?"
"The owners of the largest codebases deserve tools that bet on themselves"
```

## Cross-References

- **Corroborates**: `blog-sourcegraph-preston-agentic-batch-changes.md` —
  this post is a same-week, different-author companion piece to Preston's
  product-launch post (published 2026-09-14; this post 2026-09-16). Three
  of this note's claims restate facts already documented there: the
  outcome-based/pay-per-merge pricing model itself (Claim 1 here = Claim 11
  there), the script-over-agent-invocation cost mechanism (Claim 6 here =
  Claim 5 there), and the Canva customer quote verbatim (Claim 10 here =
  Claim 10 there). Treat these as corroborated single facts, not two
  independent data points, when citing either note in the guide.
- **Extends**: `blog-sourcegraph-preston-agentic-batch-changes.md` — this
  note adds business/strategic rationale the launch post does not contain:
  the general-purpose-vs-special-purpose-agent argument for *why*
  outcome-based pricing is structurally hard for competitors (Claims 7-8),
  the backlog/stakeholder-management diagnosis of the customer pain point
  the pricing model targets (Claim 4), the finance-team internal-adoption
  anecdote (Claim 5), and the explicit translation of the Canva case into
  outcome-billing terms (Claim 10's second half).
- **Extends**: `blog-sourcegraph-tanner-vulnerability-remediation-scale.md`
  — Claim 4 in this note (migrations stall due to "three months of
  stakeholder management and negotiations," not due to the difficulty of
  writing diffs) is an independent, differently-worded restatement of the
  same coordination bottleneck Tanner's post names as "ticket-per-team,
  PR-per-repo, status-by-spreadsheet." Two different Sourcegraph authors,
  writing about two different products/angles, converge on the same
  diagnosis: the bottleneck in large-scale code change is coordination and
  proof-of-completion, not code generation.
- **Extends**: `blog-cursor-bugbot-effort-billing.md` — that note documents
  Cursor Bugbot's pricing evolution from seat-based to usage-based (charged
  per review run, regardless of whether the run finds a bug or the fix
  gets merged). This post's outcome-based model (charged only on merge, not
  on run) is one step further along the same pricing-model spectrum
  (seat → usage → outcome) documented from a different vendor and a
  different product category (code review vs. cross-repo change
  orchestration) — worth citing together if the guide builds a spectrum of
  agentic-tool pricing models.
- **Contradicts**: None identified as a direct opposing claim. This note's
  Claim 7 (general-purpose agent design makes ROI "an impossible question")
  is in some tension with the general-purpose agent-swarm architecture
  documented favorably in `blog-cursor-agent-swarm-model-economics.md`
  (Cursor's own general-purpose swarm harness, reused across domains) and
  the general-purpose harness-evaluation practices in
  `blog-google-anatomy-harness-engineering.md` — but neither of those
  sources makes a claim about outcome-based *pricing* specifically, so this
  is a difference in emphasis (general-purpose agents can still be
  evaluated and improved) rather than a factual contradiction about
  pricing viability. Not filed as a contradiction issue per MINER.md §4a
  guidance (conditioning-variable difference, not a same-topic factual
  clash).
- **Novel**: The explicit argument that general-purpose coding-agent design
  is structurally incompatible with outcome-based pricing because it makes
  ROI unmeasurable (Claims 7-8) — a strategic/business argument not present
  in the companion launch post or elsewhere in this corpus; the specific
  diagnosis of large migrations stalling due to stakeholder-management
  coordination cost rather than diff-writing difficulty (Claim 4); the
  finance-team-skepticism-then-conversion anecdote (Claim 5); the explicit
  budget-justification framing of "a number you can count" vs. a compute
  forecast or unused seat (Claim 9); and the claimed (but uncorroborated
  in this corpus) precedent of per-resolution pricing in adjacent AI
  verticals — Sierra, Fin, Decagon (Claim 2).

## Guide Impact

- **Chapter 02 (Economics)**: Add Claims 7-8 (special-purpose agent scoping
  — harness, system prompt, permissions, tools — as the structural
  precondition for outcome-based pricing) as a named design pattern
  distinct from a generic "narrow your agent's scope" recommendation: the
  guide can frame it as "scope narrowly enough that a single outcome
  metric captures success, and pricing/ROI measurement follow." Pair with
  Claim 9's budget-justification framing ("a number you can count") as a
  practitioner-facing argument for why this scoping matters even outside
  vendor pricing — the same logic applies to internal build-vs-buy and
  cost-attribution decisions for in-house agents.
- **Chapter 04 (Production patterns & cost management)**: Add Claim 6 (a
  single agent generating a large conditional script in place of many
  separate agent invocations) as a concrete, named cost-minimization tactic
  for repetitive multi-target tasks, citing this note alongside the
  identical mechanism in `blog-sourcegraph-preston-agentic-batch-changes.md`
  Claim 5 as two independent statements of the same architecture from the
  same company (not two independent data points).
- **Chapter 02 or 08 (whichever covers large-scale migration/maintenance
  patterns)**: Add Claim 4's diagnosis (large migrations stall due to
  stakeholder-management coordination cost and inability to prove
  completion, not due to diff-writing difficulty) as a named failure mode
  that motivates *why* teams reach for cross-repo orchestration tools in
  the first place — this is a sharper framing than "AI helps write code
  faster" for explaining the actual bottleneck these tools target.

## Extraction Notes

- The blog post is served by the same SvelteKit-hydrated Sourcegraph blog
  platform noted in `blog-sourcegraph-preston-agentic-batch-changes.md`.
  Unlike that note's experience (initial WebFetch 403, requiring a
  browser-User-Agent curl retry), this fetch succeeded with WebFetch on
  the first attempt but returned an AI-summarized paraphrase rather than
  verbatim text (per the Miner instructions, a WebFetch summary is not an
  acceptable source for `Quote` fields). This Miner then fetched the raw
  HTML directly via `curl` with a browser User-Agent header (HTTP 200) and
  located the complete, unhydrated article body embedded verbatim as a
  markdown string literal inside the page's SvelteKit data-loading
  `<script>` payload (the `content` field, alongside `authors:["Dan
  Adler"]` and `tags:["batch-changes","announcement","pricing"]`). This
  string was extracted directly (not paraphrased by any summarization
  model) and used as the verbatim source for every quote in this note —
  the original markdown formatting (`##` headings, `>` blockquotes) was
  preserved in the extracted string, confirming block-quote boundaries
  exactly as reproduced in Concrete Artifacts above.
- Two in-line links in the post were not followed as separate extraction
  passes: the companion launch post (already covered in depth by
  `blog-sourcegraph-preston-agentic-batch-changes.md`) and Adler's earlier
  post `sourcegraph.com/blog/owning-a-codebase` (referenced in Claim 11,
  not in this corpus — a candidate for a future separate mining pass if
  the guide wants deeper coverage of the "codebase ownership" argument).
  No YouTube embeds or other sub-pages were present on this post.
- `confidence_overall` is set to `emerging`: one claim is graded `settled`
  (Claim 1, the pricing mechanism itself, an unambiguous verifiable fact
  about the shipped product, matching the `settled` grade already given to
  the identical fact in the Preston note); the majority of claims are
  `anecdotal` marketing framing, unsourced industry comparisons, or
  first-person unaudited anecdotes (Claims 2, 3, 4, 5, 7, 9, 11); two
  claims are `emerging` first-party architecture/mechanism descriptions
  for a shipped product (Claims 6, 8). This mix — one settled fact,
  several rhetorical/strategic framing claims, no independently-audited
  quantitative evidence — is consistent with treating this note as a
  rationale/opinion companion to the more fact-dense Preston launch post
  rather than as new primary evidence in its own right.
- No contradiction issues filed; see Cross-References — Contradicts.
