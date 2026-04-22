---
source_url: https://simonwillison.net/2026/Apr/14/replace-token-based-csrf/
source_type: blog-post
title: "datasette PR #2689: Replace token-based CSRF with Sec-Fetch-Site header protection"
author: Simon Willison
date_published: 2026-04-14
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: anecdotal
issue: "#312"
---

# datasette PR #2689: Replace token-based CSRF with Sec-Fetch-Site header protection

> A short Simon Willison link post about a production security migration done
> with Claude Code across 10 small commits under close human guidance and
> GPT-5.4 cross-review, with Willison explicitly retaining PR description
> authorship as "an exercise in keeping myself honest."

## Source Context

- **Type**: blog-post (Simon Willison link-blog style, ~200 words of original
  commentary; links to Datasette PR #2689 at github.com/simonw/datasette/pull/2689).
  Both the blog post and the PR were read for this extraction; the PR provides the
  substantive technical and AI-authorship detail that the blog post elides.
- **Author credibility**: Simon Willison is the creator of Django, the author of
  Datasette, and one of the most widely-cited independent commentators on LLM
  tooling. He is designated a `trusted-feed` source in this repo. This post
  documents work Willison did himself on his own production open-source project —
  it is a first-person observation report, not a synthesis or advocacy piece.
  No affiliation with Anthropic or OpenAI.
- **Scope**: Covers one specific production PR — a security migration replacing
  token-based CSRF protection with `Sec-Fetch-Site` header protection in Datasette,
  implemented across 10 commits with Claude Code under close human guidance and
  cross-reviewed with GPT-5.4. The AI-native engineering content is three patterns
  embedded in ~one paragraph of the blog post; the PR body provides technical depth.
  Does NOT cover: general workflows, harness configuration, or any broader methodology.
  The CSRF implementation details (Sec-Fetch-Site, Filippo Valsorda's research, Go 1.25)
  are the security context, not the AI-engineering content; they are summarized but
  not deeply extracted here.

## Extracted Claims

### Claim 1: Security-sensitive AI-assisted work should proceed in many small commits under close human direction — not as a single autonomous run

- **Evidence**: Willison describes Claude Code doing "much of the work (across 10
  commits, closely guided by me)." The PR confirms Claude Opus 4.6 (1M context) is
  listed as co-author on four specific commits covering compatibility shims, bearer
  token exemption, and documentation. The remaining commits are Willison's own. The
  10-commit structure is a deliberate decomposition of a multi-file change (6 templates,
  1 middleware, docs, upgrade guide, tests) into reviewable increments, not an artifact
  of Claude Code's output size.
- **Confidence**: anecdotal (single practitioner, one PR — but the structure is
  intentional and the PR is publicly verifiable)
- **Quote**: "Claude Code did much of the work (across 10 commits, closely guided by
  me and cross-reviewed by GPT-5.4)"
  — Simon Willison, simonwillison.net/2026/Apr/14/replace-token-based-csrf/
- **Our assessment**: This is a meaningful counter-example to single-shot AI-assisted
  development. A CSRF overhaul that removes a plugin hook (`skip_csrf`), strips hidden
  form fields from six templates, removes a dependency (`asgi-csrf`), and updates
  documentation is non-trivial surface area. Willison's approach — 10 commits, close
  guidance, explicit cross-review — treats the AI as a capable implementer that still
  requires human direction at each step. The specific commit count (10) and the
  "closely guided" qualifier are the load-bearing details; they distinguish this from
  autonomous delegation. For security-critical changes specifically, this pattern
  (human-guided incremental commits rather than one big autonomous PR) has strong
  intuitive backing even from this single data point.

### Claim 2: Multi-model cross-review — Claude Code for implementation, a second model for review — is a viable workflow for production security changes

- **Evidence**: Willison explicitly names both models: "Claude Code did much of the
  work... cross-reviewed by GPT-5.4." The PR shipped to production (merged, released
  with an upgrade guide). GPT-5.4 is used in the review role, not the implementation
  role. This is a practitioner-confirmed two-model division of labor on a real
  production security change, not a toy example.
- **Confidence**: anecdotal (one practitioner, one change, one pair of models — the
  pattern is intentional but not benchmarked)
- **Quote**: "cross-reviewed by GPT-5.4"
  — Simon Willison, same post
