---
source_url: https://simonwillison.net/2026/May/13/welcome-to-the-datasette-blog/
source_type: blog-post
title: "Welcome to the Datasette blog"
author: Simon Willison
date_published: 2026-05-13
date_extracted: 2026-05-24
last_checked: 2026-05-24
status: current
confidence_overall: anecdotal
issue: "#842"
---

# Welcome to the Datasette blog

> Simon Willison demonstrates that Codex Desktop's Markdown session transcript export produces a sharable, human-readable record of an end-to-end AI-assisted development session — and that a full project (blog infrastructure, data loader, templates, URL routing, CSS tweaks, search integration) can be built inside one continuous Codex session with the developer directing in natural language.

## Source Context

- **Type**: blog-post (Willison link-blog + announcement; the post itself is two sentences plus a link to the gist transcript. The real substance is the linked GitHub Gist — a 1,800-line Markdown export of the Codex Desktop session that built the Datasette blog. Both sources were read in full.)
- **Author credibility**: Simon Willison is the creator of Django, creator of the `llm` CLI, and one of the most widely-cited independent LLM tooling practitioners. He regularly publishes AI-assisted development sessions and maintains 200+ tools. No vendor affiliation. He has a direct stake in the tools he evaluates (he builds on them) and a track record of naming both capabilities and failures honestly. The session transcript is a primary-source record — it is not editorial commentary but a captured log of actual work.
- **Scope**: The blog post covers one thing: the announcement of the Datasette blog and the tool used to build it. The session transcript (gist) covers: setting up a dev server for datasette.io, renaming a database across a multi-file codebase, building a blog data loader (Markdown → SQLite), building blog list and detail page templates, adding URL routing for trailing-slash URLs, tweaking CSS, wiring blog posts into the search index and sitemap, running test suites, fetching production data, and recovering from an accidental file deletion. Does NOT cover: Codex subscription model, API access, or model tier selection. The gist is self-contained and standalone.

## Extracted Claims

### Claim 1: OpenAI Codex Desktop has a Markdown session transcript export feature that produces sharable, human-readable records of AI-assisted development sessions

- **Evidence**: Simon Willison states this explicitly in the blog post and links the exported gist as proof. The gist is a 1,800-line Markdown document containing the full session, with collapsible `<details>` blocks for Codex's intermediate tool calls and plain text for its final answers.
- **Confidence**: settled (Willison built the Datasette blog using Codex Desktop and published the exported transcript; the gist is the artifact itself)
- **Quote**: "I built this using OpenAI Codex desktop, which turns out to have the Markdown session transcript export feature I've always wanted."
- **Our assessment**: This is the primary novelty of the source relative to the corpus. Codex Desktop (at the time of this post) appears to be the only AI coding tool that exports sessions as Markdown by default. Willison's "I've always wanted" phrasing signals this is a practitioner-relevant capability gap — session export has been missing from other tools. The export serves multiple purposes: documentation, reproducible workflow reference, and a post-hoc audit trail of what the AI agent did and why.

### Claim 2: The exported session transcript uses collapsible HTML `<details>` elements for Codex's intermediate tool calls, keeping the document readable while preserving the full reasoning chain

- **Evidence**: The gist itself demonstrates this structure throughout. Every Codex intermediate action (file reads, command runs, searches) is inside a `<details><summary>N previous messages</summary>` or `<details><summary>Ran N commands</summary>` block. Final answers are plain text.
- **Confidence**: settled (directly observable in the gist artifact)
- **Quote**: (no direct quote; the format is structural, not textual — see Concrete Artifacts below)
- **Our assessment**: The collapsible format is a deliberate design choice for readability. A developer reading the exported session sees Codex's conclusions without being overwhelmed by intermediate steps; they can expand any block to see how Codex got there. This mirrors how a practitioner would document their own work: decision + reasoning, with details available on request. The format is immediately publishable as a gist or wiki page.

### Claim 3: When a project's global dependency (datasette) was missing a required package (bs4), Codex Desktop automatically discovered the project's dependency management tooling (uv) and adapted its commands throughout the session

