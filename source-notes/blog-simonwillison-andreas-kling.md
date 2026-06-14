---
source_url: https://simonwillison.net/2026/Jun/5/andreas-kling/
source_type: blog-post
title: "Quoting Andreas Kling"
author: Andreas Kling (Ladybird browser creator), quoted by Simon Willison
date_published: 2026-06-05
date_extracted: 2026-06-14
last_checked: 2026-06-14
status: current
confidence_overall: anecdotal
issue: "#1173"
---

# Quoting Andreas Kling: Ladybird Stops Accepting Public Pull Requests

> Andreas Kling announces that Ladybird will no longer accept public pull requests,
> grounding the policy in an accountability-not-detection argument: the old
> proxy (substantial patch effort = good faith) no longer holds in the AI era, so the
> project now requires that the people who introduce code are the same people who
> decided it belongs and who will answer for the consequences.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, "quotation" format — Willison
  posted an excerpt from Andreas Kling's announcement at
  https://ladybird.org/posts/changing-how-we-develop-ladybird/, published 2026-06-05,
  with tags: open-source, ai, generative-ai, llms, andreas-kling, ladybird, ai-ethics.
  The original Ladybird blog post was followed and read as a linked page per MINER.md §1.)
- **Author credibility**: Andreas Kling is the creator of the Ladybird browser and a key
  figure in the SerenityOS / Ladybird open-source project. He speaks as the project lead
  announcing a structural governance decision for a high-stakes application (a browser that
  runs untrusted web content on real users' machines). Simon Willison is one of the highest-
  signal LLM tooling commentators on the web; his selection of this passage for his
  link-blog signals its relevance. The original announcement appeared on the official
  Ladybird project blog.
- **Scope**: Covers Ladybird's decision to close the public PR channel, the rationale
  (the effort-as-good-faith-proxy assumption broke down under AI), the accountability
  framing, and the policy specifics (no alternative intake path for external patches).
  Does NOT cover: internal Ladybird review processes, how many open PRs were closed,
  implementation timeline, whether specific AI contributions triggered the decision, or
  what Kling's view is on developers using AI tools privately.

## Extracted Claims

### Claim 1: Ladybird will no longer accept public pull requests; all code changes will come from project maintainers

- **Evidence**: Andreas Kling's official announcement on the Ladybird blog, as quoted by
  Simon Willison. This is a firm policy announcement from the project lead, not a proposal.
- **Confidence**: settled (official project policy statement)
- **Quote**: "We will no longer accept public pull requests."
- **Our assessment**: This is the most structurally radical open-source governance response
  to AI contribution challenges documented in this corpus. Zig (`blog-simonwillison-zig-anti-ai.md`
  Claim 1) bans LLM-generated content specifically but continues accepting non-AI PRs.
  Ladybird closes the public PR channel entirely, making no distinction between AI-generated
  and human-generated contributions. The policy treats the accountability problem as
  unfixable through content-based filtering.

### Claim 2: The traditional "substantial effort = good faith" proxy assumption has broken in the AI era

- **Evidence**: Kling's direct statement in the Ladybird announcement, as quoted by Willison.
  The argument is that high-effort contributions were previously a reasonable screen for
  good-faith actors, but AI makes substantial-looking contributions cheap to produce,
  decoupling effort from intent.
- **Confidence**: emerging (widely observed across OSS communities but not empirically measured
  with controlled data; causal mechanism is well-grounded in AI capability)
- **Quote**: "A substantial patch used to imply substantial effort, and that effort was a
  reasonable proxy for good faith. That assumption no longer holds."
- **Our assessment**: This is the key diagnostic claim in the announcement — it names precisely
  what changed and why the old governance model breaks. The "proxy" framing is precise: Kling is
  not saying contributors are bad faith now, he is saying the *signal* (effort) can no longer be
  trusted as an indicator of *intent* (good faith). This logic applies beyond code contributions:
  any system that uses effort-based signals as intent proxies (application essays, proposals,
  detailed bug reports) faces the same potential collapse under AI-assisted production. The
  Ronacher post (`blog-ronacher-pi-oss.md` Claim 1) documents the same dynamic from the
  issue-description side: detailed-but-wrong AI-generated issue descriptions cause more harm
  than vague human ones precisely because the effort signal used to matter.

### Claim 3: For a browser specifically, one well-hidden vulnerability can be catastrophic, raising the accountability stakes above most software

- **Evidence**: Kling's security framing in the Ladybird announcement. A browser handles
  untrusted internet content on real users' machines — this is an established and
  well-understood threat model.
- **Confidence**: settled (this is a well-known security property of browsers, not a speculative
  claim by Kling)
- **Quote**: "A browser runs untrusted input from the entire internet on the user's machine,
  and one well-disguised vulnerability is all an attacker needs."
- **Our assessment**: Kling is providing the domain-specific amplifier for the generic
  accountability argument. Even if the effort-proxy broke, you could still accept external code
  if the downside of a bad contribution were low. For a browser, the downside of a single missed
  malicious or buggy contribution is catastrophic. This domain-specificity is important for the
  guide: Ladybird's decision is rational *given* the browser security model. Teams in lower-risk
  domains may reach different policy conclusions from the same accountability argument. The
  counterfactual is worth holding explicitly: the same reasoning applied to a documentation
  site would not justify closing the PR channel.

### Claim 4: Whether code was written by a human or an AI is beside the point; what matters is who is responsible for it

- **Evidence**: Kling's explicit reframe, as quoted by Willison. This is the core
  philosophical position that distinguishes Ladybird's policy from Zig's approach.
- **Confidence**: anecdotal (normative/philosophical position from one project lead; not
  an empirical finding)
- **Quote**: "Whether code was typed by hand is beside the point. What matters is who is
  responsible for it once it enters the browser."
- **Our assessment**: This is the sharpest divergence from Zig's approach. Zig's policy
  (`blog-simonwillison-zig-anti-ai.md`) and Kelley's detection evidence
  (`blog-simonwillison-andrew-kelley.md` Claim 1) focus on *how* code was generated.
  Kling's policy focuses on *who owns the consequences*. The two framings are complementary
  but independent: you could have a policy that bans AI contributions AND requires
  accountability, or (like Ladybird) one that requires only accountability as the
  operative gate — regardless of how the code was produced. The accountability framing
  also generalizes beyond AI: it would apply equally to a low-effort human PR from a
  contributor who does not intend to maintain the code long-term.

### Claim 5: The new policy requires that code introducers be the people who decided the changes belong in the project and who will answer for the consequences

- **Evidence**: Kling's explicit statement of the new accountability standard, quoted by
  Willison and confirmed in the Ladybird announcement.
- **Confidence**: settled (official policy statement)
- **Quote**: "The people introducing changes to it must be the people who decide those
  changes belong in the project, and who will answer for the consequences."
- **Our assessment**: This formulates the governance principle explicitly: decision-making
  authority and consequence-bearing must be held by the same person. A contributor who
  submits a PR and then disappears if it causes a regression fails this test; a contributor
  who submits, actively maintains, and defends the contribution meets it. In practice, for
  Ladybird, this means only core team members — they are the ones with sustained project
  ownership. This is a more principled framing than "we can't screen AI contributions."
  It articulates the property the project actually needs from any contributor, AI-assisted
  or not.

### Claim 6: The project will not treat external forks or patch dumps as a review queue for upstream Ladybird

- **Evidence**: Kling's announcement from the Ladybird blog, addressing the obvious
  workaround to the PR ban.
- **Confidence**: settled (explicit policy statement)
- **Quote**: "External code can of course exist under the terms of the license, but we
  will not treat forks or patch dumps as a review queue for upstream Ladybird."
- **Our assessment**: This preempts the workaround of publishing fork patches and
  asking maintainers to pull from them. The open-source license still permits forks and
  derivatives — the policy is specifically that Ladybird's maintainers will not process
  them as a contribution intake path. This is a significant signal of scope: the project
  is not moving to a proprietary model, but it is actively declining to serve as a review
  service for external code, regardless of how that code is submitted.

### Claim 7: Non-code participation — bug reports, testing, standards discussion, security reports — remains welcome

- **Evidence**: From the Ladybird announcement (summarized from the original source; specific
  sentence could not be verified verbatim via WebFetch).
- **Confidence**: emerging (confirmed in substance from source summary; exact wording not
  independently verified character-for-character)
- **Quote**: (no direct verbatim quote available; see Our assessment)
- **Our assessment**: The distinction matters because it shows the policy is not a withdrawal
  from the open-source community — it is specifically closing the *code contribution* path
  while keeping other collaboration channels open. Ladybird still needs people to find bugs,
  test the browser, participate in standards bodies, and report security vulnerabilities.
  These contribution types are not affected by the accountability problem Kling identifies,
  because they do not involve code entering the codebase under ambiguous ownership.

### Claim 8: The policy is driven by Ladybird's maturity as a project shipping to real users, not just a policy shift about AI specifically

- **Evidence**: Kling's own framing of why the policy change is happening now, as quoted
  by Willison.
- **Confidence**: anecdotal (one project lead's stated rationale)
- **Quote**: "Ladybird is becoming a browser for real users. The people introducing changes
  to it must be the people who decide those changes belong in the project, and who will
  answer for the consequences."
- **Our assessment**: This adds a temporal dimension: the accountability requirement is not
  just about AI — it is about the project maturing to a stage where real user security is
  at stake. AI lowered the cost of contributions at the same time Ladybird's requirements
  for contribution accountability increased. The two trends compounded: more low-accountability
  contributions arriving precisely when the cost of one getting through became higher. For
  AI-native teams, the implication is that governance strictness should scale with production
  risk. A side project or experimental tool can tolerate more contribution-source ambiguity
  than a browser handling real users' web traffic and credentials.

## Concrete Artifacts

### The Core Policy Statement (from the Willison blockquote, verbatim with Willison's [...] ellipses)

```text
Source: Andreas Kling, https://ladybird.org/posts/changing-how-we-develop-ladybird/ (2026-06-05)
As quoted at: https://simonwillison.net/2026/Jun/5/andreas-kling/

"We will no longer accept public pull requests. [...] A substantial patch used to imply
substantial effort, and that effort was a reasonable proxy for good faith. That assumption
no longer holds. [...] Whether code was typed by hand is beside the point. What matters is
who is responsible for it once it enters the browser. Ladybird is becoming a browser for
real users. The people introducing changes to it must be the people who decide those
changes belong in the project, and who will answer for the consequences."
```

### Ladybird's Accountability Governance Model

```text
Source: Andreas Kling, https://ladybird.org/posts/changing-how-we-develop-ladybird/ (2026-06-05)

Pre-AI-era contribution model (old assumption):
  - External contributors submit PRs
  - Substantial patch effort → reasonable good-faith proxy → acceptable review risk
  - Maintainers review and accept or reject

Post-AI governance model (effective 2026-06-05):
  - All code changes from project maintainers only
  - No public PR intake
  - No alternative patch submission via issues, email, or forks
  - External forks permitted under license; not treated as upstream review queue
  - Non-code participation still welcomed:
    * Bug reports
    * Testing
    * Standards discussion
    * Security reports

Core principle: Co-decision and co-accountability must be held by the same person.
The person introducing a change must be the one who decided it belongs AND who will
answer for its consequences.
```

## Cross-References

- **Corroborates**: `blog-simonwillison-zig-anti-ai.md` Claim 4 — "LLM-assisted PRs break
  the contributor-development investment loop even when the code is technically correct."
  Kling's policy arrives at similar structural outcome (closing PR intake) by a different
  path: Zig's reasoning focuses on the reviewer not learning about the human contributor;
  Kling's reasoning focuses on the missing accountability for code once merged. Both diagnose
  the same breakage (contribution model assumptions fail with AI) but frame the problem
  differently. Together they show that the AI-contribution governance problem has more than
  one defensible policy response, each grounded in a distinct theory of what good contributions
  are for.

- **Corroborates**: `blog-ronacher-pi-oss.md` Claim 13 — "AI has not increased the number
  of people who need software, or the number of maintainers who can review it. It has mostly
  increased the amount of code and the number of projects competing for attention." Kling's
  policy is a structural response to exactly this asymmetry: rather than trying to scale
  review capacity to match increased PR volume, Ladybird eliminates the external PR channel
  entirely.

- **Extends**: `blog-simonwillison-andrew-kelley.md` Claim 1 — "It's a common misconception
  that we can't tell who is using LLM and who is not." Kelley's detection evidence suggests
  that with sufficient reviewer experience, AI-generated PRs can be identified. Kling's policy
  goes further: even with reliable detection capability, the accountability problem remains —
  a human who submits an AI-generated PR they do not fully understand is still not accountable
  in the way Kling requires. Detection-based screening (Kelley/Zig) and accountability-based
  screening (Kling/Ladybird) are complementary mechanisms addressing different failure modes.
  A project might use both; Ladybird chose to bypass the detection question entirely by
  restructuring who can contribute.

- **Extends**: `blog-simonwillison-zig-anti-ai.md` Claim 9 — "Practical LLM-assisted OSS
  contributions caused concrete operational harm to the Zig project before the ban." Kling's
  announcement is a second high-profile systems-programming project making a structural policy
  change in response to AI-era contribution quality concerns (the first being Zig's CoC ban).
  Both are projects where security and correctness requirements are extremely high. Together
  they document an emerging pattern: security-critical OSS projects are responding to AI
  contribution challenges with governance restructuring rather than improved review tooling.

- **Extends**: `blog-ronacher-pi-oss.md` Claim 8 — Pi's 90-day tracker data (79% auto-close
  rate, 8% merge rate for new-contributor PRs). Ronacher's data quantifies the volume problem
  that motivates Kling's decision. Ladybird's response is more radical than Pi's (Pi auto-closes
  and selectively re-opens; Ladybird closes the intake channel entirely), but both are responses
  to the same underlying dynamic: high external contribution volume, low signal-to-noise, high
  review cost.

- **Novel**:
  - **Accountability-not-detection framing**: No existing corpus note frames the AI
    contribution problem as primarily an *accountability* problem rather than a *quality*
    or *detection* problem. Kling's "what matters is who is responsible" framing is entirely
    new to the corpus. It represents a third governance response alongside Zig's content-based
    ban (`blog-simonwillison-zig-anti-ai.md`) and Pi's volume-based auto-close
    (`blog-ronacher-pi-oss.md`).
  - **Co-decision and co-accountability as the operative standard**: The specific requirement
    that code introducers must also be the people who decided the code belongs and who will
    answer for consequences — combined decision-making authority and consequence-bearing — is
    not documented in any other corpus note. It is a governance principle that transcends AI:
    it would also exclude low-accountability human contributors who are not invested in the
    project's long-term outcomes.
  - **Effort-proxy collapse as the diagnostic claim**: While the AI volume problem is documented
    elsewhere (Ronacher, Zig), Kling's precise framing of *why* it matters specifically —
    that effort used to function as a good-faith proxy, and AI breaks that proxy — is new to
    the corpus. This is more mechanistic and precise than "AI contributions flood OSS projects."
  - **Domain-specific risk amplification**: The argument that browser security amplifies the
    accountability stakes to the point where a radical governance response is justified is a
    new pattern. No other corpus note makes the domain-risk-amplifier argument: that the
    same accountability failure mode justifies different policy responses depending on the
    production risk of the artifact being contributed to.

## Guide Impact

- **Chapter 03 (Safety and Verification — or chapter discussing code review under AI)**: Claim 4
  ("Whether code was typed by hand is beside the point. What matters is who is responsible.")
  should be cited as the accountability-based alternative to detection-based governance. Currently
  the guide likely discusses AI contribution detection (per Kelley) and content-based bans (per
  Zig). Kling's framing adds a third option: restructure the contribution model around
  accountability rather than attempting to filter contributions by origin. For internal teams,
  this reframes AI governance from "are we catching AI-generated code?" to "do we have clear
  ownership of every code change?"

- **Chapter 05 (Team Adoption) / governance section**: Claims 1 and 5 together should anchor
  guidance on AI contribution governance choices. The contrast between Zig's approach (ban AI
  contributions specifically) and Ladybird's approach (require accountability, close PR channel
  entirely) gives teams a principled framework: if you can reliably screen for AI (Kelley's
  detection evidence), you can take the Zig approach; if you cannot, or if accountability is
  the real requirement, the Ladybird model (require code introducers to own consequences) is
  the structural alternative. Most commercial teams will find a middle path, but the Ladybird
  principle — co-decision and co-accountability — is applicable even in contexts where the PR
  channel stays open.