- **Our assessment**: This is the first concrete, practitioner-confirmed instance in our
  corpus of the cross-model review workflow applied to a production security change.
  Osmani's orchestra post mentions multi-model routing as a recommendation (Claim 9 in
  blog-addyosmani-code-agent-orchestra: "route planning to cheaper models, implementation
  to capable models, review to security-focused models") but names no specific practitioner
  doing this. Willison's report names the models, names the roles (implementation vs.
  review), and names the result (a shipped, production-quality security migration). The
  choice to use a different vendor's model for review is notable: GPT-5.4 (OpenAI) reviews
  Claude Code's (Anthropic) implementation. This cross-vendor review eliminates any model
  self-review bias and provides a genuinely independent second opinion. Whether GPT-5.4
  is specifically better at security review than Claude is unknown from this post — the
  pattern's value is independence, not model capability ranking.

### Claim 3: Retaining PR description authorship by hand is a practitioner-discovered technique for maintaining honesty about AI attribution and scope

- **Evidence**: Willison explicitly names this as a deliberate practice and gives two
  reasons: "partly to make them more concise and also as an exercise in keeping myself
  honest." The phrasing "exercise in keeping myself honest" is a first-person reflection
  on the risk of losing track of what AI did versus what the human directed — a
  meta-cognitive accountability technique, not just a style preference.
- **Confidence**: anecdotal (one practitioner's stated practice, not benchmarked or
  replicated; but the reasoning is explicit and generalizable)
- **Quote**: "I've decided to start writing these PR descriptions by hand, partly to make
  them more concise and also as an exercise in keeping myself honest."
  — Simon Willison, same post
- **Our assessment**: This is the most novel and transferable claim in the source. The
  "keeping myself honest" framing surfaces a real risk in AI-assisted development:
  if the AI writes the PR description, the human author may accept a description that
  over-credits AI or under-credits their own direction — or, conversely, under-describes
  what the AI actually did. Writing the description by hand forces the author to
  reconstruct what happened, which surfaces their own understanding (or lack of it).
  This maps onto the "Willison test" formulation in blog-addyosmani-code-agent-orchestra
  Linked Source 4: "I won't commit code I couldn't explain to someone else." Willison
  is applying the same principle one level up — at the PR description rather than the
  code. Note the conciseness benefit is secondary; the honesty mechanism is the
  primary stated motivation.

### Claim 4: Claude Opus 4.6 with a 1M context window can co-author commits in a multi-file production security migration, including compatibility shims, bearer token exemptions, and documentation updates

- **Evidence**: The PR commit list identifies Claude Opus 4.6 (1M context) as co-author
  on four specific commits. The scope of those commits spans API compatibility (maintaining
  `csrftoken()` template function as a no-op, restoring `request.scope["csrftoken"]` for
  legacy plugins), exempting bearer token requests from the new middleware, and
  documentation. The 1M context window is explicitly named in the co-author attribution.
- **Confidence**: anecdotal (single PR; but the PR is publicly verifiable on GitHub and
  the co-author commits are explicit)
- **Quote**: "Claude Opus 4.6 (1M context)" — PR commit co-author attribution,
  github.com/simonw/datasette/pull/2689
- **Our assessment**: The 1M context window is likely what made the compatibility work
  tractable — holding the full codebase context while reasoning about which existing
  plugin integrations depended on the old CSRF tokens. The co-author commits are the
  specific, verifiable artifact that distinguishes this from a generic "I used AI"
  report. The choice of co-author attribution (rather than omitting AI involvement)
  reflects Willison's explicit practice of tracking AI contribution in git history.

### Claim 5: AI-assisted security implementation can achieve near-complete test coverage when the tests are part of the AI-assisted work scope

- **Evidence**: The PR includes a new test file `test_csrf_middleware.py` covering five
  algorithm branches of the new `CrossOriginProtectionMiddleware`, achieving 98.31%
  patch coverage. The test file was part of the AI-assisted implementation, not a
  separate human pass.
- **Confidence**: anecdotal (single PR, verifiable on GitHub; 98.31% is a specific metric
  from the PR)
- **Quote**: "98.31% patch coverage" — PR coverage report, github.com/simonw/datasette/pull/2689
- **Our assessment**: The 98.31% coverage figure is notable because high test coverage
  on security middleware is not just a quality metric — it is a verification signal for
  the new behavior. For the guide: when using AI to implement security-sensitive code,
  requiring the AI to write tests as part of the same task (not as a separate follow-up)
  raises the probability that edge cases are covered before the code is committed.
  The five algorithm branches (including Sec-Fetch-Site variants and fallback logic for
  older browsers) are the cases that matter for correct CSRF protection; the AI covering
  98.31% of the patch means nearly all the new security logic has an automated test.

## Concrete Artifacts

### The multi-model workflow pattern (from blog post + PR)

