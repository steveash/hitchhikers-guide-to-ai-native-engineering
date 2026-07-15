---
source_url: https://github.blog/changelog/2026-07-14-security-reviews-now-available-in-the-github-copilot-app
source_type: docs
title: "Security reviews now available in the GitHub Copilot app"
author: Allison (GitHub official changelog)
date_published: 2026-07-14
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: settled
issue: "#1879"
---

# Security Reviews Now Available in the GitHub Copilot App

> GitHub's July 14, 2026 changelog extends the `/security-review` slash command —
> previously documented in Copilot CLI — to the GitHub Copilot app, explicitly
> describing it as "the same AI-driven vulnerability scanning already available in
> Copilot CLI," available to Free, Pro, Business, and Enterprise plans during public
> preview, with no mention of the CLI's `/experimental on` gating requirement.

## Source Context

- **Type**: docs (GitHub official product changelog, July 14, 2026; ~180 words across
  three sections — "What it does," "Why it matters," "How to try it" — plus one
  screenshot). Fetched directly from `github.blog` HTML source to guarantee verbatim
  quotes (see Extraction Notes).
- **Author credibility**: GitHub's own changelog, byline "Allison," `Type: Improvement`
  category. Authoritative for: the feature's existence in the Copilot app surface, the
  stated output format, the stated vulnerability scope, the stated relationship to
  GitHub's pipeline security tools, and plan-tier availability. Not a credible source
  for: precision/recall or false-positive data, whether the app surface requires an
  experimental opt-in analogous to the CLI's `/experimental on`, how findings are
  deduplicated across CLI and app invocations of the same repository, or whether the
  underlying model/prompt is byte-for-byte identical to the CLI implementation (the
  claim of sameness is marketing language, not an engineering specification).
