---
source_url: https://openai.com/index/bio-bug-bounty
source_type: blog-post
title: "OpenAI Bio Bug Bounty"
author: OpenAI (unsigned corporate voice)
date_published: 2026-07-09
date_extracted: 2026-07-26
last_checked: 2026-07-26
status: current
confidence_overall: emerging
issue: "#2243"
---

# OpenAI Bio Bug Bounty

> OpenAI announces it is converting its GPT‑5.5 Bio Bug Bounty into an ongoing,
> private, NDA-gated program — the "OpenAI Bio Bounty Program" — that pays up
> to $50,000 (raised from $25,000) for a single prompt that produces a
> "universal jailbreak" defeating a predefined biosafety challenge, with
> access restricted to a vetted list of trusted bio red-teamers rather than
> run as a public bounty.

## Source Context

- **Type**: blog-post (official `openai.com/index/` announcement, "Safety"
  category, published July 9, 2026, unsigned/institutional byline). Very
  short — roughly 250 words of body text across two sections ("Invitation"
  and "How to participate"), plus a CTA button and links to a program
  application portal and two adjacent bug-bounty programs.
- **Author credibility**: First-party institutional statement from OpenAI
  about the terms of its own bug-bounty program. This is the authoritative
  source for *what the program's stated terms are* (reward amounts, scope,
  application mechanics), but — like other first-party OpenAI program
  announcements in this corpus — it discloses no information about program
  outcomes: no count of applicants, no report of whether any universal
  jailbreak has ever been found or paid out under either the original or
  evolved program, and no description of the actual biosafety questions
  used in the challenge.
- **Scope**: Covers the transition from the "GPT‑5.5 Bio Bug Bounty" to an
  ongoing "OpenAI Bio Bounty Program," the reward increase, the scope
  timeline for the transition, and high-level application mechanics. Does
  NOT cover: the content of the five biosafety questions being tested, any
  results or findings to date, how many researchers are currently enrolled,
  independent verification of program integrity, or comparison to
  competitors' bio-safety bounty programs.

## Extracted Claims

### Claim 1: OpenAI is evolving its GPT‑5.5 Bio Bug Bounty into an ongoing private program, the "OpenAI Bio Bounty Program," which will remain focused on universal jailbreaks against a predefined biosafety challenge, starting with GPT‑5.6 going forward
- **Evidence**: Direct statement in the announcement's opening paragraph.
- **Confidence**: settled (first-party statement of program structure and naming)
- **Quote**: "As part of our ongoing efforts to strengthen our safeguards for advanced AI capabilities in biology, we're evolving our GPT‑5.5 Bio Bug Bounty to become an ongoing private program—the OpenAI Bio Bounty Program. The program will remain focused on universal jailbreaks that can defeat our predefined biosafety challenge against OpenAI's frontier models, starting with GPT‑5.6 and going forward."
- **Our assessment**: The load-bearing word is "private" — OpenAI is explicitly moving from what was framed as a bounded, time-boxed cohort program (see Claim 6/7, sourced from the linked application portal) to a standing, ongoing arrangement, still gated by invitation/vetting rather than opened to the general public. This is a governance-mechanism claim (how OpenAI structures adversarial testing for a catastrophic-risk-adjacent capability), not a capability or safety-outcome claim.

### Claim 2: The reward for a universal jailbreak under the OpenAI Bio Bounty Program has been raised from $25,000 to $50,000, applicable to both GPT‑5.6 and GPT‑5.5, with smaller discretionary awards for partial wins
- **Evidence**: Direct statement in the announcement.
- **Confidence**: settled (first-party, specific, checkable dollar figures)
- **Quote**: "We're also excited to announce that we're increasing reward amounts. The reward for a universal jailbreak for the OpenAI Bio Bounty Program has been raised from $25,000 to $50,000 for both GPT‑5.6 and GPT‑5.5. Smaller awards may be granted for partial wins at our discretion."
- **Our assessment**: A concrete, doubled financial incentive for finding a specific failure mode ("universal jailbreak" against a biosafety challenge) is a checkable governance data point, but the announcement gives no baseline for whether $25,000 was previously sufficient to attract findings, or why $50,000 was judged necessary now — the reasoning for the increase (e.g., difficulty, insufficient participation, a specific incident) is not disclosed.

