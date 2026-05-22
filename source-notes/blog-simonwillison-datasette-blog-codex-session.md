---
source_url: https://simonwillison.net/2026/May/13/welcome-to-the-datasette-blog/
source_type: blog-post
title: "Welcome to the Datasette blog"
author: Simon Willison
date_published: 2026-05-13
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: anecdotal
issue: "#842"
---

# Welcome to the Datasette blog

> Simon Willison announces the Datasette project blog, notes he built it using OpenAI
> Codex Desktop and that its Markdown session transcript export is "the feature I've
> always wanted" — then links the exported session as project documentation, establishing
> session-transcript-as-provenance as a concrete practice pattern.

## Source Context

- **Type**: blog-post (Simon Willison "announcement" / link post format; very brief — two
  sentences of original text plus links; the substantive engineering content is entirely in
  the linked session transcript, a GitHub Gist at
  https://gist.github.com/simonw/885b11eee46822622b8031a1f4e5f3a3, which was followed
  per MINER.md §1 as the primary substantive linked page)
- **Author credibility**: Simon Willison is the creator of Django, creator of the `llm` CLI,
  and one of the most widely-cited independent LLM tooling commentators. He has no vendor
  affiliation with OpenAI or Anthropic. His AI tooling notes document actual first-person
  experiments with verifiable public artifacts. His consistent practice of tagging posts
  with "ai-assisted-programming" and "codex" when AI tools are used is a disclosure norm,
  not a marketing stance.
- **Scope**: The blog post itself covers: (1) the launch of the Datasette official blog;
  (2) the use of OpenAI Codex Desktop to build it; (3) the Markdown session transcript
  export feature in Codex Desktop; (4) a link to the exported session (the gist) and to
  GitHub issue 179 (datasette.io feature request for a blog). The linked gist covers the
  full session: dev server setup, database renaming, blog feature implementation, news
  integration, author metadata, search indexing, CSS adjustments, and test verification.
  Does NOT cover: multi-session workflows, team use, comparative evaluation of Codex
  Desktop vs other tools, or any cost/performance metrics.

## Extracted Claims

### Claim 1: OpenAI Codex Desktop includes a Markdown session transcript export feature that allows practitioners to share their full AI coding session publicly

- **Evidence**: Willison's direct statement in the announcement post, confirmed by the
  existence and public accessibility of the exported gist. The gist is the transcript itself —
  the artifact that proves the export feature works.
- **Confidence**: settled (the feature's existence is confirmed by the public gist; Willison's
  statement provides the vendor/product attribution)
- **Quote**: "I built this using OpenAI Codex desktop, which turns out to have the Markdown
  session transcript export feature I've always wanted."
- **Our assessment**: The phrasing "I've always wanted" is the most important signal in the
  entire source. Willison is not praising a feature he expected — he is naming a long-standing
  practitioner wish that was fulfilled. The wish is for session transparency: a durable,
  shareable record of exactly what an AI agent did, in what order, and with what inputs.
  This feature is not present by default in Claude Code or Cursor as of this post's date.
  For practitioners who want to document AI-assisted development, this marks a product
  differentiation point. For the corpus: no prior source notes that any AI coding tool ships
  native session export as Markdown.

### Claim 2: Linking an exported AI session transcript alongside a project announcement is a viable and natural documentation practice

- **Evidence**: Willison links the gist directly from the Datasette blog announcement with
  the anchor text "the session that built the blog" — treating the transcript as the
  provenance record for the project, in the same way one might link a PR or a design doc.
- **Confidence**: anecdotal (single practitioner example; but from a practitioner who
  has established many documentation norms in the LLM tooling community)
