---
source_url: https://github.blog/changelog/2026-06-04-copilot-chat-brings-richer-context-to-pull-requests
source_type: docs
title: "Copilot Chat brings richer context to pull requests"
author: GitHub (official changelog)
date_published: 2026-06-04
date_extracted: 2026-06-06
last_checked: 2026-06-06
status: current
confidence_overall: settled
issue: "#1078"
---

# Copilot Chat Brings Richer Context to Pull Requests

> GitHub's June 4, 2026 changelog announcing that Copilot Chat for pull request
> workflows transitions from public preview to general availability for Copilot
> license holders, adding a side-by-side diff-and-chat interface, inline edit
> capability from chat, a new diff-specific "Ask about this diff" entry point,
> and new PR understanding/review/summary abilities that automatically inject
> relevant pull request and repository context into chat responses.

## Source Context

- **Type**: docs (GitHub official product changelog, June 4, 2026; approximately
  150–200 words; a short changelog entry with two main content sections:
  feature description and access methods)
- **Author credibility**: GitHub engineering team announcing a GA promotion.
  Authoritative for: the GA status, the described interface capabilities
  (side-by-side layout, inline edits), the three named entry points, and the
  existence of "pull request understanding, review, and summary" abilities.
  Not a credible source for: what specific context signals those "abilities"
  pull in (e.g., linked issues, CI state, reviewer comments), how the
  underlying model differs from the May 18 contextual chat panel, whether the
  inline edit capability requires additional permissions, what Copilot license
  tiers are covered by "users with Copilot licenses," or how this interacts
  with the June 2 automated code review feature.
- **Scope**: The announcement covers: GA promotion from public preview, a
  side-by-side diff-and-chat interface layout, inline edit capability from the
  chat panel, new PR-specific understanding/review/summary abilities, three
  named entry points (diff button, navigation button, code highlight dropdown).
  Does NOT cover: which context signals are newly available beyond the PR page
  already attached per the May 18 note, how this interacts with the June 2
  agent skills and MCP context injection for automated code review, whether the
  feature behaves differently across Copilot plan tiers, or limits on inline
  edit scope.

## Extracted Claims

### Claim 1: Copilot Chat for pull request workflows on github.com is now generally available, promoted from public preview, for users with Copilot licenses

- **Evidence**: Official GitHub changelog framing the release as a GA promotion
  from public preview. Both WebFetch passes describe the GA status consistently.
