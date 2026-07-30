---
source_url: https://sourcegraph.com/blog/detection-in-one-repo-isnt-a-security-posture
source_type: blog-post
title: "Detection in one repo isn't a security posture"
author: Justin Dorfman (Sourcegraph)
date_published: 2026-07-10
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: emerging
issue: "#2320"
---

# Detection in one repo isn't a security posture

> Sourcegraph vendor blog post arguing that per-repository security scanning
> does not add up to organizational security posture — prevention, detection,
> and response are reframed as one capability that depends entirely on
> queryable visibility across every repo an org owns, with AI-driven code
> volume and supply-chain malware growth cited as the forces making the gap
> between "detection" and "posture" more urgent.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, published July 10, 2026;
  auto-discovered via the `sourcegraph` trusted feed). Short-form
  argumentative piece (TL;DR + four sections: "The reframe," "Why this is
  getting harder, fast," "What good actually looks like," "The takeaway"),
  ending in a "Schedule a demo" call-to-action and a linked "codebase
  visibility security framework" ebook.
- **Author credibility**: Byline is "Justin Dorfman," published on
  Sourcegraph's official company blog. No independent security-researcher
  credential or title is given in the article itself. This is company
  content advancing Sourcegraph's own commercial narrative (code search /
  codebase-wide visibility is Sourcegraph's core product category); the
  argument should be read as informed industry commentary with a vendor
  interest in the conclusion, not as neutral or independently peer-reviewed
  analysis. The third-party statistics it cites (Microsoft, Google, Sonatype)
  are attributed but not linked with inline citations in the extracted text,
  so this note treats them as secondhand claims, not independently verified
  figures.
- **Scope**: Covers the conceptual argument that prevention, detection, and
  response are one capability requiring cross-repository visibility, plus
  three cited statistics on AI code volume, dependency count, and malicious
  package growth as pressure vectors. Does NOT cover: any specific tooling
  implementation, how "queryable visibility" is technically built, methodology
  behind the cited third-party statistics, or any named customer case study
  with before/after metrics.

## Extracted Claims

### Claim 1: A single-repo security finding is a fact, not a posture — organizational security posture requires knowing whether the same problem exists across every repo the org owns
- **Evidence**: Stated as the article's core thesis in both the sub-headline and the TL;DR.
- **Confidence**: emerging (a conceptual/definitional argument, not an empirical finding)
- **Quote**: "A finding in one repo is a fact. A security posture means knowing whether that same problem exists everywhere else, and fixing it before it spreads."
- **Our assessment**: This is a clean, quotable reframe of a real operational gap: most security tooling is scoped to "does this repo have a problem," not "does my organization have this problem." The claim is definitional rather than measured — no data is given on how many organizations actually operate this way versus have already built cross-repo visibility — but it names a real distinction that matters for anyone reasoning about security tooling architecture at multi-repo scale.

### Claim 2: Prevention, detection, and response are not three separate programs but the same capability viewed at three moments in time, all dependent on complete, queryable visibility across every repository
- **Evidence**: Stated as the article's central architectural reframe, repeated in the TL;DR and expanded in "The reframe" section.
- **Confidence**: emerging (conceptual framework, asserted rather than empirically demonstrated)
- **Quote**: "Prevention, detection, and response aren't three separate programs you can buy and bolt together. They're one problem, and the connective tissue between them is visibility across the whole codebase. Break the visibility and all three degrade together."
- **Our assessment**: The "connective tissue" framing is the article's most useful contribution: it argues against the common practice of buying separate point solutions for prevention (e.g., pre-commit scanning), detection (e.g., alerting on new CVEs), and response (e.g., patch rollout tracking), on the grounds that all three fail together if none of them can see the whole codebase. This is a reasonable architectural claim but is not backed by a comparative study of organizations that unified these functions versus those that didn't — treat as a design thesis, not a proven result.

### Claim 3: The common assumption that per-repo scanning sums to organizational posture is false
- **Evidence**: Stated explicitly as the flawed mental model the article is arguing against, in "The reframe" section.
- **Confidence**: emerging (framed as a rebuttal of an assumption, not tested against data)
- **Quote**: "If every repo scans itself, the sum of those scans is your security posture."
- **Our assessment**: This is presented by the article as the wrong belief, immediately followed by the vulnerability-disclosure scenario (Claim 4) as the counter-example. It's a rhetorical framing device rather than a claim with independent evidence, but it's useful as a concise statement of the mental model this source (and any guide content drawing on it) is arguing against.

### Claim 4: When a new vulnerability disclosure hits, most teams cannot determine within a week which of their repositories are exposed and how fast they can all be patched
- **Evidence**: A concrete scenario the article poses as the test of whether an org has "detection" or "posture" — the question an org must be able to answer immediately upon a CVE disclosure.
- **Confidence**: anecdotal (an assertion about typical organizational capability, no survey or data cited)
- **Quote**: "Which of our 3,000 repos pull this in, directly or transitively, and how fast can we patch all of them." ... "Most teams cannot answer that in an afternoon. Many cannot answer it in a week."
- **Our assessment**: This is the article's sharpest concrete illustration of the abstract thesis, using a specific repo count (3,000) to make the scale problem tangible. No data source is cited for "most teams cannot answer that in an afternoon" — it reads as the author's professional assessment based on Sourcegraph's customer conversations, not a cited survey. Directionally plausible given the dependency-sprawl and repo-count realities of large orgs, but should be treated as anecdotal claim rather than a measured industry statistic.

### Claim 5: AI assistants now write a substantial share of production code, intensifying the volume/velocity pressure on security tooling — cited at roughly 30% for Microsoft and a similar figure for Google's new code
- **Evidence**: Attributed statements from Microsoft's CEO and a similar figure reported by Google, cited in the "Why this is getting harder, fast" section as one of two forces widening the detection/posture gap.
- **Confidence**: emerging (secondhand citation of statements attributed to named companies/executives, not independently verified by this Miner against a primary Microsoft or Google source)
- **Quote**: "Microsoft's CEO has said as much as 30% of the company's code is AI-written"
- **Our assessment**: This is a now-familiar statistic in the corpus (AI-generated code share), used here specifically as a security-posture pressure vector rather than a productivity claim: more AI-generated code, the article argues, means more code shipping faster, which strains security review capacity built for pre-AI code velocity. The claim is only as strong as the underlying Microsoft/Google statements, which are not directly quoted with a primary source link in the extracted article text — worth independently verifying against a primary Microsoft or Google statement before citing as settled in the guide.

### Claim 6: Modern applications carry around 180 dependencies on average, and AI-assisted development is increasing this further
- **Evidence**: A cited average dependency count, presented in the "Why this is getting harder, fast" section as the second pressure vector (dependency sprawl) alongside AI code volume.
- **Confidence**: emerging (a specific cited figure, source of the underlying study/survey not given in the extracted text)
- **Quote**: "Modern applications already carry around 180 dependencies on average"
- **Our assessment**: No source is cited inline for the 180-dependency figure, and this Miner did not independently trace it to a primary dataset. It is directionally consistent with widely-reported dependency-sprawl trends in modern package ecosystems (npm, PyPI) but should be treated as an unverified secondhand statistic rather than a settled figure — flag for independent verification if the guide cites the specific number.

### Claim 7: Malicious-package volume in software supply chains grew sharply in 2025, including the first self-replicating npm malware, which spread across more than 500 packages on its own
- **Evidence**: Cited Sonatype data in the "Why this is getting harder, fast" section, presented as evidence that the supply-chain threat landscape is worsening independent of AI code volume.
- **Confidence**: emerging (a specific, dated, named-source statistic — Sonatype — but not independently verified against Sonatype's own published report by this Miner)
- **Quote**: "Sonatype identified more than 454,600 new malicious packages in 2025, a 75% jump year over year" ... "including the first self-replicating npm malware that spread across more than 500 packages on its own"
- **Our assessment**: This is the article's strongest, most specific data point — a named source (Sonatype), a concrete year-over-year growth figure, and a specific named incident class (self-replicating npm malware). It corroborates a broader industry narrative of accelerating supply-chain attacks, though this note has not independently traced the 454,600/75% figures to a primary Sonatype report to confirm the exact methodology or time window. The self-replicating-npm-malware detail is specific enough to be independently checkable and is a good candidate for a follow-up source note if a primary account of that incident exists in the corpus or can be sourced separately.

### Claim 8: Teams with genuine codebase-wide visibility can do four things per-repo scanning alone cannot: find every instance of a problem across repos, see blast radius before acting, fix at the same scale they detect, and prevent recurrence
- **Evidence**: Stated as a four-item list in the "What good actually looks like" section, framed as the observable difference between "detection" and "posture."
- **Confidence**: emerging (a normative list of capabilities, not measured against real organizations achieving all four)
- **Quote**: "See the blast radius before acting. Know how many repos, services, and teams a given issue touches before triage, so prioritization is based on reach, not guesswork."
- **Our assessment**: The four capabilities (find every instance, see blast radius, fix at scale, prevent recurrence) form a reasonably well-structured checklist for evaluating whether an org's security tooling operates at "posture" level versus "single-repo detection" level. It's a normative framework rather than a report on organizations that have achieved it — no named customer or case study is given as a concrete example of a team hitting all four. Still useful as an evaluation rubric: readers can check their own tooling against these four items concretely.

### Claim 9: Without codebase-wide visibility, a fixed problem can silently recur in a different, unmonitored repository
- **Evidence**: A specific illustrative phrase used in the "What good actually looks like" section to describe the "prevent the next instance" capability.
- **Confidence**: anecdotal (illustrative example, not a documented incident)
- **Quote**: "the same class of problem can't quietly reappear in repo 3,001"
- **Our assessment**: This is a rhetorical continuation of the earlier "3,000 repos" framing (Claim 4) — the implication is that fixing a vulnerability in the 3,000 known/scanned repos does nothing to stop the same pattern from being introduced in a 3,001st repo (a new repo, or one outside current scanning scope) without organization-wide prevention rules. It's a hypothetical illustration, not a reported incident, but it names a real gap: point-in-time remediation without systemic prevention leaves the door open for recurrence.

## Concrete Artifacts

### The article's core reframe, verbatim (TL;DR section)
```
Source: https://sourcegraph.com/blog/detection-in-one-repo-isnt-a-security-posture
Author: Justin Dorfman, Sourcegraph — published July 10, 2026

"Most security tooling is very good at one thing: finding a problem inside
a single repository. That feels like security. It isn't. A finding in one
repo is a fact. A security posture is knowing whether that same problem
exists across every repo you own, stopping it from spreading, and fixing
it everywhere at once."

"Prevention, detection, and response aren't three separate programs you
can buy and bolt together. They're one problem, and the connective tissue
between them is visibility across the whole codebase. Break the
visibility and all three degrade together."

"AI is now writing a meaningful share of production code and pulling in
dependencies faster than any human review process was built to handle.
That doesn't add a fourth problem. It strains the one you already have."
```

### "Why this is getting harder, fast" — cited pressure-vector statistics
```
Source: sourcegraph.com/blog/detection-in-one-repo-isnt-a-security-posture

Volume/velocity (AI code generation):
- "Microsoft's CEO has said as much as 30% of the company's code is
  AI-written" — Google reported a similar figure for new code.

Dependency sprawl:
- "Modern applications already carry around 180 dependencies on average"
  — AI-assisted development cited as increasing this further.

Supply-chain malware growth (attributed to Sonatype):
- "Sonatype identified more than 454,600 new malicious packages in 2025,
  a 75% jump year over year"
- "including the first self-replicating npm malware that spread across
  more than 500 packages on its own"
```

### "What good actually looks like" — four-item visibility checklist
```
Source: sourcegraph.com/blog/detection-in-one-repo-isnt-a-security-posture

1. Find every instance, everywhere
2. See the blast radius before acting
   — "Know how many repos, services, and teams a given issue touches
      before triage, so prioritization is based on reach, not guesswork."
3. Fix at the same scale you detect
4. Prevent the next instance
   — "the same class of problem can't quietly reappear in repo 3,001"
```

## Cross-References

- **Corroborates**: `blog-anthropic-llms-secure-source-code.md` Claim 12 —
  Anthropic's own security research team reports 1,596 disclosed
  vulnerabilities against only 97 patched (~6% patch rate) as of May 22,
  2026, "demonstrating that patching capacity is the real bottleneck." This
  independently corroborates this source's Claim 4 (time-to-patch is the
  operational failure point orgs can't answer quickly) from a different
  angle: even a well-resourced, first-party security research team with
  strong discovery tooling is bottlenecked downstream at patching, not
  detection — the same gap this source frames as a cross-repo visibility
  problem rather than a patching-capacity problem, but pointing at the same
  underlying symptom (finding things faster than fixing them).
- **Corroborates**: `blog-cursor-security-agents.md` Claim 8 and Claim 9 —
  Cursor's Vuln Hunter and Invariant Sentinel agents already "divide repos
  into logical segments" to scan beyond single-context-window limits and
  report 200+ vulnerabilities caught per week across 3,000+ PRs. This is
  evidence that at least one practitioner organization is already building
  toward scanning at the scale this source argues is necessary, though
  Cursor's segmentation is described as operating within Cursor's own
  monorepo/codebase rather than explicitly across many separately-owned
  repositories — a narrower scope than this source's "every repo you own"
  framing, but directionally the same scaling problem.
- **Extends**: `docs-ghaw-multi-repo-ops.md` Claim 4 — GitHub Agentic
  Workflows' hub-and-spoke topology (component repos forward findings to a
  central coordination repository via the `target-repo` safe-output
  parameter) is a concrete, already-documented technical mechanism in a
  different tool ecosystem for exactly the capability this source argues
  is missing: propagating detection and fixes across many repositories from
  a central point. This source provides the conceptual "why you need this"
  argument; the gh-aw note provides one ecosystem's "how it's actually
  built" mechanism.
- **Contradicts**: None identified. No existing corpus source argues that
  per-repo scanning alone constitutes adequate security posture, so this
  source's central thesis has no direct opposing claim in the corpus to
  flag as a contradiction.
- **Novel**: The explicit "detection vs. posture" definitional distinction;
  the "prevention/detection/response as one capability at three moments"
  framing; the specific malicious-package/self-replicating-npm-malware/
  dependency-sprawl statistic bundle (Sonatype attribution); and the
  four-item "what good looks like" visibility checklist are all new to this
  corpus. No existing source note documents cross-repository (as opposed to
  single-repo or single-pipeline) security visibility as a named
  architectural requirement.

## Guide Impact

- **Chapter 06 (Security & Threat Model)**: Chapter 06 currently documents
  MCP-supply-chain rug-pull mitigation (the "The MCP supply chain: rug-pull
  tool redefinition" section) but has no section addressing
  dependency/package-registry supply-chain risk or cross-repository
  security visibility as distinct concerns. This source supports adding a
  short subsection — tentatively "Detection vs. posture: single-repo
  scanning doesn't scale" — that names the specific failure mode (a team
  can answer "does this repo have the vulnerability" but not "which of our
  N repos have it, and how fast can we patch all of them") and cites this
  source's four-item visibility checklist (find every instance, see blast
  radius, fix at scale, prevent recurrence) as a concrete evaluation rubric
  for readers assessing their own org's security tooling. Should be paired
  with `blog-anthropic-llms-secure-source-code.md`'s six-step find-and-fix
  loop and `blog-cursor-security-agents.md`'s four-agent fleet as the
  operational counterpart — this source supplies the "why cross-repo
  visibility matters" argument, those two sources supply "how teams are
  actually building detection/patching pipelines" at increasing scale.
- **Chapter 06 (Security & Threat Model) — supply-chain pressure stats**:
  If the guide adds or updates any section quantifying why AI-native
  development raises supply-chain risk, this source's cited statistics
  (454,600 new malicious packages in 2025, +75% YoY per Sonatype; ~180
  average dependencies per application; first self-replicating npm malware
  across 500+ packages) are candidate figures — but flag them as secondhand
  citations requiring independent verification against primary Sonatype
  reporting before treating as settled numbers in guide prose.

## Extraction Notes

- **WebFetch returned a summarized version on the first pass**; this Miner
  made four additional targeted WebFetch calls against the same URL with
  narrower, verbatim-only prompts to extract and cross-check specific
  quotes (the definitional claim, the statistics, the "reframe" section
  quotes, and the "repo 3,001" / "connective tissue" phrases). One WebFetch
  call requesting full verbatim reproduction of multiple entire sections was
  declined by the fetch tool's underlying model on copyright-reproduction
  grounds; this note relies on shorter, targeted verbatim-quote extractions
  instead, consistent with the guidance in MINER.md §2a to quote only the
  contiguous fragment that carries the meaning rather than reproducing full
  sections.
- **No sub-pages followed**: The article is a single, self-contained page
  with a closing CTA linking to a gated ebook ("The codebase visibility
  security framework") and a "Schedule a demo" contact link. Neither link
  was followed — the ebook is presumably gated (lead-generation content)
  and the demo link is a sales contact form, not additional substantive
  source material.
- **Confidence set to `emerging`**: The article's central architectural
  thesis (detection vs. posture; prevention/detection/response as one
  capability) is a reasoned but unproven vendor argument, and its supporting
  statistics are secondhand citations of third-party data (Microsoft,
  Google, Sonatype) that this Miner did not independently verify against
  primary sources. Individual claims are graded `emerging` or `anecdotal`
  at the claim level to reflect this — no claim in this note is graded
  `settled`, since none rests on first-party, independently-verifiable
  data produced by Sourcegraph itself.
