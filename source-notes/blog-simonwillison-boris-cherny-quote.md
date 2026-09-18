---
source_url: https://simonwillison.net/2026/Sep/11/boris-cherny/
source_type: blog-post
title: "A quote from Boris Cherny"
author: Simon Willison (quoting Boris Cherny, Head of Claude Code, Anthropic, via Twitter/X)
date_published: 2026-09-11
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: emerging
issue: "#3526"
---

# A quote from Boris Cherny

> A single-paragraph quotation post — Simon Willison reproducing a Twitter/X
> post from Boris Cherny (Head of Claude Code) stating that Claude-written
> production code at Anthropic must clear a *higher* bar than human-written
> code, and naming the specific guardrail stack that enforces it: lint
> rules, tests, Claude-driven end-to-end tests, daily Claude-powered
> fuzzing, automated code and security review, and automated refactoring.

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — a single
  blockquote plus a one-line citation, ~90 words total). Auto-discovered via
  the `simon-willison` trusted feed. The `blockquote`'s `cite` attribute
  points directly to Cherny's original Twitter/X post
  (`twitter.com/bcherny/status/2098217573276131577`); Willison adds no
  original commentary of his own — the entire page is the quote, its
  citation link, and standard site chrome (tags, date, "Recent articles").
- **Author credibility**: Boris Cherny is Head of Claude Code at Anthropic.
  This corpus already establishes his role and treats him as a
  first-party, on-the-record source for Claude Code / Anthropic engineering
  practice: `blog-anthropic-code-w-claude-london-2026.md` (his keynote,
  citing him as "Head of Claude Code") and `guide/01-daily-workflows.md`
  (his reported 15+ parallel background-agent sessions). This quote is
  first-person testimony from the person who leads the team building the
  tool it describes, about that same team's own internal practices — high
  authority for *what Anthropic does*, but it is a single social-media post
  with no supporting data, incident detail, or methodology description
  attached; Willison is a `trusted-feed` curator, not an independent
  verifier of the claim's substance.
- **Scope**: States a one-sentence principle (Claude-written production code
  should be held to a higher bar than human-written code) and names six
  guardrail categories Anthropic uses to enforce it. Does NOT explain how
  any guardrail is implemented, does not give adoption dates, team scope
  (all of Anthropic vs. just the Claude Code team), pass/fail rates, cost,
  or any example of the guardrails catching (or missing) a real bug. It is
  a compressed summary claim, not a methodology writeup.

## Extracted Claims

### Claim 1: Production code written by Claude should be held to a higher quality bar than code written by a human
- **Evidence**: Cherny's own stated principle, as the opening sentence of
  his post.
- **Confidence**: emerging (a named practitioner's stated operating
  principle for his own organization, not an industry-wide claim or a
  benchmarked outcome)
- **Quote**: "Production code written by Claude should have a higher bar than if it was written by a human."
- **Our assessment**: This inverts a common lower-trust framing of AI-generated code (treat it with *extra* suspicion, therefore review it *harder*) into a standard-setting claim: the code itself should be engineered to a *higher* bar, not merely reviewed more skeptically. This is consistent with — and gives a named-principle framing to — the general corpus thesis that verification effort must scale with agent-generated volume (e.g. `blog-addyosmani-agentic-code-quality.md` Claim 1), but Cherny's framing is about the target bar for the code, not just the review process around it.

### Claim 2: Anthropic enforces this higher bar with "many guardrails," including a baseline of extensive lint rules and tests
- **Evidence**: Cherny's own enumerated list, introduced as the mechanism
  for the Claim 1 principle.
- **Confidence**: emerging (named practitioner list, no counts or specific
  tool names given for lint/test coverage)