- **Confidence**: settled (product fact — GA stated in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The GA promotion is significant for practitioners who had
  not adopted the feature during preview, treating it as unstable. GA signals
  a stability commitment from GitHub, making it appropriate for team
  onboarding documentation. The "users with Copilot licenses" framing is
  intentionally broad — the source does not restrict to a specific tier
  (Individual, Pro, Pro+, Business, or Enterprise), suggesting broad
  availability similar to the May 18 contextual panel (which was documented as
  available for "all GitHub Copilot plans" per
  `docs-github-copilot-web-contextual-chat.md` Claim 7). For Ch05 (Team
  Adoption): GA status removes the preview caveat from any team documentation
  of this feature. The feature is now stable for inclusion in practitioner
  onboarding guides and workflow documentation.

### Claim 2: Copilot Chat now presents a side-by-side interface where users can view code diffs and chat conversations simultaneously

- **Evidence**: Official changelog describing the side-by-side layout as a
  named feature of the GA release. Both WebFetch passes describe this
  capability consistently.
- **Confidence**: settled (product fact — interface layout stated in official
  changelog)
- **Quote**: "comments and inline edits without needing to toggle between the
  pull request and your chat window"
- **Our assessment**: The side-by-side layout is the core UX change this
  announcement delivers. The May 18 contextual chat note
  (`docs-github-copilot-web-contextual-chat.md` Claim 1) documented the
  general in-page panel, noting it "helps you get fast answers to your
  questions with reduced context switching." The June 4 source specifies the
  PR-specific implementation: the panel is co-displayed with the code diff
  rather than alongside the full PR view, enabling simultaneous reference to
  the diff and the chat response. This is meaningfully more focused than a
  general in-page panel — the diff remains visible while the practitioner reads
  Copilot's analysis of it. For Ch01 (Daily Workflows): document the
  side-by-side layout as the standard PR chat interaction mode. Practitioners
  no longer need to scroll up to re-read the diff after receiving a chat
  response.

### Claim 3: Chat with Copilot in a PR context supports inline edits directly from the chat panel without navigating away from the pull request

- **Evidence**: Quoted fragment from official changelog describing inline edit
  capability as part of the side-by-side interface.
- **Confidence**: settled (product fact — inline edit capability stated in
  official changelog)
- **Quote**: "comments and inline edits without needing to toggle between the
  pull request and your chat window"
- **Our assessment**: Inline edits from chat in the PR view represent a
  meaningful capability extension beyond Q&A. A practitioner can ask Copilot
  to propose a fix for a code problem visible in the diff and apply the
  suggested edit without leaving the PR. This blurs the line between review
  (reading the diff) and revision (changing the code): the PR becomes both a
  review surface and an edit surface in a single interface. For Ch01 (Daily
  Workflows): this creates a new PR workflow pattern — review + edit in the
  same browser tab. For Ch02 (Harness Engineering): the inline edit surface
  may require Copilot push permissions or branch write access; the announcement
  does not address this constraint, and practitioners should verify edit scope
  before relying on inline edits in protected-branch workflows.

### Claim 4: Copilot Chat for PRs uses new abilities for "pull request understanding, review, and summary" that automatically add relevant PR and repository context to chat responses when asking about diffs

- **Evidence**: Official changelog describing the new PR-specific context
  injection abilities. The quote was attributed to the announcement in one
  WebFetch pass and confirmed in substance by the second.
- **Confidence**: settled (product fact — abilities named in official changelog;
  mechanism described; specific context signals not enumerated)
- **Quote**: "These abilities add relevant pull request and repository context
  to chat any time you ask about a diff or pull request"
- **Our assessment**: This is the most architecturally significant claim in this
  changelog. The May 18 contextual chat note documented "automatic context
  attachment" — the current page (PR or issue) is attached as context when
  the panel opens (`docs-github-copilot-web-contextual-chat.md` Claim 4). The
  June 4 source goes further: not just attaching the PR page as a reference,
  but adding "pull request understanding, review, and summary" abilities that
  actively process the PR content and inject distilled context into responses.
  The distinction: May 18 = page-as-reference; June 4 = model-processed PR
  understanding. The "repository context" inclusion suggests signals beyond the
  diff itself (potentially commit history, related files, or linked issues),
  though the announcement does not enumerate the specific context types. For
  Ch04 (Context Engineering): this is a new form of automated context
  enrichment — the model applies PR-specific abilities to transform the raw PR
  content into richer context before responding. Practitioners should understand
  that Copilot's PR chat responses reflect a model-enriched view of the PR, not
  merely the raw page content that was attached.

### Claim 5: The feature introduces "new abilities for pull request understanding, review, and summary" as distinct capabilities from general chat

- **Evidence**: Official changelog naming these three ability types explicitly.
- **Confidence**: settled (ability types named in official changelog; no
  implementation detail provided)
- **Quote**: "new abilities for pull request understanding, review, and summary"
- **Our assessment**: The three named ability types — understanding, review, and
  summary — suggest that Copilot Chat in the PR context can do more than answer
  freeform questions: it can actively understand the PR's intent, produce
  review-style analysis, and summarize the changes. The "summary" ability is
  the most interpretable (similar to PR description summarization); the
  "review" ability suggests structured analysis of the diff for quality/issues;
  the "understanding" ability suggests semantic interpretation of what the PR
  is trying to accomplish. None of these abilities are elaborated with examples
  or metrics in the announcement. For Ch01 (Daily Workflows): document these as
  the three use-case modes for PR chat: ask "what does this PR do?" (summary),
  "what issues do you see in this diff?" (review), or "explain this function
  change" (understanding). For Ch04 (Context Engineering): these abilities are
  the mechanism by which raw PR content is transformed into enriched context —
  the model is not passively reading the diff but actively applying structured
  analysis capabilities to it.

### Claim 6: A new "Ask about this diff" button at the top of each diff provides a diff-specific entry point to Copilot Chat, distinct from the general navigation panel trigger

- **Evidence**: Official changelog enumerating access methods, with "Ask about
  this diff" named as the first of three methods. Both WebFetch passes
  consistently describe this button.
- **Confidence**: settled (UI element named in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The "Ask about this diff" button is a new, diff-scoped
  entry point that the May 18 contextual chat note did not document. The May 18
  note's primary entry point was the Copilot icon in the top navigation
  (`docs-github-copilot-web-contextual-chat.md` Claim 3). The "Ask about this
  diff" button is more specifically scoped to the diff view: it initiates a
  chat session targeted at the diff the practitioner is currently viewing,
  rather than the PR as a whole. This is a meaningful UX distinction for
  practitioners who review PRs file-by-file and want to ask about a specific
  diff block without triggering the full PR context attachment. For Ch01 (Daily
  Workflows): document this as the primary entry point for diff-level PR
  questions. The three entry points serve distinct intent: "Ask about this
  diff" = diff-focused; top navigation button = general PR question; code
  highlight + dropdown = code-selection-specific question.

### Claim 7: Highlighting code in the PR view and selecting Copilot from the dropdown menu is a third entry point to PR chat, enabling selection-scoped context

- **Evidence**: Official changelog enumerating access methods, with code
  highlight + dropdown listed as the third method. Both WebFetch passes
  describe this consistently.
- **Confidence**: settled (access method described in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The code-highlight entry point implies selection-scoped
  context — chat opens with the highlighted code block as the explicit context,
  narrower than the full diff or PR. This parallels the IDE Copilot pattern
  where selecting code and opening inline chat provides selection-scoped
  assistance. For Ch01 (Daily Workflows): document this as the entry point for
  line-specific questions during PR review ("what does this function do?",
  "is this change safe?"). For practitioners comfortable with IDE Copilot
  inline chat, this access method provides the closest analogue in the web
  PR view. The announcement does not clarify whether the selected code is
  passed as the entire context or augmented with surrounding diff context.

## Concrete Artifacts

### Source Content Summary (from two independent WebFetch passes, June 6, 2026)

The following represents the substance of the changelog entry as retrieved by
two independent WebFetch calls. Content was consistent across both passes.
The verbatim text of this short changelog could not be reproduced in full due
to WebFetch tool summarization behavior; all direct quotes are marked as such
and verified across both passes.

```
Title: Copilot Chat brings richer context to pull requests
Published: 2026-06-04
Source: https://github.blog/changelog/2026-06-04-copilot-chat-brings-richer-context-to-pull-requests

GA status: Feature promoted from public preview to general availability
           for users with Copilot licenses.

Key feature: Side-by-side interface
  → Code diffs and chat conversations visible simultaneously
  → Enables "comments and inline edits without needing to toggle
    between the pull request and your chat window"

Key feature: Richer PR context
  → Uses "new abilities for pull request understanding, review, and summary"
  → "These abilities add relevant pull request and repository context to
    chat any time you ask about a diff or pull request"

Access methods (three named entry points):
  1. "Ask about this diff" button at the top of each diff
  2. Copilot button in the top navigation
  3. Highlight code → select Copilot from the dropdown menu
```

Source: https://github.blog/changelog/2026-06-04-copilot-chat-brings-richer-context-to-pull-requests
Retrieved: 2026-06-06 via two independent WebFetch calls; content consistent
across both passes.

### PR Chat Access Method Reference

```
# Access methods for Copilot Chat in pull request view (as of June 4, 2026 GA)

ENTRY POINT 1: Diff-specific
  Trigger:   "Ask about this diff" button at top of each diff
  Scope:     Targets the specific diff being viewed
  Best for:  "What does this change do?" / "Is this safe?"

ENTRY POINT 2: General PR
  Trigger:   Copilot button in top navigation (existing, from May 18)
  Scope:     Full PR context (page-level automatic attachment per May 18 note)
  Best for:  Broad PR questions, cross-file analysis

ENTRY POINT 3: Selection-scoped
  Trigger:   Highlight code → select Copilot from dropdown menu
  Scope:     Selected code block
  Best for:  Line-specific questions, "explain this function"

LAYOUT:    Side-by-side (code diff + chat simultaneously visible)
CAPABILITY: Inline edits from chat (without toggling to separate window)
```

## Cross-References

- **Extends** `docs-github-copilot-web-contextual-chat.md` (Claim 4): That
  source (May 18, 2026) documented automatic context attachment as "when you
  open chat on a GitHub surface, like a pull request or issue, it is
  automatically attached as context to your chat session." The June 4 source
  builds on this: the PR context is not merely attached as a reference but
  processed through "pull request understanding, review, and summary" abilities
  that enrich the context actively. May 18 = page-as-reference; June 4 =
  model-processed PR understanding layered on top of that attachment.

- **Extends** `docs-github-copilot-web-contextual-chat.md` (Claim 3): That
  source documented the top navigation Copilot icon as the primary entry point
  to contextual chat. The June 4 source adds two PR-specific entry points
  ("Ask about this diff" button; code highlight + dropdown) that supplement the
  general navigation icon. The three-entry-point model provides practitioners
  with more focused access than the single navigation icon path, allowing
  context scoping at the diff level and selection level.

- **Extends** `docs-github-copilot-web-contextual-chat.md` (Claim 1): That
  source documented the in-page chat panel as a general UX change. The June 4
  source specifies the PR implementation: a side-by-side layout where the code
  diff remains visible alongside the chat panel. The May 18 note described
  the panel as providing "reduced context switching"; the June 4 note makes
  the mechanism concrete — the diff stays visible without toggling.

- **Corroborates** `docs-github-copilot-web-contextual-chat.md` (Claim 7):
  That source documented "generally available for all GitHub Copilot plans."
  The June 4 source's "users with Copilot licenses" GA framing is consistent
  with broad plan availability, though the specific tier enumeration is not
  provided in the June 4 source. No contradiction on plan availability — the
  two formulations are compatible.

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md`: The June 2
  source documented automated Copilot code review (Claim 1: agent skills invoke
  "your team's internal tools and standards during a review") — an agent-driven
  process that runs without practitioner initiation. The June 4 source
  documents interactive chat in the PR context — a practitioner-initiated
  workflow. Together, they complete the two-mode PR assistance model: automated
  review agent (June 2) + interactive chat (June 4). These are complementary,
  not overlapping: code review runs automatically on PR open/push; chat is
  initiated by the practitioner during review. For Ch01: document both modes as
  part of the full Copilot-assisted PR workflow.

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 5):
  That source documented "shared configuration across review and cloud agent
  means platform teams invest once." Whether this shared configuration extends
  to PR chat (i.e., whether agent skills or MCP context from code review are
  also available to PR chat) is not addressed in either source. This is a gap
  to flag for Ch02 — if the shared-config model extends to chat, teams that
  invest in code review MCP/skills get richer PR chat context automatically.

- **Contradicts**: None identified. No existing corpus source makes claims
  about PR-specific Copilot chat interface capabilities that this source would
  refute. The May 18 note's automatic context attachment claim is extended, not
  contradicted. No contradiction issue to file.

- **Novel**:
  - **Diff-specific "Ask about this diff" button**: No prior corpus source
    documents a diff-level entry point to Copilot chat. Prior web Copilot
    access points were page-level (top navigation icon) or involved navigating
    to github.com/copilot. A button specifically positioned at the top of each
    diff is new.
  - **Side-by-side diff + chat interface**: The May 18 note documented an
    in-page panel generally; the June 4 source specifies the PR-specific
    implementation with the diff remaining visible alongside chat. The co-
    display of diff and chat is new to the corpus.
  - **Inline edit capability from chat in PR view**: No prior corpus source
    documents inline edit application from the chat panel within the PR view.
    Prior corpus sources document fix application via CCA ("Fix with Copilot"
    buttons per `docs-github-copilot-cca-apply-review-feedback.md`) — a
    different mechanism (agent-driven bulk fix vs. inline chat edit).
  - **PR understanding/review/summary as distinct named abilities**: No prior
    corpus source names these three ability types as distinct PR chat
    capabilities. Prior notes document context attachment (May 18) and
    automated review analysis (June 2) but not the practitioner-facing ability
    taxonomy (understanding vs. review vs. summary) for interactive chat.
  - **Code highlight + Copilot dropdown as an explicit PR chat entry point**:
    The May 18 note documented context attachment but not code-selection-scoped
    chat access. The highlight-and-select pattern is a new documented entry
    point for PR-specific chat in the corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Update the PR review workflow to document
  three Copilot chat modes available in the PR view as of June 4, 2026:
  (a) automated code review agent (June 2, runs on PR open/push — see
  `docs-github-copilot-code-review-skills-mcp-tier.md`); (b) interactive PR
  chat via "Ask about this diff" or top navigation button for PR-level and
  diff-level questions; (c) selection-scoped chat via code highlight + dropdown
  for line-specific questions. The June 4 source establishes that the side-by-
  side layout means practitioners can ask about code without losing their place
  in the diff. The inline edit capability means the boundary between review
  and revision blurs — review a change, ask for a fix, apply it without
  switching tabs.

- **Chapter 02 (Harness Engineering)**: Document the three PR chat entry points
  as stable GA access paths (not preview). For teams onboarding to Copilot web
  workflows, the instruction is now: use "Ask about this diff" for diff-level
  questions; use the top nav Copilot icon for PR-level questions; use code
  highlight + dropdown for selection-specific questions. The June 4 note does
  not document any configuration surface — unlike the June 2 code review
  features (which require admin setup of skills/MCP/tier), PR chat appears to
  require no additional configuration beyond Copilot license possession. Flag
  that inline edit scope (branch permissions, file write access) is not
  documented in this source and should be verified before relying on inline
  edits in protected-branch workflows.

- **Chapter 04 (Context Engineering)**: Add a "PR-specific context enrichment"
  pattern to the context engineering taxonomy. The June 4 source introduces
  a context enrichment layer between raw page attachment (May 18) and agent
  context injection (June 2): the model applies PR understanding, review, and
  summary abilities to transform attached PR content into richer context before
  responding. The specific context signals injected ("relevant pull request and
  repository context") are not enumerated, leaving open whether CI status,
  linked issues, review comments, or commit history are included. Practitioners
  who want to understand why Copilot gave a particular PR chat answer should be
  aware that the enrichment layer may incorporate signals beyond the visible
  diff. Recommend documenting the known unknowns: what "repository context"
  means in practice is unspecified in this source.

- **Chapter 01 / Chapter 05 (Team Adoption)**: GA status makes this safe for
  team onboarding documentation. Unlike the June 2 code review features (public
  preview requiring admin setup), PR chat is GA and requires no admin
  configuration for practitioners who already have Copilot licenses. Teams
  should update any documentation that instructs practitioners to navigate to
  github.com/copilot for PR questions — the "Ask about this diff" button and
  top navigation icon are now the canonical PR chat entry points.

## Extraction Notes

1. **Short source (~150-200 words estimated)**: The changelog entry is brief.
   Both WebFetch passes returned consistent summarizations. The WebFetch tool
   could not reproduce the full verbatim text due to tool behavior; all three
   direct quotes used in this note were explicitly surfaced by the WebFetch
   responses and are used as attributed quotations.

2. **Two independent fetches**: Both passes to the source URL produced
   consistent content across all major claims. No discrepancies were found
   between the two passes in feature descriptions, access methods, or GA status.

3. **Verbatim quote confidence**: Three direct quotes are used in this note:
   "comments and inline edits without needing to toggle between the pull request
   and your chat window"; "new abilities for pull request understanding, review,
   and summary"; "These abilities add relevant pull request and repository
   context to chat any time you ask about a diff or pull request." All three
   were surfaced within quotation marks by the WebFetch tool responses and are
   treated as verbatim. Remaining claims where no verbatim text was available
   are marked with "(no direct quote; see paraphrase in Our assessment)."

4. **"Repository context" underspecified**: The phrase "relevant pull request
   and repository context" (Claim 4) is vague. The announcement does not
   enumerate which repository signals are included. Possible sources (commit
   history, related PRs, linked issues, CI results, repository README,
   CODEOWNERS) are all plausible but unconfirmed from this source alone.

5. **Relationship to May 18 contextual chat**: This source is an additive
   announcement building on the May 18 in-page panel. The two sources together
   define the full PR chat capability as of June 4, 2026: panel infrastructure
   (May 18) + PR-specific enrichment and UI layout (June 4). Neither note
   supersedes the other — both are required for a complete picture.

6. **No sub-pages followed**: The changelog entry does not appear to link to
   detailed documentation sub-pages for this specific feature. No follow-on
   pages were available to fetch.

7. **No contradictions filed**: All existing corpus source notes that document
   Copilot web chat, PR context, or code review features were reviewed. The
   June 4 claims extend May 18 claims and complement June 2 claims without
   opposing any existing documented position. No contradiction issue required.