```
Security migration workflow — datasette PR #2689 (April 2026)

Role split:
  Implementation: Claude Code (Claude Opus 4.6, 1M context window)
  Review:         GPT-5.4 (OpenAI — cross-vendor for independent review)
  Direction:      Simon Willison (human, close guidance throughout)
  Documentation:  Simon Willison (PR description written by hand)

Commit structure:
  Total commits: ~10
  AI co-authored: 4 (compatibility shims, bearer token exemption, docs)
  Human-only:     ~6

PR description: Written by hand by human author.
Stated reason: "partly to make them more concise and also as an
                exercise in keeping myself honest"
```

### CSRF protection changes scope (multi-file, AI-assisted)

```
Files changed in datasette PR #2689:
  - 6 HTML templates: removed <input type="hidden" name="csrftoken">
  - CSRF middleware: new CrossOriginProtectionMiddleware (Sec-Fetch-Site / Origin headers)
  - Plugin system: removed skip_csrf() plugin hook entirely
  - Compatibility: csrftoken() template function now returns empty string
                   request.scope["csrftoken"] restored as per-request random string
  - Tests: test_csrf_middleware.py — 5 algorithm branches, 98.31% patch coverage
  - Docs: CSRF protection documentation revised
  - Upgrade guide: added CSRF migration guidance (bearer tokens, signed URLs, body-carried credentials)

Dependency removed: asgi-csrf
Inspiration: Filippo Valsorda's research (August 2025) + Go 1.25's http.CrossOriginProtection
```

### Willison's PR authorship principle

```
"I've decided to start writing these PR descriptions by hand, partly to make
them more concise and also as an exercise in keeping myself honest."
  — Simon Willison, simonwillison.net/2026/Apr/14/replace-token-based-csrf/
  Published: 2026-04-14
```

*Context: Willison notes this as a new practice he has "decided to start" — framed
as a deliberate behavior change, not a retrospective observation about this PR alone.*

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-servo-crate-exploration.md** — same author, same Claude Code
    + human practitioner pattern; the servo post shows Willison giving Claude Code a
    loose exploratory goal; this post shows the opposite: close guidance on a
    security-critical, multi-file change. Together they bracket the range of Willison's
    Claude Code usage: autonomous exploration (servo) vs. closely guided execution (CSRF).
    This source adds the multi-model cross-review and manual PR description patterns that
    the servo note does not contain.
  - **blog-addyosmani-code-agent-orchestra.md** (Claim 9 + Linked Source 5): Osmani
    recommends multi-model routing (different models for planning vs. implementation vs.
    review) and the two-agent verification pattern (Agent A implements, Agent B reviews).
    Willison's PR is a concrete practitioner realization of both recommendations —
    specifically the cross-vendor variant (Claude Code implements, GPT-5.4 reviews).
    This source provides the first named practitioner evidence for those patterns in a
    production security context.
  - **blog-anthropic-multi-agent-coordination-patterns.md** (generator-verifier pattern):
    Anthropic's taxonomy includes the generator-verifier pattern as a first-class
    coordination topology. Willison's Claude Code + GPT-5.4 workflow is an inter-model
    instantiation of this pattern: generator (Claude Code) produces commits; verifier
    (GPT-5.4) reviews. The Anthropic post notes that the verifier requires explicit
    criteria; Willison's case supplies those criteria implicitly through close human
    guidance throughout, not through a formal spec.

- **Contradicts**: None identified. No existing corpus note makes claims that conflict
  with the three patterns extracted here. The close-guidance pattern is novel to this
  source in the security context.

- **Extends**:
  - **blog-simonwillison-cybersecurity-proof-of-work.md** — published the same day
    (2026-04-14) by the same author; that note covers AI security economics (proof-of-work
    framing, token budgets). This source provides a concrete workflow example from the
    same author on the same day: not economics of AI security, but mechanics of how a
    practitioner actually executes an AI-assisted security migration. Together they form
    a complementary pair for Chapter 03: the economics (why) and the workflow (how).
  - **blog-addyosmani-code-agent-orchestra.md** (Linked Source 4, Willison test):
    Osmani cites Willison's principle "I won't commit code I couldn't explain to someone
    else." This source documents Willison applying the same principle at the PR description
    level: "keeping myself honest" by writing the description by hand. The manual PR
    description technique extends the accountability principle from code-level to PR-level.

