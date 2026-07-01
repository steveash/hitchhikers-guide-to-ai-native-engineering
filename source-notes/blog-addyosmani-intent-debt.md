---
source_url: https://addyosmani.com/blog/intent-debt/
source_type: blog-post
title: "The Intent Debt"
author: Addy Osmani
date_published: 2026-06-05
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: emerging
issue: "#1387"
---

# The Intent Debt

> Osmani applies Margaret-Anne Storey's Triple Debt Model (technical, cognitive,
> intent) to agentic engineering, arguing that intent debt — the unwritten
> rationale for why a system is the way it is — is the one debt category agents
> cannot pay down for you, and that agents make the cost of not externalizing
> intent compound with every session and every parallel agent, rather than
> once per hire/departure as it did for human-only teams.

## Source Context

- **Type**: blog-post
- **Author credibility**: Addy Osmani spent 14+ years at Google leading developer
  experience across Chrome and, more recently, AI (Gemini, coding agents,
  agentic engineering), most recently as a Director at Google Cloud AI. He is
  already a top-cited corpus source via `blog-addyosmani-code-agent-orchestra.md`
  and `blog-osmani-good-spec.md`. This post is a synthesis/framework piece, not
  an experiment report — his credibility here is for pattern-naming and
  cross-post consistency, not controlled evidence.
- **Scope**: Defines the Triple Debt Model and intent debt specifically; argues
  why agents cannot substitute for un-externalized intent; describes the
  economics of why agentic engineering makes this debt category compound
  faster than it did with human-only teams; gives concrete symptoms and four
  paydown strategies (specs, AGENTS.md, ADRs, learning loops). Does NOT provide
  original data, a controlled study, or a citation for the "17%" comprehension
  finding referenced only via his own earlier post. Does NOT cover
  implementation mechanics for any of the four strategies beyond a sentence or
  two each — those live in his separate Good Spec and AGENTS.md posts.

## Extracted Claims

