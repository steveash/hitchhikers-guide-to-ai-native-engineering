---
source_url: https://claude.com/blog/how-people-are-using-claude-cowork
source_type: blog-post
title: "How people are using Claude Cowork"
author: Anthropic
date_published: 2026-07-07
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1687"
---

# How people are using Claude Cowork

> First-party Anthropic usage-analytics post classifying 1.2 million anonymized Claude
> Cowork sessions (May 2026) into a 20-category task taxonomy, quantifying for the first
> time in the corpus that "business process and operations" (33.4%) and "content creation
> and copywriting" (16.4%) — the connective, non-core-responsibility "work around the work"
> — together make up roughly half of all Cowork usage, with software development and DevOps
> combined at only 15.7%.

## Source Context

- **Type**: blog-post (first-party Anthropic usage-analytics report, claude.com/blog;
  published July 7, 2026)
- **Author credibility**: Anthropic itself, presenting an internal telemetry analysis of
  its own product. Authoritative on what the raw classification data shows, but not an
  independent third-party study — Anthropic has an interest in presenting Cowork adoption
  favorably. The post is unusually transparent about method and limitations (see
  "Additional details about our research" section), which raises confidence relative to
  the vaguer usage characterizations in prior Cowork posts.
- **Scope**: Covers only the categorical distribution of task types across a sampled window
  of Cowork sessions (May 11–31, 2026) and Anthropic's interpretation of what that
  distribution implies about knowledge work. Does NOT cover: per-role or per-industry
  breakdowns beyond the two illustrative examples (lawyer, hiring manager, team lead),
  time-savings or productivity metrics, session-level workflow detail, enterprise
  governance features, or comparisons to Claude Chat. No sub-pages were linked from the
  article; the "Additional details about our research" section is part of the same page
  (methodology/limitations appendix), not a separate URL.

## Extracted Claims

### Claim 1: Roughly half of Claude Cowork usage is "the work around the work" — tasks common across many jobs but rarely anyone's core responsibility

- **Evidence**: Stated as the headline finding of the post, derived from the categorical
  breakdown (Claims 2-3 below): the top two categories together account for ~49.8% of
  sampled sessions.
- **Confidence**: emerging (first-party characterization of a single sampled month; not
  independently replicated, but backed by disclosed quantitative data rather than vague
  description)
- **Quote**: "In a sample of Claude Cowork sessions, we found that roughly half of all
  usage comprises “the work around the work”—tasks that are part of a broad
  swath of jobs, but are rarely a person’s core responsibility."
- **Our assessment**: This is a quantified, data-backed version of the "surrounding work
  first" pattern that `blog-anthropic-cowork-enterprise.md` (Claim 6) previously asserted
  without numbers ("the vast majority of Claude Cowork usage comes from outside
  engineering teams"). This source doesn't measure engineering vs. non-engineering
  headcount directly, but the category breakdown (Claims 2-4) is consistent with and adds
  hard numbers to that earlier claim.

### Claim 2: "Business process and operations" is the single largest usage category at 33.4% of sampled sessions

- **Evidence**: Categorical breakdown of 1.2M sampled sessions; this category is defined
  as work like "pulling scattered updates into a single report, building onboarding
  checklists, and reconciling spreadsheets."
- **Confidence**: emerging (single-month sample, automated classifier, but a disclosed
  hard number rather than a qualitative claim)
- **Quote**: "the largest category of use is for “business process and
  operations”—things like pulling scattered updates into a single report,
  building onboarding checklists, and reconciling spreadsheets—at 33.4%."
- **Our assessment**: Anthropic itself flags (Claim 9 below) that this category is
  inflated by taxonomy design — it absorbs marketing, finance, and HR work because those
  don't have standalone categories. The 33.4% figure should be read as "the catch-all
  connective-work bucket," not as evidence that a single task type dominates.

### Claim 3: "Content creation and copywriting" is the second-largest category at 16.4% of sampled sessions

- **Evidence**: Defined as "synthesis-intensive business communications work like
  producing drafts, slide decks, posts, and proposals."
- **Confidence**: emerging (same methodology caveats as Claim 2)
- **Quote**: "content creation and copywriting—synthesis-intensive business
  communications work like producing drafts, slide decks, posts, and proposals—at
  16.4%."
- **Our assessment**: Notably, the post frames this category, like business process and
  operations, as "overwhelmingly connective in nature" — assembling and structuring
  information for an audience rather than originating novel ideas. This is consistent
  with `blog-anthropic-cowork-getting-started.md`'s marketing workflow examples (drafts,
  posts) but adds the relative-scale context that getting-started note lacks.