- **Novel**:
  - **Manual PR description as honesty mechanism**: No existing corpus source documents
    the practice of retaining PR description authorship as a deliberate accountability
    technique for AI-assisted work. The Osmani orchestra post mentions "structured PR
    packet" (Linked Source 5) as a verification output, but it is AI-generated and
    reviewed, not human-authored-as-check. Willison's inversion — specifically choosing
    NOT to let AI write the PR description for the "honest" reason — is new.
  - **Cross-vendor model review for security changes (Claude Code + GPT-5.4)**:
    No existing corpus source documents a practitioner using competing-vendor models in
    explicit implementation-vs-review roles on a production security change. Osmani's
    recommendation is advisory; this is a named, verifiable practitioner report.
  - **AI co-authorship commits as an attribution practice**: Four commits in this PR
    name Claude Opus 4.6 as co-author in git history. No existing corpus source discusses
    git co-authorship as a tracking mechanism for AI contribution; this is the first
    observed instance.

## Guide Impact

- **Chapter 01 (Daily Workflows — Human-AI collaboration patterns)**: Add the small-commit
  close-guidance pattern as the recommended workflow for security-critical AI-assisted
  changes. Specific recommendation: "For security migrations, decompose the work into
  reviewable commit units rather than delegating end-to-end. Willison's CSRF overhaul
  (Datasette PR #2689, April 2026) ran 10 commits with close human direction; Claude
  Code co-authored 4 specific commits. This is different from a single autonomous run."
  Pair with the servo exploration note as the contrast: autonomous exploration for
  low-stakes library discovery; close-guidance incremental commits for production security
  changes. The chapter currently lacks a worked example of the close-guidance pattern.

- **Chapter 01 (Daily Workflows — PR authorship)**: Add the manual PR description
  technique as a lightweight honesty practice. Specific recommendation: "Write your own
  PR descriptions for AI-assisted work. Willison (April 2026) explicitly chose this as
  'an exercise in keeping myself honest.' It forces you to reconstruct what happened,
  which surfaces gaps in your understanding of the AI's contribution. The description
  becomes a comprehension test as much as documentation." This is a Chapter 01 daily
  workflow recommendation, not a heavy governance mechanism — it costs minutes and
  produces better descriptions while preserving human understanding.

- **Chapter 03 (Safety and Verification — Cross-model review)**: Add the Claude Code +
  GPT-5.4 cross-vendor review workflow as a named pattern for security-sensitive changes.
  Specific recommendation: "For high-stakes changes, use a different vendor's model for
  review than the one that implemented the code. Willison's 2026 CSRF migration used
  Claude Code for implementation and GPT-5.4 for review. Cross-vendor review eliminates
  self-review bias at the model level. This is the inter-model instantiation of the
  generator-verifier pattern (see blog-anthropic-multi-agent-coordination-patterns)."
  Note: this is a single practitioner observation, not a controlled study; the guide
  should present it as a promising technique rather than an established recommendation.

- **Chapter 03 (Safety and Verification — Test coverage for security code)**: Add the
  98.31% patch coverage finding as evidence that including test authorship in the AI's
  scope (same task, same session) produces high coverage for new security logic. Specific
  addition: "When AI implements security-sensitive code, include test writing in the same
  task scope rather than as a follow-up. In Willison's CSRF middleware implementation
  (April 2026), AI-assisted tests covered 98.31% of the patch across five algorithm
  branches."

## Extraction Notes

- **Thin blog post; PR is the substantive source**: The Willison link post is ~200 words.
  The PR body (github.com/simonw/datasette/pull/2689) was fetched and provides the
  commit count, co-author attribution, coverage metric, and scope of changes. Both
  were read; claims citing specific numbers or file details derive from the PR, not the
  blog post.
- **Three Prospector triage comments**: Three separate triage assessments were submitted
  (probably a pipeline artifact). All three identify the same three core patterns;
  novelty ratings vary from "low" to "medium." The cross-vendor review and manual PR
  description patterns drove the "medium" assessments; their novelty to the corpus is
  the basis for this extraction's confidence that the note adds value despite the thin
  source.
- **No sub-pages followed beyond the PR**: The blog post links to the PR, the Filippo
  Valsorda research, and Go 1.25. The Valsorda research and Go 1.25 are web security
  context, not AI-engineering content; they were not followed.
- **Willison's "decided to start" phrasing**: The manual PR description comment is
  forward-looking ("I've decided to start") — it is a new practice Willison is
  announcing, not a retrospective description of a long-standing workflow. This means
  there is no historical corpus of Willison PRs to verify the pattern against; it is a
  stated intention as of April 14, 2026.
- **Fragment URL in issue**: The issue filed the URL with `#atom-everything` fragment
  (feed anchor). The `source_url` in frontmatter uses the canonical page URL without
  the fragment.