### Claim 1: Margaret-Anne Storey's Triple Debt Model splits system health into three independent categories — technical, cognitive, and intent debt
- **Evidence**: Author's framework attribution and definitions.
- **Confidence**: emerging
- **Quote**: "Technical debt lives in the code. [...] Cognitive debt lives in people. [...] Intent debt lives in artifacts. It's the absence or erosion of the externalized rationale, goals, and constraints that explain why the system is the way it is."
- **Our assessment**: The three-way split is a genuinely useful decomposition — our corpus already has strong evidence for technical debt (standard) and cognitive/comprehension debt (via the Comprehension Debt post cited as Linked Source 6 in `blog-addyosmani-code-agent-orchestra.md`, and Shopify's warning in `blog-bvp-shopify-ai-playbook.md` Claim 8). Intent debt is the missing third leg. Osmani's claim that the three are independent — "You can have low technical debt and high intent debt" — is a clarifying distinction worth keeping: a clean, well-understood codebase can still have zero externalized rationale for its decisions.

### Claim 2: An agent cannot generate intent — it can only infer a plausible-sounding rationale from the code, which is not the same as the actual intent
- **Evidence**: Author's structural argument, with a concrete example (a 300ms debounce value).
- **Confidence**: emerging
- **Quote**: "An agent can't generate intent, because intent is the one input that has to come from you. A model can infer a plausible rationale from the code, the same way you can guess why a previous engineer did something. A guess about intent isn't the intent. The model doesn't know whether that 300ms debounce was a deliberate UX decision, a benchmark result, or a number someone typed once and never revisited. It will invent a confident-sounding reason, which is worse than admitting it doesn't know."
- **Our assessment**: This is the load-bearing claim of the post and the most concrete addition to our corpus. It names a specific failure mode — confident fabrication of rationale — that is distinct from a hallucinated fact: the model isn't wrong about what the code does, it's wrong about *why* it exists, and it states the fabrication with the same confidence as a verified answer. This should be treated as a specific, citable instance of the broader "agents fabricate plausible answers" pattern, applied narrowly to design rationale.

### Claim 3: Of the three debts, only intent debt cannot be recovered by pointing an agent at the problem — technical debt is refactorable and cognitive debt is explainable, but rationale can only be fabricated, not restored
- **Evidence**: Author's structural contrast across the three debt categories.
- **Confidence**: emerging
- **Quote**: "Of the three debts, intent debt is the only one where the agent can't bail you out. It can write the code and restore your comprehension. The why is the one thing it can only fabricate."
- **Our assessment**: This sharpens Claim 2 into a prioritization argument: if agents can pay down two of three debt categories on demand, the un-payable one deserves proportionally more deliberate investment, not less, precisely because it's the one nobody will fix for you later. This is a useful framing device for a guide chapter on debt/investment tradeoffs in agentic teams.

### Claim 4: Human-only teams tolerated high intent debt for decades because tacit knowledge transferred person-to-person over years; agents remove that transfer mechanism entirely
- **Evidence**: Author's structural argument contrasting onboarding-by-osmosis with agent statelessness.
- **Confidence**: emerging
- **Quote**: "When a new human joined a team, you didn't write everything down, because they picked up intent over time: hallway conversations, code review comments, 'oh, we don't do it that way because of an incident in 2023.' [...] Agents break that model. [...] An agent starts most sessions cold. It carries none of the tacit intent your humans built up over years."
- **Our assessment**: This is a plausible mechanistic account for why "we never wrote it down and it was fine" stops being fine once agents join. It matches the general shape of Fung's claim in `blog-anthropic-ai-native-engineering-org.md` (Claim 4) that "who wrote this" stopped being a useful question once all PRs are Claude-assisted — both describe institutional knowledge no longer accumulating in a human head that can be asked later.

### Claim 5: Un-externalized intent used to cost a team once per onboarding/departure event; with agents it is paid every session, multiplied by every agent run in parallel
- **Evidence**: Author's economic argument, extending Claim 4.
- **Confidence**: emerging
- **Quote**: "That changes the economics of not writing things down. Un-externalized intent used to cost you once in a while, at onboarding or after someone left. Now you pay it every session, multiplied by every agent you run. [...] The orchestration tax I wrote about is partly an intent-debt tax. Much of what makes managing many agents exhausting is re-supplying the intent you never wrote down."
- **Our assessment**: This is the most quantifiable-sounding claim in the post, though it has no actual measurement behind it — it's a cost-structure argument, not a benchmark. It directly extends Osmani's own "orchestration tax" concept from `blog-addyosmani-code-agent-orchestra.md`, explicitly naming intent debt as a component of that tax. We buy the direction (repeated re-supplying of context to cold-start agents is a real, observed cost in that source's WIP-limit and check-in-cadence claims) but the "multiplied by every agent" framing is asserted, not measured.

### Claim 6: Detailed specs cannot capture all implicit decisions, but that limitation is not license to write nothing down — the load-bearing decisions must still be recorded
- **Evidence**: Author's self-referential argument, explicitly revisiting his own earlier claim from the Comprehension Debt post.
- **Confidence**: emerging
- **Quote**: "I argued that detailed specs aren't a complete answer. [...] Intent debt is the complementary truth. Being unable to capture all intent is no license to capture none of it. [...] You do have to write down the why behind the choices that would be expensive to get wrong, because nobody will reconstruct those later."
- **Our assessment**: This resolves a potential tension inside Osmani's own corpus footprint (his Comprehension Debt post argues against exhaustive specs; this post could be read as arguing for exhaustive documentation) by drawing a distinction: capture load-bearing rationale selectively, not exhaustively. This directly complements `blog-osmani-good-spec.md` Claim 5 (the "curse of instructions" — adherence drops as instruction count grows): the same U-curve applies to intent capture as to spec length. Neither "document everything" nor "document nothing" is right; document what's expensive to get wrong.

### Claim 7: High intent debt shows up as a specific pattern — agents make silent behavioral changes and nobody can say whether the change was safe, because the reason for the prior behavior was never recorded
- **Evidence**: Author's three worked examples.
- **Confidence**: anecdotal
- **Quote**: "An agent 'fixes' a bug by deleting a guard clause, and nobody can say whether that guard was load-bearing or leftover, because no doc or commit message ever recorded why it was there. [...] You ask why two services talk over a queue instead of a direct call, and the honest answer is 'an agent suggested it and it seemed fine.' That answer is intent debt, already accruing interest."
- **Our assessment**: These are illustrative anecdotes, not documented incidents with sources — treat as anecdotal, not as case studies. They are useful as diagnostic examples for a guide checklist ("can you explain why this code path exists, or only what it does?") but should not be cited as if they were observed failures with attribution.

### Claim 8: Four concrete practices pay down intent debt: intent-focused specs, AGENTS.md as an intent ledger (not auto-generated config), lightweight ADRs at decision time, and a session-end learning loop that writes rationale back into the repo
- **Evidence**: Author's prescriptive list, each tied to a concrete artifact.
- **Confidence**: emerging (practitioner prescription, not evaluated)
- **Quote**: "Write the spec for the intent, not the implementation. [...] Treat AGENTS.md as your intent ledger, not your config. It's why I keep saying stop using /init. [...] Capture decisions where they happen. Lightweight decision logs (ADRs) are pure intent-debt paydown. [...] Make the learning loop write intent back down. [...] every 'we tried X and it didn't work because Y' is intent that would otherwise have lived only in your memory of a bad afternoon."
- **Our assessment**: Three of the four practices are already independently supported elsewhere in our corpus (specs: `blog-osmani-good-spec.md`; AGENTS.md as curated rather than auto-generated: the ETH Zurich finding cited via `blog-addyosmani-code-agent-orchestra.md` Claim 7; learning loops: the Self-Improving Agents Linked Source in the same note). The genuinely new framing here is naming all four as instances of one underlying discipline — externalizing intent — rather than four unrelated best practices. The ADR recommendation is the one practice not previously covered in our corpus in this form.

### Claim 9: Software's scarce resource shifted from the ability to produce correct implementation (now cheap) to intent (the one input that must still originate with a human)
- **Evidence**: Author's closing economic argument.
- **Confidence**: emerging
- **Quote**: "AI made code cheap, and comprehension is recoverable. Intent, the goals and constraints and reasons, is the one input that still has to originate with a human. [...] Write down the why, because it's becoming the most valuable thing you can leave in the repo."
- **Our assessment**: This is a values-reframing claim rather than an empirical one — it asserts what "the most valuable thing" is without a measurement of value. Directionally consistent with the corpus's existing bottleneck-shift convergence (Osmani's own "verification, not generation" thesis; Fung's identical claim in `blog-anthropic-ai-native-engineering-org.md` Claim 1; Shopify's code-review bottleneck in `blog-bvp-shopify-ai-playbook.md`), which together establish that human effort in AI-native teams concentrates on judgment/rationale rather than code production. Intent debt is a plausible fourth data point in that same convergence, framed at the level of "what should the human write down" rather than "what should the human review."

### Claim 10: Comprehension debt and intent debt are complementary, not overlapping, warnings — one says don't trust the code is correct, the other says don't trust the reason survives because the code does
- **Evidence**: Author's explicit distinction between his two posts.
- **Confidence**: emerging
- **Quote**: "Comprehension debt warns you not to trust that code is correct because it exists. Intent debt warns you not to trust that the reason survives because the code does. Code is the answer; the intent was the question it was meant to solve."
- **Our assessment**: This is a clean, quotable distinction that resolves how the guide should relate the two concepts if both are cited: they are not two names for the same risk, they are two independent risks that both increase as agent-generated code volume grows. Useful for a guide section that wants to introduce both debts without implying redundancy.

## Concrete Artifacts

```
Triple Debt Model (Margaret-Anne Storey, applied by Osmani to agentic engineering)
  Technical debt  — lives in the code (implementation shortcuts, tangled modules)
  Cognitive debt  — lives in people (erosion of shared understanding; Osmani's
                     "comprehension debt")
  Intent debt     — lives in artifacts (absent/eroded externalized rationale,
                     goals, constraints)

Four intent-debt paydown practices (Osmani, "The Intent Debt", June 2026):
  1. Write the spec for the intent, not the implementation
     (goals, constraints, non-negotiables, explicit definition of done)
  2. Treat AGENTS.md as an intent ledger, not auto-generated config
     ("stop using /init")
  3. Capture decisions where they happen — lightweight ADRs
  4. Make the session-end learning loop write intent back into the repo
     (root causes of failed approaches, not just successful patterns)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-ai-native-engineering-org.md` (Claim 4): Fung's observation
    that "who wrote this" stopped being a useful question once PRs are
    Claude-assisted matches Osmani's claim that agents carry none of the tacit
    intent humans built up over years — both describe the same mechanism
    (institutional knowledge no longer accumulating in a queryable human head)
    from different vantage points (Fung: org practice; Osmani: framework).
  - `blog-addyosmani-code-agent-orchestra.md` (Claim 7, on the ETH Zurich
    finding that auto-generated AGENTS.md hurts while developer-written files
    help): directly supports Claim 8 here ("AGENTS.md as intent ledger, not
    config" / "stop using /init") with independent quantitative backing from
    the same corpus.
  - `blog-fowler-fragments-2026-06-02.md` (Claims 7–8, Pavel Voronin's
    "generative debt"): a parallel, independently-coined three-way debt
    taxonomy (technical/cognitive/generative rather than
    technical/cognitive/intent) published in the same window (May–June 2026).
    The two frameworks are not the same claim — generative debt is about
    LLMs reproducing bad *code patterns* as precedent; intent debt is about
    LLMs fabricating *rationale* for decisions. They are complementary risks
    from the same "code is cheap, understanding is not" moment, not
    competing definitions, so this is not filed as a contradiction.

- **Contradicts**: None identified. This post explicitly reconciles a
  potential internal tension with Osmani's own earlier Comprehension Debt
  argument (see Claim 6) rather than leaving it unresolved.

- **Extends**:
  - `blog-osmani-good-spec.md`: Claim 8's "write the spec for the intent, not
    the implementation" is the compressed restatement of the six-section
    SPEC.md template in that note; this post reframes that template as
    specifically an intent-debt paydown mechanism rather than a general
    best practice.
  - `blog-addyosmani-code-agent-orchestra.md` (Claim 5, "the bottleneck is no
    longer generation, it's verification" and the "orchestration tax"
    concept): this post explicitly names intent debt as a component of that
    orchestration tax (Claim 5 here), giving the earlier, vaguer "exhausting
    to manage many agents" observation a specific mechanism.
  - `blog-addyosmani-code-agent-orchestra.md` (Linked Source 6, "Comprehension
    Debt"): Claim 10 here is Osmani's own explicit reconciliation of how the
    two concepts relate, useful if the guide cites both.

- **Novel**:
  - The Triple Debt Model attribution (Margaret-Anne Storey) and the specific
    naming of "intent debt" as the third category are new to the corpus —
    no existing note names this framework.
  - The claim that agent-generated rationale is fabrication rather than
    inference-with-uncertainty (Claim 2's confident-sounding-reason framing)
    is a specific, citable mechanism not previously stated this precisely in
    the corpus.
  - The ADR-at-decision-time recommendation (Claim 8) as an intent-debt
    paydown practice is not covered by any existing corpus note in this
    framing.

## Guide Impact

- **Chapter 00 (Principles)**: Add intent debt as a named third debt category
  alongside the existing verification-over-generation principle, citing this
  source directly. The guide's principles section should distinguish
  technical debt (code), comprehension/cognitive debt (people), and intent
  debt (artifacts) as three independent axes teams should track separately,
  using Claim 1's independence argument as the justification for treating
  them as distinct rather than folding intent debt into "documentation" as a
  generic catch-all.

- **Chapter 02 (Harness Engineering)**: Reframe the existing AGENTS.md
  guidance (currently framed around the ETH Zurich auto-generation findings
  in `blog-addyosmani-code-agent-orchestra.md`) with Claim 8's "intent
  ledger, not config" framing as the *why* behind writing AGENTS.md by hand.
  Add lightweight ADRs as a recommended companion artifact for load-bearing
  decisions, citing Claim 8 — this is not currently covered by any existing
  Ch02 content.

- **Chapter 04 (Context Engineering)**: Add Claim 6's resolution of the
  spec-completeness tension (specs can't capture everything, but that's not
  license to capture nothing — capture what's expensive to get wrong) as an
  explicit companion to the existing "curse of instructions" U-curve from
  `blog-osmani-good-spec.md`. Both claims describe the same shape of tradeoff
  (too little and too much are both failure modes) applied to different
  artifacts (spec length vs. intent-capture completeness).

- **Chapter 05 (Team Adoption)**: Cite Claim 5 (orchestration tax as
  partly an intent-debt tax) when discussing WIP limits and check-in cadence
  for multi-agent setups from `blog-addyosmani-code-agent-orchestra.md` —
  this source provides the mechanism (re-supplying un-externalized intent
  every session) behind why managing many agents is exhausting, strengthening
  rather than just restating that earlier claim.

## Extraction Notes

- Fetched the full article twice: once via WebFetch (AI-summarized) and once
  by downloading the raw HTML directly (`curl`) and stripping tags, to verify
  every quote used here against the unprocessed source text. All quotes above
  were checked against the raw HTML extraction, not the WebFetch summary.
- No sub-pages were followed. The post links to the author's O'Reilly book
  ("Beyond Vibe Coding") as a call-to-action, which is a book promotion, not
  a substantive linked source, so it was not fetched.
- The "17% lower comprehension" figure Osmani references elsewhere is not
  repeated in this post; it lives in his separate Comprehension Debt post
  (already captured as Linked Source 6 in `blog-addyosmani-code-agent-orchestra.md`)
  and was not re-verified here since this post does not cite it directly.
- No contradiction with existing corpus notes was found that would warrant
  filing a contradiction issue (see Cross-References → Contradicts).
- The post is a synthesis/framework piece with no original data, benchmark,
  or citation beyond the Storey attribution (no link or paper reference for
  the Triple Debt Model was given in the post itself — treat the attribution
  as Osmani's characterization, not a verified citation of Storey's original
  work).