### Claim 4: Software development and DevOps/infrastructure combined account for only 15.7% of Cowork sessions, while Claude Code remains the primary developer surface

- **Evidence**: Software development at 8.7%, DevOps and infrastructure at 7% — the third-
  and fourth-largest categories, but far behind the top two. The post explicitly contrasts
  this with Claude Code usage.
- **Confidence**: emerging (disclosed hard numbers; single-month sample)
- **Quote**: "Developers are much more likely to use Claude Code than Claude Cowork to
  write code, but the work they do in Claude Cowork is the connective, communications-
  focused work that surrounds every role, software engineering included."
- **Our assessment**: This is the cleanest quantitative evidence in the corpus for the
  Chat/Cowork/Code three-surface division described qualitatively in
  `blog-anthropic-cowork-deploy-guide.md` (Claim 1). It shows the division holds even for
  developers themselves: engineers show up in Cowork's data, but for the surrounding
  communications work, not core coding — directly numeric support for a claim that source
  note could only assert qualitatively.

### Claim 5: The remaining categories form a long tail, each individually under 7% of sessions

- **Evidence**: Research and intelligence (6.4%), data analysis and business intelligence
  (5.8%), document processing and extraction (4.1%), sales and revenue operations (4%),
  personal assistance (3.8%), education (2.4%), meeting intelligence (1.8%), with "all
  other categories" (including legal/compliance at 1.3% and customer support at 0.8%,
  per the Limitations section) comprising less than 4% combined.
- **Confidence**: emerging (disclosed hard numbers; single-month sample)
- **Quote**: "All other categories comprised less than 4% of the data set, including
  personal assistance at 3.8%, education at 2.4%, and meeting intelligence at 1.8%."
- **Our assessment**: This is the first corpus source to place `blog-anthropic-bryant-
  cowork-sales.md`'s sales/account-management archetype in aggregate context: sales and
  revenue operations is a real but modest 4% of overall Cowork usage, meaning Bryant's
  detailed account is illustrative of a real but numerically minor category, not a
  dominant use case. Similarly, legal and compliance work (1.3%) is a small slice despite
  the lawyer example the post uses to illustrate value.

### Claim 6: Knowledge workers use Cowork to assemble and structure information so they can spend more time applying domain expertise, not to replace that expertise

- **Evidence**: Three illustrative examples: a lawyer using Cowork for document formatting
  and filing to free up time for legal judgment; a hiring manager using it to schedule
  meetings and synthesize interview feedback to free up time for candidate conversations;
  a team lead using it to produce a slide deck explaining a decision, freeing time to make
  the decision itself.
- **Confidence**: anecdotal (illustrative examples, not measured outcomes; presented as
  interpretation of the aggregate data rather than as case studies with named individuals)
- **Quote**: "A lawyer, for example, might use Claude Cowork to handle document formatting
  and filing, giving them more time to apply their legal judgment to challenging cases."
- **Our assessment**: This is the same "human role shifts to validation, refinement, and
  decision-making" framing as Joel Hron's quote in `blog-anthropic-cowork-enterprise.md`
  (Claim 8), now illustrated with hypothetical (not named) examples rather than a named
  executive quote. It is directionally consistent but adds no new named evidence — treat
  as reinforcement of an existing claim, not independent corroboration.

### Claim 7: The sample was collected via privacy-preserving, capped-rate automated classification, not full-traffic sampling — so figures are shares, not volumes

- **Evidence**: The methodology section states the analysis used "a privacy-preserving
  analysis tool that keeps all user information anonymous; no individual session was read
  by a human analyst," and that sampling was rate-capped rather than proportional to
  traffic.
- **Confidence**: settled (first-party methodology disclosure)
- **Quote**: "The sample is collected at a capped rate—a fixed maximum number of
  sessions per hour—rather than as a fixed percentage of traffic. As a result, every
  number in this report is a share of sampled sessions and not an absolute volume."
- **Our assessment**: This is an important caveat for anyone citing the specific
  percentages: they describe the *composition* of a rate-capped sample, not Cowork's
  total session volume or growth rate, and usage during busier hours is somewhat
  underrepresented. The guide should cite these numbers as relative-share evidence only,
  not as absolute usage volume.