- **Chapter 06 (Community / Open Source impact)**: This source is a primary case study for
  the guide's treatment of AI's impact on OSS contribution models. The triage note correctly
  identifies this as a "precedent-setting governance decision" from a high-visibility project
  (browser engine). Ladybird's policy should be presented alongside Zig's policy as contrasting
  governance responses: both cite AI as a driver, both arrive at restricted PR acceptance, but
  they diagnose differently and apply different operative tests. A comparison table would be
  useful to help practitioners reason about which approach fits their context.

- **Chapter 01/02 (Introduction / Landscape — framing what AI changes)**: Claim 2 (the
  effort-proxy collapse) should be added to any framing of "what structurally changed with AI"
  beyond raw productivity. AI does not merely speed up development; it decouples effort from
  intent, breaking the signals on which existing quality and accountability systems were built.
  This is a structural change to the incentive landscape of open-source collaboration, not a
  productivity metric.

## Extraction Notes

- The primary source (Willison's page) was fetched via WebFetch twice. Both fetches returned
  summarized content rather than full verbatim text, but the blockquote excerpt on the page
  was reproduced verbatim in the first fetch (including Willison's [...] ellipses, confirmed
  consistent across both fetches). The blockquote in the Concrete Artifacts section preserves
  this verbatim including ellipses — it is Willison's selection from the Kling announcement,
  not a full reproduction of the announcement text.
- The original Ladybird announcement at https://ladybird.org/posts/changing-how-we-develop-ladybird/
  was fetched as a follow-up linked page per MINER.md §1. WebFetch returned summarized content
  there too; additional verbatim sentences were extracted from that fetch and are noted as
  "from the Ladybird source." All Quote fields are populated only where the quoted text appeared
  verbatim (or as a clear blockquote presentation) in the WebFetch output. Claim 7, where no
  verbatim quote was reliably available, is marked accordingly.
- The Willison page is his standard "quotation" format — very brief, with the analytical payload
  entirely in the Kling excerpt. Willison adds no prose commentary of his own; the page consists
  of the blockquote and tags only (consistent with the `blog-simonwillison-andrew-kelley.md`
  extraction pattern).
- No contradiction issue filed. The Ladybird accountability model and the Zig content-ban model
  are not in contradiction — they address different aspects of the same governance problem. The
  "detection is possible" claim in `blog-simonwillison-andrew-kelley.md` is not contradicted by
  Kling's policy: detection being possible does not mean detection alone is sufficient for
  accountability. No existing corpus note takes a position that would be materially opposed to
  any of the eight claims extracted here.
- Cross-reference claim numbers verified against source notes read in full during this extraction
  session: `blog-simonwillison-zig-anti-ai.md` (Claims 4 and 9), `blog-simonwillison-andrew-kelley.md`
  (Claim 1), and `blog-ronacher-pi-oss.md` (Claims 8 and 13).