### Claim 3: OpenAI will continue to honor the original GPT‑5.5 Bio Bounty Program's scope through July 27, 2026, after which only GPT‑5.6 will be in scope, with further scope changes to be communicated to researchers directly
- **Evidence**: Direct statement of the transition timeline.
- **Confidence**: settled (first-party stated timeline)
- **Quote**: "We will continue to honor the scope for the GPT‑5.5 Bio Bounty Program as originally announced, with testing ending on July 27, 2026. After this date, only GPT‑5.6 will be in scope; we will continue to communicate any future changes in scope to our researchers."
- **Our assessment**: This confirms the article was published (2026-07-09) roughly 18 days before the older program's stated end date, and that scope communication happens through a private researcher channel rather than public updates to this page — meaning outside readers (including this note) cannot track future scope changes from the public article alone.

### Claim 4: Interested applicants apply through a rolling application process; accepted applicants are onboarded to the bio bug bounty platform, and researchers previously accepted into the GPT‑5.5 Bio Bounty Program do not need to reapply
- **Evidence**: Direct statement of application mechanics.
- **Confidence**: settled (first-party stated process)
- **Quote**: "Interested applicants should apply through our rolling application process⁠. Once selected, accepted applicants will be onboarded to the bio bug bounty platform. All past applicants to the GPT‑5.5 Bio Bounty Program will not need to reapply."
- **Our assessment**: "Rolling" plus no-reapplication-needed for prior participants indicates OpenAI intends continuity of its existing vetted researcher pool into the new program, not a fresh open call — consistent with Claim 1's "private" framing.

### Claim 5: To participate, applicants submit a short application (name, affiliation, experience); accepted applicants must already hold a ChatGPT account and must sign an NDA
- **Evidence**: Direct statement under the "How to participate" heading.
- **Confidence**: settled (first-party stated eligibility/process requirements)
- **Quote**: "Submit a short application here⁠ (name, affiliation, experience). Accepted applicants must have existing ChatGPT accounts to apply, and will sign a NDA. Apply now and help us make frontier AI safer."
- **Our assessment**: The application bar is minimal on paper (three fields), but the ChatGPT-account and mandatory-NDA requirements, combined with Claim 7 below (invitation to "a vetted list of trusted bio red-teamers"), indicate the real gate is OpenAI's discretionary vetting/invitation step, not the application form itself.

### Claim 6: Per the linked GPT‑5.5 Bio Bounty Program application-portal page, the program's actual biosafety challenge is to identify a single universal jailbreaking prompt that gets the model to answer all five predefined bio safety questions "from a clean chat without prompting moderation," and the model in scope was narrowly defined as "GPT‑5.5 in Codex Desktop only"
- **Evidence**: The article's top-of-page "Apply here" button links directly to this program listing (`openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program`), which is OpenAI's own official description of the challenge for the original GPT‑5.5 program — the one the announcement (Claim 3) says continues to be honored through July 27, 2026.
- **Confidence**: settled (first-party program description, directly linked from the article as its primary call-to-action)
- **Quote**: "Model in scope: GPT-5.5 in Codex Desktop only. Challenge: Identify one universal jailbreaking prompt to successfully answer all five bio safety questions from a clean chat without prompting moderation." (from `openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program`, "Program overview" section, captured via the same Wayback Machine snapshot window as the announcement)
- **Our assessment**: This is the single most concrete technical detail in either page and is not stated anywhere in the announcement article itself — the challenge is narrower and more specific than "test GPT‑5.5 for bio risk" in two ways: (1) it's scoped to a fixed set of five predefined questions, not open-ended probing, and (2) the model-in-scope is specifically "GPT‑5.5 in Codex Desktop," an agentic coding surface, not general ChatGPT. Whether the evolved "OpenAI Bio Bounty Program" (GPT‑5.6 onward, per Claim 1) uses the same five-question/single-prompt/clean-chat challenge design is not stated in either source — this claim describes the original program's terms, which the announcement says are being honored unchanged through the transition window, not confirmed terms for the new program.

### Claim 7: Per the same linked program page, access to the GPT‑5.5 Bio Bounty Program is by invitation to "a vetted list of trusted bio red-teamers," combined with review of new applications — not an open public bounty
- **Evidence**: Direct statement in the program listing's "Access" field.
- **Confidence**: settled (first-party stated access model)
- **Quote**: "Access: Application and invites We will extend invitations to a vetted list of trusted bio red-teamers and review new applications. Once selected, successful applicants will be onboarded to the Safety - Bio Bug Bounty platform." (from `openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program`)
- **Our assessment**: This confirms the "private" framing in Claim 1 is not new to the evolved program — the original GPT‑5.5 program was already invitation/vetting-gated, not a general public bounty. The evolution described in the announcement is about program duration (time-boxed → ongoing) and reward amount, not about broadening public access.