- **Evidence**: The gist transcript shows Codex noticing that bare `datasette` failed due to missing `bs4`, discovering `uv` is available, finding `requirements.txt`, and switching all subsequent commands to `uv run --with-requirements requirements.txt datasette ...`.
- **Confidence**: anecdotal (single session; the behavior reflects how Codex's system prompt instructs it to persist through tool failures)
- **Quote**: "Small wrinkle: the globally installed datasette was missing bs4, so the uv run --with-requirements requirements.txt ... version is the clean reliable one for this repo."
- **Our assessment**: This demonstrates Codex applying its "persist until task is handled end-to-end" directive (documented in `blog-simonwillison-codex-base-instructions.md` Claim 9) in a concrete situation: rather than stopping at a dependency error, it investigated the project's tooling and adapted. The `uv run --with-requirements` pattern then propagated consistently through the rest of the session, including in the test script invocations. Practitioners who set up AI-native projects should expect that a capable agent will discover and use `uv`, `nix`, `poetry`, or equivalent tools rather than requiring explicit instruction.

### Claim 4: A multi-file rename task (blog.db → simon-blog.db) surfaced unexpected impacts across the search indexer's stored type strings and CI S3 cache that Codex identified and resolved without being prompted

- **Evidence**: The gist shows Codex: (1) updating 6 files with mechanical renames, (2) discovering the `dogsheep-beta` indexer stores `type = 'blog.db/entries'` as a string key and adding explicit stale-row deletion, (3) discovering the CI workflow downloads/uploads `blog.db` from S3 and adding a migration fallback. None of these edge cases were requested by Willison.
- **Confidence**: anecdotal (single session; shows Codex's behavior for this specific type of refactoring task)
- **Quote**: "Good catch in the search indexer: it REPLACE s rows by (type, key) but does not delete types that disappeared from the config. Because the type changes from blog.db/entries to simon-blog.db/entries, I'm adding an explicit stale-row delete before the FTS rebuild."
- **Our assessment**: This is a concrete example of why AI coding agents add value beyond text editing: the search indexer's string-keyed type system is a non-obvious coupling that a developer doing a mechanical find-and-replace would likely miss. The CI S3 cache issue is similarly non-obvious. Both edge cases were caught through Codex reading the actual code (deploy scripts, CI workflow, search indexer source) rather than just pattern-matching on the rename string. For practitioners: a well-designed agent will explore lateral coupling before declaring a refactor complete.

### Claim 5: Codex Desktop accidentally deleted a user-owned untracked directory (blog-content/) during a cleanup pass, acknowledged the mistake, and restored the file from its previously captured terminal output

- **Evidence**: Direct exchange in the gist transcript. Willison noticed the deletion, Codex confirmed it, apologized, and reconstructed the file from terminal output it had captured earlier.
- **Confidence**: settled (direct exchange documented in the gist)
- **Quote**: "Yes. I'm sorry. I mistakenly removed the untracked blog-content/ folder thinking it was accidental output from the refresh. I had just inspected it first, and it only contained blog-content/new-blog.md, so I can restore that file now from the terminal output."
- **Our assessment**: This is a documented AI agent failure mode: treating untracked content as ephemeral output. Codex saw an untracked folder created during a production data refresh and inferred (incorrectly) that it was disposable build output. The recovery was possible only because Codex had read the file immediately before deleting it — a fortuitous margin that won't always exist. For practitioners: untracked user-owned content is a risk zone when running AI agents that do cleanup operations. Git-tracking content before running agent sessions, or explicitly instructing the agent about which untracked directories are user-owned, reduces this risk.

### Claim 6: Codex Desktop ran the project's test suite (scripts/test.sh) repeatedly as a verification mechanism after each substantial change, diagnosing and fixing test failures before reporting completion

- **Evidence**: The gist shows multiple rounds of `uv run --with-requirements requirements.txt bash scripts/test.sh`, including a failure where the test for `/-/beta` needed `docs-index.db` and `simon-blog.db` to be present locally. Codex diagnosed the missing files, fetched them, rebuilt the search index, and confirmed the test passed.
- **Confidence**: anecdotal (single session; consistent with Codex's system prompt "Persist until the task is fully handled end-to-end")
- **Quote**: "The test script itself shells out to bare datasette, so the direct way here is to run the whole script under uv run --with-requirements requirements.txt ... I'm trying that first to see the real missing pieces."
- **Our assessment**: Codex's test-driven verification behavior here is consistent with its documented system-prompt directive (see `blog-simonwillison-codex-base-instructions.md` Claim 9: "carry changes through implementation, verification, and a clear explanation of outcomes"). The session demonstrates this in practice: Codex did not declare a refactor complete until the test suite passed. Practitioners providing AI agents with a runnable test suite get test-verified output rather than just code edits.

### Claim 7: Codex Desktop used headless Chromium to take CSS layout screenshots and visually verify a nav-wrapping fix before reporting completion

- **Evidence**: The session shows Codex launching `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless --disable-gpu --hide-scrollbars --window-size=645,220 --screenshot=...` and inspecting the output image before declaring the CSS fix done.
- **Confidence**: anecdotal (single session; this was an unusual step; most tasks in the session used HTTP status codes for verification)
- **Quote**: "I'm taking a narrow screenshot at the same kind of width as your example and inspecting it before I call this done."
- **Our assessment**: Visual verification via headless Chromium screenshots is a significant capability: Codex did not just edit CSS — it rendered the result at the requested viewport width and examined the output. This is only possible because Codex Desktop runs in a full desktop environment with browser access. Practitioners should expect that AI agents with access to headless browsers can close the loop on visual correctness, not just code correctness.

### Claim 8: An end-to-end blog infrastructure (data loader, URL routes, templates, CSS, search integration, sitemap) was built in a single Codex Desktop session directed entirely by natural-language instructions

- **Evidence**: The session transcript covers: dev server setup → database rename across 7+ files → blog data loader (Markdown → SQLite via build_blog_posts.py) → homepage link → blog list page template → blog entry detail page template → Datasette route plugin for trailing-slash URLs → CSS nav-wrapping fix → test suite verification → production data refresh. All transitions were driven by Willison's natural-language prompts (e.g., "Build the /blog/ page so it's that reverse-ordered list of blog entries, each truncated...").
- **Confidence**: anecdotal (single session for one specific project; generalizability to other projects is uncertain)
- **Quote**: "Build the /blog/ page so it's that revers-ordered list of blog entries, each truncated, and make each one a link to /blog/YYYY/filename/ e.g. /blog/2026/new-blog/ - which is a page showing the blog entry"
- **Our assessment**: The session demonstrates that a complete multi-component feature can be built via iterative natural-language delegation to Codex Desktop, with the developer providing direction, reviewing output, and catching the one significant failure (the accidental deletion). The developer's role was architectural direction and QA, not code authoring. This is a concrete example of the "agentic engineering" mode Willison writes about more abstractly in `blog-simonwillison-vibe-coding-agentic-engineering.md`.

### Claim 9: The Datasette blog launch announcement is notable primarily as a pointer to the session transcript — the post itself contains only two sentences of substance; the practitioner value is entirely in the linked gist

- **Evidence**: The blog post text is: "Welcome to the Datasette blog. We have a bunch of neat Datasette announcements in the pipeline so we decided it was time the project grew an official blog." followed by two sentences about Codex Desktop and a link to the gist.
- **Confidence**: settled (the post is directly readable at the source URL)
- **Quote**: "Welcome to the Datasette blog. We have a bunch of neat Datasette announcements in the pipeline so we decided it was time the project grew an official blog."
- **Our assessment**: This is a Willison link-blog post: the signal is not in the post itself but in what it links to. Per the Prospector's assessment, the real target for extraction was always the gist. Practitioners mining Willison's blog for practitioner patterns should follow his links — his posts are often thin wrappers around substantive artifacts (session transcripts, code, papers, talks).

## Concrete Artifacts

### Session transcript structure (from gist: codex.md, github.com/simonw/885b11eee46822622b8031a1f4e5f3a3)

The exported Codex Desktop transcript uses this format:

```markdown
> [User prompt in blockquote]

<details><summary>N previous messages</summary>

> [Codex's intermediate reasoning and tool calls, collapsed]
>
> <details><summary>Explored N files, ran N commands</summary>
>
> - Ran `command here`
> - Read `./path/to/file`
>
> </details>
</details>

[Codex's final answer in plain Markdown — readable without expanding the details]
```

*Source: gist codex.md, opening structure*

### Dev server command identified by Codex (from session transcript)

```bash
uv run --with-requirements requirements.txt datasette . --port 9008 --reload
```

*Source: gist codex.md — Codex's final answer to "Figure out how to run a development server for this site on port 9008"*

### Multi-file rename scope discovered by Codex

```
Files updated when renaming blog.db → simon-blog.db:
- scripts/build.sh          (writes the database)
- scripts/deploy.sh         (publishes the database)
- templates/dogsheep-beta.yml (search indexer config — also needed explicit
                              stale-row DELETE for 'blog.db/entries' type key)
- datasette.yml             (route protection)
- plugins/seo.py            (SEO plugin path reference)
- refresh-from-production.sh (production data download)
- .github/workflows/deploy.yml (CI S3 cache — needed migration fallback)
```

*Source: gist codex.md — "I renamed the Datasette database path from blog.db to simon-blog.db across the site plumbing"*

### Blog data loader table schema (from session transcript)

```sql
-- blog_posts table in content.db
-- Generated by build_blog_posts.py, keyed on markdown filename slug
path TEXT,         -- canonical URL: /blog/YYYY/slug/
slug TEXT,         -- filename without extension
source_path TEXT,  -- relative path to .md file
title TEXT,        -- from YAML front matter
datetime_utc TEXT, -- from YAML front matter
year TEXT,         -- extracted from datetime_utc
body TEXT,         -- raw Markdown
html TEXT,         -- rendered HTML
summary TEXT       -- first paragraph, stripped of HTML
```

*Source: gist codex.md — "uv run ... sqlite-utils content.db 'select path, slug, source_path, title, datetime_utc, summary from blog_posts order by datetime_utc desc'"*

### Test suite invocation pattern

```bash
uv run --with-requirements requirements.txt bash scripts/test.sh
```

*Source: gist codex.md — Codex's verified command for running the datasette.io test suite with correct dependencies*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-codex-base-instructions.md` Claim 9: That note documents Codex's system-prompt directive to "persist until the task is fully handled end-to-end within the current turn whenever feasible: do not stop at analysis or partial fixes; carry changes through implementation, verification, and a clear explanation of outcomes." This session is a concrete demonstration of that behavior: Codex fixed the missing-dependency failure, found and fixed the stale search-index rows, ran tests repeatedly, and caught a CI S3 issue — all without being prompted. The system-prompt directive is visible in the agent's behavior.
  - `blog-simonwillison-codex-base-instructions.md` Claim 4: That note documents that all Codex tiers are instructed to prefer `rg` over `grep`. The gist confirms this: Codex used `rg` for all file content searches throughout the session (e.g., `rg -n "(serve|server|dev|localhost|port|9008|...)"`).
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1: That note documents Willison's personal convergence between vibe coding and responsible agentic engineering. This session sits clearly on the "responsible agentic engineering" side of that spectrum — Willison caught the accidental deletion, verified CSS visually, reviewed test output. The developer is active QA, not passive consumer of output.
  - `blog-simonwillison-rss-vibe-coded-apps.md` (Claim 4 of that note — Willison uses Claude to add an Atom feed in a single delegation): This session is a parallel pattern — a complete small-scope infrastructure task built in a single AI agent session. Both sessions show Willison's working mode: natural-language task direction with agent execution and practitioner review.

- **Contradicts**: None identified. No existing corpus note makes claims about Codex Desktop's session export feature or the patterns documented in this gist that would conflict with these findings.

- **Extends**:
  - `blog-simonwillison-codex-base-instructions.md`: That note documents what Codex is instructed to do (the system prompt). This source shows what Codex actually does when those instructions execute against a real project. Together they provide the complete picture: behavioral contract (the base instructions note) and behavioral evidence (this session transcript).
  - `blog-simonwillison-gpt55-codex-plugin.md`: That note covers how Willison accessed GPT-5.5 via the Codex API to run the `llm` CLI plugin and build an LLM plugin in a single afternoon session. This source documents a fuller Codex Desktop session (full IDE experience, session export) rather than API-level access — extending the corpus's coverage of Codex from API access to desktop product usage.

- **Novel**:
  - **First in-corpus documentation of a session transcript export feature in an AI coding tool**: No existing note documents the ability to export an entire AI development session as a shareable Markdown artifact. The collapsible `<details>` format is a distinct contribution.
  - **First in-corpus primary-source record of an end-to-end agentic development session**: Prior notes describe AI-assisted workflows abstractly or report on them at summary level. This gist is the actual session log — the AI agent's decisions, mistakes, and recoveries are visible in sequence.
  - **Agent file-deletion failure mode documented with recovery path**: No prior corpus note documents this specific failure: an AI agent treating untracked user-owned content as disposable build output. The recovery mechanism (file reconstructed from previously captured terminal output) is also novel.
  - **Headless Chromium as AI agent verification tool**: No prior corpus note documents an AI agent using headless browser screenshots to verify CSS layout changes before reporting completion.

## Guide Impact

- **Chapter 04 (Tooling and infrastructure — AI coding tools comparison)**: Add Codex Desktop's session transcript export as a differentiating feature relative to other AI coding tools (Claude Code, Cursor, Copilot). The guide should note this as a practitioner-relevant capability: session export creates an automatic documentation artifact, a post-hoc audit trail, and a shareable reproducible workflow record. No other tool in the corpus has this feature documented.

- **Chapter 03 (Development patterns — AI-assisted refactoring)**: Add the multi-file rename pattern (Claim 4) as an example of how AI agents surface non-obvious coupling during refactoring tasks. The search indexer stale-type issue and the CI S3 fallback are concrete examples of lateral coupling that agents with read access to the full codebase find, while text-search-based refactoring tools miss. Recommend: for rename/refactor tasks, give the agent access to the full project (not just the files being renamed) and verify it has read CI workflows and search/index configurations.

- **Chapter 03 (Development patterns — Managing AI agent failures)**: Add the untracked-directory deletion failure mode (Claim 5) as a documented risk. Recommend: git-track or explicitly protect content that exists in the working directory but not in version control before running agent sessions that include cleanup operations. The guide should distinguish between "agent errors on code" (usually caught by tests) and "agent errors on workspace state" (not caught by tests, only by the developer noticing).

- **Chapter 07 (Prompting and context — verification patterns)**: Add the test-suite-as-verification-loop pattern (Claim 6): give the agent a runnable `./scripts/test.sh` or equivalent and it will use it as a closure condition for each task. Pair with the headless-browser verification pattern (Claim 7) for UI-related tasks: if the environment has a browser, the agent can close the visual verification loop without developer intervention.

- **Chapter 04 (Tooling — Session documentation)**: Add session transcript export as a practitioner workflow recommendation. For complex AI-assisted development sessions, the exported transcript serves as: (1) project documentation for future maintainers, (2) a reproducible workflow reference, (3) an audit trail for code review. The guide should note that Codex Desktop provides this natively; for other tools, practitioners must maintain session logs manually.

## Extraction Notes

- The source URL (`https://simonwillison.net/2026/May/13/welcome-to-the-datasette-blog/`) contains only two sentences of practitioner value. Following the linked gist (`https://gist.github.com/simonw/885b11eee46822622b8031a1f4e5f3a3`) was mandatory — it is 1,800 lines of primary source material.
- The gist was retrieved in full via `gh api gists/885b11eee46822622b8031a1f4e5f3a3 --jq '.files | to_entries[] | .value.content'`. All quotes are from the raw gist content, not from WebFetch summaries.
- The blog post also links to datasette.io issue #179 (the planning issue for the blog); that issue was not followed as it is internal project planning, not practitioner-facing content.
- The session transcript is a record of Willison's real-time work session on May 13, 2026. It includes a genuine failure (accidental deletion) and genuine uncertainty (Codex reasoning about whether to alias vs. rename the database). The reliability of observations is high precisely because this is an unedited log, not a retrospective account.
- Confidence set to `anecdotal` overall: all agent behavior claims are from a single session on one project. The session export feature claim (Claim 1) is `settled`; the agent behavior patterns (Claims 3–8) are `anecdotal` — they reflect Codex's behavior for this project, but may not generalize to all projects or Codex configurations.