### Claim 8: The taxonomy has no standalone categories for marketing, finance, or HR — those functions are folded into "business process and operations"

- **Evidence**: Explicitly disclosed in the Limitations section as a source of ambiguity
  in interpreting the largest category's size.
- **Confidence**: settled (first-party methodology disclosure)
- **Quote**: "There are no standalone categories for marketing, finance, or HR—those
  functions are best represented by the “business process and operations”
  category, which is likely part of why it occupies a third of all usage."
- **Our assessment**: This is a rare case of a vendor explicitly flagging a limitation
  that could otherwise be read as inflating its own headline number. It should temper how
  confidently the guide cites the 33.4% figure — it is a taxonomy artifact as much as a
  behavioral finding.

### Claim 9: Roughly 5% of sampled sessions are personal, non-work use — the sample is not purely workplace activity

- **Evidence**: Disclosed in the Limitations section, despite the sample being drawn from
  external organizations (not individual consumer accounts).
- **Confidence**: settled (first-party methodology disclosure)
- **Quote**: "the Claude Cowork sessions sampled include some personal, non-work use
  (personal assistance, hobbies, and companionship-style conversations together account
  for roughly 5% of sessions), so the sample doesn’t purely represent workplace
  activity."
- **Our assessment**: This means the "personal assistance" category (3.8%, Claim 5) plus
  parts of other categories reflect non-work use even within an org-sampled dataset. Worth
  noting for any guide claim that treats the full 1.2M sessions as pure workplace
  telemetry.

### Claim 10: Category labels were applied by an automated classifier, not a human reviewer, and ambiguous sessions' classification depends on taxonomy definitions

- **Evidence**: Disclosed in the Limitations section as the "Automated classification"
  caveat.
- **Confidence**: settled (first-party methodology disclosure)
- **Quote**: "Category labels were applied by an automated system, not by a human
  reviewer, and any classifier could have errors."
- **Our assessment**: Combined with Claim 8 (taxonomy gaps), this means the precision of
  any individual category percentage should not be over-read — the categories with the
  most definitional ambiguity (chiefly "business process and operations," which absorbs
  several unlabeled functions) carry the most classifier-error risk.

## Concrete Artifacts

### Cowork Session Taxonomy — May 2026 Sample (from post)