### Claim 8: The program page states that all prompts, completions, findings, and communications under the GPT‑5.5 Bio Bounty Program are covered by NDA, and the announcement separately points readers to OpenAI's distinct public "Safety Bug Bounty" and "Security Bug Bounty" programs (both hosted on Bugcrowd) for non-biosafety vulnerability reporting
- **Evidence**: Direct statement from the program page plus a direct statement from the announcement article distinguishing the bio program from its general-purpose bounty programs.
- **Confidence**: settled (first-party stated disclosure policy and program taxonomy)
- **Quote**: "Disclosure: All prompts, completions, findings, and communications are covered by NDA." (from `openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program`) / "If you're interested in supporting OpenAI's work to deliver safe and secure artificial intelligence beyond the Bio Bounty program, you can learn about our Safety Bug Bounty⁠ and Security Bug Bounty⁠⁠ programs." (from the announcement article)
- **Our assessment**: This establishes that OpenAI runs at least three structurally distinct bug-bounty tracks: a public, Bugcrowd-hosted Security Bug Bounty; a public, Bugcrowd-hosted Safety Bug Bounty; and a closed, NDA-gated, invitation-only Bio Bounty Program specifically for biosafety universal jailbreaks. The blanket NDA over "all prompts, completions, findings, and communications" means no public disclosure mechanism exists for this program's results even in aggregate (e.g., no public count of submissions or successful jailbreaks) — readers cannot independently verify how effective or active the program is from any public source.

## Concrete Artifacts

### Full body text of the announcement (verbatim, both sections)

```
Source: https://openai.com/index/bio-bug-bounty (July 9, 2026; "Safety" category)
Title: OpenAI Bio Bug Bounty
Subhead: Testing for universal jailbreaks for biorisks

[Invitation]
As part of our ongoing efforts to strengthen our safeguards for advanced AI
capabilities in biology, we're evolving our GPT‑5.5 Bio Bug Bounty to become
an ongoing private program—the OpenAI Bio Bounty Program. The program will
remain focused on universal jailbreaks that can defeat our predefined
biosafety challenge against OpenAI's frontier models, starting with GPT‑5.6
and going forward.

We're also excited to announce that we're increasing reward amounts. The
reward for a universal jailbreak for the OpenAI Bio Bounty Program has been
raised from $25,000 to $50,000 for both GPT‑5.6 and GPT‑5.5. Smaller awards
may be granted for partial wins at our discretion.

We will continue to honor the scope for the GPT‑5.5 Bio Bounty Program as
originally announced, with testing ending on July 27, 2026. After this date,
only GPT‑5.6 will be in scope; we will continue to communicate any future
changes in scope to our researchers.

Interested applicants should apply through our rolling application process.
Once selected, accepted applicants will be onboarded to the bio bug bounty
platform. All past applicants to the GPT‑5.5 Bio Bounty Program will not
need to reapply.

[How to participate]
Submit a short application here (name, affiliation, experience). Accepted
applicants must have existing ChatGPT accounts to apply, and will sign a
NDA. Apply now and help us make frontier AI safer.

If you're interested in supporting OpenAI's work to deliver safe and secure
artificial intelligence beyond the Bio Bounty program, you can learn about
our Safety Bug Bounty and Security Bug Bounty programs.
```

### Original GPT‑5.5 Bio Bounty Program listing (verbatim, from linked application portal)

```
Source: https://openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program
(captured in the same Wayback Machine snapshot window as the announcement,
2026-07-09; this is the article's own "Apply here" destination)

Program: GPT-5.5 Bio Bounty Program
Opens: Apr 23 2026 08:00 AM (PDT)
Deadline: Jun 22 2026 11:59 PM (PDT)
Value: $0.00 to $25,000.00

Program overview
Model in scope: GPT-5.5 in Codex Desktop only.
Challenge: Identify one universal jailbreaking prompt to successfully
  answer all five bio safety questions from a clean chat without
  prompting moderation.
Rewards: $25,000 to the first true universal jailbreak to clear all five
  questions. Smaller awards may be granted for partial wins at our
  discretion.
Timeline: Applications open April 23, 2026, with rolling acceptances. If
  you are not accepted in the initial cohort, your application may still
  be accepted in future cohorts; you do not need to reapply to the
  program.
Access: Application and invites. We will extend invitations to a vetted
  list of trusted bio red-teamers and review new applications. Once
  selected, successful applicants will be onboarded to the Safety - Bio
  Bug Bounty platform.
Disclosure: All prompts, completions, findings, and communications are
  covered by NDA.
```