- **Scope**: Covers what the app-surface `/security-review` command does, why GitHub
  built it, and how to access it (including plan gating). Does NOT cover: cost per
  invocation, session/credit consumption, how scan scope is determined (which files
  count as "in-flight" or "workstream" changes in the app's model), integration with
  CI/CD, or any behavioral differences from the CLI command beyond what the article
  states outright.

## Extracted Claims

### Claim 1: The `/security-review` command now ships in public preview inside the GitHub Copilot app, explicitly reusing the vulnerability-scanning capability already shipped in Copilot CLI

- **Evidence**: Opening paragraph of the changelog, stated as the lead fact of the
  announcement.
- **Confidence**: settled (direct product statement from GitHub's own changelog)
- **Quote**: "You can now run a security review on your in-flight code changes directly from the GitHub Copilot app. The /security-review slash command is shipping in public preview, bringing the same AI-driven vulnerability scanning already available in Copilot CLI into your everyday coding workflow."
- **Our assessment**: This directly answers the Prospector's triage question about
  CLI/app parity: GitHub's own copy asserts this is "the same" scanning capability,
  not a separately built feature that happens to share a name. That's a marketing
  claim, not an engineering guarantee — the article gives no detail on whether the
  app surface invokes the identical backend, prompt, or model version as the CLI
  command documented in `docs-github-copilot-cli-security-review.md` (Claim 1). What
  is verifiable is that both surfaces target the same five vulnerability categories
  (see Claim 3) and the app's first output bullet is word-for-word identical to the
  CLI's stated output (see Claim 2) — corroborating evidence for "same capability,"
  even if not proof of an identical implementation.

### Claim 2: The command's output in the app is a three-part structure — high-confidence findings, actionable suggestions, and a focused prioritized view

- **Evidence**: The "What it does" section lists three explicit output bullets.
- **Confidence**: settled (stated directly in the changelog)
- **Quote**: "High-confidence security findings, scored by severity and confidence. Actionable suggestions you can apply and reverify without leaving Copilot. A focused, prioritised view so you can fix the issues that matter before code lands."
- **Our assessment**: The first bullet ("High-confidence security findings, scored by
  severity and confidence") is a verbatim match to the CLI announcement's stated
  output (`docs-github-copilot-cli-security-review.md`, Claim 2), which reused
  identical marketing copy — strong internal evidence the two changelog entries
  describe the same underlying scoring model. The third bullet — a "focused,
  prioritised view" — is new phrasing not present as a distinct bullet in the CLI
  note's extraction; whether this is a genuinely new app-specific feature or simply a
  detail the CLI's miner didn't capture verbatim cannot be determined from this source
  alone. Notably this article uses British spelling ("prioritised," "analyses"),
  suggesting a different (or at least differently-edited) copy source than the CLI
  changelog, which is a weak signal against the two being a single reused press
  release.

### Claim 3: The app's scan targets the same five vulnerability categories as the CLI command: injection flaws, cross-site scripting, insecure data handling, path traversal, and weak cryptography

- **Evidence**: Stated directly following the output bullets in "What it does."
- **Confidence**: settled (stated as product scope in the changelog)
- **Quote**: "The scan is tuned to catch common, high-impact vulnerability classes such as injection flaws, cross-site scripting, insecure data handling, path traversal and weak cryptography."
- **Our assessment**: This is an exact match to the five categories documented for the
  CLI command in `docs-github-copilot-cli-security-review.md` (Claim 3), which is the
  strongest corroborating evidence in this source that the app and CLI commands share
  a detection engine rather than being independently built with coincidentally similar
  scope. The phrase "such as" leaves the list open-ended (not "limited to"), which is a
  subtle wording difference worth flagging — it is slightly less bounded than the CLI
  changelog's implied exhaustive five-category list, though in practice the enumerated
  categories are identical.

### Claim 4: The app command is positioned as complementary to GitHub code scanning, Dependabot, and secret scanning — a lightweight, on-demand check on local changes performed without leaving the coding environment

- **Evidence**: The "Why it matters" section states the positioning directly.
- **Confidence**: settled (stated directly in the changelog)
- **Quote**: "The /security-review command gives you a way to catch issues while you're still working without leaving your coding environment. It complements GitHub code scanning, Dependabot, and secret scanning by giving you a lightweight, on-demand check on your local changes."
- **Our assessment**: This positioning statement is thematically identical to the
  CLI's framing in `docs-github-copilot-cli-security-review.md` (Claim 4 and Claim 5:
  "a lightweight, on-demand way to review your changes before you commit") but is not
  a verbatim match — the wording is paraphrased/rewritten between the two changelog
  entries even though the underlying claim (complements pipeline tools, doesn't
  replace them) is the same. This is useful evidence: GitHub is consistent in message
  even where copy isn't literally reused, reinforcing that this is a deliberate,
  coordinated product positioning rather than an accidental overlap.

### Claim 5: The app command is available to Copilot Free, Pro, Business, and Enterprise plans during public preview, with no `/experimental on` or equivalent opt-in flag mentioned

- **Evidence**: The "How to try it" section states plan availability and the access
  steps (open a project, make changes, run the command) without referencing any
  experimental-mode toggle.
- **Confidence**: settled for plan availability (explicitly stated); emerging/absent
  for the opt-in-gating comparison (this is an absence of evidence, not a stated fact)
- **Quote**: "Open a project in the Copilot app, make your code changes, and run /security-review to scan those changes. The command is available to Copilot Free, Pro, Business, and Enterprise users during public preview."
- **Our assessment**: This is the most concrete parity difference this source
  surfaces. `docs-github-copilot-cli-security-review.md` (Claim 1) documents the CLI
  command as gated behind `/experimental on` — a mode developers must explicitly
  enable. This app-surface changelog describes accessing the command with no mention
  of an equivalent toggle: just open a project and run the command. Two readings are
  possible: (a) the app surface genuinely has a lower-friction access path than the
  CLI (a real UX/gating difference between surfaces), or (b) the changelog simply
  omitted an access-mode detail that exists but isn't newsworthy for this audience.
  The source does not resolve this ambiguity. This is a conditioning variable (a
  difference between two release channels of the same evolving feature), not a
  factual contradiction between two claims about the same context — no contradiction
  issue filed per MINER.md §4a. It is, however, an open question worth flagging for
  future sources: does the app's public-preview label alone gate access, or is there
  an undocumented settings toggle?

### Claim 6: The command surfaces as a suggested slash command inside the Copilot app's chat window

- **Evidence**: Screenshot embedded in the article with descriptive alt text.
- **Confidence**: settled (visual product evidence, image alt text)
- **Quote**: "The /security-review appearing as a suggested command in the GitHub Copilot app chat window"
- **Our assessment**: This confirms the app surface is chat-based (conversational
  slash-command entry), distinct from the CLI's terminal invocation model. It also
  implies discoverability via autocomplete/suggestion in the chat input — a lower
  barrier to finding the command than the CLI, where a developer must already know to
  type `/security-review` after enabling experimental mode. This is a UX advantage of
  the app surface independent of any backend-capability question.

### Claim 7: GitHub directs feedback on this feature to a public GitHub Community discussions category rather than a private support channel

- **Evidence**: Closing line of the "How to try it" section, with an outbound link.
- **Confidence**: settled (stated directly, with a live link in the source)
- **Quote**: "Join the discussion and share your feedback in the GitHub Community."
- **Our assessment**: Public-preview features routed to a public community forum
  (rather than a private beta channel) is consistent with GitHub's general public
  preview pattern for other Copilot features covered elsewhere in the corpus (e.g.,
  the CLI's `/feedback` command documented in
  `docs-github-copilot-cli-security-review.md`, Concrete Artifacts). It signals GitHub
  expects and wants broad usage feedback during the preview window, which typically
  precedes changes before GA — teams adopting this now should expect behavior to
  shift before the feature stabilizes.

## Concrete Artifacts

### Article structure (verbatim section headers, from page HTML)

```
H1: Security reviews now available in the GitHub Copilot app
H3: What it does
H3: Why it matters
H3: How to try it

Metadata (from page <script type="application/ld+json"> and <meta> tags):
  Author:          Allison
  datePublished:   2026-07-14T12:54:12+00:00 (05:54:12-07:00)
  dateModified:    2026-07-14T13:02:40+00:00
  Reading time:    2 minutes (twitter:data1 meta tag)
  Article class:   editorial-typography Type--improvements  (i.e. changelog category "Improvement")
  Canonical URL:   https://github.blog/changelog/2026-07-14-security-reviews-now-available-in-the-github-copilot-app/
```

*Source: raw HTML of the changelog page, fetched directly (not via summarizing
WebFetch) to guarantee verbatim extraction — see Extraction Notes.*

### App vs. CLI comparison table (synthesized from this source + `docs-github-copilot-cli-security-review.md`)

```
Dimension                  Copilot CLI (June 10, 2026)        Copilot app (July 14, 2026)
──────────────────────────────────────────────────────────────────────────────────────────
Access gating stated       /experimental on required          none mentioned
Invocation surface         terminal slash command              chat window, suggested command
Vulnerability categories   injection, XSS, insecure data       injection, XSS, insecure data
                            handling, path traversal,           handling, path traversal,
                            weak cryptography (5, exhaustive)   weak cryptography ("such as" — 5 listed)
Output — bullet 1          "High-confidence security           "High-confidence security
                            findings, scored by severity         findings, scored by severity
                            and confidence" (verbatim match)     and confidence" (verbatim match)
Output — bullet 2          actionable recommendations,          "Actionable suggestions you can
                            in-terminal actionable               apply and reverify without
                                                                  leaving Copilot"
Output — bullet 3          not captured as distinct bullet      "A focused, prioritised view so
                            by CLI note's extraction             you can fix the issues that
                                                                  matter before code lands"
Positioning vs. pipeline    "doesn't rely on GitHub code         "complements GitHub code
tools                       scanning, Dependabot, or GitHub      scanning, Dependabot, and
                            secret scanning"                     secret scanning"
Plan-tier availability      not stated in CLI changelog          Free, Pro, Business, Enterprise
                            (gap noted in that note's            (explicitly stated)
                            Source Context)
```

*Synthesized by the Miner from this source and the cross-referenced CLI note; not a
verbatim artifact from either source.*

## Cross-References

- **Corroborates** `docs-github-copilot-cli-security-review.md` (Claim 2): The app
  changelog's first output bullet — "High-confidence security findings, scored by
  severity and confidence" — is a verbatim match to the CLI note's Claim 2 quote of
  the same phrase. This is strong evidence the two surfaces share the same underlying
  scoring model, not just a coincidentally similar feature name.

- **Corroborates** `docs-github-copilot-cli-security-review.md` (Claim 3): The five
  vulnerability categories (injection, XSS, insecure data handling, path traversal,
  weak cryptography) are identical between the CLI and app announcements — the
  strongest evidence in this source that both surfaces run the same detection scope.

- **Extends** `docs-github-copilot-cli-security-review.md` (Claim 1): That note
  established `/security-review` as an experimental, `/experimental on`-gated CLI
  command. This source extends the command to a second surface (the Copilot app) and
  adds plan-tier availability detail (Free/Pro/Business/Enterprise) that the CLI note
  explicitly flagged as missing from its own source (see that note's Source Context:
  "Does NOT cover: ... plan-tier availability details"). This source fills that gap,
  at least for the app surface — it does not retroactively confirm CLI plan-tier
  gating.

- **Extends** `docs-github-copilot-cli-security-review.md` (Claim 4 and Claim 5): Both
  sources position `/security-review` as complementary to (not a replacement for)
  GitHub's pipeline security tools (code scanning, Dependabot, secret scanning) and as
  a lightweight, on-demand, pre-landing check. The core positioning claim is
  consistent across both surfaces, though the two changelogs use different wording
  rather than reused copy (see Claim 4 above) — this is corroboration of intent, not
  a literal text match.

- **Related** `docs-github-copilot-web-contextual-chat.md`: That May 18, 2026 note
  documents "Copilot on web," an in-page contextual chat panel embedded in GitHub
  pages (PRs, issues) — a different surface from the "GitHub Copilot app" this source
  describes, which the screenshot alt text shows as its own dedicated chat window with
  suggested-command autocomplete. The two notes should not be treated as describing
  the same product surface; this source gives no indication that `/security-review`
  is also available inside the in-page "Copilot on web" panel documented there.

- **Related** `docs-github-copilot-security-validation-third-party-agents.md`: That
  note documents a structurally different feature — automatic, always-on, default
  CodeQL/Advisory-Database/secret-scanning validation applied to code generated by
  Claude and Codex agents on GitHub, with no developer-invoked command. This source's
  `/security-review` is developer-initiated and Copilot-specific (not available for
  third-party agent output). The two features occupy different positions in a
  security-tooling taxonomy: platform-automatic validation (that note) vs.
  developer-initiated scanning (this note) — worth distinguishing in the guide rather
  than conflating as "GitHub's AI security tooling."

- **Contradicts**: None filed. The access-gating difference noted in Claim 5 (no
  `/experimental on` equivalent mentioned for the app surface, vs. the CLI's explicit
  requirement) is a difference in *stated* access mechanics across two release-channel
  announcements for an evolving feature, not two sources making opposing factual
  claims about the same context — per MINER.md §4a ("differ only in context ... that's
  a conditioning variable"), this does not meet the bar for a contradiction issue.

- **Novel**:
  - **First documented cross-surface extension of a named Copilot security command**:
    No prior corpus source documents the same named slash command (`/security-review`)
    shipping to a second distinct product surface with an explicit "same capability"
    claim from the vendor. This establishes a pattern worth watching: GitHub appears
    to be building security-review capability once and distributing it across
    surfaces (CLI, now app) rather than building surface-specific tooling.
  - **Explicit plan-tier availability for a security-review feature**: This is the
    first corpus source to state which Copilot plan tiers (Free through Enterprise)
    can access an AI-driven security-scanning command — the CLI announcement did not
    specify this.

## Guide Impact

### Chapter 03: Safety and Verification

- **Update the `/security-review` entry to note the two-surface availability**: The
  guide's coverage of `/security-review` (informed by
  `docs-github-copilot-cli-security-review.md`) should be updated to state the
  command is now available in both Copilot CLI (experimental, `/experimental on`) and
  the Copilot app (public preview, no stated opt-in, available on all plan tiers
  including Free). Recommend the guide present the app surface as the lower-friction
  on-ramp for teams not already using Copilot CLI.
- **Flag the unresolved access-gating question**: The guide should note as an open
  question (not a settled fact) whether the app surface has any access gating
  equivalent to the CLI's `/experimental on`, since this source does not state one
  exists or doesn't — only that the changelog didn't mention it.

### Chapter 05: Tools and Frameworks — Copilot

- **Add a surface-availability note to the Copilot CLI feature matrix**: The matrix
  built from `docs-github-copilot-cli-security-review.md` (Concrete Artifacts →
  "Updated Copilot CLI Verification and Feature Matrix") should be extended with a
  column or note indicating `/security-review` is also available in the Copilot app,
  gated only by public-preview status and plan tier (Free/Pro/Business/Enterprise) —
  not by an experimental flag as in the CLI.
- **Distinguish this feature from platform-level agent validation**: When discussing
  GitHub's AI-driven security tooling in Chapter 05, keep `/security-review`
  (developer-initiated, Copilot-only, this note and the CLI note) distinct from the
  automatic CodeQL/Advisory-Database/secret-scanning validation applied to third-party
  agent output (`docs-github-copilot-security-validation-third-party-agents.md`) —
  they are different tools with different trigger models and should not be described
  as the same capability in the guide.

## Extraction Notes

1. **WebFetch summarization risk avoided by direct HTML fetch**: An initial WebFetch
   call against this URL returned content processed by a summarizing model, including
   a "Read time: 1 minute" figure. Cross-checking against the raw page HTML's
   `twitter:data1` meta tag showed the actual stated reading time is "2 minutes" —
   the WebFetch summary was measurably wrong on a factual detail. Because of this
   discrepancy, all quotes and facts in this note were re-verified against a direct
   `curl` fetch of the live page HTML (saved locally during extraction), not the
   WebFetch summary. Every `Quote` field above was copied character-for-character
   from the `<article>` content in that raw HTML.
2. **No sub-pages followed**: The changelog is a single short entry (~180 words) with
   one outbound link (to a GitHub Community discussions category, not a documentation
   sub-page). No further pages were substantive enough to warrant following per
   MINER.md §1.
3. **British spelling in source copy**: The article uses "prioritised" and "analyses"
   (British/international spelling), differing from the CLI changelog's copy. Noted
   under Claim 2 as a weak signal that the two changelog entries were not produced
   from a single shared press-release template, even though their factual content
   (vulnerability categories, first output bullet) matches closely.
4. **No contradictions filed**: The one notable cross-surface difference (access
   gating: CLI requires `/experimental on`, app changelog states none) is treated as
   a conditioning variable between two release-channel announcements, not a factual
   contradiction — see Cross-References → Contradicts. No contradiction issue opened.