```
Claude Cowork Usage by Category — 1.2M sampled sessions, May 11-31, 2026
(Anthropic, published 2026-07-07)

1. Business process and operations ......... 33.4%
2. Content creation and copywriting ......... 16.4%
3. Software development ...................... 8.7%
4. DevOps and infrastructure .................. 7.0%
5. Research and intelligence .................. 6.4%
6. Data analysis and business intelligence .... 5.8%
7. Document processing and extraction ......... 4.1%
8. Sales and revenue operations ............... 4.0%
9. Personal assistance ......................... 3.8%
10. Education ................................... 2.4%
11. Meeting/conversation intelligence ........... 1.8%
12. Legal and compliance work ................... 1.3%
13. Customer support ............................ 0.8%
    (remaining ~7 of 20 categories not individually named;
     "all other categories" collectively < 4%)

Sample: 1.2 million anonymized, aggregated sessions from 600,000+ organizations
Method: capped-rate collection (fixed max sessions/hour, not % of traffic)
Classification: fully automated, 20-category taxonomy, no human session review
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-enterprise.md` (Claim 6, "surrounding work first" /
    non-engineering-majority usage) — this post supplies the first quantified data behind
    that earlier qualitative claim. Software development + DevOps together are only 15.7%
    of sessions (Claim 4 here), consistent with Claim 6's "vast majority...comes from
    outside engineering teams," though the two sources measure slightly different things
    (task category share here vs. user population share there).
  - `blog-anthropic-cowork-deploy-guide.md` (Claim 1, three-surface decision framework:
    Chat / Cowork / Code) — Claim 4 here is direct numeric evidence that developers use
    Cowork for the connective work around their role rather than core coding, which stays
    on Claude Code. This is the first source to quantify that split rather than assert it.
  - `blog-anthropic-cowork-enterprise.md` (Claim 8, human role shifts to "validation,
    refinement, and decision-making") — Claim 6 here reiterates the same framing with
    fresh (if hypothetical) illustrative examples across law, hiring, and management.

- **Extends**:
  - `blog-anthropic-bryant-cowork-sales.md` (sales/account-management archetype) — this
    post places that archetype's category (sales and revenue operations) at 4% of overall
    Cowork usage, giving the detailed practitioner account a sense of relative scale it
    did not have on its own.
  - `blog-anthropic-cowork-getting-started.md` and `blog-anthropic-cowork-deploy-guide.md`
    — both describe content-creation and business-process workflows anecdotally (marketing
    drafts, Legal/Finance department plugins); this post supplies the aggregate share data
    (33.4% and 16.4% respectively) that situates those anecdotes within overall usage.

- **Contradicts**: None filed. No existing source note asserts a materially different
  category distribution or disputes the "surrounding work" framing. Reviewed
  `blog-anthropic-cowork-enterprise.md`, `blog-anthropic-bryant-cowork-sales.md`,
  `blog-anthropic-cowork-deploy-guide.md`, `blog-anthropic-cowork-getting-started.md`, and
  `blog-anthropic-claude-code-cowork-government.md` — all are directionally consistent
  with this source's aggregate breakdown.

- **Novel**:
  - **Quantified 20-category usage taxonomy with a disclosed methodology** (Claims 2-5,
    Concrete Artifacts): No prior corpus source provides a hard percentage breakdown of
    Cowork task categories. Every prior Cowork source note relies on named case studies,
    executive quotes, or qualitative characterizations ("vast majority," "the work around
    the work") without disclosed sample size or category-level numbers.
  - **Explicit taxonomy-limitation disclosure** (Claims 8-10): No prior corpus source
    includes a vendor's own self-critique of its usage-analytics methodology (rate-capped
    sampling, automated-classifier error risk, taxonomy gaps inflating the largest
    category). This raises the evidentiary bar relative to prior Cowork usage claims and
    should be modeled as a positive practice when the guide cites vendor telemetry.

## Guide Impact

- **Ch05 (Team Adoption)**: Add the quantified category breakdown (business process and
  operations 33.4%, content creation 16.4%, combined engineering categories 15.7%) as the
  first hard-numbers evidence for the "AI adoption starts with surrounding work, not core
  work" pattern already recommended in the guide (citing `blog-anthropic-cowork-
  enterprise.md`). Note the taxonomy caveat (Claim 8) so the guide doesn't overstate
  precision on the 33.4% figure specifically.

- **Ch01 (Daily Workflows)**: When describing the Chat/Cowork/Code decision boundary
  (already sourced from `blog-anthropic-cowork-deploy-guide.md` Claim 1), cite Claim 4
  here as quantitative confirmation that even developers route core coding to Claude Code
  and connective work (status updates, docs, communications) to Cowork — useful for
  readers deciding which surface fits a given task.

- **Ch05 (Team Adoption)**: When citing `blog-anthropic-bryant-cowork-sales.md`'s
  detailed sales archetype, add this source's context that sales/revenue-ops work is ~4%
  of overall Cowork usage — the practitioner account is a useful workflow template, not
  evidence that sales is a dominant use case.

- **General citation guidance**: Any guide text quoting these percentages should also
  carry the methodology caveat (rate-capped single-organization-external sample, ~5%
  personal/non-work sessions, automated classification, taxonomy gaps) rather than citing
  bare percentages as precise workplace-usage statistics.

## Extraction Notes

- Full article text was retrieved via a direct HTTP fetch of the page and HTML-tag
  stripped to plain text (the WebFetch tool's summarization pass was cross-checked against
  this raw extraction to confirm accuracy and recover exact wording for quotes). All quotes
  above were copied verbatim from that raw text, including the "Additional details about
  our research" methodology/limitations appendix, which is part of the same page (not a
  separate URL) and was read in full — it contains several of the most load-bearing claims
  (7-10) and would have been missed by a shallower read.
- The article's related-posts sidebar lists a companion piece,
  "How Anthropic's marketing operations team uses Claude Cowork to automate reporting and
  campaign builds" (published 2026-07-08). That is a distinct URL and case study, not
  covered by this note; it may be a candidate for a future source-submission issue but was
  out of scope here since it wasn't linked inline from the article body (only from the
  "Related posts" carousel).
- No contradictions were found against the five existing Cowork-related source notes
  reviewed (see Cross-References → Contradicts). No contradiction issue was filed.
- Confidence set to **emerging** overall: the methodology is disclosed and reasonably
  rigorous (a meaningful step up from prior Cowork posts' vague usage characterizations),
  but it remains a single vendor's single-month, rate-capped, automated-classifier sample
  with self-disclosed taxonomy gaps — not an independently replicated or audited finding.