## Cross-References

- **Extends**: `blog-openai-gpt5-immunology-mystery.md` Claim 7 (OpenAI's
  own dual-use framing: "AI could help researchers move faster in biology
  and medicine, but those capabilities could also lower barriers for
  misuse... citing its Preparedness Framework"). That note only recorded
  an abstract policy reference to the Preparedness Framework as the stated
  mitigation for bio dual-use risk. This source is a concrete, operational
  instance of that mitigation: a named, dollar-figured, ongoing bug-bounty
  program specifically targeting universal jailbreaks against a biosafety
  challenge. Read together, the two notes move the corpus from "OpenAI says
  it manages bio dual-use risk via its Preparedness Framework" to "here is
  one specific adversarial-testing mechanism OpenAI funds under that
  framework, and its stated terms."
- **Corroborates / contrasts**: `blog-simonwillison-aisi-gpt55-cyber.md`
  Claim 6 (UK AISI's expert red-teamers "identified a universal jailbreak
  that elicited violative content across all malicious cyber queries" for
  GPT‑5.5 in approximately 6 hours, with OpenAI's subsequent safeguard fix
  left unverified due to a configuration issue). Both sources use the same
  specific term — "universal jailbreak" — for a frontier-model safety
  failure mode, and both concern GPT‑5.5-generation models within roughly
  the same publication window. The mechanisms differ sharply: AISI's
  finding came from a government-commissioned, time-boxed expert
  evaluation (unpaid, one report, verification later blocked); this
  source describes an open-ended, financially incentivized ($25k–$50k),
  ongoing, NDA-gated private bounty program for the same class of failure
  in a different risk domain (bio vs. cyber). Neither source states
  whether a universal jailbreak has actually been found and paid out under
  the Bio Bounty Program — this source discloses program terms, not
  results, so the two should not be read as evidence that bio-domain
  safeguards are either more or less robust than the cyber-domain ones
  AISI tested.
- **Related but distinct**: `blog-openai-government-national-security-partnerships.md`
  Claim 5 (OpenAI "announced expanded trusted access to our GPT‑Rosalind
  model for select U.S. government and allied partners supporting public
  health and biodefense missions"). Both sources are OpenAI biosecurity-
  adjacent governance announcements from within a month of each other
  (GPT‑Rosalind government access: referenced as "last month" in the
  2026-07-08 partnerships post; this Bio Bug Bounty update: 2026-07-09).
  They describe different mechanisms for different audiences, however:
  GPT‑Rosalind access-expansion is about which government entities may use
  a specific model for biodefense work, while the Bio Bounty Program is
  about paying private researchers to find universal jailbreaks against
  GPT‑5.5/GPT‑5.6's safety controls. Both should be read as parts of
  OpenAI's broader biosecurity governance posture in mid-2026, not as the
  same program under two names — this note found no textual link between
  them.
- **Novel**: First source in the corpus to document (a) a named, ongoing,
  dollar-figured OpenAI bug-bounty program specifically for biosafety
  universal jailbreaks, with a reward increase disclosed; (b) the actual
  mechanics of a *closed*, invitation/vetting-gated, NDA-blanketed
  red-teaming program, as distinct from the public Bugcrowd-hosted safety
  and security bounty model documented elsewhere; and (c) a concrete,
  narrowly-scoped example of what a "universal jailbreak" biosafety
  challenge looks like in practice (five fixed questions, single prompt,
  clean chat, no moderation triggered, scoped to a specific product
  surface — "GPT‑5.5 in Codex Desktop only").
- **Contradicts**: None identified. No existing source note stakes out a
  position on bio-bounty program structure or reward economics that this
  source disagrees with.

## Guide Impact

- **Chapter 06 (Security and Threat Model)**: The chapter currently has no
  content on AI-safety-specific bug bounty programs or on "universal
  jailbreak" as a named vulnerability class. Recommend adding a short note
  citing this source's Claim 2 (paid, scaled financial incentive — up to
  $50,000 — for a single working universal-jailbreak prompt against a
  frontier model's safety layer) alongside `blog-simonwillison-aisi-gpt55-cyber.md`
  Claim 6 (an unpaid, commissioned expert red-team found an analogous
  universal jailbreak for GPT‑5.5's cyber controls in ~6 hours) as two
  contrasting real-world mechanisms labs use to source adversarial testing
  for catastrophic-risk-adjacent model capabilities: paid/open-ended/vetted
  private bounty vs. commissioned/time-boxed government evaluation.
  Practitioners building their own harness-level safety controls for
  high-stakes domains should not assume model-provider safety layers are
  adversarially hardened by default — both sources show frontier labs
  still treat "does a universal jailbreak exist" as an open, actively
  paid/commissioned question for their current models.
- **Chapter 06, same section**: This source's Claim 8 (three structurally
  distinct OpenAI bounty tracks — public Security, public Safety, and
  closed/NDA'd Bio) is a citable example of tiered vulnerability-disclosure
  program design by risk sensitivity, worth noting for any guide discussion
  of how organizations should structure red-teaming/bounty programs for
  systems with catastrophic-risk-adjacent failure modes versus ordinary
  security bugs.
- **No chapter should cite this source as evidence of GPT‑5.5/GPT‑5.6's
  actual biosafety robustness** — the source discloses program *terms*
  (rewards, scope, application process) only. It contains no information
  on whether any jailbreak has been found, how many researchers are
  enrolled, or how the challenge questions were validated, so it cannot
  support any claim about how safe or unsafe these models currently are
  against biosafety jailbreaks.

## Extraction Notes

1. **Direct fetch blocked (403)**: `https://openai.com/index/bio-bug-bounty`
   returned HTTP 403 to WebFetch, consistent with other `openai.com/index/`
   posts in this corpus. Recovered via the Wayback Machine CDX API
   (`web.archive.org/cdx/search/cdx?url=openai.com/index/bio-bug-bounty*&output=json`),
   which surfaced a snapshot at `20260709174112` with HTTP status 200 (the
   same-day 403 snapshot at `20260709173359` was skipped in favor of this
   working one). Fetched directly via `curl` and HTML-stripped for
   full-text extraction; quotes in this note were re-verified against the
   raw HTML (not the stripped text) to preserve exact punctuation
   (em-dashes, curly quotes, non-breaking hyphens in "GPT‑5.5"/"GPT‑5.6").
2. **One substantive linked page followed**: The article's primary "Apply
   here" call-to-action button links to
   `https://openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program`, a
   SurveyMonkey Apply-hosted program listing that contains program
   mechanics (model scope, exact challenge description, timeline,
   access/vetting model, disclosure terms) not stated anywhere in the blog
   post itself. This page was fetched (via the same Wayback Machine
   snapshot window, `curl -L`, HTTP 200) and is the source for Claims 6–8.
   Because this listing is explicitly for the *original* GPT‑5.5 Bio
   Bounty Program (not the newly announced ongoing "OpenAI Bio Bounty
   Program"), Claims 6–8 are scoped accordingly in their assessments —
   readers should not assume the evolved program's challenge design is
   identical, only that the announcement says the original program's scope
   is being honored unchanged through July 27, 2026.
3. **Other linked pages not usable**: The "Submit a short application
   here" / "rolling application process" links both point to the same
   Google Form intake page; the archived Wayback snapshot of that URL
   returned only the Wayback Machine's own wrapper content, not the form
   itself, so no additional detail could be extracted from it. The two
   Bugcrowd links ("Safety Bug Bounty," "Security Bug Bounty") are
   JavaScript-rendered single-page applications; their archived HTML
   snapshots returned no usable body text (only page `<title>` and nav
   chrome). Both are cited above only via what the announcement article
   itself states about them (Claim 8), not via independently fetched
   content from those pages.
4. **Discrepancy noted, not extracted as a claim**: The `smapply.org`
   program-listing snapshot, captured the same day as the announcement
   (2026-07-09), still displayed the pre-increase $25,000 reward figure
   and a "Deadline: Jun 22 2026" that had already passed relative to the
   capture date — i.e., the public program-listing page had visibly not
   yet been updated to reflect either the reward increase or the "rolling"
   ongoing-acceptance framing announced the same day. This is treated as a
   publishing-lag observation about page staleness, not a claim the source
   makes about itself, and is not extracted as a numbered claim per
   MINER.md §2a (no fabricated claim of intent — it may simply be a CMS
   update that lagged the blog post by hours or days).
5. **No contradictions with existing source notes identified**; none filed
   per MINER.md §4a.