- **Quote**: (no direct prose quote; the evidence is the anchor text "the session that
  built the blog" and its placement in the announcement post)
- **Our assessment**: This is a new form of software provenance documentation: instead of
  (or in addition to) linking commits and PRs, the developer links the AI session that
  produced the work. Anyone reading the Datasette blog announcement can see exactly how
  it was built — what prompts were used, what the agent did step by step, what decisions
  were made along the way. This is analogous to the "build in public" norm in indie
  developer culture, extended to AI-assisted development. The Markdown format is
  significant: it is immediately readable in any browser without special tooling.

### Claim 3: A single Codex Desktop session built a complete blog infrastructure for an existing project, integrating with multiple pre-existing systems end-to-end

- **Evidence**: The gist (WebFetch summary; not verbatim text — see Extraction Notes)
  documents the session scope: development server setup via `uv`, database renaming,
  a Markdown-to-database loader (`build_blog_posts.py`), blog list and individual entry
  pages, news integration across the homepage and Atom feed, author metadata with bylines,
  sitemap generation, dogsheep-beta search indexing, CSS refinements, and smoke test
  extensions. All this was accomplished in a single session on an existing codebase.
- **Confidence**: anecdotal (single session, one project; the gist is public and verifiable
  but the WebFetch returned a summary rather than verbatim transcript content)
- **Quote**: (no direct quote from the gist; WebFetch returned a structured summary rather
  than verbatim text — see Extraction Notes)
- **Our assessment**: The complexity is not in any single feature but in the breadth and
  integration requirements. The session did not build against a green-field project; it
  extended an existing datasette.io codebase with its own conventions, build scripts,
  CI workflows, and infrastructure (dogsheep-beta, uv, datasette). This is the class of
  task — "add a substantial new feature to an existing, moderately complex codebase" —
  that practitioners most often delegate to AI agents. The fact that Codex Desktop
  completed it in a single session without requiring human intervention mid-session
  extends the one-session corpus (previously documented for smaller-scope tasks in
  `blog-simonwillison-servo-crate-exploration.md` Claim 1 and
  `blog-simonwillison-gpt55-codex-plugin.md` Claim 3).

### Claim 4: The Codex session used headless Chrome screenshots for visual verification of the blog output alongside automated tests

- **Evidence**: Gist WebFetch summary explicitly notes "Chrome headless screenshots for
  visual verification" as a key command used alongside `pytest` and `bash scripts/test.sh`.
- **Confidence**: anecdotal (from gist summary; not verbatim)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The dual verification approach — automated tests plus visual
  screenshots — is worth noting as a pattern. Visual verification catches layout and
  rendering issues that unit tests miss; automated tests catch logic and integration
  issues that screenshots miss. An AI agent that self-verifies visually is doing
  more than code generation: it is doing a basic acceptance test of its own output.
  This is consistent with the responsible agentic engineering pattern, not pure
  vibe-coding.

### Claim 5: The Codex session completed all work without making git commits, leaving version control decisions to the developer

- **Evidence**: Gist WebFetch summary explicitly states: "The agent completed all work
  without version control commits, leaving changes in a working state for the user
  to review."
- **Confidence**: anecdotal (from gist summary; whether this is a Codex Desktop default,
  a user instruction, or a session-specific decision is not documented in the source)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The no-commit pattern is a conservative design choice that keeps
  humans in control of version history. It contrasts with fully automated agentic
  patterns that commit and push. The handoff state ("working state for the user to
  review") is the responsible human-in-the-loop checkpoint: the agent delivers a
  complete working implementation but withholds the irrevocable action of committing
  it. This pattern aligns with the concerns Willison himself raised in
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 2 about normalization
  of deviance — maintaining review checkpoints even when the agent is reliable.

### Claim 6: The Datasette blog was created to serve a backlog of Datasette feature announcements that had no publication venue

- **Evidence**: Willison's direct statement in the opening of the post.
- **Confidence**: settled (first-person statement from the project maintainer)
- **Quote**: "We have a bunch of neat Datasette announcements in the pipeline so we
  decided it was time the project grew an official blog."
- **Our assessment**: This is project context, not a pattern claim, but it confirms
  that the blog (and the Codex session that built it) was driven by a real content
  need — not an experiment or a demo. The infrastructure built in the session was
  immediately put to use: the first post published was the announcement itself, with
  the Datasette Agent post following on May 21 (referenced in the blog's sidebar).
  This is a real-world, production-deployed outcome from a single AI coding session,
  not a proof of concept.

## Concrete Artifacts

### Blog post verbatim text (complete)

```
Source: Simon Willison, simonwillison.net/2026/May/13/welcome-to-the-datasette-blog/

"Welcome to the Datasette blog. We have a bunch of neat Datasette announcements
in the pipeline so we decided it was time the project grew an official blog."

"I built this using OpenAI Codex desktop, which turns out to have the Markdown
session transcript export feature I've always wanted."

Links:
  "the session that built the blog" → https://gist.github.com/simonw/885b11eee46822622b8031a1f4e5f3a3
  "issue 179"                       → https://github.com/simonw/datasette.io/issues/179
```

*Source: The complete text of the blog post body as returned by WebFetch.*

### Codex session scope (from gist WebFetch summary — not verbatim transcript)

```
Session: Codex Desktop building the datasette.io blog
Gist: https://gist.github.com/simonw/885b11eee46822622b8031a1f4e5f3a3
Last active: May 13, 2026 21:52 (2 revisions)

WORK COMPLETED IN SESSION (from WebFetch summary; not verbatim gist text):

1. Dev server setup:
   uv run --with-requirements requirements.txt datasette . --port 9008 --reload

2. Database: renamed blog.db → simon-blog.db across build scripts, CI, deployment

3. Blog implementation:
   - build_blog_posts.py: Markdown-to-database loader for blog content
   - /blog/ list page (reverse-chronological)
   - /blog/YYYY/slug/ individual entry pages
   - Route plugin for trailing slashes

4. Integration:
   - Homepage "Latest news and blog" section
   - /news listing page
   - /content/feed.atom Atom feed

5. Author metadata: front matter with author name and URL, UTC bylines

6. Discoverability: blog URLs added to sitemap; indexed in dogsheep-beta search

7. CSS: header nav wrapping, spacing, blog-specific styles

8. Verification: pytest + bash scripts/test.sh + Chrome headless screenshots

9. Version control: NO commits made; agent left working state for developer review

NOTE: All above items are from a WebFetch model summary of the gist page, not
verbatim transcript text. The gist is publicly accessible for direct verification.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-servo-crate-exploration.md` Claim 1 ("Claude Code can cold-start
    on a brand-new, sparsely-documented crate and deliver a working tool in one task"):
    The Codex session here is the same one-session-complete-project pattern, applied to
    a larger, integration-heavy task (blog infrastructure on an existing codebase) rather
    than a new library exploration. Both produce publicly verifiable artifacts. Together
    they provide two data points supporting the "AI agent delivers working implementation
    in one session" pattern across different project types and AI tools (Claude Code vs
    Codex Desktop).
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 3 ("Claude Code can reverse-engineer
    an open-source OAuth/auth flow and produce a working CLI plugin in a single session"):
    Third data point for the one-session-complete-project pattern from the same practitioner,
    now across three different task types (library exploration, plugin development, blog
    infrastructure). Strengthens the corpus case for this as a repeatable workflow pattern
    rather than cherry-picked examples.
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 4 ("RSS/Atom syndication is an
    immediately deployable mechanism... implementable in a single Claude delegation"):
    That note documents Willison adding an Atom feed to his tools page as a one-shot
    Claude task. This source shows the same same-day-implementation pattern applied at
    larger scope (full blog infrastructure vs a single feed). Both document Willison's
    pattern of using AI agents to close infrastructure gaps quickly.

- **Extends**:
  - `blog-simonwillison-codex-base-instructions.md`: That note documents what Codex models
    are instructed to do (system prompt contents). This note shows Codex Desktop in actual
    use for a real, production-deployed project. Together they provide the full picture for
    Codex Desktop practitioners: what behavioral contract the model operates under (the
    base instructions note) and what it does in practice on a real project (this note).
  - `blog-simonwillison-gpt55-codex-plugin.md`: That note covers accessing GPT-5.5 via the
    Codex subscription path and Codex as a model access mechanism. This note shows Codex
    Desktop as a standalone development environment with its own product features (session
    export). Together they document two distinct aspects of Codex: model access route and
    development tool capability.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 5 ("Evidence of actual
    sustained use is now the primary quality signal for software, replacing artifact
    inspection"): Willison's session transcript is itself a form of use-evidence — a
    durable, inspectable record of the AI's actions during development. The transcript
    export feature operationalizes Willison's own quality-evidence principle: instead of
    just publishing the resulting code, the developer publishes the process.

- **Contradicts**: None identified. No existing corpus note makes claims about AI coding
  tool session transcript export that conflict with this source.

- **Novel**:
  - **First in-corpus documentation of a native session transcript export feature in an
    AI coding tool**: No prior source note identifies any tool (Claude Code, Cursor, Windsurf,
    GitHub Copilot) as shipping native session-to-Markdown export. This is a new capability
    claim in the corpus.
  - **Session transcript as project provenance documentation**: No prior source note describes
    the practice of publishing the AI session alongside the project announcement as a form
    of documentation. This is a new practice pattern: the session transcript is positioned
    as a first-class project artifact, not an internal log.
  - **"The feature I've always wanted" as practitioner demand signal**: Willison's explicit
    naming of session transcript export as a long-standing practitioner wish — not a nice-to-
    have — is the first in-corpus statement of demand for this specific capability. It signals
    that the absence of session export has been a felt gap in other tools, not just a missing
    bell-and-whistle.

## Guide Impact

- **Chapter 04 (Tooling and Infrastructure)**: Add Codex Desktop's session transcript export
  (Claim 1) as a product differentiation item in any comparative overview of AI coding tools.
  Practitioners selecting between Claude Code, Cursor, and Codex Desktop should know that
  Codex Desktop offers native Markdown session export; other tools (as of May 2026) do not.
  Note: this may change as other tools add similar features.

- **Chapter 03 (Development Patterns — Documentation and Provenance)**: Add the
  session-transcript-as-documentation pattern (Claim 2) as a concrete practice for
  AI-assisted development transparency. The pattern: when you publish a project or feature
  built with an AI agent, link the session transcript alongside the announcement. This is
  analogous to linking commits and PRs — it creates an inspectable provenance record for
  AI-generated work. Currently only feasible with Codex Desktop's native export; other
  tools would require manual session capture or workarounds.

- **Chapter 03 (Development Patterns — One-Session Project Builds)**: This source is the
  third in-corpus example of Willison completing a meaningful, verifiable project in a
  single AI agent session (`blog-simonwillison-servo-crate-exploration.md` Claim 1;
  `blog-simonwillison-gpt55-codex-plugin.md` Claim 3; this source Claim 3). With three
  examples across different tool types (Claude Code, Codex Desktop) and task types (library
  exploration, plugin development, blog infrastructure), the guide has enough evidence to
  present this as a documented workflow pattern: "AI agents can deliver working
  implementations of mid-complexity infrastructure tasks in a single session on existing
  codebases." Frame the no-commit pattern (Claim 5) as the recommended human-in-the-loop
  handoff point.

- **Chapter 03 (Development Patterns — Verification Practices)**: Claim 4 (headless Chrome
  screenshots + pytest) is a concrete dual-verification pattern worth extracting as a
  recommendation for AI sessions that produce UI or web output. The guide can present this
  as: "for sessions producing web output, combine automated tests (logic/integration) with
  headless screenshot verification (rendering/layout)."

## Extraction Notes

- **Primary source is extremely brief**: The Willison post is two sentences plus links.
  All substantive engineering content comes from following the gist link (the second
  "linked page that seems substantive" per MINER.md §1). The gist is the real source;
  the blog post is the framing and the provenance claim.
- **Gist content accessed via WebFetch summary**: WebFetch returned a structured summary
  of the gist rather than verbatim transcript text. This is noted explicitly in Claims
  3–5 and in Concrete Artifacts. All claims derived from the gist are marked as "(no
  direct quote; from gist summary, not verbatim)" and rated accordingly. The gist is
  publicly accessible at the URL in Concrete Artifacts for direct verification.
- **Blog post verbatim text confirmed**: The two sentences in Claim 1 Quote and Claim 6
  Quote were confirmed verbatim via WebFetch (the tool returned them as direct text
  rather than as reconstructed summaries). These are the only verbatim quotes in this
  note; all other quoted items reference the gist summary.
- **Fragment URL**: The issue body includes `#atom-everything` as a URL fragment (an
  Atom feed anchor on the page, not a section heading). The `source_url` uses the
  canonical page URL without the fragment, consistent with prior Willison source notes
  in this corpus.
- **No additional linked pages followed**: The gist is the substantive linked page.
  The GitHub issue 179 (datasette.io feature request) was fetched; it is a minimal
  enhancement request ("a Datasette official blog") that adds no substantive engineering
  claims. The blog's sidebar references other posts (Datasette Agent, Gemini 3.5 Flash
  discussion) but these are separate sources, not sub-pages of this source.
- **Cross-reference verification**:
  - `blog-simonwillison-servo-crate-exploration.md` Claim 1 verified at line 41: "Claude
    Code can cold-start on a brand-new, sparsely-documented crate and deliver a working
    tool in one task" ✓
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 3 verified at line 42: "Claude Code
    can reverse-engineer an open-source OAuth/auth flow and produce a working CLI plugin
    in a single session" ✓
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 4 verified at line 106: "RSS/Atom
    syndication is an immediately deployable mechanism for distributing abundant vibe-coded
    apps, implementable in a single Claude delegation" ✓
  - `blog-simonwillison-codex-base-instructions.md`: Cross-referenced by scope description
    (system prompt contents) rather than specific claim number, since the relevant content
    spans multiple claims rather than one specific numbered claim ✓
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 5 verified at line 128:
    "Evidence of actual sustained use is now the primary quality signal for software,
    replacing artifact inspection" ✓
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 2 (normalization of
    deviance) referenced in Claim 5 Our assessment — verified at line 69 ✓
- **Confidence ceiling: anecdotal**: The source is a brief announcement post from a single
  practitioner. Claim 1 (session export feature exists) is settled; all remaining claims
  are anecdotal observations from one session, reported by one practitioner, via a WebFetch
  summary rather than verbatim transcript. The guide should cite this source for the
  feature capability (Claim 1) and the practice pattern (Claim 2) with appropriate
  caveats about single-practitioner evidence.
