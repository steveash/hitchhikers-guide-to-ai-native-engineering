---
source_url: https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/
source_type: blog-post
title: "Actual curl rewrites in rust"
author: Daniel Stenberg (curl creator and lead maintainer); surfaced via Simon Willison's link-blog quote (2026-11-18)
date_published: 2026-11-17
date_extracted: 2026-11-19
last_checked: 2026-11-19
status: current
confidence_overall: emerging
issue: "#4820"
---

# Actual curl rewrites in rust

> Stenberg argues that agent-driven C-to-Rust rewrites of curl (~185K lines C to ~340K lines Rust in ~3 weeks) are cheap to produce but start "behind": upstream curl shipped 300+ commits and ~200 bugfixes in the same window, so the real value of a mature project is its ongoing maintenance and community, not its code.

## Source Context

- **Type**: blog-post. Primary source is Stenberg's post (read in full from daniel.haxx.se). Simon Willison's entry (https://simonwillison.net/2026/Nov/18/daniel-stenberg/) is only a short quotation of the "Behind already" paragraph; all quotes below are from Stenberg's post.
- **Author credibility**: Daniel Stenberg created and has led curl for ~30 years; he counted the line numbers himself ("I counted") and has direct access to curl's commit/bug/vulnerability data. He is also an interested party (curl maintainer), which colours the "no rewrites" stance.
- **Scope**: Opinion/commentary on two AI-produced Rust clones (`urlx`, and a November project literally named "curl, rewritten in Rust", claiming a US$8,600 cost). He did not evaluate those rewrites' quality, test pass rates or behaviour, and has not contacted their authors. Not an empirical study.

## Extracted Claims

### Claim 1: Agent teams can now port a large, mature C codebase to Rust in a few weeks for a low sum
- **Evidence**: Two public examples (urlx; "curl, rewritten in Rust"). The latter claims 8,600 USD cost. Stenberg counted 185,000 lines C into 340,000 lines Rust.
- **Confidence**: emerging (cost is the rewrite author's own claim; line counts are Stenberg's)
- **Quote**: "This latter one claims to have spent 8,600 USD to make it happen."
- **Our assessment**: Believable as a lower bound on feasibility. Note the 1.84x line expansion, which is a reviewability cost; the post does not discuss it.

### Claim 2: The port was feasible because curl is an unusually well-specified, heavily trained-on target (docs, API consumers, thousands of tests)
- **Evidence**: Stenberg's reasoning, no measurements.
- **Confidence**: anecdotal
- **Quote**: "The C code sits there and all the AI needs to do is convert it to rust, then polish until the tests work."
- **Our assessment**: Strong and useful conditioning variable: the existing test suite acts as the verification oracle. Results should not generalise to projects lacking thousands of tests. Also implies "polish until the tests work" is the agents' stopping criterion, so parity beyond the tests is unverified.

### Claim 3: Writing code once was never the hard part of software; value lies in accumulated feedback, community and time
- **Evidence**: Argument from experience of maintaining curl for decades.
- **Confidence**: emerging
- **Quote**: "Writing code once was never the big deal with software and it still isn’t."
- **Our assessment**: Aligns with the guide's verification/maintenance-over-generation theme. Opinion, but from someone with unusual long-horizon evidence.

### Claim 4: During the ~3-week rewrite window upstream curl merged 300+ commits and ~200 bugfixes (plus a few vulnerability fixes) that the Rust clones lack
- **Evidence**: Upstream commit/bug counts from the curl project; Stenberg counted the rewrite's lines. Absence of the fixes in the clones is inferred, not audited.
- **Confidence**: emerging
- **Quote**: "During the time these agents converted 185,000 lines of C code into 340,000 lines of Rust code (I counted), we merged over 300 commits in the actual curl project."
- **Our assessment**: Concrete, quantified framing of the "fork drift" cost of agent-generated ports. Caveat: clones could in principle re-port commits; Stenberg himself notes this (Claim 6). Also, a snapshot port that is not behind in any way you care about may not need all 200 fixes (some fix bugs only in the C code).

### Claim 5: Continuous fixing, not the implementation language, is what sustains a project; curl's moat is development speed, team, community and decades of ABI/API stability
- **Evidence**: Argument; 30-year history.
- **Confidence**: emerging
- **Quote**: "A primary reason it is hard to make a competing curl alternative is because of the development speed, the development team and the community around curl.  It is not because of the chosen language it is implemented in."
- **Our assessment**: Credible; the "decades of stability can only be proven over time" point is a real limit on what a fast AI port can demonstrate.

### Claim 6: Rewrites can keep up only by continuously re-converting upstream commits (~11/day), and their maintainers' intent is unknown
- **Evidence**: Stenberg's commit rate figure; speculation about the clones' future.
- **Confidence**: anecdotal
- **Quote**: "They can of course follow along our commits and convert them to rust on the fly if they want – we only do about 11 commits per day on average."
- **Our assessment**: Interesting: continuous agent-driven porting of upstream is plausible and cheap-ish, which weakens the "behind" argument if automated. The open question ("Will these clones keep up?") is untested.

### Claim 7: Memory safety would have prevented only a minority of curl's 2026 vulnerabilities (14 of 81, 17.3%)
- **Evidence**: curl's own confirmed-vulnerability classification for 2026 to date; Stenberg says he is repeating himself.
- **Confidence**: emerging (project-maintainer classification; "most likely would have been avoided" is a judgement)
- **Quote**: "A Rust implementation of curl would thus still have had 67 of those vulnerabilities."
- **Our assessment**: Useful data point for the security chapter: a language swap addresses a minority class; logic/protocol bugs remain. The count is 2026 AI-assisted-report-era data (see the-pressure note).

### Claim 8: Stenberg does not believe in rewrites into any language; prefers continuous polishing and refactoring
- **Evidence**: Stated position.
- **Confidence**: anecdotal (opinion)
- **Quote**: "I don’t believe in rewrites into any language. I believe in constant and never-ending polishing, iterating and refactoring."
- **Our assessment**: A stance to record, in tension with the Bun and Claude-Code Rust-rewrite notes, which describe a successful rewrite (see Cross-References). Context differs (owner-led rewrite vs third-party clone), so not filed as a contradiction.

### Claim 9: Stenberg's reaction to the clones is amused, puzzled, fascinated; their status as more than proofs of concept is unknown
- **Evidence**: Personal reaction.
- **Confidence**: anecdotal
- **Quote**: "I’m amused. A little puzzled. Fascinated. They spent their money and effort on that?"
- **Our assessment**: Low informational value beyond tone; shows maintainers see these as proofs of concept not successors.

## Concrete Artifacts

```
Metrics reported by Daniel Stenberg, "Actual curl rewrites in rust" (2026-11-17):
- Rewrite A: urlx (claimed memory-safe, from-scratch reimplementation of curl/libcurl); appeared "a few months" earlier
- Rewrite B: "curl, rewritten in Rust"; claimed cost 8,600 USD
- Rewrite size: 185,000 lines C -> 340,000 lines Rust (Stenberg counted); ~3+ weeks
- Upstream curl, same window: 300+ merged commits; a little over 200 bugfixes; a few vulnerability fixes
- Upstream average pace: about 11 commits/day
- 2026 confirmed curl vulnerabilities: 81; memory-safety-preventable: 14 (17.3%); remaining: 67
```

## Cross-References

- **Corroborates**: `source-notes/blog-simonwillison-the-pressure.md` (same author/project; Claim 7 there says curl's actual security posture remains strong despite the report surge; this post supplies the 2026 vulnerability breakdown). `source-notes/blog-thoughtworks-ford-gall-zero-cost-fallacy.md` shares the theme that cheap generation shifts cost onto maintenance.
- **Contradicts**: None filed. Tension (not a direct contradiction): `source-notes/blog-simonwillison-rewriting-bun-rust.md`, `source-notes/blog-pragmaticengineer-bun-rust-rewrite.md` and `source-notes/blog-simonwillison-claude-code-bun-in-rust.md` describe an agent-driven Rust rewrite as a success, while Stenberg "[doesn't] believe in rewrites". Difference is conditioning: the Bun rewrite was owner-driven in-repo, whereas the curl clones are third-party forks with no upstream tracking.
- **Extends**: `source-notes/blog-simonwillison-the-pressure.md` (Claim 1: report surge) from the incoming-load side to the "AI-generated competing ports" side.
- **Novel**: Quantified comparison of AI-port output against upstream maintenance throughput; the 17.3% memory-safety share of 2026 curl vulnerabilities; the "existing test suite as oracle" explanation for why the port was feasible. (`source-notes/blog-simonwillison-parse-number-sqlite-c-vs-rust.md` and `blog-simonwillison-rust-targeted-attacks.md` are only loosely related Rust context.)

## Guide Impact

- **Chapter 03 (verification)**: Add the curl example that agent ports are bounded by the target's test suite ("polish until the tests work"); parity beyond tests is unmeasured. Cite as emerging, single-author evidence.
- **Chapter 05 (team adoption)**: Use the 185K→340K lines vs 300+ upstream commits / ~200 bugfixes figures as an illustration that generation cost is not maintenance cost.
- **Chapter 06 (security)**: Add the 14/81 (17.3%) figure as evidence that language migration addresses a minority of vulnerabilities; consider pairing with the-pressure note.

## Extraction Notes

- Read Stenberg's primary post in full (fetched raw HTML; quotes copied from the page text, with Stenberg's typographic apostrophes). Willison's page is a short excerpt; the quoted "Behind already" paragraph matches Stenberg's post.
- Did not inspect the urlx or "curl, rewritten in Rust" repositories; the issue's question about what they were tested against is NOT answered by this source. The post only notes that curl has "thousands of test cases".
- Comments section (16 comments) not extracted.