- **Quote**: "At Anthropic, we have many guardrails in place to make sure this is happening: lots of lint rules, lots of tests,"
- **Our assessment**: "Lots of lint rules, lots of tests" is the least novel item in the list — it restates a baseline already well documented elsewhere in the corpus (e.g. `blog-addyosmani-agentic-code-quality.md` Claim 2's "quality gates" taxonomy). Its value here is narrower: confirming that Anthropic's own internal practice for its own flagship product matches the general industry guidance the corpus already recommends, rather than departing from it.

### Claim 3: Claude-driven end-to-end tests are a named guardrail in Anthropic's production pipeline
- **Evidence**: Named item in Cherny's guardrail list.
- **Confidence**: anecdotal (named once, no description of scope, trigger
  frequency, or what "Claude-driven" means operationally — e.g., whether
  Claude authors the E2E tests, executes them, or both)
- **Quote**: "Claude-driven end to end tests,"
- **Our assessment**: This is a genuinely thin data point — three words with no elaboration — but it is a distinct claim from ordinary "tests" in the same sentence, implying Anthropic treats agent-authored/agent-run E2E coverage as a separate, named guardrail category rather than folding it into generic "tests." `blog-anthropic-claudecode-quality-postmortem.md` Claim 7 independently confirms Claude Code has "E2E tests" as one of its verification layers, though that source documents a case where E2E tests (among other layers) *failed* to catch a real production bug — see Cross-References.

### Claim 4: Claude-powered fuzzers run daily as a named guardrail
- **Evidence**: Named item in Cherny's guardrail list.
- **Confidence**: anecdotal (named once, no target codebase, bug-yield, or
  crash-count data given — contrast with the more detailed fuzzing account
  in Claim 9 of the cross-referenced Sumner interview, which does give a
  number for a specific project)
- **Quote**: "Claude-powered fuzzers running daily,"
- **Our assessment**: The "running daily" cadence is the most concrete operational detail in the entire quote — it specifies a fixed schedule rather than an ad hoc or pre-release-only practice. This corroborates `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 9, where Jarred Sumner (also Anthropic) describes "24/7 coverage-guided fuzzing across all Bun parsers" using Claude-written fuzzers for the Bun Rust rewrite — two independent Anthropic-adjacent accounts both describing continuous/scheduled (not one-off) Claude-driven fuzzing as a standing practice, not a single project's one-time hardening pass.

### Claim 5: Automated code reviews and automated security reviews are both named as guardrails, distinct from lint/test coverage
- **Evidence**: Named items in Cherny's guardrail list.
- **Confidence**: anecdotal (named once, no description of what the
  automated reviewer checks for, its acceptance/rejection criteria, or
  whether a human review step remains downstream of it)
- **Quote**: "automated code reviews and security reviews,"
- **Our assessment**: This directly corroborates two separate, more detailed corpus sources: `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 8, where Sumner (also Anthropic) states Claude's automated code review "catches bugs that would take me an hour of closely reading the code to figure out" (with an explicit cost caveat), and `blog-anthropic-llms-secure-source-code.md`, Anthropic's own detailed six-step methodology for AI-driven security review/vulnerability discovery. Cherny's one-clause mention is consistent with, but far less detailed than, either of those — it confirms the practice is standard enough to be named in a single breezy list rather than needing its own explanation.

### Claim 6: Automated code refactoring is named as a guardrail, alongside review, testing, and fuzzing
- **Evidence**: Named item in Cherny's guardrail list.
- **Confidence**: anecdotal (named once, no description of trigger
  conditions, scope, or what "automated" means here — e.g., agent-initiated
  vs. tool-driven mechanical refactoring)
- **Quote**: "automated code refactoring, and so on."
- **Our assessment**: This is the only item in the list that is about improving existing code shape rather than catching defects — the other five (lint, tests, E2E tests, fuzzing, review) are detection mechanisms, while refactoring is a maintenance/prevention mechanism. `blog-google-go-ai-assisted-engineering.md` Claim 13 gives the most concrete corpus example of what "automated refactoring at scale, safe enough for agents to invoke directly" can look like (Go's `gopls` and `go fix` modernizers) — Cherny's mention confirms Anthropic treats this as a standing guardrail category too, though without naming any specific tool. The trailing "and so on" signals the list is illustrative, not exhaustive.

### Claim 7: Without these guardrails, Claude-generated code accumulates into a codebase that is hard to maintain
- **Evidence**: Cherny's own stated consequence, as the closing sentence of
  his post.
- **Confidence**: anecdotal (a stated belief/warning, not a documented
  incident or before/after comparison)
- **Quote**: "Without these, you can end up with a mess that is hard to maintain down the line."
- **Our assessment**: This is the stated rationale for Claim 1's "higher bar," but it is asserted, not evidenced — no incident, metric, or specific "mess" is described. It is directionally consistent with `blog-addyosmani-agentic-code-quality.md` Claim 4's related but distinct point that agent failures often stem from the *same* environmental weaknesses that already cause human engineers to ship bad code (brittle environments, weak tests) — both frame the risk as a maintainability failure mode requiring proactive environmental/process investment, not an inherent flaw specific to AI-written code as such.

## Concrete Artifacts

```
Source: twitter.com/bcherny/status/2098217573276131577, reproduced verbatim
by simonwillison.net/2026/Sep/11/boris-cherny/ (raw HTML blockquote,
confirmed character-for-character by this Miner via direct curl fetch of
the Willison page)

Full quote:
"Production code written by Claude should have a higher bar than if it was
written by a human. At Anthropic, we have many guardrails in place to make
sure this is happening: lots of lint rules, lots of tests, Claude-driven
end to end tests, Claude-powered fuzzers running daily, automated code
reviews and security reviews, automated code refactoring, and so on.
Without these, you can end up with a mess that is hard to maintain down
the line."

Named guardrail list (six items, as enumerated in the quote):
  1. Lint rules ("lots of")
  2. Tests ("lots of")
  3. Claude-driven end-to-end tests
  4. Claude-powered fuzzers (cadence: daily)
  5. Automated code reviews and automated security reviews
  6. Automated code refactoring
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 8 (Jarred
    Sumner, Anthropic: Claude's automated code review "catches bugs that
    would take me an hour of closely reading the code to figure out," with
    an explicit cost caveat) and Claim 9 (11 runs of the Claude Security
    Scanner plus Claude-written parser fuzzers on the Bun Rust rewrite,
    independently corroborated there against `blog-pragmaticengineer-bun-rust-rewrite.md`'s
    "24/7 coverage-guided fuzzing" figure): this note's Claims 4 and 5 are a
    second, independent Anthropic-insider naming the same two practices
    (Claude-driven fuzzing on a cadence; automated code/security review) as
    standing guardrails, not one-off hardening measures for a single
    project.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 1 (verification,
    code review, and security replaced code-writing as the primary
    bottleneck at Anthropic once agentic coding became the default) and
    Claim 6 (code review has bifurcated — Claude handles style, linting,
    bug-catching, test addition; humans retain domain/legal/security
    judgment): this note's Claim 1 (higher bar for Claude-written code) and
    Claim 2 (lint/test baseline) are consistent with that bifurcation —
    Cherny's list names exactly the categories (lint, tests, review) that
    source attributes to Claude's side of the split.
  - `blog-anthropic-llms-secure-source-code.md` (Anthropic's own six-step
    find-and-fix vulnerability research loop, used to disclose 1,596
    vulnerabilities as of May 2026): this note's Claim 5 ("automated ...
    security reviews") names the practice category; that source is the
    detailed methodology behind it, from the same organization.
  - `blog-google-go-ai-assisted-engineering.md` Claim 13 (Go's `gopls` and
    `go fix` modernizers provide deterministic, agent-safe refactoring at
    scale): the most concrete corpus example of what this note's Claim 6
    ("automated code refactoring") names only abstractly for Anthropic's
    own (unspecified) tooling.

- **Contradicts**: No contradiction issue filed. One in-corpus tension is
  worth flagging for the Assayer rather than treated as a genuine
  contradiction: `blog-anthropic-claudecode-quality-postmortem.md` Claim 7
  documents a case where "human code review, automated code review, unit
  tests, E2E tests, and dogfooding all failed to catch" a real production
  bug in Claude Code itself — i.e., the same guardrail categories this
  quote names (automated code review, E2E tests) did not, in that instance,
  prevent a shipped regression. This does not rise to a MINER.md §4a
  contradiction: Cherny's claim is that these guardrails are necessary to
  avoid "a mess... down the line," not that they are sufficient or
  infallible against any single bug, and the postmortem source itself
  describes process changes added *after* the gap (more ablation testing,
  per-model evals) rather than disputing the value of the existing
  guardrails. Flagged here as useful counterweight context: this quote's
  guardrail list should not be read by the guide as a guarantee of defect
  prevention.

- **Extends**: `blog-addyosmani-agentic-code-quality.md` Claim 2 (the
  general "quality gates" taxonomy: unit/property/acceptance tests,
  mutation testing, code-quality metrics, type safety, security scanning,
  linter-enforced architecture rules) — this note supplies a named,
  first-party account of what that taxonomy looks like in practice at one
  specific, high-profile AI lab, adding two items (Claude-driven E2E tests,
  daily Claude-powered fuzzing) not named in that more abstract framework
  piece, and a specific cadence ("running daily") that Osmani's post does
  not attach to any gate.

- **Novel**:
  - The explicit "higher bar than human-written code" framing (Claim 1) —
    as a stated target for the code's quality, not merely a stated policy
    for reviewing it more skeptically — is new phrasing to this corpus,
    though consistent in spirit with the existing verification-scaling
    thesis.
  - "Claude-powered fuzzers running daily" (Claim 4) is the first corpus
    mention of a *fixed, named cadence* for AI-driven fuzzing as a standing
    practice, rather than a one-time hardening pass tied to a specific
    rewrite or release (contrast the Bun Rust rewrite's fuzzing, which was
    a bounded post-merge hardening effort for one project).
  - Naming "automated code refactoring" as a peer guardrail category
    alongside review, testing, and security scanning (Claim 6) — most
    corpus sources on refactoring discuss it as a language/ecosystem
    tooling capability (e.g. Go's modernizers) rather than as a named item
    in an enumerated production guardrail list.

## Guide Impact

- **Chapter 03 (Verification)**: Add Claim 1's "higher bar than if it was
  written by a human" as a named, quotable principle from Anthropic's Head
  of Claude Code, framing the goal of verification infrastructure as
  raising the target quality bar for agent-written code, not merely adding
  scrutiny. Pair with the existing three-lever framework from
  `blog-addyosmani-agentic-code-quality.md` Claim 10 (scale verification /
  throttle generation / lower the bar) as a real-world instance of choosing
  "scale verification" rather than "lower the bar."

- **Chapter 06 (Security)**: Add "Claude-powered fuzzers running daily" and
  "automated ... security reviews" (Claims 4–5) as a named, first-party
  example of continuous (not release-gated) AI-driven security tooling,
  citing this source alongside the more detailed methodology in
  `blog-anthropic-llms-secure-source-code.md` and the independent
  corroboration in `blog-pragmaticengineer-orosz-inside-anthropic.md`
  Claim 9.

- **Chapter 02 (Harness Engineering)**: When listing what a production
  agentic-coding harness's guardrail layer should include, add "automated
  code refactoring" (Claim 6) as a distinct, named category — most existing
  guide material frames refactoring as a manual or occasional activity
  rather than a standing, automated guardrail alongside tests and review.

## Extraction Notes

1. **Source is a single ~90-word quotation post with no companion links to
   follow**: unlike other Willison "quotation" posts in this corpus (e.g.
   `blog-simonwillison-akshat-bubna-quote.md`, which linked to a companion
   Willison analysis post and, through it, primary technical documents),
   this page contains no body commentary from Willison and no secondary
   links beyond the `cite` attribute pointing directly at Cherny's original
   Twitter/X post and the site's standard "Recent articles" navigation
   (unrelated posts). There was no substantive secondary page to follow per
   MINER.md §1.
2. **Original tweet not independently fetchable**: this Miner attempted to
   fetch `twitter.com/bcherny/status/2098217573276131577` directly via
   `curl` to check for additional thread context (replies, a follow-up
   tweet) beyond what Willison quoted. Twitter/X returned a 200 status but
   a client-rendered JavaScript SPA shell with no `og:description` or
   readable text content in the raw HTML — consistent with Twitter/X
   blocking unauthenticated/non-JS scraping. The claims in this note are
   therefore sourced entirely through Willison's blockquote reproduction,
   which this Miner did independently verify character-for-character
   against the raw HTML of Willison's own page (not merely trusting
   WebFetch's summary of it).
3. **Claim count below MINER.md's "5-15" guideline, deliberately**: this
   note extracts 7 claims, at the low end of the suggested range, because
   the entire source is one paragraph with six named guardrail items plus
   an opening principle and a closing consequence — there is no additional
   substantive content to extract without inventing detail the source does
   not contain. Splitting the six-item guardrail list into one claim per
   named practice (rather than one combined claim) is what keeps the count
   at 7 rather than 3; further subdivision would not add information.
4. **`confidence_overall` set to `emerging`**: the overarching principle
   (Claim 1) and the fact that Anthropic uses *some* guardrail stack
   (Claim 2) are named-practitioner, on-record claims about the speaker's
   own organization — a credible but single-source, unelaborated account.
   Most individual guardrail-item claims (3–6) are capped at `anecdotal`
   individually, since each is named only once with no supporting detail;
   `emerging` for the note overall reflects that several items (fuzzing,
   automated review) do have independent, more detailed corroboration
   elsewhere in the corpus (see Cross-References), which a single
   `anecdotal` rating for the whole note would understate.
